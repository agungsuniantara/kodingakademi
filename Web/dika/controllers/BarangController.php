<?php
require_once 'models/BarangModel.php';
require_once 'config/functions.php';

class BarangController {
    private $barangModel;
    
    public function __construct() {
        $this->barangModel = new BarangModel();
    }
    
    public function index() {
        try {
            $barang = $this->barangModel->getAllBarang();
            include 'views/barang/index.php';
        } catch (Exception $e) {
            $_SESSION['error'] = "Error loading products: " . $e->getMessage();
            include 'views/barang/index.php';
        }
    }
    
    public function create() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            try {
                // Validate required fields
                $requiredFields = ['nama_barang', 'harga_beli', 'harga_jual', 'stok', 'kategori'];
                foreach ($requiredFields as $field) {
                    if (!isset($_POST[$field]) || empty($_POST[$field])) {
                        throw new Exception("Missing required field: {$field}");
                    }
                }

                // Validate numeric fields
                if (!is_numeric($_POST['harga_beli']) || !is_numeric($_POST['harga_jual']) || !is_numeric($_POST['stok'])) {
                    throw new Exception("Invalid numeric values");
                }

                $data = [
                    'nama_barang' => sanitizeString($_POST['nama_barang']),
                    'harga_beli' => filter_var($_POST['harga_beli'], FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION),
                    'harga_jual' => filter_var($_POST['harga_jual'], FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION),
                    'stok' => filter_var($_POST['stok'], FILTER_SANITIZE_NUMBER_INT),
                    'kategori' => sanitizeString($_POST['kategori'])
                ];
                
                $this->barangModel->createBarang($data);
                $_SESSION['success'] = "Product created successfully";
                header('Location: index.php?page=barang');
                exit;
            } catch (Exception $e) {
                $_SESSION['error'] = $e->getMessage();
            }
        }
        include 'views/barang/create.php';
    }
    
    public function edit($id) {
        try {
            if (!$id) {
                throw new Exception("Invalid product ID");
            }

            $barang = $this->barangModel->getBarangById($id);
            if (!$barang) {
                throw new Exception("Product not found");
            }
            
            if ($_SERVER['REQUEST_METHOD'] === 'POST') {
                // Validate required fields
                $requiredFields = ['nama_barang', 'harga_beli', 'harga_jual', 'stok', 'kategori'];
                foreach ($requiredFields as $field) {
                    if (!isset($_POST[$field]) || empty($_POST[$field])) {
                        throw new Exception("Missing required field: {$field}");
                    }
                }

                // Validate numeric fields
                if (!is_numeric($_POST['harga_beli']) || !is_numeric($_POST['harga_jual']) || !is_numeric($_POST['stok'])) {
                    throw new Exception("Invalid numeric values");
                }

                $data = [
                    'nama_barang' => sanitizeString($_POST['nama_barang']),
                    'harga_beli' => filter_var($_POST['harga_beli'], FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION),
                    'harga_jual' => filter_var($_POST['harga_jual'], FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION),
                    'stok' => filter_var($_POST['stok'], FILTER_SANITIZE_NUMBER_INT),
                    'kategori' => sanitizeString($_POST['kategori'])
                ];
                
                $this->barangModel->updateBarang($id, $data);
                $_SESSION['success'] = "Product updated successfully";
                header('Location: index.php?page=barang');
                exit;
            }
        } catch (Exception $e) {
            $_SESSION['error'] = $e->getMessage();
            if ($_SERVER['REQUEST_METHOD'] === 'POST') {
                header('Location: index.php?page=barang');
                exit;
            }
        }
        include 'views/barang/edit.php';
    }
    
    public function delete($id) {
        try {
            if (!$id) {
                throw new Exception("Invalid product ID");
            }
            $this->barangModel->deleteBarang($id);
            $_SESSION['success'] = "Product deleted successfully";
        } catch (Exception $e) {
            $_SESSION['error'] = $e->getMessage();
        }
        header('Location: index.php?page=barang');
        exit;
    }
    
    public function search() {
        try {
            $keyword = sanitizeString($_GET['keyword'] ?? '');
            
            // Debug logging
            error_log("Search request received. Keyword: " . $keyword);
            
            if (empty($keyword)) {
                error_log("Empty keyword, returning empty array");
                echo json_encode([]);
                return;
            }
            
            $barang = $this->barangModel->searchBarang($keyword);
            
            // Debug logging
            error_log("Search results: " . json_encode($barang));
            
            header('Content-Type: application/json');
            echo json_encode($barang);
        } catch (Exception $e) {
            error_log("Search error: " . $e->getMessage());
            http_response_code(400);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }
    
    public function laporanTerlaris() {
        try {
            $startDate = filter_input(INPUT_GET, 'start_date', FILTER_SANITIZE_STRING) ?? date('Y-m-01');
            $endDate = filter_input(INPUT_GET, 'end_date', FILTER_SANITIZE_STRING) ?? date('Y-m-d');
            
            $data = $this->barangModel->getBarangTerlaris($startDate, $endDate);
            include 'views/laporan/barang_terlaris.php';
        } catch (Exception $e) {
            $_SESSION['error'] = "Error generating best-selling products report: " . $e->getMessage();
            include 'views/laporan/barang_terlaris.php';
        }
    }
    
    public function laporanTidakLaku() {
        try {
            $startDate = filter_input(INPUT_GET, 'start_date', FILTER_SANITIZE_STRING) ?? date('Y-m-01');
            $endDate = filter_input(INPUT_GET, 'end_date', FILTER_SANITIZE_STRING) ?? date('Y-m-d');
            
            $data = $this->barangModel->getBarangTidakLaku($startDate, $endDate);
            include 'views/laporan/barang_tidak_laku.php';
        } catch (Exception $e) {
            $_SESSION['error'] = "Error generating non-selling products report: " . $e->getMessage();
            include 'views/laporan/barang_tidak_laku.php';
        }
    }
}
?>