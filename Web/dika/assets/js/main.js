// Main JavaScript for Kasir System

$(document).ready(function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize sidebar collapse for mobile
    initSidebarToggle();
    
    // Format currency inputs
    formatCurrencyInputs();
    
    // Auto-hide alerts
    autoHideAlerts();
    
    // Initialize data tables if available
    initDataTables();
    
    // Initialize form validation
    initFormValidation();
});

// Sidebar toggle for mobile
function initSidebarToggle() {
    // Add mobile menu button if not exists
    if (window.innerWidth <= 768 && !document.getElementById('sidebarToggle')) {
        const toggleBtn = document.createElement('button');
        toggleBtn.id = 'sidebarToggle';
        toggleBtn.className = 'btn btn-primary d-md-none position-fixed';
        toggleBtn.style.cssText = 'top: 10px; left: 10px; z-index: 1001;';
        toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
        document.body.appendChild(toggleBtn);
        
        toggleBtn.addEventListener('click', function() {
            const sidebar = document.querySelector('.sidebar');
            sidebar.classList.toggle('show');
        });
    }
}

// Format currency inputs
function formatCurrencyInputs() {
    $('input[type="number"]').on('input', function() {
        if ($(this).hasClass('currency-format')) {
            let value = $(this).val().replace(/[^0-9]/g, '');
            if (value) {
                $(this).val(parseInt(value).toLocaleString('id-ID'));
            }
        }
    });
}

// Auto-hide alerts after 5 seconds
function autoHideAlerts() {
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);
}

// Initialize DataTables if jQuery DataTables is loaded
function initDataTables() {
    if (typeof $.fn.DataTable !== 'undefined') {
        $('.data-table').DataTable({
            responsive: true,
            language: {
                url: '//cdn.datatables.net/plug-ins/1.10.24/i18n/Indonesian.json'
            },
            dom: 'Bfrtip',
            buttons: [
                'copy', 'csv', 'excel', 'pdf', 'print'
            ]
        });
    }
}

// Form validation
function initFormValidation() {
    // Add was-validated class to forms on submit
    $('form').on('submit', function() {
        $(this).addClass('was-validated');
    });
    
    // Real-time validation feedback
    $('.form-control').on('blur', function() {
        if (this.checkValidity()) {
            $(this).removeClass('is-invalid').addClass('is-valid');
        } else {
            $(this).removeClass('is-valid').addClass('is-invalid');
        }
    });
}

// Utility Functions
const Utils = {
    // Format number to Indonesian currency
    formatCurrency: function(amount) {
        return new Intl.NumberFormat('id-ID', {
            style: 'currency',
            currency: 'IDR',
            minimumFractionDigits: 0
        }).format(amount);
    },
    
    // Format number with thousand separator
    formatNumber: function(number) {
        return parseInt(number).toLocaleString('id-ID');
    },
    
    // Show loading state
    showLoading: function(element) {
        const original = $(element).html();
        $(element).data('original-html', original);
        $(element).html('<span class="loading"></span> Loading...').prop('disabled', true);
    },
    
    // Hide loading state
    hideLoading: function(element) {
        const original = $(element).data('original-html');
        $(element).html(original).prop('disabled', false);
    },
    
    // Show toast notification
    showToast: function(type, message, title = '') {
        const toastId = 'toast-' + Date.now();
        const toastHtml = `
            <div class="toast align-items-center text-white bg-${type} border-0" role="alert" id="${toastId}">
                <div class="d-flex">
                    <div class="toast-body">
                        ${title ? '<strong>' + title + '</strong><br>' : ''}
                        ${message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                </div>
            </div>
        `;
        
        // Create toast container if not exists
        if (!document.getElementById('toast-container')) {
            const container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
            container.style.zIndex = '1055';
            document.body.appendChild(container);
        }
        
        $('#toast-container').append(toastHtml);
        const toast = new bootstrap.Toast(document.getElementById(toastId));
        toast.show();
        
        // Remove toast element after it's hidden
        document.getElementById(toastId).addEventListener('hidden.bs.toast', function() {
            this.remove();
        });
    },
    
    // Confirm delete with SweetAlert2 (if available)
    confirmDelete: function(callback, title = 'Apakah Anda yakin?', text = 'Data yang dihapus tidak dapat dikembalikan!') {
        if (typeof Swal !== 'undefined') {
            Swal.fire({
                title: title,
                text: text,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Ya, hapus!',
                cancelButtonText: 'Batal'
            }).then((result) => {
                if (result.isConfirmed && callback) {
                    callback();
                }
            });
        } else {
            if (confirm(title + '\n' + text)) {
                if (callback) callback();
            }
        }
    },
    
    // Validate form data
    validateForm: function(formData, rules) {
        const errors = [];
        
        for (const field in rules) {
            const value = formData[field];
            const rule = rules[field];
            
            if (rule.required && (!value || value.trim() === '')) {
                errors.push(`${rule.label || field} harus diisi`);
            }
            
            if (rule.min && value && parseFloat(value) < rule.min) {
                errors.push(`${rule.label || field} minimal ${rule.min}`);
            }
            
            if (rule.max && value && parseFloat(value) > rule.max) {
                errors.push(`${rule.label || field} maksimal ${rule.max}`);
            }
            
            if (rule.pattern && value && !rule.pattern.test(value)) {
                errors.push(`${rule.label || field} format tidak valid`);
            }
        }
        
        return errors;
    },
    
    // Debounce function for search
    debounce: function(func, wait, immediate) {
        let timeout;
        return function executedFunction() {
            const context = this;
            const args = arguments;
            const later = function() {
                timeout = null;
                if (!immediate) func.apply(context, args);
            };
            const callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func.apply(context, args);
        };
    }
};

// AJAX Setup
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        // Add loading state to buttons with data-loading attribute
        if (settings.loadingButton) {
            Utils.showLoading(settings.loadingButton);
        }
    },
    complete: function(xhr, textStatus) {
        // Hide loading state
        if (this.loadingButton) {
            Utils.hideLoading(this.loadingButton);
        }
    },
    error: function(xhr, textStatus, errorThrown) {
        let message = 'Terjadi kesalahan pada server';
        
        if (xhr.responseJSON && xhr.responseJSON.message) {
            message = xhr.responseJSON.message;
        } else if (xhr.responseText) {
            try {
                const response = JSON.parse(xhr.responseText);
                message = response.message || message;
            } catch (e) {
                // Use default message
            }
        }
        
        Utils.showToast('danger', message, 'Error');
    }
});

// Global event handlers
$(document).on('click', '[data-toggle="loading"]', function() {
    Utils.showLoading(this);
});

$(document).on('click', '[data-confirm-delete]', function(e) {
    e.preventDefault();
    const url = $(this).attr('href') || $(this).data('url');
    const title = $(this).data('title') || 'Apakah Anda yakin?';
    const text = $(this).data('text') || 'Data yang dihapus tidak dapat dikembalikan!';
    
    Utils.confirmDelete(function() {
        window.location.href = url;
    }, title, text);
});

// Print function
function printElement(elementId) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    const printWindow = window.open('', '_blank');
    printWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Print</title>
            <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
            <style>
                @media print {
                    body { margin: 0; }
                    .no-print { display: none !important; }
                }
            </style>
        </head>
        <body>
            ${element.outerHTML}
            <script>
                window.onload = function() {
                    window.print();
                    window.close();
                }
            </script>
        </body>
        </html>
    `);
    printWindow.document.close();
}

// Export functions
const Export = {
    toCSV: function(tableId, filename = 'export.csv') {
        const table = document.getElementById(tableId);
        if (!table) return;
        
        let csv = '';
        const rows = table.querySelectorAll('tr');
        
        for (let i = 0; i < rows.length; i++) {
            const cells = rows[i].querySelectorAll('td, th');
            const rowData = [];
            
            for (let j = 0; j < cells.length; j++) {
                let cellData = cells[j].textContent.trim();
                cellData = cellData.replace(/"/g, '""'); // Escape quotes
                rowData.push('"' + cellData + '"');
            }
            
            csv += rowData.join(',') + '\n';
        }
        
        // Download CSV
        const blob = new Blob([csv], { type: 'text/csv' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        a.click();
        window.URL.revokeObjectURL(url);
    },
    
    toPDF: function(elementId, filename = 'export.pdf') {
        // This would require a PDF library like jsPDF
        // For now, just use the browser's print to PDF function
        printElement(elementId);
    }
};

// Make functions globally available
window.Utils = Utils;
window.Export = Export;
window.printElement = printElement;