<?php
$page = 'barang';
$pageTitle = 'Kelola Barang';

ob_start();
?>

<div class="d-flex justify-content-between align-items-center mb-3">
    <div>
        <a href="index.php?page=barang&action=create" class="btn btn-primary">
            <i class="fas fa-plus"></i> Tambah Barang
        </a>
    </div>
    <div class="col-md-4">
        <div class="input-group">
            <input type="text" class="form-control" id="searchInput" placeholder="Cari barang...">
            <button class="btn btn-outline-secondary" type="button" id="searchBtn">
                <i class="fas fa-search"></i>
            </button>
        </div>
    </div>
</div>

<div class="card">
    <div class="card-header">
        <h5 class="card-title mb-0">Daftar Barang</h5>
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-striped table-hover" id="barangTable">
                <thead class="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Nama Barang</th>
                        <th>Kategori</th>
                        <th>Harga Beli</th>
                        <th>Harga Jual</th>
                        <th>Stok</th>
                        <th>Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($barang as $item): ?>
                    <tr>
                        <td><?= $item['id_barang'] ?></td>
                        <td><?= htmlspecialchars($item['nama_barang']) ?></td>
                        <td>
                            <span class="badge bg-info"><?= htmlspecialchars($item['kategori']) ?></span>
                        </td>
                        <td>Rp <?= number_format($item['harga_beli'], 0, ',', '.') ?></td>
                        <td>Rp <?= number_format($item['harga_jual'], 0, ',', '.') ?></td>
                        <td>
                            <span class="badge bg-<?= $item['stok'] < 10 ? 'danger' : 'success' ?>">
                                <?= $item['stok'] ?>
                            </span>
                        </td>
                        <td>
                            <div class="btn-group" role="group">
                                <a href="index.php?page=barang&action=edit&id=<?= $item['id_barang'] ?>" 
                                   class="btn btn-sm btn-warning">
                                    <i class="fas fa-edit"></i>
                                </a>
                                <button type="button" class="btn btn-sm btn-danger" 
                                        onclick="confirmDelete(<?= $item['id_barang'] ?>, '<?= htmlspecialchars($item['nama_barang']) ?>')">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- Delete Confirmation Modal -->
<div class="modal fade" id="deleteModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Konfirmasi Hapus</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <p>Apakah Anda yakin ingin menghapus barang <strong id="itemName"></strong>?</p>
                <p class="text-danger"><small>Tindakan ini tidak dapat dibatalkan.</small></p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Batal</button>
                <a href="#" class="btn btn-danger" id="deleteConfirmBtn">Hapus</a>
            </div>
        </div>
    </div>
</div>

<?php
$content = ob_get_clean();

// JavaScript untuk fitur pencarian dan konfirmasi hapus
ob_start();
?>
<script>
// Search functionality
$('#searchInput').on('keyup', function() {
    var value = $(this).val().toLowerCase();
    $('#barangTable tbody tr').filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
});

$('#searchBtn').on('click', function() {
    $('#searchInput').trigger('keyup');
});

// Delete confirmation
function confirmDelete(id, name) {
    $('#itemName').text(name);
    $('#deleteConfirmBtn').attr('href', 'index.php?page=barang&action=delete&id=' + id);
    $('#deleteModal').modal('show');
}

// Enter key search
$('#searchInput').on('keypress', function(e) {
    if (e.which == 13) {
        $(this).trigger('keyup');
    }
});
</script>
<?php
$scripts = ob_get_clean();

include 'views/layout/template.php';
?>