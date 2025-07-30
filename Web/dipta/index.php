<?php
    session_start();
    include "koneksi.php";
    include "alert.php";

    if(!isset($_SESSION["user"]) && !isset($_SESSION["admin"])){
        showAlert('Silahkan login terlebih dahulu', 'warning', 'login.php');
        exit();
    }

    // Get latest products
    $sql = "SELECT * FROM db_project.product ORDER BY id_product DESC LIMIT 6";
    $query = mysqli_query($koneksi, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce - Home</title>
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
        /* Hero Section */
        .hero-section {
            background: linear-gradient(135deg, #4e73df 0%, #224abe 100%);
            color: white;
            padding: 6rem 0;
            margin-bottom: 4rem;
        }
        .hero-title {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }
        .hero-subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 2rem;
        }
        /* Features Section */
        .features-section {
            padding: 4rem 0;
            background: white;
        }
        .feature-card {
            text-align: center;
            padding: 2rem;
            border-radius: 1rem;
            background: white;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            height: 100%;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        .feature-icon {
            font-size: 2.5rem;
            color: #4e73df;
            margin-bottom: 1rem;
        }
        /* Products Section */
        .products-section {
            padding: 4rem 0;
        }
        .section-title {
            font-size: 2rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 2rem;
            text-align: center;
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
        /* Footer */
        .footer {
            background: #2c3e50;
            color: white;
            padding: 4rem 0 2rem;
            margin-top: 4rem;
        }
        .footer-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
        }
        .footer-link {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            transition: all 0.3s ease;
            display: block;
            margin-bottom: 0.5rem;
        }
        .footer-link:hover {
            color: white;
            transform: translateX(5px);
        }
        .social-link {
            color: white;
            font-size: 1.5rem;
            margin-right: 1rem;
            transition: all 0.3s ease;
        }
        .social-link:hover {
            color: #4e73df;
            transform: translateY(-3px);
        }
        .copyright {
            border-top: 1px solid rgba(255,255,255,0.1);
            padding-top: 2rem;
            margin-top: 3rem;
            text-align: center;
            color: rgba(255,255,255,0.6);
        }
        /* Admin Styles */
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
        .admin-card {
            border: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .admin-card .card-body {
            padding: 2rem;
        }
        .admin-stats {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .sidebar .nav-link.text-danger {
            color: #dc3545 !important;
            font-weight: 600;
        }
        .sidebar .nav-link.text-danger:hover {
            background: rgba(220, 53, 69, 0.1);
            color: #dc3545 !important;
        }
    </style>
</head>
<body>
    <?php if(isset($_SESSION["admin"])): ?>
        <div class="container-fluid">
            <div class="row">
                <!-- Admin Sidebar -->
                <div class="col-md-3 col-lg-2 px-0 sidebar">
                    <div class="p-3">
                        <h4 class="text-center mb-4">Admin Panel</h4>
                        <div class="nav flex-column">
                            <a href="index.php" class="nav-link active">
                                <i class="fas fa-home me-2"></i> Dashboard
                            </a>
                            <a href="admin/produk.php" class="nav-link">
                                <i class="fas fa-box me-2"></i> Kelola Produk
                            </a>
                            <a href="admin/pesanan.php" class="nav-link">
                                <i class="fas fa-clipboard-list me-2"></i> Kelola Pesanan
                            </a>
                            <a href="logout.php" class="nav-link text-danger">
                                <i class="fas fa-sign-out-alt me-2"></i> Logout
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Admin Main Content -->
                <div class="col-md-9 col-lg-10 main-content">
                    <div class="row mb-4">
                        <div class="col-12">
                            <h2 class="mb-4">Admin Dashboard</h2>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-4">
                            <div class="card admin-card bg-white">
                                <div class="card-body">
                                    <div class="d-flex justify-content-between align-items-center mb-4">
                                        <div>
                                            <h5 class="card-title mb-0">Kelola Produk</h5>
                                            <p class="text-muted mb-0">Tambah, edit, atau hapus produk</p>
                                        </div>
                                        <div class="admin-stats text-primary">
                                            <i class="fas fa-box"></i>
                                        </div>
                                    </div>
                                    <a href="admin/produk.php" class="btn btn-primary">
                                        <i class="fas fa-arrow-right me-2"></i>Kelola Produk
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-4">
                            <div class="card admin-card bg-white">
                                <div class="card-body">
                                    <div class="d-flex justify-content-between align-items-center mb-4">
                                        <div>
                                            <h5 class="card-title mb-0">Kelola Pesanan</h5>
                                            <p class="text-muted mb-0">Lihat dan konfirmasi pesanan</p>
                                        </div>
                                        <div class="admin-stats text-success">
                                            <i class="fas fa-clipboard-list"></i>
                                        </div>
                                    </div>
                                    <a href="admin/pesanan.php" class="btn btn-success">
                                        <i class="fas fa-arrow-right me-2"></i>Kelola Pesanan
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    <?php else: ?>
        <!-- Navbar -->
        <nav class="navbar navbar-expand-lg navbar-dark">
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
                            <a class="nav-link active" href="index.php">
                                <i class="fas fa-home me-1"></i> Home
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="produk.php">
                                <i class="fas fa-box me-1"></i> Produk
                            </a>
                        </li>
                        <?php if(isset($_SESSION["user"])): ?>
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
                        <?php else: ?>
                            <li class="nav-item">
                                <a class="nav-link" href="login.php">
                                    <i class="fas fa-sign-in-alt me-1"></i> Login
                                </a>
                            </li>
                        <?php endif; ?>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="hero-section">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-md-6">
                        <h1 class="hero-title">Selamat Datang di E-Commerce Kami</h1>
                        <p class="hero-subtitle">Temukan berbagai produk berkualitas dengan harga terbaik untuk kebutuhan Anda.</p>
                        <a href="produk.php" class="btn btn-light btn-lg">
                            <i class="fas fa-shopping-bag me-2"></i>Belanja Sekarang
                        </a>
                    </div>
                    <div class="col-md-6">
                        <img src="assets/hero-image.png" alt="Shopping" class="img-fluid">
                    </div>
                </div>
            </div>
        </section>

        <!-- Features Section -->
        <section class="features-section">
            <div class="container">
                <div class="row g-4">
                    <div class="col-md-4">
                        <div class="feature-card">
                            <i class="fas fa-truck feature-icon"></i>
                            <h3>Pengiriman Cepat</h3>
                            <p>Layanan pengiriman cepat ke seluruh Indonesia dengan berbagai pilihan kurir.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="feature-card">
                            <i class="fas fa-shield-alt feature-icon"></i>
                            <h3>Pembayaran Aman</h3>
                            <p>Transaksi aman dengan berbagai metode pembayaran yang terpercaya.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="feature-card">
                            <i class="fas fa-headset feature-icon"></i>
                            <h3>Layanan 24/7</h3>
                            <p>Customer service siap membantu Anda kapan saja dan di mana saja.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Latest Products Section -->
        <section class="products-section">
            <div class="container">
                <h2 class="section-title">Produk Terbaru</h2>
                <div class="row g-4">
                    <?php while($data = mysqli_fetch_assoc($query)): ?>
                        <div class="col-md-4">
                            <div class="product-card">
                                <img src="<?php echo $data['temp']; ?>" alt="<?php echo $data['nama']; ?>" class="product-image">
                                <div class="p-3">
                                    <h5 class="product-title"><?php echo $data['nama']; ?></h5>
                                    <p class="product-description"><?php echo $data['deskripsi']; ?></p>
                                    <div class="d-flex justify-content-between align-items-center">
                                        <div class="product-price">Rp <?php echo number_format($data['harga'], 0, ',', '.'); ?></div>
                                        <a href="produk.php" class="btn btn-primary">
                                            <i class="fas fa-shopping-cart me-2"></i>Beli
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    <?php endwhile; ?>
                </div>
                <div class="text-center mt-4">
                    <a href="produk.php" class="btn btn-outline-primary btn-lg">
                        Lihat Semua Produk
                    </a>
                </div>
            </div>
        </section>
    <?php endif; ?>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <h5 class="footer-title">Tentang Kami</h5>
                    <p>E-Commerce terpercaya dengan berbagai produk berkualitas untuk memenuhi kebutuhan Anda.</p>
                    <div class="mt-3">
                        <a href="#" class="social-link"><i class="fab fa-facebook"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-twitter"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
                <div class="col-md-4">
                    <h5 class="footer-title">Link Cepat</h5>
                    <a href="index.php" class="footer-link">Home</a>
                    <a href="produk.php" class="footer-link">Produk</a>
                    <a href="keranjang.php" class="footer-link">Keranjang</a>
                    <a href="riwayat_pesanan.php" class="footer-link">Riwayat Pesanan</a>
                </div>
                <div class="col-md-4">
                    <h5 class="footer-title">Kontak</h5>
                    <p><i class="fas fa-map-marker-alt me-2"></i>Jl. Contoh No. 123, Jakarta</p>
                    <p><i class="fas fa-phone me-2"></i>+62 123 4567 890</p>
                    <p><i class="fas fa-envelope me-2"></i>info@ecommerce.com</p>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2024 E-Commerce. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>