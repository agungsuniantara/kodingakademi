<?php
require_once 'config/database.php';

class TransaksiModel {
    private $db;
    
    public function __construct() {
        $this->db = new Database();
    }
    
    public function getAllTransaksi() {
        try {
            $sql = "SELECT t.*, COUNT(dt.id_detail) as jumlah_item
                    FROM transaksi t
                    LEFT JOIN detail_transaksi dt ON t.id_transaksi = dt.id_transaksi
                    GROUP BY t.id_transaksi
                    ORDER BY t.created_at DESC";
            return $this->db->fetchAll($sql);
        } catch (Exception $e) {
            throw new Exception("Error fetching transactions: " . $e->getMessage());
        }
    }
    
    public function getTransaksiById($id) {
        try {
            if (!$id) {
                throw new Exception("Invalid transaction ID");
            }
            $sql = "SELECT * FROM transaksi WHERE id_transaksi = ?";
            $result = $this->db->fetch($sql, [$id]);
            if (!$result) {
                throw new Exception("Transaction not found");
            }
            return $result;
        } catch (Exception $e) {
            throw new Exception("Error fetching transaction: " . $e->getMessage());
        }
    }
    
    public function getDetailTransaksi($id_transaksi) {
        try {
            if (!$id_transaksi) {
                throw new Exception("Invalid transaction ID");
            }
            $sql = "SELECT dt.*, b.nama_barang
                    FROM detail_transaksi dt
                    JOIN barang b ON dt.id_barang = b.id_barang
                    WHERE dt.id_transaksi = ?";
            return $this->db->fetchAll($sql, [$id_transaksi]);
        } catch (Exception $e) {
            throw new Exception("Error fetching transaction details: " . $e->getMessage());
        }
    }
    
    public function createTransaksi($data) {
        try {
            if (!isset($data['tanggal_transaksi']) || !isset($data['total_harga'])) {
                throw new Exception("Missing required transaction data");
            }
            
            $sql = "INSERT INTO transaksi (tanggal_transaksi, total_harga, diskon) 
                    VALUES (?, ?, ?)";
            $this->db->query($sql, [
                $data['tanggal_transaksi'],
                $data['total_harga'],
                $data['diskon'] ?? 0
            ]);
            return $this->db->lastInsertId();
        } catch (Exception $e) {
            throw new Exception("Error creating transaction: " . $e->getMessage());
        }
    }
    
    public function addDetailTransaksi($data) {
        try {
            if (!isset($data['id_transaksi'], $data['id_barang'], $data['quantity'], 
                      $data['harga_satuan'], $data['subtotal'])) {
                throw new Exception("Missing required transaction detail data");
            }
            
            $sql = "INSERT INTO detail_transaksi (id_transaksi, id_barang, quantity, harga_satuan, subtotal, diskon_item) 
                    VALUES (?, ?, ?, ?, ?, ?)";
            return $this->db->query($sql, [
                $data['id_transaksi'],
                $data['id_barang'],
                $data['quantity'],
                $data['harga_satuan'],
                $data['subtotal'],
                $data['diskon_item'] ?? 0
            ]);
        } catch (Exception $e) {
            throw new Exception("Error adding transaction detail: " . $e->getMessage());
        }
    }
    
    public function deleteTransaksi($id) {
        try {
            if (!$id) {
                throw new Exception("Invalid transaction ID");
            }
            
            // Start transaction
            $this->db->beginTransaction();
            
            try {
                // Delete detail_transaksi first
                $sql = "DELETE FROM detail_transaksi WHERE id_transaksi = ?";
                $this->db->query($sql, [$id]);
                
                // Then delete transaksi
                $sql = "DELETE FROM transaksi WHERE id_transaksi = ?";
                $this->db->query($sql, [$id]);
                
                $this->db->commit();
                return true;
            } catch (Exception $e) {
                $this->db->rollback();
                throw $e;
            }
        } catch (Exception $e) {
            throw new Exception("Error deleting transaction: " . $e->getMessage());
        }
    }
    
    public function getLaporanPenjualan($startDate, $endDate) {
        try {
            if (!$startDate || !$endDate) {
                throw new Exception("Invalid date range");
            }
            
            $sql = "SELECT 
                        DATE(t.tanggal_transaksi) as tanggal,
                        COUNT(t.id_transaksi) as jumlah_transaksi,
                        SUM(t.total_harga) as total_penjualan,
                        SUM(t.diskon) as total_diskon,
                        AVG(t.total_harga) as rata_rata_transaksi
                    FROM transaksi t
                    WHERE t.tanggal_transaksi BETWEEN ? AND ?
                    GROUP BY DATE(t.tanggal_transaksi)
                    ORDER BY tanggal DESC";
            return $this->db->fetchAll($sql, [$startDate, $endDate]);
        } catch (Exception $e) {
            throw new Exception("Error generating sales report: " . $e->getMessage());
        }
    }
    
    public function getLaporanMargin($startDate, $endDate) {
        try {
            if (!$startDate || !$endDate) {
                throw new Exception("Invalid date range");
            }
            
            $sql = "SELECT 
                        b.nama_barang,
                        b.kategori,
                        SUM(dt.quantity) as total_quantity,
                        b.harga_beli,
                        AVG(dt.harga_satuan) as avg_harga_jual,
                        SUM(dt.quantity * b.harga_beli) as total_hpp,
                        SUM(dt.subtotal) as total_penjualan,
                        SUM(dt.subtotal - (dt.quantity * b.harga_beli)) as total_margin,
                        ROUND(((SUM(dt.subtotal - (dt.quantity * b.harga_beli)) / SUM(dt.subtotal)) * 100), 2) as margin_persen
                    FROM detail_transaksi dt
                    JOIN barang b ON dt.id_barang = b.id_barang
                    JOIN transaksi t ON dt.id_transaksi = t.id_transaksi
                    WHERE t.tanggal_transaksi BETWEEN ? AND ?
                    GROUP BY b.id_barang
                    ORDER BY total_margin DESC";
            return $this->db->fetchAll($sql, [$startDate, $endDate]);
        } catch (Exception $e) {
            throw new Exception("Error generating margin report: " . $e->getMessage());
        }
    }
    
    public function getLaporanHPP($startDate, $endDate) {
        try {
            if (!$startDate || !$endDate) {
                throw new Exception("Invalid date range");
            }
            
            $sql = "SELECT 
                        b.nama_barang,
                        b.kategori,
                        b.harga_beli,
                        SUM(dt.quantity) as quantity_terjual,
                        SUM(dt.quantity * b.harga_beli) as total_hpp,
                        SUM(dt.subtotal) as total_revenue,
                        (SUM(dt.subtotal) - SUM(dt.quantity * b.harga_beli)) as gross_profit
                    FROM detail_transaksi dt
                    JOIN barang b ON dt.id_barang = b.id_barang
                    JOIN transaksi t ON dt.id_transaksi = t.id_transaksi
                    WHERE t.tanggal_transaksi BETWEEN ? AND ?
                    GROUP BY b.id_barang
                    ORDER BY total_hpp DESC";
            return $this->db->fetchAll($sql, [$startDate, $endDate]);
        } catch (Exception $e) {
            throw new Exception("Error generating HPP report: " . $e->getMessage());
        }
    }
    
    public function getLaporanDiskon($startDate, $endDate) {
        try {
            if (!$startDate || !$endDate) {
                throw new Exception("Invalid date range");
            }
            
            $sql = "SELECT 
                        b.nama_barang,
                        COUNT(CASE WHEN dt.diskon_item > 0 THEN 1 END) as frekuensi_diskon,
                        AVG(dt.diskon_item) as rata_rata_diskon,
                        SUM(dt.diskon_item) as total_diskon_item,
                        SUM(dt.quantity) as total_quantity
                    FROM detail_transaksi dt
                    JOIN barang b ON dt.id_barang = b.id_barang
                    JOIN transaksi t ON dt.id_transaksi = t.id_transaksi
                    WHERE t.tanggal_transaksi BETWEEN ? AND ?
                    GROUP BY b.id_barang
                    HAVING frekuensi_diskon > 0
                    ORDER BY frekuensi_diskon DESC, total_diskon_item DESC";
            return $this->db->fetchAll($sql, [$startDate, $endDate]);
        } catch (Exception $e) {
            throw new Exception("Error generating discount report: " . $e->getMessage());
        }
    }

    public function getTransaksiList($tanggal_dari, $tanggal_sampai, $total_min = 0, $page = 1) {
        try {
            if (!$tanggal_dari || !$tanggal_sampai) {
                throw new Exception("Invalid date range");
            }
            
            $limit = 10;
            $offset = ($page - 1) * $limit;
            
            // Get total records for pagination
            $countSql = "SELECT COUNT(DISTINCT t.id_transaksi) as total 
                        FROM transaksi t 
                        WHERE t.tanggal_transaksi BETWEEN ? AND ?";
            $params = [$tanggal_dari, $tanggal_sampai];
            
            if ($total_min > 0) {
                $countSql .= " AND t.total_harga >= ?";
                $params[] = $total_min;
            }
            
            $totalRecords = $this->db->fetch($countSql, $params)['total'];
            $totalPages = ceil($totalRecords / $limit);
            
            // Get transaction data
            $sql = "SELECT t.*, 
                    COUNT(dt.id_detail) as total_item
                    FROM transaksi t 
                    LEFT JOIN detail_transaksi dt ON t.id_transaksi = dt.id_transaksi 
                    WHERE t.tanggal_transaksi BETWEEN ? AND ?";
            
            $params = [$tanggal_dari, $tanggal_sampai];
            
            if ($total_min > 0) {
                $sql .= " AND t.total_harga >= ?";
                $params[] = $total_min;
            }
            
            $sql .= " GROUP BY t.id_transaksi ORDER BY t.created_at DESC LIMIT ? OFFSET ?";
            $params[] = $limit;
            $params[] = $offset;
            
            $transaksiData = $this->db->fetchAll($sql, $params);
            
            return [
                'transaksi' => $transaksiData,
                'summary' => $this->getSummary($tanggal_dari, $tanggal_sampai),
                'pagination' => [
                    'current_page' => $page,
                    'total_pages' => $totalPages,
                    'total_records' => $totalRecords,
                    'limit' => $limit
                ]
            ];
        } catch (Exception $e) {
            throw new Exception("Error fetching transaction list: " . $e->getMessage());
        }
    }
    
    public function getSummary($tanggal_dari, $tanggal_sampai) {
        try {
            if (!$tanggal_dari || !$tanggal_sampai) {
                throw new Exception("Invalid date range");
            }
            
            $sql = "SELECT 
                    COUNT(*) as total_transaksi,
                    SUM(total_harga) as total_pendapatan,
                    AVG(total_harga) as rata_transaksi,
                    SUM(diskon) as total_diskon
                    FROM transaksi 
                    WHERE tanggal_transaksi BETWEEN ? AND ?";
            
            return $this->db->fetch($sql, [$tanggal_dari, $tanggal_sampai]);
        } catch (Exception $e) {
            throw new Exception("Error generating summary: " . $e->getMessage());
        }
    }
}
?>
