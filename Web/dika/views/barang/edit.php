<?php
$page = 'barang';
$pageTitle = 'Edit Barang';

ob_start();

// Ambil ID barang dari parameter URL
$id_barang = isset($_GET['id']) ? (int)$_GET['id'] : 0;

if ($id_barang == 0) {
    header('Location: index.php?page=barang');
    exit;
}

// Konfigurasi database - sesuaikan dengan setting Anda
$host = 'localhost';
$dbname = 'kasir_db';
$username = 'root';
$password = 'root';

// Buat koneksi database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
} catch(PDOException $e) {
    die("Connection failed: " . $e->getMessage() . "<br>Please check your database configuration.");
}

// Ambil data barang berdasarkan ID
try {
    $stmt = $pdo->prepare("SELECT * FROM barang WHERE id_barang = ?");
    $stmt->execute([$id_barang]);
    $barang = $stmt->fetch();
    
    if (!$barang) {
        echo "<div class='alert alert-danger'>Data barang dengan ID $id_barang tidak ditemukan.</div>";
        echo "<a href='index.php?page=barang' class='btn btn-secondary'>Kembali ke Daftar Barang</a>";
        exit;
    }
} catch(PDOException $e) {
    echo "<div class='alert alert-danger'>Database Error: " . $e->getMessage() . "</div>";
    echo "<a href='index.php?page=barang' class='btn btn-secondary'>Kembali ke Daftar Barang</a>";
    exit;
}

// Proses form submit
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    try {
        // Validasi input
        $required_fields = ['nama_barang', 'kategori', 'harga_beli', 'harga_jual', 'stok'];
        foreach ($required_fields as $field) {
            if (empty($_POST[$field])) {
                throw new Exception("Field $field harus diisi");
            }
        }
        
        $stmt = $pdo->prepare("UPDATE barang SET 
            nama_barang = ?, 
            kategori = ?, 
            harga_beli = ?, 
            harga_jual = ?, 
            stok = ?,
            updated_at = CURRENT_TIMESTAMP
            WHERE id_barang = ?");
        
        $result = $stmt->execute([
            trim($_POST['nama_barang']),
            trim($_POST['kategori']),
            (float)$_POST['harga_beli'],
            (float)$_POST['harga_jual'],
            (int)$_POST['stok'],
            $id_barang
        ]);
        
        if ($result) {
            echo "<script>alert('Data berhasil diupdate!'); window.location='index.php?page=barang';</script>";
            exit;
        } else {
            $error = "Gagal mengupdate data";
        }
    } catch(Exception $e) {
        $error = $e->getMessage();
    } catch(PDOException $e) {
        $error = "Database error: " . $e->getMessage();
    }
}

// Ambil kategori untuk dropdown
try {
    $stmt = $pdo->query("SELECT DISTINCT kategori FROM barang WHERE kategori IS NOT NULL AND kategori != '' ORDER BY kategori");
    $kategoris = $stmt->fetchAll(PDO::FETCH_COLUMN);
    
    // Jika tidak ada kategori, berikan default
    if (empty($kategoris)) {
        $kategoris = ['Makanan', 'Minuman', 'Elektronik', 'Pakaian', 'Alat Tulis', 'Lainnya'];
    }
} catch(PDOException $e) {
    // Default categories jika query gagal
    $kategoris = ['Makanan', 'Minuman', 'Elektronik', 'Pakaian', 'Alat Tulis', 'Lainnya'];
}
?>

<div class="container-fluid">
<!-- <div class="row">
        <div class="col-12">
            <div class="page-header">
                <h1 class="page-title">Edit Barang</h1>
                <nav aria-label="breadcrumb">
                    
                     <ol class="breadcrumb">
                        <li class="breadcrumb-item"><a href="index.php">Dashboard</a></li>
                        <li class="breadcrumb-item"><a href="index.php?page=barang">Kelola Barang</a></li>
                        <li class="breadcrumb-item active" aria-current="page">Edit Barang</li>
                    </ol> 
                </nav>
            </div>
        </div>
    </div> -->
   
    <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
            <div class="card">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0">
                        <i class="fas fa-edit me-2"></i>Form Edit Barang
                    </h5>
                    <a href="index.php?page=barang" class="btn btn-secondary btn-sm">
                        <i class="fas fa-arrow-left me-1"></i>Kembali
                    </a>
                </div>
                
                <div class="card-body">
                    <?php if (isset($error)): ?>
                        <div class="alert alert-danger alert-dismissible fade show" role="alert">
                            <i class="fas fa-exclamation-triangle me-2"></i>
                            <?php echo htmlspecialchars($error); ?>
                            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                        </div>
                    <?php endif; ?>

                    <form method="POST" class="needs-validation" novalidate>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="mb-3">
                                    <label for="nama_barang" class="form-label">
                                        Nama Barang <span class="text-danger">*</span>
                                    </label>
                                    <input type="text" 
                                           class="form-control" 
                                           id="nama_barang" 
                                           name="nama_barang" 
                                           value="<?php echo htmlspecialchars($barang['nama_barang']); ?>" 
                                           required>
                                    <div class="invalid-feedback">
                                        Nama barang harus diisi.
                                    </div>
                                </div>
                            </div>
                            
                            <div class="col-md-6">
                                <div class="mb-3">
                                    <label for="kategori" class="form-label">
                                        Kategori <span class="text-danger">*</span>
                                    </label>
                                    <select class="form-select" id="kategori" name="kategori" required>
                                        <option value="">Pilih Kategori</option>
                                        <?php foreach ($kategoris as $kategori): ?>
                                            <option value="<?php echo htmlspecialchars($kategori); ?>" 
                                                    <?php echo ($barang['kategori'] == $kategori) ? 'selected' : ''; ?>>
                                                <?php echo htmlspecialchars($kategori); ?>
                                            </option>
                                        <?php endforeach; ?>
                                    </select>
                                    <div class="invalid-feedback">
                                        Kategori harus dipilih.
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-4">
                                <div class="mb-3">
                                    <label for="harga_beli" class="form-label">
                                        Harga Beli <span class="text-danger">*</span>
                                    </label>
                                    <div class="input-group">
                                        <span class="input-group-text">Rp</span>
                                        <input type="number" 
                                               class="form-control" 
                                               id="harga_beli" 
                                               name="harga_beli" 
                                               value="<?php echo $barang['harga_beli']; ?>" 
                                               min="0" 
                                               step="0.01" 
                                               required>
                                        <div class="invalid-feedback">
                                            Harga beli harus diisi dan valid.
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="col-md-4">
                                <div class="mb-3">
                                    <label for="harga_jual" class="form-label">
                                        Harga Jual <span class="text-danger">*</span>
                                    </label>
                                    <div class="input-group">
                                        <span class="input-group-text">Rp</span>
                                        <input type="number" 
                                               class="form-control" 
                                               id="harga_jual" 
                                               name="harga_jual" 
                                               value="<?php echo $barang['harga_jual']; ?>" 
                                               min="0" 
                                               step="0.01" 
                                               required>
                                        <div class="invalid-feedback">
                                            Harga jual harus diisi dan valid.
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="col-md-4">
                                <div class="mb-3">
                                    <label for="stok" class="form-label">
                                        Stok <span class="text-danger">*</span>
                                    </label>
                                    <input type="number" 
                                           class="form-control" 
                                           id="stok" 
                                           name="stok" 
                                           value="<?php echo $barang['stok']; ?>" 
                                           min="0" 
                                           required>
                                    <div class="invalid-feedback">
                                        Stok harus diisi dan valid.
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="card mt-4">
                            <div class="card-body bg-light">
                                <h6 class="card-title">Informasi Margin</h6>
                                <div class="row">
                                    <div class="col-md-6">
                                        <small class="text-muted">Margin Keuntungan:</small>
                                        <div class="fw-bold" id="margin-amount">Rp 0</div>
                                    </div>
                                    <div class="col-md-6">
                                        <small class="text-muted">Persentase Margin:</small>
                                        <div class="fw-bold" id="margin-percent">0%</div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="d-flex justify-content-between mt-4">
                            <a href="index.php?page=barang" class="btn btn-secondary">
                                <i class="fas fa-times me-1"></i>Batal
                            </a>
                            <button type="submit" class="btn btn-primary">
                                <i class="fas fa-save me-1"></i>Update Barang
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Hitung margin ketika harga berubah
    function hitungMargin() {
        const hargaBeli = parseFloat(document.getElementById('harga_beli').value) || 0;
        const hargaJual = parseFloat(document.getElementById('harga_jual').value) || 0;
        
        const margin = hargaJual - hargaBeli;
        const marginPercent = hargaBeli > 0 ? ((margin / hargaBeli) * 100) : 0;
        
        document.getElementById('margin-amount').textContent = 
            'Rp ' + margin.toLocaleString('id-ID');
        document.getElementById('margin-percent').textContent = 
            marginPercent.toFixed(2) + '%';
            
        // Ubah warna berdasarkan margin
        const marginAmountEl = document.getElementById('margin-amount');
        const marginPercentEl = document.getElementById('margin-percent');
        
        if (margin < 0) {
            marginAmountEl.className = 'fw-bold text-danger';
            marginPercentEl.className = 'fw-bold text-danger';
        } else if (margin === 0) {
            marginAmountEl.className = 'fw-bold text-warning';
            marginPercentEl.className = 'fw-bold text-warning';
        } else {
            marginAmountEl.className = 'fw-bold text-success';
            marginPercentEl.className = 'fw-bold text-success';
        }
    }

    // Event listeners untuk hitung margin
    document.getElementById('harga_beli').addEventListener('input', hitungMargin);
    document.getElementById('harga_jual').addEventListener('input', hitungMargin);
    
    // Hitung margin awal
    hitungMargin();

    // Validasi harga jual tidak boleh kurang dari harga beli
    document.getElementById('harga_jual').addEventListener('blur', function() {
        const hargaBeli = parseFloat(document.getElementById('harga_beli').value) || 0;
        const hargaJual = parseFloat(this.value) || 0;
        
        if (hargaJual < hargaBeli && hargaBeli > 0) {
            if (confirm('Harga jual lebih rendah dari harga beli. Apakah Anda yakin?')) {
                // User konfirmasi, biarkan
            } else {
                this.focus();
            }
        }
    });

    // Auto generate kode barang jika kosong - REMOVED karena tidak ada field kode_barang
    
    // Focus ke nama barang saat halaman load
    document.getElementById('nama_barang').focus();
});
</script>

<?php
$content = ob_get_clean();
include 'views/layout/template.php';
?>