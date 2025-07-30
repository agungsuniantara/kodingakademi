<?php
$page = 'dashboard';
$pageTitle = 'Dashboard';
require_once 'config/database.php';

// Get dashboard statistics
$db = new Database();

// Total Barang
$totalBarang = $db->fetch("SELECT COUNT(*) as total FROM barang")['total'];

// Total Transaksi Hari Ini
$totalTransaksiHariIni = $db->fetch("SELECT COUNT(*) as total FROM transaksi WHERE DATE(tanggal_transaksi) = CURDATE()")['total'];

// Total Penjualan Hari Ini
$totalPenjualanHariIni = $db->fetch("SELECT SUM(total_harga) as total FROM transaksi WHERE DATE(tanggal_transaksi) = CURDATE()")['total'] ?? 0;

// Total Penjualan Bulan Ini
$totalPenjualanBulanIni = $db->fetch("SELECT SUM(total_harga) as total FROM transaksi WHERE MONTH(tanggal_transaksi) = MONTH(CURDATE()) AND YEAR(tanggal_transaksi) = YEAR(CURDATE())")['total'] ?? 0;

// Barang dengan Stok Rendah (< 10)
$barangStokRendah = $db->fetchAll("SELECT nama_barang, stok FROM barang WHERE stok < 10 ORDER BY stok ASC LIMIT 5");

// Transaksi Terbaru
$transaksiTerbaru = $db->fetchAll("SELECT t.id_transaksi, t.tanggal_transaksi, t.total_harga, COUNT(dt.id_detail) as jumlah_item 
                                   FROM transaksi t 
                                   LEFT JOIN detail_transaksi dt ON t.id_transaksi = dt.id_transaksi 
                                   GROUP BY t.id_transaksi 
                                   ORDER BY t.created_at DESC LIMIT 5");

ob_start();
?>

<div class="row">
    <!-- Statistics Cards -->
    <div class="col-xl-3 col-md-6">
        <div class="card bg-primary text-white mb-4">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <div class="text-xs font-weight-bold text-uppercase mb-1">Total Barang</div>
                        <div class="h5 mb-0"><?= number_format($totalBarang) ?></div>
                    </div>
                    <div class="fa-2x">
                        <i class="fas fa-box"></i>
                    </div>
                </div>
            </div>
            <div class="card-footer d-flex align-items-center justify-content-between">
                <a class="small text-white stretched-link" href="index.php?page=barang">Lihat Detail</a>
                <div class="small text-white"><i class="fas fa-angle-right"></i></div>
            </div>
        </div>
    </div>

    <div class="col-xl-3 col-md-6">
        <div class="card bg-success text-white mb-4">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <div class="text-xs font-weight-bold text-uppercase mb-1">Transaksi Hari Ini</div>
                        <div class="h5 mb-0"><?= number_format($totalTransaksiHariIni) ?></div>
                    </div>
                    <div class="fa-2x">
                        <i class="fas fa-shopping-cart"></i>
                    </div>
                </div>
            </div>
            <div class="card-footer d-flex align-items-center justify-content-between">
                <a class="small text-white stretched-link" href="index.php?page=transaksi">Lihat Detail</a>
                <div class="small text-white"><i class="fas fa-angle-right"></i></div>
            </div>
        </div>
    </div>

    <div class="col-xl-3 col-md-6">
        <div class="card bg-warning text-white mb-4">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <div class="text-xs font-weight-bold text-uppercase mb-1">Penjualan Hari Ini</div>
                        <div class="h5 mb-0">Rp <?= number_format($totalPenjualanHariIni, 0, ',', '.') ?></div>
                    </div>
                    <div class="fa-2x">
                        <i class="fas fa-dollar-sign"></i>
                    </div>
                </div>
            </div>
            <div class="card-footer d-flex align-items-center justify-content-between">
                <a class="small text-white stretched-link" href="index.php?page=transaksi&action=laporan-penjualan">Lihat Detail</a>
                <div class="small text-white"><i class="fas fa-angle-right"></i></div>
            </div>
        </div>
    </div>

    <div class="col-xl-3 col-md-6">
        <div class="card bg-info text-white mb-4">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <div class="text-xs font-weight-bold text-uppercase mb-1">Penjualan Bulan Ini</div>
                        <div class="h5 mb-0">Rp <?= number_format($totalPenjualanBulanIni, 0, ',', '.') ?></div>
                    </div>
                    <div class="fa-2x">
                        <i class="fas fa-chart-line"></i>
                    </div>
                </div>
            </div>
            <div class="card-footer d-flex align-items-center justify-content-between">
                <a class="small text-white stretched-link" href="index.php?page=transaksi&action=laporan-penjualan">Lihat Detail</a>
                <div class="small text-white"><i class="fas fa-angle-right"></i></div>
            </div>
        </div>
    </div>
</div>

<div class="row">
    <!-- Barang Stok Rendah -->
    <div class="col-lg-6">
        <div class="card mb-4">
            <div class="card-header">
                <i class="fas fa-exclamation-triangle text-warning"></i>
                Barang Stok Rendah
            </div>
            <div class="card-body">
                <?php if (empty($barangStokRendah)): ?>
                    <p class="text-muted">Semua barang memiliki stok yang cukup.</p>
                <?php else: ?>
                    <div class="table-responsive">
                        <table class="table table-sm">
                            <thead>
                                <tr>
                                    <th>Nama Barang</th>
                                    <th>Stok</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($barangStokRendah as $barang): ?>
                                <tr>
                                    <td><?= htmlspecialchars($barang['nama_barang']) ?></td>
                                    <td>
                                        <span class="badge bg-<?= $barang['stok'] < 5 ? 'danger' : 'warning' ?>">
                                            <?= $barang['stok'] ?>
                                        </span>
                                    </td>
                                </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                <?php endif; ?>
            </div>
        </div>
    </div>

    <!-- Transaksi Terbaru -->
    <div class="col-lg-6">
        <div class="card mb-4">
            <div class="card-header">
                <i class="fas fa-clock"></i>
                Transaksi Terbaru
            </div>
            <div class="card-body">
                <?php if (empty($transaksiTerbaru)): ?>
                    <p class="text-muted">Belum ada transaksi.</p>
                <?php else: ?>
                    <div class="table-responsive">
                        <table class="table table-sm">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Tanggal</th>
                                    <th>Total</th>
                                    <th>Item</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($transaksiTerbaru as $transaksi): ?>
                                <tr>
                                    <td>#<?= $transaksi['id_transaksi'] ?></td>
                                    <td><?= date('d/m/Y', strtotime($transaksi['tanggal_transaksi'])) ?></td>
                                    <td>Rp <?= number_format($transaksi['total_harga'], 0, ',', '.') ?></td>
                                    <td><?= $transaksi['jumlah_item'] ?> item</td>
                                </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                <?php endif; ?>
            </div>
        </div>
    </div>
</div>

<?php
$content = ob_get_clean();
include 'views/layout/template.php';
?>