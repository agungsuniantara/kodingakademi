<?php
require_once __DIR__ . '/../models/TransaksiModel.php';

class TransaksiController
{
    public function index()
    {
        $model = new TransaksiModel();
        include __DIR__ . '/../views/transaksi/index.php';
    }

    public function cetak($id)
    {
        $model = new TransaksiModel();
        $data = $model->find($id);
    
        $barangModel = new BarangModel();
        $daftarBarang = $barangModel->getArrayIdNama();
    
        $subtotal = 0;
        $total_diskon = 0;
        if (!empty($data['detail'])) {
            foreach ($data['detail'] as $det) {
                $subtotal += $det['harga_satuan'] * $det['quantity'];
                $total_diskon += $det['diskon_item'];
            }
        }
    
        // include view (semua variabel di atas otomatis tersedia di view)
        include __DIR__ . '/../views/transaksi/cetak_transaksi.php';
    }    
}
