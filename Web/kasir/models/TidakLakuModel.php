<?php
    class TidakLakuModel {
        private $db;
        public function __construct() {
            $this->db = Database::getInstance();
        }
        public function getData($dari, $sampai) {
            $stmt = $this->db->prepare("
                SELECT 
                    b.id_barang, 
                    b.nama_barang,
                    b.stok
                FROM barang b
                LEFT JOIN (
                    SELECT DISTINCT dt.id_barang
                    FROM detail_transaksi dt
                    JOIN transaksi t ON dt.id_transaksi = t.id_transaksi
                    WHERE t.tanggal_transaksi BETWEEN ? AND ?
                ) d ON b.id_barang = d.id_barang
                WHERE d.id_barang IS NULL
                ORDER BY b.stok DESC, b.nama_barang ASC
            ");
            $stmt->execute([$dari, $sampai]);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        }
    }
    
?>