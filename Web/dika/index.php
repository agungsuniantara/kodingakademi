<?php
session_start();

// Include utility functions
require_once 'config/functions.php';

// Security headers
header("X-Frame-Options: DENY");
header("X-XSS-Protection: 1; mode=block");
header("X-Content-Type-Options: nosniff");

// Autoload controllers
spl_autoload_register(function ($class) {
    if (file_exists("controllers/{$class}.php")) {
        require_once "controllers/{$class}.php";
    }
});

// Sanitize input
$page = sanitizeString($_GET['page'] ?? 'dashboard');
$action = sanitizeString($_GET['action'] ?? 'index');
$id = filter_input(INPUT_GET, 'id', FILTER_SANITIZE_NUMBER_INT);

// Route handling
switch ($page) {
    case 'dashboard':
        include 'views/dashboard.php';
        break;
        
    case 'barang':
        $controller = new BarangController();
        switch ($action) {
            case 'create':
                $controller->create();
                break;
            case 'edit':
                $controller->edit($id);
                break;
            case 'delete':
                $controller->delete($id);
                break;
            case 'search':
                $controller->search();
                break;
            case 'laporan-terlaris':
                $controller->laporanTerlaris();
                break;
            case 'laporan-tidak-laku':
                $controller->laporanTidakLaku();
                break;
            default:
                $controller->index();
        }
        break;
        
    case 'transaksi':
        $controller = new TransaksiController();
        switch ($action) {
            case 'create':
                $controller->create();
                break;
            case 'store':
                $controller->store();
                break;
            case 'detail':
                $controller->detail($id);
                break;
            case 'delete':
                $controller->delete($id);
                break;
            case 'laporan-penjualan':
                $controller->laporanPenjualan();
                break;
            case 'laporan-margin':
                $controller->laporanMargin();
                break;
            case 'laporan-hpp':
                $controller->laporanHPP();
                break;
            case 'laporan-diskon':
                $controller->laporanDiskon();
                break;
            default:
                $controller->index();
        }
        break;
        
    default:
        include 'views/404.php';
}

// Di index.php, pastikan ada routing seperti ini:
if (isset($_GET['page']) && $_GET['page'] == 'transaksi') {
    require_once 'controllers/TransaksiController.php';
    $controller = new TransaksiController();
    
    $action = $_GET['action'] ?? 'index';
    
    switch($action) {
        case 'list':
            $controller->list();
            break;
        case 'detail_data':
            // $controller->detailData();
            break;
        case 'store':
            $controller->store();
            break;
        default:
            include 'views/transaksi/index.php';
    }
}
?>
