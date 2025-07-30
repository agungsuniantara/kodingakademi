<?php
    session_start();
    include "koneksi.php";
    include "alert.php";

    if(!isset($_SESSION["user"])){
        showAlert('Silahkan login terlebih dahulu', 'warning', 'login.php');
        exit();
    }

    // Handle add to cart
    if(isset($_POST['add_to_cart'])) {
        $id_product = $_POST['id_product'];
        $id_user = $_SESSION["id_user"];
        $quantity = 1; // default
    
        // Cek stok produk dulu
        $stock_sql = "SELECT stock FROM db_project.product WHERE id_product = '$id_product'";
        $stock_query = mysqli_query($koneksi, $stock_sql);
        $product = mysqli_fetch_assoc($stock_query);
    
        if(!$product || $product['stock'] <= 0) {
            showAlert('Stok produk habis, tidak dapat menambahkan ke keranjang', 'error', 'produk.php');
            exit();
        }
    
        // Cek apakah produk sudah ada di cart
        $check_sql = "SELECT * FROM db_project.cart WHERE id_product = '$id_product' AND id_user = '$id_user'";
        $check_query = mysqli_query($koneksi, $check_sql);
    
        if(mysqli_num_rows($check_query) == 0) {
            // Insert new cart item
            $insert_sql = "INSERT INTO db_project.cart (id_user, id_product, quantity) VALUES ('$id_user', '$id_product', '$quantity')";
            $insert_query = mysqli_query($koneksi, $insert_sql);
    
            if(!$insert_query) {
                showAlert('Gagal menambahkan ke keranjang', 'error', 'produk.php');
            } else {
                showAlert('Produk berhasil ditambahkan ke keranjang', 'success', 'keranjang.php');
            }
        } else {
            // Produk sudah ada di keranjang
            showAlert('Produk sudah ada di keranjang', 'warning', 'keranjang.php');
        }
    }
    

    $sql = "SELECT * FROM db_project.product";
    $query = mysqli_query($koneksi, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Produk - E-Commerce</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .navbar {
            background: linear-gradient(135deg, #4e73df 0%, #224abe 100%);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .navbar-brand {
            font-weight: 600;
            color: white !important;
        }
        .nav-link {
            color: rgba(255,255,255,0.9) !important;
            transition: all 0.3s ease;
        }
        .nav-link:hover {
            color: white !important;
            transform: translateY(-1px);
        }
        .product-card {
            background: white;
            border-radius: 1rem;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            height: 100%;
        }
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        .product-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 1rem 1rem 0 0;
        }
        .product-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2c3e50;
            margin: 1rem 0;
        }
        .product-price {
            font-size: 1.2rem;
            font-weight: 700;
            color: #224abe;
        }
        .product-description {
            color: #6c757d;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        .quantity-input {
            width: 80px;
            text-align: center;
            border: 2px solid #e9ecef;
            border-radius: 0.5rem;
            padding: 0.5rem;
            margin-bottom: 1rem;
        }
        .btn-add-cart {
            background: #28a745;
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 0.5rem;
            transition: all 0.3s ease;
            font-weight: 600;
            width: 100%;
        }
        .btn-add-cart:hover {
            background: #218838;
            color: white;
            transform: translateY(-2px);
        }
        .stock-info {
            color: #6c757d;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }
        .search-container {
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
            margin-bottom: 2rem;
        }
        .search-input {
            border: 2px solid #e9ecef;
            border-radius: 0.5rem;
            padding: 0.8rem 1rem;
            transition: all 0.3s ease;
        }
        .search-input:focus {
            border-color: #224abe;
            box-shadow: 0 0 0 0.2rem rgba(34,74,190,0.25);
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="index.php">
                <i class="fas fa-store me-2"></i>E-Commerce
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="index.php">
                            <i class="fas fa-home me-1"></i> Home
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="produk.php">
                            <i class="fas fa-box me-1"></i> Produk
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="keranjang.php">
                            <i class="fas fa-shopping-cart me-1"></i> Cart
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="riwayat_pesanan.php">
                            <i class="fas fa-history me-1"></i> Riwayat
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="logout.php">
                            <i class="fas fa-sign-out-alt me-1"></i> Logout
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container">
        <!-- Search Section -->
        <div class="search-container">
            <div class="row">
                <div class="col-md-6 mx-auto">
                    <form action="" method="GET" class="d-flex">
                        <input type="text" name="search" class="form-control search-input" placeholder="Cari produk..." value="<?php echo isset($_GET['search']) ? htmlspecialchars($_GET['search']) : ''; ?>">
                        <button type="submit" class="btn btn-primary ms-2">
                            <i class="fas fa-search"></i>
                        </button>
                    </form>
                </div>
            </div>
        </div>

        <!-- Products Grid -->
        <div class="row g-4">
            <?php
                $search = isset($_GET['search']) ? $_GET['search'] : '';
                $sql = "SELECT * FROM db_project.product WHERE nama LIKE '%$search%' OR deskripsi LIKE '%$search%'";
                $query = mysqli_query($koneksi, $sql);
                
                while($data = mysqli_fetch_assoc($query)):
            ?>
            <div class="col-md-6 col-lg-4">
                <div class="product-card">
                    <img src="<?php echo $data['temp']; ?>" alt="<?php echo $data['nama']; ?>" class="product-image">
                    <div class="p-3">
                        <h5 class="product-title"><?php echo $data['nama']; ?></h5>
                        <p class="product-description"><?php echo $data['deskripsi']; ?></p>
                        <div class="product-price mb-2">Rp <?php echo number_format($data['harga'], 0, ',', '.'); ?></div>
                        <div class="stock-info">Stok: <?php echo $data['stock']; ?></div>
                        <form method="POST">
                            <input type="hidden" name="id_product" value="<?php echo $data['id_product']; ?>">
                            <button type="submit" name="add_to_cart" class="btn btn-add-cart">
                                <i class="fas fa-cart-plus me-2"></i>Tambah ke Keranjang
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        <?php endwhile; ?>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>