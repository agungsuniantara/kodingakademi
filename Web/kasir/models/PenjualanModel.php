<?php
class PenjualanModel {
    private $db;
    public function __construct() {
        $this->db = Database::getInstance();
    }
    public function getData($dari, $sampai) {
        // Query per hari dan summary
        $stmt = $this->db->prepare("
            SELECT 
                tanggal_transaksi as tanggal,
                COUNT(*) as jumlah_transaksi,
                SUM(total_harga) as total_penjualan,
                SUM(diskon) as total_diskon,
                AVG(total_harga) as rata2
            FROM transaksi
            WHERE tanggal_transaksi BETWEEN ? AND ?
            GROUP BY tanggal_transaksi
            ORDER BY tanggal_transaksi ASC
        ");
        $stmt->execute([$dari, $sampai]);
        $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Summary total
        $summary = [
            'total_penjualan' => array_sum(array_column($rows, 'total_penjualan')),
            'total_transaksi' => array_sum(array_column($rows, 'jumlah_transaksi')),
            'total_diskon'    => array_sum(array_column($rows, 'total_diskon')),
            'rata2'           => count($rows) ? round(array_sum(array_column($rows, 'total_penjualan'))/array_sum(array_column($rows, 'jumlah_transaksi'))) : 0
        ];

        return ['data'=>$rows, 'summary'=>$summary];
    }
}
