<?php
    session_start();
    include "../koneksi.php";
    include "../alert.php";

    if(!isset($_SESSION["admin"])){
        showAlert('Lakukan login terlebih dahulu', 'error', 'login.php');
        session_destroy();
    }

    $id = $_GET['id'];
    $sql = "SELECT * FROM product WHERE id_product = $id";
    $query = mysqli_query($koneksi, $sql);
    $data = mysqli_fetch_assoc($query);

    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $id = $_POST['id'];
        $nama = $_POST['nama'];
        $harga = $_POST['harga'];
        $deskripsi = $_POST['deskripsi'];
        $stock = $_POST['stock'];

        $image = $_FILES['gambar'];
        $imagefilename = $image['name'];
        $imagefiletmp = $image['tmp_name'];
        $filename_separate = explode('.', $imagefilename);
        $file_extension = strtolower(end($filename_separate));
        $extension = array('jpeg', 'jpg', 'png');
        if(in_array($file_extension,$extension)){
            $upload_image='../gambar/'.$imagefilename;
            move_uploaded_file($imagefiletmp,$upload_image);
            $tmp_image = 'gambar/'.$imagefilename;
        }
        else{
            $tmp_image = $data['temp'];
        }

        $sql = "UPDATE product SET nama = '$nama', harga = '$harga', deskripsi = '$deskripsi', stock = '$stock', temp = '$tmp_image' WHERE id_product = '$id'";
        $query = mysqli_query($koneksi, $sql);
        
        if($query){
            showAlert('Data berhasil diubah', 'success', 'produk.php');
        }
        else{
            showAlert('Data gagal diubah', 'error', 'produk.php');
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Produk - Admin Dashboard</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
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
        .main-content {
            padding: 2rem;
        }
        .form-container {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 0.5rem;
            margin-bottom: 2rem;
        }
        .current-image {
            max-width: 300px;
            height: auto;
            border-radius: 0.5rem;
            margin: 1rem 0;
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
                        <h2 class="mb-4">Edit Produk</h2>
                    </div>
                </div>

                <div class="form-container">
                    <form method="POST" enctype="multipart/form-data" class="row g-3">
                        <input type="text" name="id" value="<?php echo $data['id_product']; ?>" hidden>
                        
                        <div class="col-md-6">
                            <label for="nama" class="form-label">Nama Produk</label>
                            <input type="text" class="form-control" id="nama" name="nama" 
                                   placeholder="Masukan nama" value="<?php echo $data['nama']; ?>" required>
                        </div>
                        
                        <div class="col-md-6">
                            <label for="harga" class="form-label">Harga</label>
                            <input type="number" class="form-control" id="harga" name="harga" 
                                   placeholder="Masukan harga" value="<?php echo $data['harga']; ?>" required>
                        </div>
                        
                        <div class="col-md-6">
                            <label for="deskripsi" class="form-label">Deskripsi</label>
                            <input type="text" class="form-control" id="deskripsi" name="deskripsi" 
                                   placeholder="Masukan deskripsi" value="<?php echo $data['deskripsi']; ?>" required>
                        </div>
                        
                        <div class="col-md-6">
                            <label for="stock" class="form-label">Stock</label>
                            <input type="number" class="form-control" id="stock" name="stock" 
                                   placeholder="Masukan stock" value="<?php echo $data['stock']; ?>" required>
                        </div>
                        
                        <div class="col-12">
                            <label class="form-label">Gambar Saat Ini</label>
                            <div>
                                <img src="<?php echo '../'.$data['temp']; ?>" alt="gambar" class="current-image">
                            </div>
                        </div>
                        
                        <div class="col-12">
                            <label for="gambar" class="form-label">Ganti Gambar</label>
                            <input type="file" class="form-control" id="gambar" name="gambar" accept="image/*">
                            <div class="form-text">Biarkan kosong jika tidak ingin mengubah gambar. Format yang didukung: JPG, JPEG, PNG</div>
                        </div>
                        
                        <div class="col-12 mt-4">
                            <button type="submit" class="btn btn-primary">
                                <i class="fas fa-save me-2"></i>Simpan Perubahan
                            </button>
                            <a href="produk.php" class="btn btn-secondary">
                                <i class="fas fa-arrow-left me-2"></i>Kembali
                            </a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>