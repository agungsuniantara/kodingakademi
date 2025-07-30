<?php
class BarangController {
    public function index() {
        $model = new BarangModel();
        $barang = $model->all();
        include '../views/barang/index.php';
    }
}
?>
