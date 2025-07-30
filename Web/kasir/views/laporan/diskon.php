<?php include '../views/layouts/header.php'; ?>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<div class="content">
    <h2 class="fw-bold mb-4">Laporan Diskon</h2>
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
    <div class="card shadow-sm mb-4">
        <div class="card-body">
            <div class="table-responsive">
                <table class="table table-dashboard align-middle mb-0" id="tabelBarangDiskon">
                    <thead>
                        <tr style="background:#111; color:#fff">
                            <th>RANK</th>
                            <th>ID BARANG</th>
                            <th>NAMA BARANG</th>
                            <th>JUMLAH DISKON</th>
                            <th>TOTAL DISKON</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Data by JS -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
function formatRupiah(angka) {
    return "Rp " + (angka || 0).toLocaleString('id');
}

function loadBarangSeringDiskon() {
    let dari = $('#filterDari').val();
    let sampai = $('#filterSampai').val();
    $.get('ajax/BarangSeringDiskonAjax.php', {dari, sampai}, function(res){
        // TABEL
        let rows = '';
        res.data.forEach((row, idx) => {
            rows += `<tr>
                <td>${idx + 1}</td>
                <td>${row.id_barang}</td>
                <td>${row.nama_barang}</td>
                <td>${row.jumlah_diskon}</td>
                <td>${formatRupiah(row.total_diskon)}</td>
            </tr>`;
        });
        if (!rows) {
            rows = `<tr><td colspan="5" class="text-center text-muted">Tidak ada data barang diskon.</td></tr>`;
        }
        $('#tabelBarangDiskon tbody').html(rows);
    }, 'json');
}

$(function(){
    loadBarangSeringDiskon();
    $('#filterForm').submit(function(e){
        e.preventDefault();
        loadBarangSeringDiskon();
    });
});
</script>
<?php include '../views/layouts/footer.php'; ?>
