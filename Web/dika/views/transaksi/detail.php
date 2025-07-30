<?php
$page = 'transaksi';
$pageTitle = 'Detail Transaksi';

// Ambil ID dari parameter
$id_transaksi = $_GET['id'] ?? 0;

ob_start();
?>

<div class="row">
    <div class="col-12">
        <div class="card">
            <div class="card-header d-flex justify-content-between align-items-center">
                <h5 class="card-title mb-0">
                    <i class="fas fa-receipt"></i> Detail Transaksi
                </h5>
                <div>
                    <button type="button" class="btn btn-outline-primary" onclick="printStruk()">
                        <i class="fas fa-print"></i> Print Struk
                    </button>
                    <a href="index.php?page=transaksi" class="btn btn-secondary">
                        <i class="fas fa-arrow-left"></i> Kembali
                    </a>
                </div>
            </div>
            <div class="card-body" id="transaksiDetail">
                <div class="text-center">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <p class="mt-2">Memuat detail transaksi...</p>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Modal Print Preview -->
<div class="modal fade" id="printModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Preview Struk</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <div id="strukContent" class="text-center" style="font-family: 'Courier New', monospace;">
                    <!-- Struk akan diisi dengan JavaScript -->
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
                <button type="button" class="btn btn-primary" onclick="doPrint()">
                    <i class="fas fa-print"></i> Print
                </button>
            </div>
        </div>
    </div>
</div>

<?php
$content = ob_get_clean();

// JavaScript untuk functionality
ob_start();
?>
<script>
let transaksiData = null;

$(document).ready(function() {
    loadDetailTransaksi();
});

function loadDetailTransaksi() {
    $.ajax({
        url: 'index.php?page=transaksi&action=detail_data',
        method: 'GET',
        data: { id: <?= $id_transaksi ?> },
        success: function(response) {
            const data = JSON.parse(response);
            if (data.success) {
                transaksiData = data.transaksi;
                displayDetailTransaksi(data.transaksi);
            } else {
                displayError(data.error);
            }
        },
        error: function() {
            displayError('Gagal memuat detail transaksi');
        }
    });
}

function displayDetailTransaksi(transaksi) {
    const tanggal = new Date(transaksi.tanggal_transaksi).toLocaleDateString('id-ID', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
    
    const waktu = new Date(transaksi.created_at).toLocaleTimeString('id-ID');
    const subtotal = parseFloat(transaksi.total_harga) + parseFloat(transaksi.diskon);
    
    let itemsHtml = '';
    transaksi.items.forEach(function(item, index) {
        const itemSubtotal = (parseFloat(item.harga_satuan) * parseInt(item.quantity)) - parseFloat(item.diskon_item);
        itemsHtml += `
            <tr>
                <td>${index + 1}</td>
                <td>
                    <strong>${item.nama_barang}</strong><br>
                    <small class="text-muted">${item.kategori}</small>
                </td>
                <td class="text-end">Rp ${parseFloat(item.harga_satuan).toLocaleString('id-ID')}</td>
                <td class="text-center">${item.quantity}</td>
                <td class="text-end">
                    ${parseFloat(item.diskon_item) > 0 ? 
                        `<span class="badge bg-warning text-dark">Rp ${parseFloat(item.diskon_item).toLocaleString('id-ID')}</span>` : 
                        '<span class="text-muted">-</span>'
                    }
                </td>
                <td class="text-end"><strong>Rp ${itemSubtotal.toLocaleString('id-ID')}</strong></td>
            </tr>
        `;
    });
    
    const html = `
        
        <div class="row mb-4">
            <div class="col-md-6">
                <div class="card bg-light">
                    <div class="card-body">
                        <h6 class="card-title">
                            <i class="fas fa-info-circle"></i> Informasi Transaksi
                        </h6>
                        <table class="table table-borderless table-sm">
                            <tr>
                                <td width="40%"><strong>ID Transaksi</strong></td>
                                <td>: #${transaksi.id_transaksi}</td>
                            </tr>
                            <tr>
                                <td><strong>Tanggal</strong></td>
                                <td>: ${tanggal}</td>
                            </tr>
                            <tr>
                                <td><strong>Waktu</strong></td>
                                <td>: ${waktu}</td>
                            </tr>
                            <tr>
                                <td><strong>Total Item</strong></td>
                                <td>: ${transaksi.items.length} jenis barang</td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card bg-success text-white">
                    <div class="card-body">
                        <h6 class="card-title">
                            <i class="fas fa-calculator"></i> Ringkasan Pembayaran
                        </h6>
                        <table class="table table-borderless table-sm text-white">
                            <tr>
                                <td width="50%">Subtotal</td>
                                <td>: Rp ${subtotal.toLocaleString('id-ID')}</td>
                            </tr>
                            <tr>
                                <td>Diskon</td>
                                <td>: Rp ${parseFloat(transaksi.diskon).toLocaleString('id-ID')}</td>
                            </tr>
                            <tr class="border-top">
                                <td><strong>Total</strong></td>
                                <td><strong>: Rp ${parseFloat(transaksi.total_harga).toLocaleString('id-ID')}</strong></td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        
       
        <h6><i class="fas fa-list"></i> Detail Item Pembelian</h6>
        <div class="table-responsive">
            <table class="table table-striped table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th width="5%">No</th>
                        <th width="30%">Nama Barang</th>
                        <th width="15%">Harga Satuan</th>
                        <th width="10%">Qty</th>
                        <th width="15%">Diskon Item</th>
                        <th width="15%">Subtotal</th>
                    </tr>
                </thead>
                <tbody>
                    ${itemsHtml}
                </tbody>
                <tfoot class="table-light">
                    <tr>
                        <td colspan="5" class="text-end"><strong>Total Keseluruhan:</strong></td>
                        <td class="text-end"><strong>Rp ${parseFloat(transaksi.total_harga).toLocaleString('id-ID')}</strong></td>
                    </tr>
                </tfoot>
            </table>
        </div>
        
        
        <div class="row mt-4">
            <div class="col-md-4">
                <div class="card border-primary">
                    <div class="card-body text-center">
                        <h5 class="text-primary">${transaksi.items.reduce((sum, item) => sum + parseInt(item.quantity), 0)}</h5>
                        <small class="text-muted">Total Quantity</small>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card border-warning">
                    <div class="card-body text-center">
                        <h5 class="text-warning">Rp ${(parseFloat(transaksi.diskon) + transaksi.items.reduce((sum, item) => sum + parseFloat(item.diskon_item), 0)).toLocaleString('id-ID')}</h5>
                        <small class="text-muted">Total Diskon</small>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card border-info">
                    <div class="card-body text-center">
                        <h5 class="text-info">Rp ${(parseFloat(transaksi.total_harga) / transaksi.items.length).toLocaleString('id-ID')}</h5>
                        <small class="text-muted">Rata-rata per Item</small>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    $('#transaksiDetail').html(html);
}

function displayError(message) {
    const html = `
        <div class="text-center">
            <div class="alert alert-danger">
                <i class="fas fa-exclamation-triangle"></i> ${message}
            </div>
            <a href="index.php?page=transaksi" class="btn btn-primary">
                <i class="fas fa-arrow-left"></i> Kembali ke Daftar Transaksi
            </a>
        </div>
    `;
    $('#transaksiDetail').html(html);
}

function printStruk() {
    if (!transaksiData) {
        alert('Data transaksi belum tersedia');
        return;
    }
    
    generateStruk();
    $('#printModal').modal('show');
}

function generateStruk() {
    const transaksi = transaksiData;
    const tanggal = new Date(transaksi.tanggal_transaksi).toLocaleDateString('id-ID');
    const waktu = new Date(transaksi.created_at).toLocaleTimeString('id-ID');
    const subtotal = parseFloat(transaksi.total_harga) + parseFloat(transaksi.diskon);
    
    let itemsStruk = '';
    transaksi.items.forEach(function(item) {
        const itemSubtotal = (parseFloat(item.harga_satuan) * parseInt(item.quantity)) - parseFloat(item.diskon_item);
        itemsStruk += `
            <div style="display: flex; justify-content: space-between; margin: 2px 0;">
                <span>${item.nama_barang}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 2px 0; padding-left: 10px;">
                <span>${item.quantity} x Rp ${parseFloat(item.harga_satuan).toLocaleString('id-ID')}</span>
                <span>Rp ${itemSubtotal.toLocaleString('id-ID')}</span>
            </div>
            ${parseFloat(item.diskon_item) > 0 ? 
                `<div style="display: flex; justify-content: space-between; margin: 2px 0; padding-left: 20px; color: #666;">
                    <span>Diskon Item</span>
                    <span>-Rp ${parseFloat(item.diskon_item).toLocaleString('id-ID')}</span>
                </div>` : ''
            }
        `;
    });
    
    const strukHtml = `
        <div style="width: 300px; margin: 0 auto; border: 1px solid #ccc; padding: 20px;">
            <div style="text-align: center; border-bottom: 1px dashed #000; padding-bottom: 10px; margin-bottom: 10px;">
                <h4 style="margin: 0;">TOKO KASIR</h4>
                <small>Jl. Contoh No. 123<br>Telp: 0123-456-789</small>
            </div>
            
            <div style="margin-bottom: 10px;">
                <div>No. Transaksi: #${transaksi.id_transaksi}</div>
                <div>Tanggal: ${tanggal}</div>
                <div>Waktu: ${waktu}</div>
            </div>
            
            <div style="border-top: 1px dashed #000; border-bottom: 1px dashed #000; padding: 10px 0; margin: 10px 0;">
                ${itemsStruk}
            </div>
            
            <div style="margin-top: 10px;">
                <div style="display: flex; justify-content: space-between;">
                    <span>Subtotal:</span>
                    <span>Rp ${subtotal.toLocaleString('id-ID')}</span>
                </div>
                ${parseFloat(transaksi.diskon) > 0 ? 
                    `<div style="display: flex; justify-content: space-between;">
                        <span>Diskon:</span>
                        <span>-Rp ${parseFloat(transaksi.diskon).toLocaleString('id-ID')}</span>
                    </div>` : ''
                }
                <div style="display: flex; justify-content: space-between; font-weight: bold; border-top: 1px solid #000; padding-top: 5px; margin-top: 5px;">
                    <span>TOTAL:</span>
                    <span>Rp ${parseFloat(transaksi.total_harga).toLocaleString('id-ID')}</span>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 15px; border-top: 1px dashed #000; padding-top: 10px;">
                <small>Terima kasih atas kunjungan Anda<br>Barang yang sudah dibeli tidak dapat dikembalikan</small>
            </div>
        </div>
    `;
    
    $('#strukContent').html(strukHtml);
}

function doPrint() {
    const printContent = document.getElementById('strukContent').innerHTML;
    const printWindow = window.open('', '_blank');
    printWindow.document.write(`
        <html>
        <head>
            <title>Struk Transaksi #${transaksiData.id_transaksi}</title>
            <style>
                body { font-family: 'Courier New', monospace; margin: 0; padding: 20px; }
                @media print { body { margin: 0; padding: 0; } }
            </style>
        </head>
        <body onload="window.print(); window.close();">
            ${printContent}
        </body>
        </html>
    `);
    printWindow.document.close();
}
</script>
<?php
$scripts = ob_get_clean();

include 'views/layout/template.php';
?>