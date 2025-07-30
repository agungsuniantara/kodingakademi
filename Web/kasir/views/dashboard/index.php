<?php include '../views/layouts/header.php'; ?>

<div class="content">
    <h2 class="fw-bold mb-4">Dashboard</h2>
    <div class="row g-4 mb-4">
        <div class="col-lg-3 col-md-6">
            <div class="card card-dashboard card-blue p-4">
                <div class="icon-bg"><i class="bi bi-box-seam"></i></div>
                <div class="title mb-1">TOTAL BARANG</div>
                <div class="value mb-2"><?= $data['total_barang'] ?? 0 ?></div>
            </div>
        </div>
        <div class="col-lg-3 col-md-6">
            <div class="card card-dashboard card-green p-4">
                <div class="icon-bg"><i class="bi bi-cart2"></i></div>
                <div class="title mb-1">TRANSAKSI HARI INI</div>
                <div class="value mb-2"><?= $data['transaksi_hari_ini'] ?? 0 ?></div>
            </div>
        </div>
        <div class="col-lg-3 col-md-6">
            <div class="card card-dashboard card-yellow p-4">
                <div class="icon-bg"><i class="bi bi-currency-dollar"></i></div>
                <div class="title mb-1">PENJUALAN HARI INI</div>
                <div class="value mb-2">Rp <?= number_format($data['penjualan_hari_ini'] ?? 0) ?></div>
            </div>
        </div>
        <div class="col-lg-3 col-md-6">
            <div class="card card-dashboard card-cyan p-4">
                <div class="icon-bg"><i class="bi bi-graph-up-arrow"></i></div>
                <div class="title mb-1">PENJUALAN BULAN INI</div>
                <div class="value mb-2">Rp <?= number_format($data['penjualan_bulan_ini'] ?? 0) ?></div>
            </div>
        </div>
    </div>

    <div class="row g-4">
        <div class="col-lg-6">
            <div class="card shadow-sm">
                <div class="card-header bg-white border-0 fw-bold">
                    <span class="text-warning"><i class="bi bi-exclamation-triangle-fill me-1"></i></span> Barang Stok Rendah
                </div>
                <div class="card-body">
                    <?php if (empty($data['stok_rendah'])): ?>
                        <div class="alert alert-light mb-0">Semua barang memiliki stok yang cukup.</div>
                    <?php else: ?>
                    <table class="table table-sm">
                        <thead>
                            <tr><th>Nama Barang</th><th>Stok</th></tr>
                        </thead>
                        <tbody>
                        <?php foreach ($data['stok_rendah'] as $brg): ?>
                            <tr>
                                <td><?= htmlspecialchars($brg['nama_barang']) ?></td>
                                <td><?= $brg['stok'] ?></td>
                            </tr>
                        <?php endforeach ?>
                        </tbody>
                    </table>
                    <?php endif ?>
                </div>
            </div>
        </div>
        <div class="col-lg-6">
            <div class="card shadow-sm">
                <div class="card-header bg-white border-0 fw-bold">
                    <span class="text-dark"><i class="bi bi-clock-history me-1"></i></span> Transaksi Terbaru
                </div>
                <div class="card-body">
                    <table class="table table-dashboard table-hover mb-0">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>TANGGAL</th>
                                <th>TOTAL</th>
                                <th>ITEM</th>
                            </tr>
                        </thead>
                        <tbody>
                        <?php foreach ($data['transaksi_baru'] as $trx): ?>
                            <tr>
                                <td>#<?= $trx['id_transaksi'] ?></td>
                                <td><?= $trx['tanggal_transaksi'] ?></td>
                                <td>Rp <?= number_format($trx['total_harga']) ?></td>
                                <td><?= $trx['jumlah_item'] ?? '1 item' ?></td>
                            </tr>
                        <?php endforeach ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<?php include '../views/layouts/footer.php'; ?>
