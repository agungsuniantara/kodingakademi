<?php include '../views/layouts/header.php'; ?>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<div class="content">
    <h2 class="fw-bold mb-4">Laporan Margin</h2>
    <div class="card shadow-sm mb-4">
        <div class="card-body">
            <form class="row align-items-end g-2 mb-4" id="filterFormMargin">
                <div class="col-auto"><label class="form-label">Periode</label></div>
                <div class="col"><input type="date" id="filterDari" class="form-control" value="<?= date('Y-m-01') ?>"></div>
                <div class="col"><input type="date" id="filterSampai" class="form-control" value="<?= date('Y-m-d') ?>"></div>
                <div class="col-auto"><button type="submit" class="btn btn-primary"><i class="bi bi-funnel-fill me-2"></i>Filter</button></div>
            </form>
            <div class="row g-3 mb-4">
                <div class="col-lg-3 col-md-6">
                    <div class="card-dashboard card-blue px-4 py-3">
                        <div class="title mb-1">TOTAL MARGIN</div>
                        <div class="value" id="total_margin">Rp 0</div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="card-dashboard card-green px-4 py-3">
                        <div class="title mb-1">TOTAL PENJUALAN</div>
                        <div class="value" id="total_penjualan">Rp 0</div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="card-dashboard card-yellow px-4 py-3">
                        <div class="title mb-1">TOTAL HPP</div>
                        <div class="value" id="total_hpp">Rp 0</div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="card-dashboard card-cyan px-4 py-3">
                        <div class="title mb-1">RATA-RATA MARGIN</div>
                        <div class="value" id="rata2_margin">Rp 0</div>
                    </div>
                </div>
            </div>
            <div class="mb-4">
                <div class="table-responsive">
                    <table class="table table-dashboard align-middle mb-0" id="tabelMargin">
                        <thead>
                            <tr style="background:#111; color:#fff">
                                <th>TANGGAL</th>
                                <th>JUMLAH TRANSAKSI</th>
                                <th>TOTAL PENJUALAN</th>
                                <th>TOTAL HPP</th>
                                <th>TOTAL MARGIN</th>
                                <th>RATA-RATA MARGIN</th>
                            </tr>
                        </thead>
                        <tbody></tbody>
                        <tfoot>
                            <tr style="font-weight:bold; background:#fafbfc">
                                <td>TOTAL</td>
                                <td id="footer_transaksi"></td>
                                <td id="footer_penjualan"></td>
                                <td id="footer_hpp"></td>
                                <td id="footer_margin"></td>
                                <td id="footer_rata2"></td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
            </div>
            <div>
                <div class="text-center fw-bold mb-2">Grafik Margin Harian</div>
                <canvas id="grafikMargin" height="80"></canvas>
            </div>
        </div>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
function formatRupiah(angka) { return "Rp " + (angka || 0).toLocaleString('id'); }
function loadLaporanMargin() {
    let dari = $('#filterDari').val();
    let sampai = $('#filterSampai').val();
    $.get('ajax/MarginAjax.php', {dari, sampai}, function(res){
        $('#total_margin').text(formatRupiah(res.summary.total_margin));
        $('#total_penjualan').text(formatRupiah(res.summary.total_penjualan));
        $('#total_hpp').text(formatRupiah(res.summary.total_hpp));
        $('#rata2_margin').text(formatRupiah(res.summary.rata2_margin));
        // Tabel
        let rows = '';
        let totalTransaksi=0, totalPenjualan=0, totalHpp=0, totalMargin=0;
        res.data.forEach(row => {
            rows += `<tr>
                <td>${row.tanggal}</td>
                <td><span class="badge bg-success">${row.jumlah_transaksi}</span></td>
                <td>${formatRupiah(row.total_penjualan)}</td>
                <td>${formatRupiah(row.total_hpp)}</td>
                <td>${formatRupiah(row.total_margin)}</td>
                <td>${formatRupiah(row.rata2_margin)}</td>
            </tr>`;
            totalTransaksi += parseInt(row.jumlah_transaksi);
            totalPenjualan += parseInt(row.total_penjualan);
            totalHpp += parseInt(row.total_hpp);
            totalMargin += parseInt(row.total_margin);
        });
        $('#tabelMargin tbody').html(rows);
        $('#footer_transaksi').text(totalTransaksi);
        $('#footer_penjualan').text(formatRupiah(totalPenjualan));
        $('#footer_hpp').text(formatRupiah(totalHpp));
        $('#footer_margin').text(formatRupiah(totalMargin));
        $('#footer_rata2').text(formatRupiah(res.summary.rata2_margin));
        // Grafik
        let labels = res.data.map(r=>r.tanggal);
        let dataMargin = res.data.map(r=>r.total_margin);
        let ctx = document.getElementById('grafikMargin').getContext('2d');
        if(window.grafikMarginObj) window.grafikMarginObj.destroy();
        window.grafikMarginObj = new Chart(ctx, {
            type: 'line',
            data: {labels: labels, datasets:[{
                label: 'Total Margin',
                data: dataMargin,
                borderColor: '#06b6d4',
                backgroundColor: 'rgba(6,182,212,0.1)'
            }]},
            options: {responsive:true, plugins:{legend:{position:'top'}}}
        });
    },'json');
}
$(function(){
    loadLaporanMargin();
    $('#filterFormMargin').submit(function(e){
        e.preventDefault();
        loadLaporanMargin();
    });
});
</script>
<?php include '../views/layouts/footer.php'; ?>
