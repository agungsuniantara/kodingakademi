<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $title ?? 'Sistem Kasir' ?></title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="assets/css/style.css" rel="stylesheet">
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <!-- Sidebar -->
            <nav class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
                <div class="position-sticky pt-3">
                    <div class="text-center mb-4">
                        <h4 class="text-primary">
                            <i class="fas fa-cash-register"></i> Sistem Kasir
                        </h4>
                    </div>
                    
                    <ul class="nav flex-column">
                        <li class="nav-item">
                            <a class="nav-link <?= ($page ?? '') == 'dashboard' ? 'active' : '' ?>" 
                               href="index.php?page=dashboard">
                                <i class="fas fa-tachometer-alt"></i> Dashboard
                            </a>
                        </li>
                        
                        <li class="nav-item">
                            <a class="nav-link <?= ($page ?? '') == 'barang' ? 'active' : '' ?>" 
                               href="index.php?page=barang">
                                <i class="fas fa-box"></i> Kelola Barang
                            </a>
                        </li>
                        
                        <li class="nav-item">
                            <a class="nav-link <?= ($page ?? '') == 'transaksi' ? 'active' : '' ?>" 
                               href="index.php?page=transaksi">
                                <i class="fas fa-shopping-cart"></i> Kelola Transaksi
                            </a>
                        </li>
                        
                        <!-- Dropdown Laporan -->
                        <li class="nav-item">
                            <a class="nav-link collapsed" href="#" data-bs-toggle="collapse" data-bs-target="#laporanSubmenu">
                                <i class="fas fa-chart-bar"></i> Laporan
                                <i class="fas fa-chevron-down float-end"></i>
                            </a>
                            <div class="collapse" id="laporanSubmenu">
                                <ul class="nav flex-column ms-3">
                                    <li class="nav-item">
                                        <a class="nav-link py-1" href="index.php?page=transaksi&action=laporan-penjualan">
                                            <i class="fas fa-chart-line"></i> Laporan Penjualan
                                        </a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link py-1" href="index.php?page=transaksi&action=laporan-margin">
                                            <i class="fas fa-percentage"></i> Laporan Margin
                                        </a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link py-1" href="index.php?page=barang&action=laporan-terlaris">
                                            <i class="fas fa-fire"></i> Barang Terlaris
                                        </a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link py-1" href="index.php?page=barang&action=laporan-tidak-laku">
                                            <i class="fas fa-times-circle"></i> Barang Tidak Laku
                                        </a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link py-1" href="index.php?page=transaksi&action=laporan-hpp">
                                            <i class="fas fa-calculator"></i> Laporan HPP
                                        </a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link py-1" href="index.php?page=transaksi&action=laporan-diskon">
                                            <i class="fas fa-tags"></i> Laporan Diskon
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </li>
                    </ul>
                </div>
            </nav>

            <!-- Main content -->
            <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                    <h1 class="h2"><?= $pageTitle ?? 'Dashboard' ?></h1>
                </div>

                <!-- Alert messages -->
                <?php if (isset($_GET['message'])): ?>
                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                        <?php
                        switch ($_GET['message']) {
                            case 'success':
                                echo 'Data berhasil ditambahkan!';
                                break;
                            case 'updated':
                                echo 'Data berhasil diperbarui!';
                                break;
                            case 'deleted':
                                echo 'Data berhasil dihapus!';
                                break;
                            default:
                                echo 'Operasi berhasil!';
                        }
                        ?>
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                <?php endif; ?>

                <?php if (isset($_GET['error'])): ?>
                    <div class="alert alert-danger alert-dismissible fade show" role="alert">
                        <?= htmlspecialchars($_GET['error']) ?>
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                <?php endif; ?>

                <!-- Content will be loaded here -->
                <?= $content ?? '' ?>
            </main>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    <script src="assets/js/main.js"></script>
    <?= $scripts ?? '' ?>
</body>
</html>