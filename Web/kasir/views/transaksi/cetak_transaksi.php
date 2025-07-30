<!DOCTYPE html>
<html>
<head>
    <title>Cetak Transaksi #<?= $id ?></title>
    <style>
        body { font-family: Arial; margin:20px; }
        h2 { margin-bottom:10px; }
        table { width:100%; border-collapse:collapse; }
        th,td { border:1px solid #333; padding:5px; }
        .center { text-align:center; }
    </style>
</head>
<body onload="window.print()">
    <h4>Toko Kamu<br>Jl. Contoh Alamat, Kota</h4>
    <h2>Struk Transaksi #<?= $id ?></h2>
    <p>Tanggal: <?= date('d-m-Y H:i', strtotime($data['tanggal_transaksi'])) ?></p>
    <table>
        <thead>
            <tr><th>Nama Barang</th><th>Qty</th><th>Harga</th><th>Diskon</th><th>Subtotal</th></tr>
        </thead>
        <tbody>
            <?php foreach($data['detail'] as $det): ?>
            <tr>
                <td><?= $daftarBarang[$det['id_barang']] ?? $det['id_barang'] ?></td>
                <td class="center"><?= $det['quantity'] ?></td>
                <td class="center"><?= number_format($det['harga_satuan']) ?></td>
                <td class="center"><?= number_format($det['diskon_item']) ?></td>
                <td class="center"><?= number_format($det['subtotal']) ?></td>
            </tr>
            <?php endforeach ?>
        </tbody>
    </table>
    <br>
    <p>Subtotal: Rp <?= number_format($subtotal) ?></p>
    <p>Total Diskon: Rp <?= number_format($total_diskon) ?></p>
    <h3>Total: Rp <?= number_format($data['total_harga']) ?></h3>
</body>
</html>
