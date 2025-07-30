<?php include '../views/layouts/header.php'; ?>
<div class="content">
    <h2 class="fw-bold mb-4">Barang Terlaris</h2>
    <div class="card shadow-sm mb-4">
        <div class="card-body">
            <form class="row align-items-end g-2 mb-4" id="filterFormTerlaris">
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
                    <label class="form-label">Top</label>
                    <input type="number" id="filterLimit" name="limit" class="form-control" value="10" min="1" style="width:80px;">
                </div>
                <div class="col-auto">
                    <button type="submit" class="btn btn-primary">
                        <i class="bi bi-funnel-fill me-2"></i>Filter
                    </button>
                </div>
            </form>
            <div class="table-responsive">
                <table class="table table-dashboard align-middle mb-0" id="tabelTerlaris">
                    <thead>
                        <tr style="background:#111; color:#fff">
                            <th>RANK</th>
                            <th>ID BARANG</th>
                            <th>NAMA BARANG</th>
                            <th>TOTAL TERJUAL</th>
                            <th>TOTAL PENJUALAN</th>
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
function loadTerlaris() {
    let dari = $('#filterDari').val();
    let sampai = $('#filterSampai').val();
    let limit = $('#filterLimit').val();
    $.get('ajax/TerlarisAjax.php', {dari, sampai, limit}, function(res){
        let rows = '';
        res.data.forEach(function(row, i){
            rows += `<tr>
                <td>${i + 1}</td>
                <td>${row.id_barang}</td>
                <td>${row.nama_barang}</td>
                <td>${row.total_jual}</td>
                <td>${formatRupiah(row.total_penjualan)}</td>
            </tr>`;
        });
        $('#tabelTerlaris tbody').html(rows);
    }, 'json');
}
$(function(){
    loadTerlaris();
    $('#filterFormTerlaris').submit(function(e){
        e.preventDefault();
        loadTerlaris();
    });
});
</script>
<?php include '../views/layouts/footer.php'; ?>
