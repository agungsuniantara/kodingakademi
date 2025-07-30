<?php
$page = 'transaksi';
$pageTitle = 'Daftar Transaksi';

ob_start();
?>

<div class="row">
    <div class="col-12">
        <div class="card">
            <div class="card-header d-flex justify-content-between align-items-center">
                <h5 class="card-title mb-0">
                    <i class="fas fa-receipt"></i> Daftar Transaksi
                </h5>
                <a href="index.php?page=transaksi&action=create" class="btn btn-primary">
                    <i class="fas fa-plus"></i> Transaksi Baru
                </a>
            </div>
            <div class="card-body">
                <!-- Filter -->
                <div class="row mb-3">
                    <div class="col-md-3">
                        <label class="form-label">Tanggal Dari</label>
                        <input type="date" class="form-control" id="tanggalDari" value="<?= date('Y-m-01') ?>">
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Tanggal Sampai</label>
                        <input type="date" class="form-control" id="tanggalSampai" value="<?= date('Y-m-d') ?>">
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Total Minimum</label>
                        <input type="number" class="form-control" id="totalMin" placeholder="Minimal total">
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">&nbsp;</label>
                        <div class="d-grid">
                            <button type="button" class="btn btn-outline-primary" id="btnFilter">
                                <i class="fas fa-filter"></i> Filter
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Ringkasan -->
                <div class="row mb-4">
                    <div class="col-md-3">
                        <div class="card bg-primary text-white">
                            <div class="card-body">
                                <div class="d-flex justify-content-between">
                                    <div>
                                        <h6>Total Transaksi</h6>
                                        <h4 id="totalTransaksi">0</h4>
                                    </div>
                                    <div class="align-self-center">
                                        <i class="fas fa-shopping-cart fa-2x"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card bg-success text-white">
                            <div class="card-body">
                                <div class="d-flex justify-content-between">
                                    <div>
                                        <h6>Total Pendapatan</h6>
                                        <h4 id="totalPendapatan">Rp 0</h4>
                                    </div>
                                    <div class="align-self-center">
                                        <i class="fas fa-money-bill-wave fa-2x"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card bg-info text-white">
                            <div class="card-body">
                                <div class="d-flex justify-content-between">
                                    <div>
                                        <h6>Rata-rata Transaksi</h6>
                                        <h4 id="rataTransaksi">Rp 0</h4>
                                    </div>
                                    <div class="align-self-center">
                                        <i class="fas fa-chart-line fa-2x"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card bg-warning text-white">
                            <div class="card-body">
                                <div class="d-flex justify-content-between">
                                    <div>
                                        <h6>Total Diskon</h6>
                                        <h4 id="totalDiskon">Rp 0</h4>
                                    </div>
                                    <div class="align-self-center">
                                        <i class="fas fa-percent fa-2x"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Tabel Transaksi -->
                <div class="table-responsive">
                    <table class="table table-striped table-hover" id="transaksiTable">
                        <thead class="table-dark">
                            <tr>
                                <th>ID</th>
                                <th>Tanggal</th>
                                <th>Total Item</th>
                                <th>Subtotal</th>
                                <th>Diskon</th>
                                <th>Total</th>
                                <th>Aksi</th>
                            </tr>
                        </thead>
                        <tbody id="transaksiList">
                            <tr>
                                <td colspan="7" class="text-center">
                                    <div class="spinner-border text-primary" role="status">
                                        <span class="visually-hidden">Loading...</span>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Pagination -->
                <nav aria-label="Page navigation" id="pagination">
                    <!-- Pagination akan diisi dengan JavaScript -->
                </nav>
            </div>
        </div>
    </div>
</div>

<!-- Modal Konfirmasi Hapus -->
<div class="modal fade" id="deleteModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Konfirmasi Hapus</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                Apakah Anda yakin ingin menghapus transaksi ini? Tindakan ini tidak dapat dibatalkan.
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Batal</button>
                <button type="button" class="btn btn-danger" id="confirmDelete">Hapus</button>
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
let currentPage = 1;
let deleteTransaksiId = null;

$(document).ready(function() {
    loadTransaksi();
    
    // Event listeners
    $('#btnFilter').on('click', function() {
        currentPage = 1;
        loadTransaksi();
    });
    
    $('#confirmDelete').on('click', function() {
        if (deleteTransaksiId) {
            hapusTransaksi(deleteTransaksiId);
        }
    });
});

function loadTransaksi(page = 1) {
    const tanggalDari = $('#tanggalDari').val();
    const tanggalSampai = $('#tanggalSampai').val();
    const totalMin = $('#totalMin').val();
    
    $.ajax({
        url: 'index.php?page=transaksi&action=list',
        method: 'GET',
        data: {
            page: page,
            tanggal_dari: tanggalDari,
            tanggal_sampai: tanggalSampai,
            total_min: totalMin
        },
        success: function(response) {
            const data = JSON.parse(response);
            displayTransaksi(data.transaksi);
            displaySummary(data.summary);
            displayPagination(data.pagination);
        },
        error: function() {
            $('#transaksiList').html('<tr><td colspan="7" class="text-center text-danger">Gagal memuat data transaksi</td></tr>');
        }
    });
}

function displayTransaksi(transaksi) {
    let html = '';
    
    if (transaksi.length === 0) {
        html = '<tr><td colspan="7" class="text-center text-muted">Tidak ada transaksi dalam periode ini</td></tr>';
    } else {
        transaksi.forEach(function(item) {
            const tanggal = new Date(item.tanggal_transaksi).toLocaleDateString('id-ID');
            const subtotal = parseFloat(item.total_harga) + parseFloat(item.diskon);
            
            html += `
                <tr>
                    <td><strong>#${item.id_transaksi}</strong></td>
                    <td>${tanggal}</td>
                    <td>
                        <span class="badge bg-primary">${item.total_item} item</span>
                    </td>
                    <td>Rp ${subtotal.toLocaleString('id-ID')}</td>
                    <td>
                        <span class="badge bg-warning text-dark">
                            Rp ${parseFloat(item.diskon).toLocaleString('id-ID')}
                        </span>
                    </td>
                    <td><strong>Rp ${parseFloat(item.total_harga).toLocaleString('id-ID')}</strong></td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="index.php?page=transaksi&action=detail&id=${item.id_transaksi}" 
                               class="btn btn-outline-info" title="Detail">
                                <i class="fas fa-eye"></i>
                            </a>
                            <button type="button" class="btn btn-outline-primary" 
                                    onclick="printStruk(${item.id_transaksi})" title="Print Struk">
                                <i class="fas fa-print"></i>
                            </button>
                            <button type="button" class="btn btn-outline-danger" 
                                    onclick="confirmDelete(${item.id_transaksi})" title="Hapus">
                                <i class="fas fa-trash"></i>
                            </button>
                        </div>
                    </td>
                </tr>
            `;
        });
    }
    
    $('#transaksiList').html(html);
}

function displaySummary(summary) {
    $('#totalTransaksi').text(summary.total_transaksi || 0);
    $('#totalPendapatan').text('Rp ' + (parseFloat(summary.total_pendapatan) || 0).toLocaleString('id-ID'));
    $('#rataTransaksi').text('Rp ' + (parseFloat(summary.rata_transaksi) || 0).toLocaleString('id-ID'));
    $('#totalDiskon').text('Rp ' + (parseFloat(summary.total_diskon) || 0).toLocaleString('id-ID'));
}

function displayPagination(pagination) {
    if (pagination.total_pages <= 1) {
        $('#pagination').html('');
        return;
    }
    
    let html = '<ul class="pagination justify-content-center">';
    
    // Previous button
    if (pagination.current_page > 1) {
        html += `<li class="page-item"><a class="page-link" href="#" onclick="loadTransaksi(${pagination.current_page - 1})">Previous</a></li>`;
    }
    
    // Page numbers
    for (let i = 1; i <= pagination.total_pages; i++) {
        const active = i === pagination.current_page ? 'active' : '';
        html += `<li class="page-item ${active}"><a class="page-link" href="#" onclick="loadTransaksi(${i})">${i}</a></li>`;
    }
    
    // Next button
    if (pagination.current_page < pagination.total_pages) {
        html += `<li class="page-item"><a class="page-link" href="#" onclick="loadTransaksi(${pagination.current_page + 1})">Next</a></li>`;
    }
    
    html += '</ul>';
    $('#pagination').html(html);
}

function confirmDelete(id) {
    deleteTransaksiId = id;
    $('#deleteModal').modal('show');
}

function hapusTransaksi(id) {
    $.ajax({
        url: 'index.php?page=transaksi&action=delete',
        method: 'POST',
        data: { id: id },
        success: function(response) {
            const result = JSON.parse(response);
            if (result.success) {
                $('#deleteModal').modal('hide');
                loadTransaksi(currentPage);
                alert('Transaksi berhasil dihapus!');
            } else {
                alert('Error: ' + result.error);
            }
        },
        error: function() {
            alert('Terjadi kesalahan saat menghapus transaksi!');
        }
    });
}

function printStruk(id) {
    window.open('index.php?page=transaksi&action=print&id=' + id, '_blank', 'width=800,height=600');
}
</script>
<?php
$scripts = ob_get_clean();

include 'views/layout/template.php';
?>