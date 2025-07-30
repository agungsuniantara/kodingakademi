<?php
class TerlarisModel {
    private $db;
    public function __construct() {
        $this->db = Database::getInstance();
    }
    public function getData($dari, $sampai, $limit = 10) {
        $limit = intval($limit);
        $sql = "
            SELECT 
                dt.id_barang,
                b.nama_barang, 
                SUM(dt.quantity) as total_jual,
                SUM(dt.harga_satuan * dt.quantity) as total_penjualan
            FROM detail_transaksi dt
            JOIN barang b ON b.id_barang = dt.id_barang
            JOIN transaksi t ON t.id_transaksi = dt.id_transaksi
            WHERE t.tanggal_transaksi BETWEEN ? AND ?
            GROUP BY dt.id_barang
            ORDER BY total_jual DESC
            LIMIT $limit
        ";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$dari, $sampai]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
    
    
}
