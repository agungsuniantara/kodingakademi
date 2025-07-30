<?php
session_start();
require_once __DIR__ . '/../config/database.php';

// Autoload Controller dan Model
spl_autoload_register(function ($class) {
    foreach ([__DIR__ . '/../controllers/', __DIR__ . '/../models/'] as $dir) {
        if (file_exists($dir . $class . '.php')) {
            require_once $dir . $class . '.php';
            break;
        }
    }
});

// Routing
$page = $_GET['page'] ?? 'dashboard';
switch ($page) {
    case 'barang':
        (new BarangController)->index();
        break;
    case 'transaksi':
        (new TransaksiController)->index();
        break;
    case 'cetak_transaksi':
        $id = $_GET['id'];
        (new TransaksiController)->cetak($id);
        break;

    // Routing Laporan via Controller
    case 'laporan_penjualan':
        (new LaporanController)->penjualan();
        break;
    case 'laporan_margin':
        (new LaporanController)->margin();
        break;
    case 'barang_terlaris':
        (new LaporanController)->terlaris();
        break;
    case 'barang_tidak_laku':
        (new LaporanController)->tidakLaku();
        break;
    case 'laporan_hpp':
        (new LaporanController)->hpp();
        break;
    case 'laporan_diskon':
        (new LaporanController)->diskon();
        break;

    default:
        (new DashboardController)->index();
}

?>
