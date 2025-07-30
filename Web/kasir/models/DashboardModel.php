<?php
class DashboardModel {
    private $db;
    public function __construct() {
        $this->db = Database::getInstance();
    }

    public function getTotalBarang() {
        $stmt = $this->db->query("SELECT COUNT(*) FROM barang");
        return $stmt->fetchColumn();
    }

    public function getTransaksiHariIni() {
        $today = date('Y-m-d');
        $stmt = $this->db->prepare("SELECT COUNT(*) FROM transaksi WHERE tanggal_transaksi = ?");
        $stmt->execute([$today]);
        return $stmt->fetchColumn();
    }

    public function getPenjualanHariIni() {
        $today = date('Y-m-d');
        $stmt = $this->db->prepare("SELECT SUM(total_harga) FROM transaksi WHERE tanggal_transaksi = ?");
        $stmt->execute([$today]);
        return $stmt->fetchColumn() ?: 0;
    }

    public function getPenjualanBulanIni() {
        $month = date('Y-m');
        $stmt = $this->db->prepare("SELECT SUM(total_harga) FROM transaksi WHERE tanggal_transaksi LIKE ?");
        $stmt->execute([$month . '%']);
        return $stmt->fetchColumn() ?: 0;
    }

    public function getStokRendah($limit = 5) {
        $stmt = $this->db->prepare("SELECT * FROM barang WHERE stok <= 5 ORDER BY stok ASC LIMIT ?");
        $stmt->bindValue(1, $limit, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getTransaksiBaru($limit = 5) {
        $stmt = $this->db->prepare("SELECT * FROM transaksi ORDER BY tanggal_transaksi DESC LIMIT ?");
        $stmt->bindValue(1, $limit, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}
?>
