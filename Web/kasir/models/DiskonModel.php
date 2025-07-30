<?php
class DiskonModel {
    private $db;
    public function __construct() {
        $this->db = Database::getInstance();
    }

    public function getData($dari, $sampai) {
        // Diskon per hari
        $stmt = $this->db->prepare("
            SELECT 
                tanggal_transaksi as tanggal,
                COUNT(*) as jumlah_transaksi,
                SUM(diskon) as total_diskon,
                SUM(total_harga) as total_penjualan,
                AVG(diskon) as rata2_diskon
            FROM transaksi
            WHERE tanggal_transaksi BETWEEN ? AND ?
              AND diskon > 0
            GROUP BY tanggal_transaksi
            ORDER BY tanggal_transaksi DESC
        ");
        $stmt->execute([$dari, $sampai]);
        $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Summary
        $summary = [
            'total_diskon' => array_sum(array_column($rows, 'total_diskon')),
            'total_transaksi' => array_sum(array_column($rows, 'jumlah_transaksi')),
            'rata2_diskon' => count($rows) ? round(array_sum(array_column($rows, 'total_diskon')) / array_sum(array_column($rows, 'jumlah_transaksi'))) : 0,
        ];

        return ['data' => $rows, 'summary' => $summary];
    }

    public function getBarangSeringDiskon($dari, $sampai, $limit = 10) {
        $stmt = $this->db->prepare("
            SELECT 
                b.id_barang,
                b.nama_barang,
                COUNT(dt.id_detail) AS jumlah_diskon,
                SUM(dt.diskon_item) AS total_diskon
            FROM detail_transaksi dt
            JOIN barang b ON dt.id_barang = b.id_barang
            JOIN transaksi t ON t.id_transaksi = dt.id_transaksi
            WHERE dt.diskon_item > 0
              AND t.tanggal_transaksi BETWEEN ? AND ?
            GROUP BY b.id_barang, b.nama_barang
            ORDER BY jumlah_diskon DESC, total_diskon DESC
            LIMIT $limit
        ");
        $stmt->execute([$dari, $sampai]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }    
}
