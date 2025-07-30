<?php
class DashboardController {
    public function index() {
        // Ambil data summary dari model
        $dashboard = new DashboardModel();
        $data = [
            'total_barang'         => $dashboard->getTotalBarang(),
            'transaksi_hari_ini'   => $dashboard->getTransaksiHariIni(),
            'penjualan_hari_ini'   => $dashboard->getPenjualanHariIni(),
            'penjualan_bulan_ini'  => $dashboard->getPenjualanBulanIni(),
            'stok_rendah'          => $dashboard->getStokRendah(),
            'transaksi_baru'       => $dashboard->getTransaksiBaru()
        ];
        include '../views/dashboard/index.php';
    }
}
?>
