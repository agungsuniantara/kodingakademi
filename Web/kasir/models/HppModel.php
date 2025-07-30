<?php
    class HppModel {
        private $db;
        public function __construct() {
            $this->db = Database::getInstance();
        }
    
        public function getData($dari, $sampai) {
            $stmt = $this->db->prepare("
                SELECT 
                    t.tanggal_transaksi AS tanggal,
                    SUM(dt.quantity * dt.harga_satuan) AS total_penjualan,
                    SUM(dt.quantity * b.harga_beli) AS total_hpp,
                    SUM(dt.quantity * dt.harga_satuan) - SUM(dt.quantity * b.harga_beli) AS laba_kotor
                FROM transaksi t
                JOIN detail_transaksi dt ON t.id_transaksi = dt.id_transaksi
                JOIN barang b ON dt.id_barang = b.id_barang
                WHERE t.tanggal_transaksi BETWEEN ? AND ?
                GROUP BY t.tanggal_transaksi
                ORDER BY t.tanggal_transaksi DESC
            ");
        
            $stmt->execute([$dari, $sampai]);
            $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
            // Summary total
            $summary = [
                'total_penjualan' => array_sum(array_column($rows, 'total_penjualan')),
                'total_hpp'       => array_sum(array_column($rows, 'total_hpp')),
                'laba_kotor'      => array_sum(array_column($rows, 'laba_kotor')),
            ];
    
            return ['data'=>$rows, 'summary'=>$summary];
        }
    }
    
?>