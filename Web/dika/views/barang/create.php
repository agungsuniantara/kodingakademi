<?php
$page = 'barang';
$pageTitle = 'Tambah Barang';

ob_start();
?>

<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h5 class="card-title mb-0">
                    <i class="fas fa-plus"></i> Tambah Barang Baru
                </h5>
            </div>
            <div class="card-body">
                <?php if (isset($error)): ?>
                    <div class="alert alert-danger">
                        <?= htmlspecialchars($error) ?>
                    </div>
                <?php endif; ?>

                <form method="POST" id="barangForm">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="nama_barang" class="form-label">Nama Barang <span class="text-danger">*</span></label>
                                <input type="text" class="form-control" id="nama_barang" name="nama_barang" 
                                       value="<?= $_POST['nama_barang'] ?? '' ?>" required>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="kategori" class="form-label">Kategori</label>
                                <select class="form-control" id="kategori" name="kategori">
                                    <option value="">Pilih Kategori</option>
                                    <option value="Makanan" <?= ($_POST['kategori'] ?? '') == 'Makanan' ? 'selected' : '' ?>>Makanan</option>
                                    <option value="Minuman" <?= ($_POST['kategori'] ?? '') == 'Minuman' ? 'selected' : '' ?>>Minuman</option>
                                    <option value="Snack" <?= ($_POST['kategori'] ?? '') == 'Snack' ? 'selected' : '' ?>>Snack</option>
                                    <option value="Lainnya" <?= ($_POST['kategori'] ?? '') == 'Lainnya' ? 'selected' : '' ?>>Lainnya</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="harga_beli" class="form-label">Harga Beli <span class="text-danger">*</span></label>
                                <div class="input-group">
                                    <span class="input-group-text">Rp</span>
                                    <input type="number" class="form-control" id="harga_beli" name="harga_beli" 
                                           value="<?= $_POST['harga_beli'] ?? '' ?>" min="0" step="0.01" required>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="harga_jual" class="form-label">Harga Jual <span class="text-danger">*</span></label>
                                <div class="input-group">
                                    <span class="input-group-text">Rp</span>
                                    <input type="number" class="form-control" id="harga_jual" name="harga_jual" 
                                           value="<?= $_POST['harga_jual'] ?? '' ?>" min="0" step="0.01" required>
                                </div>
                                <div class="form-text">
                                    <span id="marginInfo" class="text-muted"></span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="stok" class="form-label">Stok Awal</label>
                                <input type="number" class="form-control" id="stok" name="stok" 
                                       value="<?= $_POST['stok'] ?? '0' ?>" min="0">
                            </div>
                        </div>
                    </div>

                    <div class="d-flex justify-content-between">
                        <a href="index.php?page=barang" class="btn btn-secondary">
                            <i class="fas fa-arrow-left"></i> Kembali
                        </a>
                        <button type="submit" class="btn btn-primary">
                            <i class="fas fa-save"></i> Simpan Barang
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<?php
$content = ob_get_clean();

// JavaScript untuk kalkulasi margin
ob_start();
?>
<script>
$(document).ready(function() {
    // Format currency input
    $('#harga_beli, #harga_jual').on('input', function() {
        calculateMargin();
    });

    function calculateMargin() {
        var hargaBeli = parseFloat($('#harga_beli').val()) || 0;
        var hargaJual = parseFloat($('#harga_jual').val()) || 0;
        
        if (hargaBeli > 0 && hargaJual > 0) {
            var margin = hargaJual - hargaBeli;
            var marginPercent = ((margin / hargaJual) * 100).toFixed(2);
            
            var marginText = 'Margin: Rp ' + margin.toLocaleString('id-ID') + ' (' + marginPercent + '%)';
            
            if (margin < 0) {
                $('#marginInfo').html('<span class="text-danger">' + marginText + ' - Rugi!</span>');
            } else if (margin == 0) {
                $('#marginInfo').html('<span class="text-warning">' + marginText + ' - Tidak ada keuntungan</span>');
            } else {
                $('#marginInfo').html('<span class="text-success">' + marginText + '</span>');
            }
        } else {
            $('#marginInfo').text('');
        }
    }

    // Form validation
    $('#barangForm').on('submit', function(e) {
        var hargaBeli = parseFloat($('#harga_beli').val()) || 0;
        var hargaJual = parseFloat($('#harga_jual').val()) || 0;
        
        if (hargaBeli >= hargaJual) {
            e.preventDefault();
            alert('Harga jual harus lebih besar dari harga beli!');
            return false;
        }
    });
});
</script>
<?php
$scripts = ob_get_clean();

include 'views/layout/template.php';
?>