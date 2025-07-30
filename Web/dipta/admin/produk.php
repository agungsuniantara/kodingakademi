<?php
    session_start();
    include "../koneksi.php";
    include "../alert.php";

    if(!isset($_SESSION["admin"])){
        showAlert('Lakukan login terlebih dahulu', 'error', 'login.php');
        session_destroy();
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST"){
        $productname = $_POST['nama'];
        $harga = $_POST['harga'];
        $deskripsi = $_POST['deskripsi'];
        $stock = $_POST['stock'];
    
        $image = $_FILES['gambar'];
        
        // Check for upload errors
        if ($image['error'] !== UPLOAD_ERR_OK) {
            $error_message = match($image['error']) {
                UPLOAD_ERR_INI_SIZE, UPLOAD_ERR_FORM_SIZE => 'Ukuran file terlalu besar. Maksimal 1MB',
                UPLOAD_ERR_PARTIAL => 'File hanya terupload sebagian',
                UPLOAD_ERR_NO_FILE => 'Tidak ada file yang diupload',
                UPLOAD_ERR_NO_TMP_DIR => 'Folder temporary tidak ditemukan',
                UPLOAD_ERR_CANT_WRITE => 'Gagal menulis file ke disk',
                UPLOAD_ERR_EXTENSION => 'Upload dihentikan oleh ekstensi PHP',
                default => 'Terjadi kesalahan saat upload'
            };
            showAlert($error_message, 'error', 'produk.php');
            exit();
        }

        $imagefilename = $image['name'];
        $imagefiletmp = $image['tmp_name'];
        $filesize = $image['size']; // Get file size in bytes
        
        // Check if file size is more than 1MB (1MB = 1048576 bytes)
        if($filesize > 1048576) {
            showAlert('Ukuran file terlalu besar. Maksimal 1MB', 'error', 'produk.php');
            exit();
        }
        
        $filename_separate = explode('.', $imagefilename);
        $file_extension = strtolower(end($filename_separate));
        $extension = array('jpeg', 'jpg', 'png');
        if(in_array($file_extension,$extension)){
            $upload_image='../gambar/'.$imagefilename;
            move_uploaded_file($imagefiletmp,$upload_image);
            $tmp_image = 'gambar/'.$imagefilename;
    
            $sql = "INSERT INTO db_project.product (nama, harga, deskripsi, stock, temp) VALUES ('$productname', '$harga', '$deskripsi', '$stock', '$tmp_image')";
    
            $query=mysqli_query($koneksi,$sql);
    
            if($query)
            {
                showAlert('Tambah produk berhasil', 'success', 'produk.php');
            }
            else
            {   
                showAlert('Tambah produk gagal', 'error', '../index.php');
            }	
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kelola Produk - Admin Dashboard</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <!-- SweetAlert2 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css">
    <style>
        .sidebar {
            min-height: 100vh;
            background: #343a40;
            color: white;
        }
        .sidebar .nav-link {
            color: rgba(255,255,255,.8);
            padding: 1rem;
            margin: 0.2rem 0;
            border-radius: 0.25rem;
        }
        .sidebar .nav-link:hover {
            background: rgba(255,255,255,.1);
            color: white;
        }
        .sidebar .nav-link.active {
            background: #0d6efd;
            color: white;
        }
        .sidebar .nav-link.text-danger {
            color: #dc3545 !important;
            font-weight: 600;
        }
        .sidebar .nav-link.text-danger:hover {
            background: rgba(220, 53, 69, 0.1);
            color: #dc3545 !important;
        }
        .main-content {
            padding: 2rem;
        }
        .product-image {
            max-width: 100px;
            height: auto;
        }
        .form-container {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 0.5rem;
            margin-bottom: 2rem;
        }
    </style>
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <!-- Sidebar -->
            <div class="col-md-3 col-lg-2 px-0 sidebar">
                <div class="p-3">
                    <h4 class="text-center mb-4">Admin Panel</h4>
                    <div class="nav flex-column">
                        <a href="../index.php" class="nav-link">
                            <i class="fas fa-home me-2"></i> Dashboard
                        </a>
                        <a href="produk.php" class="nav-link active">
                            <i class="fas fa-box me-2"></i> Kelola Produk
                        </a>
                        <a href="pesanan.php" class="nav-link">
                            <i class="fas fa-clipboard-list me-2"></i> Kelola Pesanan
                        </a>
                        <a href="../logout.php" class="nav-link text-danger">
                            <i class="fas fa-sign-out-alt me-2"></i> Logout
                        </a>
                    </div>
                </div>
            </div>

            <!-- Main Content -->
            <div class="col-md-9 col-lg-10 main-content">
                <div class="row mb-4">
                    <div class="col-12">
                        <h2 class="mb-4">Kelola Produk</h2>
                    </div>
                </div>

                <!-- Add Product Form -->
                <div class="form-container">
                    <h4 class="mb-4">Tambah Produk Baru</h4>
                    <form method="POST" enctype="multipart/form-data" class="row g-3">
                        <div class="col-md-6">
                            <label for="nama" class="form-label">Nama Produk</label>
                            <input type="text" class="form-control" id="nama" name="nama" placeholder="Masukan nama" required>
                        </div>
                        <div class="col-md-6">
                            <label for="harga" class="form-label">Harga</label>
                            <input type="number" class="form-control" id="harga" name="harga" placeholder="Masukan harga" required>
                        </div>
                        <div class="col-md-6">
                            <label for="deskripsi" class="form-label">Deskripsi</label>
                            <input type="text" class="form-control" id="deskripsi" name="deskripsi" placeholder="Masukan deskripsi" required>
                        </div>
                        <div class="col-md-6">
                            <label for="stock" class="form-label">Stock</label>
                            <input type="number" class="form-control" id="stock" name="stock" placeholder="Masukan stock" required>
                        </div>
                        <div class="col-12">
                            <label for="gambar" class="form-label">Gambar Produk</label>
                            <input type="file" class="form-control" id="gambar" name="gambar" accept="image/*" required>
                            <div class="form-text">Maksimal ukuran file 1MB. Format yang didukung: JPG, JPEG, PNG</div>
                        </div>
                        <div class="col-12">
                            <button type="submit" class="btn btn-primary">
                                <i class="fas fa-save me-2"></i>Simpan Produk
                            </button>
                        </div>
                    </form>
                </div>

                <!-- Products Table -->
                <div class="table-responsive">
                    <table class="table table-striped table-hover">
                        <thead class="table-dark">
                            <tr>
                                <th>No</th>
                                <th>Nama</th>
                                <th>Harga</th>
                                <th>Deskripsi</th>
                                <th>Stock</th>
                                <th>Gambar</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php
                                include "../koneksi.php";
                                $sql="select * from db_project.product";
                                $query=mysqli_query($koneksi, $sql);
                                $no = 0;
                                while ($data=mysqli_fetch_assoc($query)):
                                    $no++;
                            ?>
                            <tr>
                                <td><?php echo $no; ?></td>
                                <td><?php echo $data['nama']; ?></td>
                                <td>Rp <?php echo number_format($data['harga'], 0, ',', '.'); ?></td>
                                <td><?php echo $data['deskripsi']; ?></td>
                                <td><?php echo $data['stock']; ?></td>
                                <td>
                                    <img src="<?php echo '../'.$data['temp']; ?>" alt="gambar" class="product-image">
                                </td>
                                <td>
                                    <a href="edit.php?id=<?php echo $data['id_product']; ?>" class="btn btn-warning btn-sm">
                                        <i class="fas fa-edit"></i> Edit
                                    </a>
                                    <button 
                                        class="btn btn-danger btn-sm btn-hapus" 
                                        data-id="<?php echo $data['id_product']; ?>"
                                        data-nama="<?php echo htmlspecialchars($data['nama']); ?>"
                                    >
                                        <i class="fas fa-trash"></i> Hapus
                                    </button>
                                </td>
                            </tr>
                            <?php endwhile; ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- SweetAlert2 JS -->
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script>
        document.querySelectorAll('.btn-hapus').forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                var id = this.getAttribute('data-id');
                var nama = this.getAttribute('data-nama');
                Swal.fire({
                    title: 'Hapus Produk?',
                    html: 'Apakah Anda yakin ingin menghapus <b>' + nama + '</b>?',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#d33',
                    cancelButtonColor: '#aaa',
                    confirmButtonText: 'Ya, Hapus!',
                    cancelButtonText: 'Batal'
                }).then((result) => {
                    if (result.isConfirmed) {
                        // Redirect ke hapus.php
                        window.location.href = 'hapus.php?id=' + id;
                    }
                });
            });
        });
    </script>
</body>
</html>
