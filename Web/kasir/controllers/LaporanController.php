<?php
class LaporanController
{
    public function penjualan()
    {
        $model = new PenjualanModel();
        include __DIR__ . '/../views/laporan/penjualan.php';
    }

    public function margin()
    {
        $model = new MarginModel();
        include __DIR__ . '/../views/laporan/margin.php';
    }

    public function terlaris()
    {
        $model = new TerlarisModel();
        include __DIR__ . '/../views/laporan/terlaris.php';
    }

    public function tidakLaku()
    {
        $model = new TidakLakuModel();
        include __DIR__ . '/../views/laporan/tidaklaku.php';
    }

    public function hpp()
    {
        $model = new HppModel();
        include __DIR__ . '/../views/laporan/hpp.php';
    }

    public function diskon()
    {
        $model = new DiskonModel();
        include __DIR__ . '/../views/laporan/diskon.php';
    }
}

