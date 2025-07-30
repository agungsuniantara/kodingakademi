<?php include '../views/layouts/header.php'; ?>
<link rel="stylesheet" href="../assets/css/laporan.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<div class="content">
    <h2 class="fw-bold mb-4">Laporan HPP</h2>
    <div class="card shadow-sm mb-4">
        <div class="card-body">
            <form class="row align-items-end g-2 mb-4" id="filterForm">
                <div class="col-auto"><label class="form-label">Periode</label></div>
                <div class="col">
                    <input type="date" id="filterDari" class="form-control" value="<?= date('Y-m-01') ?>">
                </div>
                <div class="col">
                    <input type="date" id="filterSampai" class="form-control" value="<?= date('Y-m-d') ?>">
                </div>
                <div class="col-auto">
                    <button type="submit" class="btn btn-primary"><i class="bi bi-funnel-fill me-2"></i>Filter</button>
                </div>
            </form>
            <div class="row g-3 mb-4">
                <div class="col-lg-4 col-md-6">
                    <div class="card-dashboard card-blue d-flex justify-content-between align-items-center px-4 py-3">
                        <div>
                            <div class="title mb-1">TOTAL PENJUALAN</div>
                            <div class="value" id="total_penjualan">Rp 0</div>
                        </div>
                        <div class="icon-bg"><i class="bi bi-currency-dollar"></i></div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="card-dashboard card-yellow d-flex justify-content-between align-items-center px-4 py-3">
                        <div>
                            <div class="title mb-1">TOTAL HPP</div>
                            <div class="value" id="total_hpp">Rp 0</div>
                        </div>
                        <div class="icon-bg"><i class="bi bi-cash-stack"></i></div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="card-dashboard card-green d-flex justify-content-between align-items-center px-4 py-3">
                        <div>
                            <div class="title mb-1">LABA KOTOR</div>
                            <div class="value" id="laba_kotor">Rp 0</div>
                        </div>
                        <div class="icon-bg"><i class="bi bi-bar-chart"></i></div>
                    </div>
                </div>
            </div>
            <div class="mb-4">
                <div class="table-responsive">
                    <table class="table table-dashboard align-middle mb-0" id="tabelHPP">
                        <thead>
                            <tr style="background:#111; color:#fff">
                                <th>TANGGAL</th>
                                <th>TOTAL PENJUALAN</th>
                                <th>TOTAL HPP</th>
                                <th>LABA KOTOR</th>
                            </tr>
                        </thead>
                        <tbody></tbody>
                        <tfoot>
                            <tr style="font-weight:bold; background:#fafbfc">
                                <td>TOTAL</td>
                                <td id="footer_penjualan"></td>
                                <td id="footer_hpp"></td>
                                <td id="footer_laba"></td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
            </div>
            <div>
                <div class="text-center fw-bold mb-2">Grafik Penjualan vs HPP</div>
                <canvas id="grafikHPP" height="80"></canvas>
            </div>
        </div>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
function formatRupiah(angka) { return "Rp " + (angka || 0).toLocaleString('id'); }
function loadLaporanHPP() {
    let dari = $('#filterDari').val();
    let sampai = $('#filterSampai').val();
    $.get('ajax/HppAjax.php', {dari, sampai}, function(res){
        $('#total_penjualan').text(formatRupiah(res.summary.total_penjualan));
        $('#total_hpp').text(formatRupiah(res.summary.total_hpp));
        $('#laba_kotor').text(formatRupiah(res.summary.laba_kotor));
        let rows = '';
        res.data.forEach(row => {
            rows += `<tr>
                <td>${row.tanggal}</td>
                <td>${formatRupiah(row.total_penjualan)}</td>
                <td>${formatRupiah(row.total_hpp)}</td>
                <td>${formatRupiah(row.laba_kotor)}</td>
            </tr>`;
        });
        $('#tabelHPP tbody').html(rows);
        $('#footer_penjualan').text(formatRupiah(res.summary.total_penjualan));
        $('#footer_hpp').text(formatRupiah(res.summary.total_hpp));
        $('#footer_laba').text(formatRupiah(res.summary.laba_kotor));
        // Chart.js
        let labels = res.data.map(r=>r.tanggal);
        let dataPenjualan = res.data.map(r=>r.total_penjualan);
        let dataHPP = res.data.map(r=>r.total_hpp);
        let dataLaba = res.data.map(r=>r.laba_kotor);
        let ctx = document.getElementById('grafikHPP').getContext('2d');
        if(window.grafikHPPObj) window.grafikHPPObj.destroy();
        window.grafikHPPObj = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Total Penjualan',
                        data: dataPenjualan,
                        backgroundColor: 'rgba(59,130,246,0.7)',
                    },
                    {
                        label: 'Total HPP',
                        data: dataHPP,
                        backgroundColor: 'rgba(250,204,21,0.7)',
                    },
                    {
                        label: 'Laba Kotor',
                        data: dataLaba,
                        backgroundColor: 'rgba(34,197,94,0.7)',
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {legend: {position: 'top'}},
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {callback: value => "Rp " + value.toLocaleString('id')}
                    }
                }
            }
        });
    },'json');
}
$(function(){
    loadLaporanHPP();
    $('#filterForm').submit(function(e){
        e.preventDefault();
        loadLaporanHPP();
    });
});
</script>
<?php include '../views/layouts/footer.php'; ?>
