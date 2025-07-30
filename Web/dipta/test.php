<?php
    session_start();
    include "koneksi.php";
    include "alert.php";

    if(!isset($_SESSION["user"]) && !isset($_SESSION["admin"])){
        showAlert('Silahkan login terlebih dahulu', 'warning', 'login.php');
        exit();
    }

    $sql = "SELECT * FROM db_project.product";
    $query = mysqli_query($koneksi, $sql);
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UPTD Dinas Perikanan & Kelautan</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background: #f8f9fa;
        }
        .hero-section {
            background: #2991cb;
            color: #fff;
            padding: 70px 0 60px 0;
            text-align: center;
        }
        .hero-title {
            font-size: 1.6rem;
            font-weight: 700;
        }
        .hero-subtitle {
            font-size: 1.15rem;
            margin-top: 15px;
        }
        .section-title {
            font-weight: 700;
            font-size: 1.35rem;
            margin-bottom: 0.5rem;
        }
        .main-card {
            background: #fff;
            border-radius: 1rem;
            box-shadow: 0 0 20px rgba(0,0,0,0.04);
            padding: 36px 32px;
            margin: 30px auto 32px auto;
            max-width: 500px;
            text-align: center;
        }
        .btn-orange {
            background: #fd7904;
            color: #fff;
            font-weight: 600;
            border: none;
            padding: 0.7rem 2.2rem;
            border-radius: 8px;
            transition: 0.2s;
        }
        .btn-orange:hover {
            background: #f26400;
            color: #fff;
        }
        .why-box {
            background: #fafbfc;
            border-radius: 14px;
            box-shadow: 0 0 10px rgba(0,0,0,0.04);
            padding: 25px 12px 18px 12px;
            margin: 7px 0;
            min-height: 130px;
            text-align: center;
        }
        .why-icon {
            color: #2991cb;
            font-size: 1.5rem;
            margin-bottom: 8px;
        }
        .why-title {
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 5px;
        }
        .testimonial-section {
            background: #e9f6ff;
            padding: 44px 0 30px 0;
            margin-top: 42px;
        }
        .testimonial-card {
            background: #fff;
            border-radius: 18px;
            box-shadow: 0 2px 14px rgba(0,0,0,0.07);
            padding: 28px 24px 18px 24px;
            max-width: 480px;
            margin: 0 auto;
            text-align: center;
        }
        .testimonial-quote {
            font-size: 1.14rem;
            font-style: italic;
            color: #353535;
            margin-bottom: 10px;
        }
        .testimonial-author {
            color: #2991cb;
            font-weight: 600;
            font-size: 1rem;
        }
        .footer {
            background: #1e7bbf;
            color: #fff;
            padding: 25px 0 7px 0;
            text-align: center;
            font-size: 0.95rem;
            margin-top: 44px;
        }
        .footer a {
            color: #fff;
            text-decoration: underline;
        }
        @media (max-width: 991px) {
            .main-card { padding: 28px 10px; }
            .hero-section { padding: 54px 0 40px 0; }
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark" style="background: #2991cb;">
        <div class="container">
            <span class="navbar-brand fw-bold" style="font-size: 1.05rem;">
                UPTD Dinas Perikanan & Kelautan
            </span>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link <?php if(basename($_SERVER['PHP_SELF']) == 'index.php') echo 'active'; ?>" href="index.php">Beranda</a></li>
                    <li class="nav-item"><a class="nav-link" href="produk.php">Produk</a></li>
                    <li class="nav-item"><a class="nav-link" href="kontak.php">Kontak</a></li>
                    <li class="nav-item"><a class="nav-link" href="riwayat_pesanan.php">Pesanan</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
        <div class="container">
            <div class="hero-title">Benih Ikan & Udang Berkualitas</div>
            <div class="hero-subtitle">Solusi terbaik untuk budidaya perikanan Andal</div>
        </div>
    </section>

    <!-- Tentang Kami -->
    <div class="container">
        <div class="main-card mt-4">
            <div class="section-title">Tentang Kami</div>
            <div class="mb-3" style="font-size:1rem;">
                Kami menyediakan benih ikan dan udang berkualitas tinggi untuk pembudidaya di seluruh Indonesia.
            </div>
            <a href="produk.php" class="btn btn-orange">Cara Belanja</a>
        </div>
    </div>

    <!-- Kenapa Memilih Kami? -->
    <div class="container">
        <div class="text-center" style="font-size:1.17rem;font-weight:600;margin-bottom:12px;margin-top:20px;">
            Kenapa Memilih Kami?
        </div>
        <div class="row justify-content-center">
            <div class="col-12 col-md-4 mb-3">
                <div class="why-box">
                    <div class="why-icon"><i class="fa-solid fa-fish"></i></div>
                    <div class="why-title">Benih Berkualitas</div>
                    <div style="font-size:0.97rem;">Benih ikan dan udang unggulan yang sehat dan siap dibudidayakan.</div>
                </div>
            </div>
            <div class="col-12 col-md-4 mb-3">
                <div class="why-box">
                    <div class="why-icon"><i class="fa-solid fa-truck-fast"></i></div>
                    <div class="why-title">Pengiriman Cepat</div>
                    <div style="font-size:0.97rem;">Kami bekerja sama dengan jasa ekspedisi terpercaya.</div>
                </div>
            </div>
            <div class="col-12 col-md-4 mb-3">
                <div class="why-box">
                    <div class="why-icon"><i class="fa-solid fa-tags"></i></div>
                    <div class="why-title">Harga Terjangkau</div>
                    <div style="font-size:0.97rem;">Dapatkan benih terbaik dengan harga kompetitif.</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Testimoni -->
    <div class="testimonial-section">
        <div class="container">
            <div class="text-center mb-3" style="font-size:1.13rem;font-weight:600;">
                <i class="fa-regular fa-comments"></i>
                Apa Kata Mereka?
            </div>
            <div class="testimonial-card">
                <div class="testimonial-quote">“Benihnya sehat dan pertumbuhannya cepat!”</div>
                <div class="testimonial-author">- Pak Made, Petani Ikan Koi di Gianyar</div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <div class="footer">
        &copy; 2025 UPTD Dinas Perikanan & Kelautan | Penjualan Benih Ikan & Udang<br>
        <a href="https://wa.me/6281234567890" target="_blank">Hubungi via WhatsApp</a>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
