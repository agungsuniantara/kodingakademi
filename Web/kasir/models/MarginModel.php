<?php
class MarginModel {
    private $db;
    public function __construct() {
        $this->db = Database::getInstance();
    }
    public function getData($dari, $sampai) {
        $stmt = $this->db->prepare("
            SELECT 
                t.tanggal_transaksi as tanggal,
                COUNT(DISTINCT t.id_transaksi) as jumlah_transaksi,
                SUM(t.total_harga) as total_penjualan,
                SUM(dt.quantity * b.harga_beli) as total_hpp,
                SUM(t.total_harga) - SUM(dt.quantity * b.harga_beli) as total_margin,
                ROUND((SUM(t.total_harga) - SUM(dt.quantity * b.harga_beli)) / COUNT(DISTINCT t.id_transaksi), 2) as rata2_margin
            FROM transaksi t
            JOIN detail_transaksi dt ON dt.id_transaksi = t.id_transaksi
            JOIN barang b ON dt.id_barang = b.id_barang
            WHERE t.tanggal_transaksi BETWEEN ? AND ?
            GROUP BY t.tanggal_transaksi
            ORDER BY t.tanggal_transaksi ASC
        ");
    
        $stmt->execute([$dari, $sampai]);
        $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Summary
        $summary = [
            'total_margin'   => array_sum(array_column($rows, 'total_margin')),
            'total_penjualan'=> array_sum(array_column($rows, 'total_penjualan')),
            'total_hpp'      => array_sum(array_column($rows, 'total_hpp')),
            'rata2_margin'   => count($rows) ? round(array_sum(array_column($rows, 'total_margin'))/array_sum(array_column($rows, 'jumlah_transaksi')), 2) : 0
        ];
        return ['data' => $rows, 'summary' => $summary];
    }
}
