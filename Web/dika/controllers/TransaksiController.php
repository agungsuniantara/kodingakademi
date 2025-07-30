<?php
require_once 'models/TransaksiModel.php';
require_once 'models/BarangModel.php';
require_once 'config/functions.php';

class TransaksiController {
    private $transaksiModel;
    private $barangModel;
    
    public function __construct() {
        $this->transaksiModel = new TransaksiModel();
        $this->barangModel = new BarangModel();
    }
    
    public function index() {
        try {
            $transaksi = $this->transaksiModel->getAllTransaksi();
            include 'views/transaksi/index.php';
        } catch (Exception $e) {
            $_SESSION['error'] = "Error loading transactions: " . $e->getMessage();
            include 'views/transaksi/index.php';
        }
    }
    
    public function create() {
        try {
            $barang = $this->barangModel->getAllBarang();
            include 'views/transaksi/create.php';
        } catch (Exception $e) {
            $_SESSION['error'] = "Error loading products: " . $e->getMessage();
            include 'views/transaksi/create.php';
        }
    }
    
    public function store() {
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            http_response_code(405);
            echo json_encode(['success' => false, 'error' => 'Method not allowed']);
            return;
        }

        try {
            // Validate required fields
            $requiredFields = ['tanggal_transaksi', 'total_harga', 'items'];
            foreach ($requiredFields as $field) {
                if (!isset($_POST[$field]) || empty($_POST[$field])) {
                    throw new Exception("Missing required field: {$field}");
                }
            }

            $transaksiData = [
                'tanggal_transaksi' => sanitizeString($_POST['tanggal_transaksi']),
                'total_harga' => filter_var($_POST['total_harga'], FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION),
                'diskon' => filter_var($_POST['diskon'] ?? 0, FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION)
            ];
            
            $id_transaksi = $this->transaksiModel->createTransaksi($transaksiData);
            
            // Process items
            $items = json_decode($_POST['items'], true);
            if (!is_array($items)) {
                throw new Exception("Invalid items data format");
            }

            foreach ($items as $item) {
                if (!isset($item['id_barang'], $item['quantity'], $item['harga_satuan'], $item['subtotal'])) {
                    throw new Exception("Invalid item data structure");
                }

                $detailData = [
                    'id_transaksi' => $id_transaksi,
                    'id_barang' => filter_var($item['id_barang'], FILTER_SANITIZE_NUMBER_INT),
                    'quantity' => filter_var($item['quantity'], FILTER_SANITIZE_NUMBER_INT),
                    'harga_satuan' => filter_var($item['harga_satuan'], FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION),
                    'subtotal' => filter_var($item['subtotal'], FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION),
                    'diskon_item' => filter_var($item['diskon_item'] ?? 0, FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION)
                ];
                
                $this->transaksiModel->addDetailTransaksi($detailData);
                $this->barangModel->updateStok($item['id_barang'], $item['quantity']);
            }
            
            echo json_encode(['success' => true, 'id_transaksi' => $id_transaksi]);
        } catch (Exception $e) {
            http_response_code(400);
            echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        }
    }
    
    public function detail($id) {
        try {
            if (!$id) {
                throw new Exception("Invalid transaction ID");
            }
            $transaksi = $this->transaksiModel->getTransaksiById($id);
            if (!$transaksi) {
                throw new Exception("Transaction not found");
            }
            $detail = $this->transaksiModel->getDetailTransaksi($id);
            include 'views/transaksi/detail.php';
        } catch (Exception $e) {
            $_SESSION['error'] = $e->getMessage();
            header('Location: index.php?page=transaksi');
            exit;
        }
    }
    
    public function delete($id) {
        try {
            if (!$id) {
                throw new Exception("Invalid transaction ID");
            }
            $this->transaksiModel->deleteTransaksi($id);
            $_SESSION['success'] = "Transaction deleted successfully";
        } catch (Exception $e) {
            $_SESSION['error'] = $e->getMessage();
        }
        header('Location: index.php?page=transaksi');
        exit;
    }
    
    public function laporanPenjualan() {
        try {
            $startDate = filter_input(INPUT_GET, 'start_date', FILTER_SANITIZE_STRING) ?? date('Y-m-01');
            $endDate = filter_input(INPUT_GET, 'end_date', FILTER_SANITIZE_STRING) ?? date('Y-m-d');
            
            $data = $this->transaksiModel->getLaporanPenjualan($startDate, $endDate);
            
            // Calculate totals
            $totalPenjualan = array_sum(array_column($data, 'total_penjualan'));
            $totalTransaksi = array_sum(array_column($data, 'jumlah_transaksi'));
            $totalDiskon = array_sum(array_column($data, 'total_diskon'));
            
            include 'views/laporan/penjualan.php';
        } catch (Exception $e) {
            $_SESSION['error'] = "Error generating sales report: " . $e->getMessage();
            include 'views/laporan/penjualan.php';
        }
    }
    
    public function laporanMargin() {
        $startDate = $_GET['start_date'] ?? date('Y-m-01');
        $endDate = $_GET['end_date'] ?? date('Y-m-d');
        
        $data = $this->transaksiModel->getLaporanMargin($startDate, $endDate);
        include 'views/laporan/margin.php';
    }
    
    public function laporanHPP() {
        $startDate = $_GET['start_date'] ?? date('Y-m-01');
        $endDate = $_GET['end_date'] ?? date('Y-m-d');
        
        $data = $this->transaksiModel->getLaporanHPP($startDate, $endDate);
        include 'views/laporan/hpp.php';
    }
    
    public function laporanDiskon() {
        $startDate = $_GET['start_date'] ?? date('Y-m-01');
        $endDate = $_GET['end_date'] ?? date('Y-m-d');
        
        $data = $this->transaksiModel->getLaporanDiskon($startDate, $endDate);
        include 'views/laporan/diskon.php';
    }

    public function list() {
        // Handle AJAX request untuk menampilkan daftar transaksi
        $page = $_GET['page'] ?? 1;
        $tanggal_dari = $_GET['tanggal_dari'] ?? date('Y-m-01');
        $tanggal_sampai = $_GET['tanggal_sampai'] ?? date('Y-m-d');
        $total_min = $_GET['total_min'] ?? 0;
        
        // Query dengan JOIN untuk mendapatkan data lengkap
        $transaksiModel = new TransaksiModel();
        $result = $transaksiModel->getTransaksiList($tanggal_dari, $tanggal_sampai, $total_min, $page);
        
        header('Content-Type: application/json');
        echo json_encode($result);
        exit;
    }
}
?>
