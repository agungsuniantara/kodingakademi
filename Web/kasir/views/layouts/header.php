<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aplikasi Kasir</title>
  <!-- Bootstrap CSS CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">
  <link rel="stylesheet" href="../assets/css/navbar.css">
</head>
<body>
<div class="sidebar d-flex flex-column position-fixed">
    <div class="logo mb-4 ms-3">
        <i class="bi bi-cash-coin me-2"></i> Sistem Kasir
    </div>
    <nav class="nav flex-column ms-2">
      <a class="nav-link <?= ($page=='dashboard'?'active':'') ?>" href="index.php?page=dashboard">
        <i class="bi bi-house-door me-2"></i> Dashboard
      </a>
      <a class="nav-link <?= ($page=='barang'?'active':'') ?>" href="index.php?page=barang">
        <i class="bi bi-box-seam me-2"></i> Kelola Barang
      </a>
      <a class="nav-link <?= ($page=='transaksi'?'active':'') ?>" href="index.php?page=transaksi">
        <i class="bi bi-cart2 me-2"></i> Kelola Transaksi
      </a>

      <!-- Dropdown Laporan -->
      <div class="nav-link p-0 laporan-dropdown">
        <a class="nav-link d-flex justify-content-between align-items-center laporan-toggle" data-bs-toggle="collapse" href="#laporanMenu" role="button" aria-expanded="<?= (strpos($page,'laporan')!==false || $page=='barang_terlaris' || $page=='barang_tidak_laku')?'true':'false' ?>" aria-controls="laporanMenu" style="padding-left: 12px; background:none;">
          <span><i class="bi bi-journal-text me-2"></i> Laporan</span>
          <i class="bi bi-chevron-down"></i>
        </a>
        <div class="collapse <?= (strpos($page,'laporan')!==false || $page=='barang_terlaris' || $page=='barang_tidak_laku')?'show':'' ?>" id="laporanMenu">
          <ul class="nav flex-column ms-3">
            <li>
              <a class="nav-link <?= ($page=='laporan_penjualan'?'active':'') ?>" href="index.php?page=laporan_penjualan">
                <i class="bi bi-graph-up me-2"></i> Laporan Penjualan
              </a>
            </li>
            <li>
              <a class="nav-link <?= ($page=='laporan_margin'?'active':'') ?>" href="index.php?page=laporan_margin">
                <i class="bi bi-percent me-2"></i> Laporan Margin
              </a>
            </li>
            <li>
              <a class="nav-link <?= ($page=='barang_terlaris'?'active':'') ?>" href="index.php?page=barang_terlaris">
                <i class="bi bi-fire me-2"></i> Barang Terlaris
              </a>
            </li>
            <li>
              <a class="nav-link <?= ($page=='barang_tidak_laku'?'active':'') ?>" href="index.php?page=barang_tidak_laku">
                <i class="bi bi-x-circle me-2"></i> Barang Tidak Laku
              </a>
            </li>
            <li>
              <a class="nav-link <?= ($page=='laporan_hpp'?'active':'') ?>" href="index.php?page=laporan_hpp">
                <i class="bi bi-calculator me-2"></i> Laporan HPP
              </a>
            </li>
            <li>
              <a class="nav-link <?= ($page=='laporan_diskon'?'active':'') ?>" href="index.php?page=laporan_diskon">
                <i class="bi bi-ticket-detailed me-2"></i> Laporan Diskon
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
</div>


