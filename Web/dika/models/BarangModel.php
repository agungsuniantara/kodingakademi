<?php
require_once 'config/database.php';

class BarangModel {
    private $db;
    
    public function __construct() {
        $this->db = new Database();
    }
    
    public function getAllBarang() {
        try {
            $sql = "SELECT * FROM barang ORDER BY nama_barang";
            return $this->db->fetchAll($sql);
        } catch (Exception $e) {
            throw new Exception("Error fetching products: " . $e->getMessage());
        }
    }
    
    public function getBarangById($id) {
        try {
            if (!$id) {
                throw new Exception("Invalid product ID");
            }
            $sql = "SELECT * FROM barang WHERE id_barang = ?";
            $result = $this->db->fetch($sql, [$id]);
            if (!$result) {
                throw new Exception("Product not found");
            }
            return $result;
        } catch (Exception $e) {
            throw new Exception("Error fetching product: " . $e->getMessage());
        }
    }
    
    public function searchBarang($keyword) {
        try {
            if (empty($keyword)) {
                return [];
            }
            
            // Debug logging
            error_log("Searching for keyword: " . $keyword);
            
            $sql = "SELECT * FROM barang WHERE nama_barang LIKE ? OR kategori LIKE ?";
            $keyword = "%{$keyword}%";
            
            // Debug logging
            error_log("SQL Query: " . $sql);
            error_log("Search parameters: " . json_encode([$keyword, $keyword]));
            
            $results = $this->db->fetchAll($sql, [$keyword, $keyword]);
            
            // Debug logging
            error_log("Search results count: " . count($results));
            
            return $results;
        } catch (Exception $e) {
            error_log("Error in searchBarang: " . $e->getMessage());
            throw new Exception("Error searching products: " . $e->getMessage());
        }
    }
    
    public function createBarang($data) {
        try {
            if (!isset($data['nama_barang'], $data['harga_beli'], $data['harga_jual'], 
                      $data['stok'], $data['kategori'])) {
                throw new Exception("Missing required product data");
            }
            
            // Validate numeric values
            if (!is_numeric($data['harga_beli']) || !is_numeric($data['harga_jual']) || 
                !is_numeric($data['stok'])) {
                throw new Exception("Invalid numeric values");
            }
            
            $sql = "INSERT INTO barang (nama_barang, harga_beli, harga_jual, stok, kategori) 
                    VALUES (?, ?, ?, ?, ?)";
            return $this->db->query($sql, [
                $data['nama_barang'],
                $data['harga_beli'],
                $data['harga_jual'],
                $data['stok'],
                $data['kategori']
            ]);
        } catch (Exception $e) {
            throw new Exception("Error creating product: " . $e->getMessage());
        }
    }
    
    public function updateBarang($id, $data) {
        try {
            if (!$id) {
                throw new Exception("Invalid product ID");
            }
            
            if (!isset($data['nama_barang'], $data['harga_beli'], $data['harga_jual'], 
                      $data['stok'], $data['kategori'])) {
                throw new Exception("Missing required product data");
            }
            
            // Validate numeric values
            if (!is_numeric($data['harga_beli']) || !is_numeric($data['harga_jual']) || 
                !is_numeric($data['stok'])) {
                throw new Exception("Invalid numeric values");
            }
            
            $sql = "UPDATE barang SET nama_barang = ?, harga_beli = ?, harga_jual = ?, 
                    stok = ?, kategori = ? WHERE id_barang = ?";
            return $this->db->query($sql, [
                $data['nama_barang'],
                $data['harga_beli'],
                $data['harga_jual'],
                $data['stok'],
                $data['kategori'],
                $id
            ]);
        } catch (Exception $e) {
            throw new Exception("Error updating product: " . $e->getMessage());
        }
    }
    
    public function deleteBarang($id) {
        try {
            if (!$id) {
                throw new Exception("Invalid product ID");
            }
            
            // Check if product exists
            $barang = $this->getBarangById($id);
            if (!$barang) {
                throw new Exception("Product not found");
            }
            
            // Check if product is used in transactions
            $sql = "SELECT COUNT(*) as count FROM detail_transaksi WHERE id_barang = ?";
            $result = $this->db->fetch($sql, [$id]);
            if ($result['count'] > 0) {
                throw new Exception("Cannot delete product that has been used in transactions");
            }
            
            $sql = "DELETE FROM barang WHERE id_barang = ?";
            return $this->db->query($sql, [$id]);
        } catch (Exception $e) {
            throw new Exception("Error deleting product: " . $e->getMessage());
        }
    }
    
    public function updateStok($id, $stok) {
        try {
            if (!$id || !is_numeric($stok)) {
                throw new Exception("Invalid product ID or stock value");
            }
            
            // Check if product exists
            $barang = $this->getBarangById($id);
            if (!$barang) {
                throw new Exception("Product not found");
            }
            
            // Check if there's enough stock
            if ($barang['stok'] < $stok) {
                throw new Exception("Insufficient stock");
            }
            
            $sql = "UPDATE barang SET stok = stok - ? WHERE id_barang = ?";
            return $this->db->query($sql, [$stok, $id]);
        } catch (Exception $e) {
            throw new Exception("Error updating stock: " . $e->getMessage());
        }
    }
    
    public function getBarangTerlaris($startDate, $endDate) {
        try {
            if (!$startDate || !$endDate) {
                throw new Exception("Invalid date range");
            }
            
            $sql = "SELECT b.id_barang, b.nama_barang, b.kategori, 
                           SUM(dt.quantity) as total_terjual,
                           SUM(dt.subtotal) as total_penjualan
                    FROM detail_transaksi dt
                    JOIN barang b ON dt.id_barang = b.id_barang
                    JOIN transaksi t ON dt.id_transaksi = t.id_transaksi
                    WHERE t.tanggal_transaksi BETWEEN ? AND ?
                    GROUP BY b.id_barang
                    ORDER BY total_terjual DESC";
            return $this->db->fetchAll($sql, [$startDate, $endDate]);
        } catch (Exception $e) {
            throw new Exception("Error generating best-selling products report: " . $e->getMessage());
        }
    }
    
    public function getBarangTidakLaku($startDate, $endDate) {
        try {
            if (!$startDate || !$endDate) {
                throw new Exception("Invalid date range");
            }
            
            $sql = "SELECT b.id_barang, b.nama_barang, b.kategori, b.stok,
                           COALESCE(SUM(dt.quantity), 0) as total_terjual
                    FROM barang b
                    LEFT JOIN detail_transaksi dt ON b.id_barang = dt.id_barang
                    LEFT JOIN transaksi t ON dt.id_transaksi = t.id_transaksi 
                        AND t.tanggal_transaksi BETWEEN ? AND ?
                    GROUP BY b.id_barang
                    HAVING total_terjual = 0
                    ORDER BY b.nama_barang";
            return $this->db->fetchAll($sql, [$startDate, $endDate]);
        } catch (Exception $e) {
            throw new Exception("Error generating non-selling products report: " . $e->getMessage());
        }
    }
}
?>