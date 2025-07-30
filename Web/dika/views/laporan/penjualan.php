<?php
$page = 'transaksi';
$pageTitle = 'Laporan Penjualan';

ob_start();
?>

<div class="card">
    <div class="card-header">
        <div class="row align-items-center">
            <div class="col">
                <h5 class="card-title mb-0">
                    <i class="fas fa-chart-line"></i> Laporan Penjualan
                </h5>
            </div>
            <div class="col-auto">
                <form method="GET" class="d-flex gap-2">
                    <input type="hidden" name="page" value="transaksi">
                    <input type="hidden" name="action" value="laporan-penjualan">
                    <input type="date" name="start_date" class="form-control" 
                           value="<?= $_GET['start_date'] ?? date('Y-m-01') ?>">
                    <input type="date" name="end_date" class="form-control" 
                           value="<?= $_GET['end_date'] ?? date('Y-m-d') ?>">
                    <button type="submit" class="btn btn-primary">
                        <i class="fas fa-filter"></i> Filter
                    </button>
                </form>
            </div>
        </div>
    </div>
    <div class="card-body">
        <!-- Summary Cards -->
        <div class="row mb-4">
            <div class="col-md-3">
                <div class="card bg-primary text-white">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <div class="text-xs font-weight-bold text-uppercase mb-1">Total Penjualan</div>
                                <div class="h5 mb-0">Rp <?= number_format($totalPenjualan, 0, ',', '.') ?></div>
                            </div>
                            <div class="fa-2x opacity-75">
                                <i class="fas fa-dollar-sign"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="col-md-3">
                <div class="card bg-success text-white">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <div class="text-xs font-weight-bold text-uppercase mb-1">Total Transaksi</div>
                                <div class="h5 mb-0"><?= number_format($totalTransaksi) ?></div>
                            </div>
                            <div class="fa-2x opacity-75">
                                <i class="fas fa-shopping-cart"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="col-md-3">
                <div class="card bg-warning text-white">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <div class="text-xs font-weight-bold text-uppercase mb-1">Total Diskon</div>
                                <div class="h5 mb-0">Rp <?= number_format($totalDiskon, 0, ',', '.') ?></div>
                            </div>
                            <div class="fa-2x opacity-75">
                                <i class="fas fa-tags"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="col-md-3">
                <div class="card bg-info text-white">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <div class="text-xs font-weight-bold text-uppercase mb-1">Rata-rata/Transaksi</div>
                                <div class="h5 mb-0">Rp <?= $totalTransaksi > 0 ? number_format($totalPenjualan / $totalTransaksi, 0, ',', '.') : '0' ?></div>
                            </div>
                            <div class="fa-2x opacity-75">
                                <i class="fas fa-chart-bar"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tabel Detail -->
        <?php if (empty($data)): ?>
            <div class="text-center py-4">
                <i class="fas fa-inbox fa-3x text-muted mb-3"></i>
                <h5 class="text-muted">Tidak ada data penjualan</h5>
                <p class="text-muted">Pada rentang tanggal yang dipilih</p>
            </div>
        <?php else: ?>
            <div class="table-responsive">
                <table class="table table-striped table-hover">
                    <thead class="table-dark">
                        <tr>
                            <th>Tanggal</th>
                            <th>Jumlah Transaksi</th>
                            <th>Total Penjualan</th>
                            <th>Total Diskon</th>
                            <th>Rata-rata Transaksi</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach ($data as $row): ?>
                        <tr>
                            <td><?= date('d/m/Y', strtotime($row['tanggal'])) ?></td>
                            <td>
                                <span class="badge bg-success"><?= number_format($row['jumlah_transaksi']) ?></span>
                            </td>
                            <td>Rp <?= number_format($row['total_penjualan'], 0, ',', '.') ?></td>
                            <td>Rp <?= number_format($row['total_diskon'], 0, ',', '.') ?></td>
                            <td>Rp <?= number_format($row['rata_rata_transaksi'], 0, ',', '.') ?></td>
                        </tr>
                        <?php endforeach; ?>
                    </tbody>
                    <tfoot class="table-light">
                        <tr>
                            <th>Total</th>
                            <th><span class="badge bg-success"><?= number_format($totalTransaksi) ?></span></th>
                            <th>Rp <?= number_format($totalPenjualan, 0, ',', '.') ?></th>
                            <th>Rp <?= number_format($totalDiskon, 0, ',', '.') ?></th>
                            <th>Rp <?= $totalTransaksi > 0 ? number_format($totalPenjualan / $totalTransaksi, 0, ',', '.') : '0' ?></th>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <!-- Chart Section -->
            <div class="mt-4">
                <canvas id="penjualanChart" width="400" height="200"></canvas>
            </div>
        <?php endif; ?>
    </div>
</div>

<?php
$content = ob_get_clean();

// JavaScript untuk chart
ob_start();
?>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
<script>
<?php if (!empty($data)): ?>
// Prepare chart data
const chartLabels = <?= json_encode(array_map(function($row) { return date('d/m', strtotime($row['tanggal'])); }, $data)) ?>;
const chartData = <?= json_encode(array_column($data, 'total_penjualan')) ?>;
const chartTransaksi = <?= json_encode(array_column($data, 'jumlah_transaksi')) ?>;

// Create chart
const ctx = document.getElementById('penjualanChart').getContext('2d');
const penjualanChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: chartLabels,
        datasets: [{
            label: 'Total Penjualan (Rp)',
            data: chartData,
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.1)',
            tension: 0.1,
            yAxisID: 'y'
        }, {
            label: 'Jumlah Transaksi',
            data: chartTransaksi,
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.1)',
            tension: 0.1,
            yAxisID: 'y1'
        }]
    },
    options: {
        responsive: true,
        interaction: {
            mode: 'index',
            intersect: false,
        },
        scales: {
            x: {
                display: true,
                title: {
                    display: true,
                    text: 'Tanggal'
                }
            },
            y: {
                type: 'linear',
                display: true,
                position: 'left',
                title: {
                    display: true,
                    text: 'Total Penjualan (Rp)'
                },
                ticks: {
                    callback: function(value) {
                        return 'Rp ' + value.toLocaleString('id-ID');
                    }
                }
            },
            y1: {
                type: 'linear',
                display: true,
                position: 'right',
                title: {
                    display: true,
                    text: 'Jumlah Transaksi'
                },
                grid: {
                    drawOnChartArea: false,
                }
            }
        },
        plugins: {
            title: {
                display: true,
                text: 'Grafik Penjualan Harian'
            },
            legend: {
                display: true,
                position: 'top'
            }
        }
    }
});
<?php endif; ?>
</script>
<?php
$scripts = ob_get_clean();

include 'views/layout/template.php';
?>