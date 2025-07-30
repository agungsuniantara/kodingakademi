<?php include '../views/layouts/header.php'; ?>
<!-- Chart.js CDN -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<div class="content">
    <h2 class="fw-bold mb-4">Laporan Penjualan</h2>

    <div class="card shadow-sm mb-4">
        <div class="card-body">
            <form class="row align-items-end g-2 mb-4" id="filterForm">
                <div class="col-auto">
                    <label class="form-label">Periode</label>
                </div>
                <div class="col">
                    <input type="date" id="filterDari" name="dari" class="form-control" value="<?= date('Y-m-01') ?>">
                </div>
                <div class="col">
                    <input type="date" id="filterSampai" name="sampai" class="form-control" value="<?= date('Y-m-d') ?>">
                </div>
                <div class="col-auto">
                    <button type="submit" class="btn btn-primary">
                        <i class="bi bi-funnel-fill me-2"></i>Filter
                    </button>
                </div>
            </form>
            <div class="row g-3 mb-4">
                <div class="col-lg-3 col-md-6">
                    <div class="card-dashboard card-blue d-flex justify-content-between align-items-center px-4 py-3">
                        <div>
                            <div class="title mb-1">TOTAL PENJUALAN</div>
                            <div class="value" id="total_penjualan">Rp 0</div>
                        </div>
                        <div class="icon-bg"><i class="bi bi-currency-dollar"></i></div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="card-dashboard card-green d-flex justify-content-between align-items-center px-4 py-3">
                        <div>
                            <div class="title mb-1">TOTAL TRANSAKSI</div>
                            <div class="value" id="total_transaksi">0</div>
                        </div>
                        <div class="icon-bg"><i class="bi bi-cart2"></i></div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="card-dashboard card-yellow d-flex justify-content-between align-items-center px-4 py-3">
                        <div>
                            <div class="title mb-1">TOTAL DISKON</div>
                            <div class="value" id="total_diskon">Rp 0</div>
                        </div>
                        <div class="icon-bg"><i class="bi bi-tag"></i></div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="card-dashboard card-cyan d-flex justify-content-between align-items-center px-4 py-3">
                        <div>
                            <div class="title mb-1">RATA-RATA/TRANSAKSI</div>
                            <div class="value" id="rata2_transaksi">Rp 0</div>
                        </div>
                        <div class="icon-bg"><i class="bi bi-clipboard-data"></i></div>
                    </div>
                </div>
            </div>
            <div class="mb-4">
                <div class="table-responsive">
                    <table class="table table-dashboard align-middle mb-0" id="tabelPenjualan">
                        <thead>
                            <tr style="background:#111; color:#fff">
                                <th>TANGGAL</th>
                                <th>JUMLAH TRANSAKSI</th>
                                <th>TOTAL PENJUALAN</th>
                                <th>TOTAL DISKON</th>
                                <th>RATA-RATA TRANSAKSI</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Data by JS -->
                        </tbody>
                        <tfoot>
                            <tr style="font-weight:bold; background:#fafbfc">
                                <td>TOTAL</td>
                                <td id="footer_transaksi"></td>
                                <td id="footer_penjualan"></td>
                                <td id="footer_diskon"></td>
                                <td id="footer_rata2"></td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
            </div>
            <div>
                <div class="text-center fw-bold mb-2">Grafik Penjualan Harian</div>
                <canvas id="grafikPenjualan" height="80"></canvas>
            </div>
        </div>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
function formatRupiah(angka) {
    return "Rp " + (angka || 0).toLocaleString('id');
}

function loadLaporanPenjualan() {
    let dari = $('#filterDari').val();
    let sampai = $('#filterSampai').val();
    $.get('ajax/PenjualanAjax.php', {dari, sampai}, function(res){
        // Kartu ringkasan
        $('#total_penjualan').text(formatRupiah(res.summary.total_penjualan));
        $('#total_transaksi').text(res.summary.total_transaksi);
        $('#total_diskon').text(formatRupiah(res.summary.total_diskon));
        $('#rata2_transaksi').text(formatRupiah(res.summary.rata2));

        // Tabel data
        let rows = '';
        let totalTransaksi=0, totalPenjualan=0, totalDiskon=0, totalRata2=0;
        res.data.forEach(row => {
            rows += `<tr>
                <td>${row.tanggal}</td>
                <td><span class="badge bg-success">${row.jumlah_transaksi}</span></td>
                <td>${formatRupiah(row.total_penjualan)}</td>
                <td>${formatRupiah(row.total_diskon)}</td>
                <td>${formatRupiah(row.rata2)}</td>
            </tr>`;
            totalTransaksi += parseInt(row.jumlah_transaksi);
            totalPenjualan += parseInt(row.total_penjualan);
            totalDiskon += parseInt(row.total_diskon);
        });
        $('#tabelPenjualan tbody').html(rows);
        $('#footer_transaksi').text(totalTransaksi);
        $('#footer_penjualan').text(formatRupiah(totalPenjualan));
        $('#footer_diskon').text(formatRupiah(totalDiskon));
        $('#footer_rata2').text(formatRupiah(res.summary.rata2));

        // Grafik
        let labels = res.data.map(r=>r.tanggal);
        let dataPenjualan = res.data.map(r=>r.total_penjualan);
        let dataTransaksi = res.data.map(r=>r.jumlah_transaksi);
        // Chart.js multi-axis
        let ctx = document.getElementById('grafikPenjualan').getContext('2d');
        if(window.grafikPenjualanObj) window.grafikPenjualanObj.destroy();
        window.grafikPenjualanObj = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Total Penjualan (Rp)',
                        data: dataPenjualan,
                        borderColor: '#06b6d4',
                        backgroundColor: 'rgba(6,182,212,0.2)',
                        yAxisID: 'y1'
                    },
                    {
                        label: 'Jumlah Transaksi',
                        data: dataTransaksi,
                        borderColor: '#fa466b',
                        backgroundColor: 'rgba(250,70,107,0.1)',
                        yAxisID: 'y2'
                    }
                ]
            },
            options: {
                responsive: true,
                interaction: {mode: 'index', intersect: false},
                stacked: false,
                plugins: {
                    legend: {position: 'top'}
                },
                scales: {
                    y1: {
                        type: 'linear',
                        position: 'right',
                        title: {display: true, text: 'Total Penjualan (Rp)'},
                        beginAtZero: true,
                        ticks: {callback: value => "Rp " + value.toLocaleString('id')}
                    },
                    y2: {
                        type: 'linear',
                        position: 'left',
                        title: {display: true, text: 'Jumlah Transaksi'},
                        beginAtZero: true,
                        grid: {drawOnChartArea: false}
                    }
                }
            }
        });
    },'json');
};

$(function(){
    loadLaporanPenjualan();
    $('#filterForm').submit(function(e){
        e.preventDefault();
        loadLaporanPenjualan();
    });
});
</script>
<?php include '../views/layouts/footer.php'; ?>
