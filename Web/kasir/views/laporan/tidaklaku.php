<?php include '../views/layouts/header.php'; ?>
<div class="content">
    <h2 class="fw-bold mb-4">Barang Tidak Laku</h2>
    <form class="row align-items-end g-2 mb-4" id="filterForm">
        <div class="col-auto"><label class="form-label">Periode</label></div>
        <div class="col"><input type="date" id="filterDari" class="form-control" value="<?= date('Y-m-01') ?>"></div>
        <div class="col"><input type="date" id="filterSampai" class="form-control" value="<?= date('Y-m-d') ?>"></div>
        <div class="col-auto">
            <button type="submit" class="btn btn-primary">
                <i class="bi bi-funnel-fill me-2"></i>Filter
            </button>
        </div>
    </form>
    <div class="card shadow-sm mb-4">
        <div class="card-body">
            <div class="table-responsive">
                <table class="table table-dashboard align-middle mb-0" id="tabelTidakLaku">
                    <thead>
                        <tr style="background:#111; color:#fff">
                            <th>RANK</th>
                            <th>ID BARANG</th>
                            <th>NAMA BARANG</th>
                            <th>SISA STOK</th>
                        </tr>
                    </thead>
                    <tbody><!-- Data by JS --></tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
function loadBarangTidakLaku() {
    let dari = $('#filterDari').val();
    let sampai = $('#filterSampai').val();
    $.get('ajax/TidaklakuAjax.php', {dari, sampai}, function(res){
        let rows = '';
        res.data.forEach((row, idx) => {
            rows += `<tr>
                <td>${idx + 1}</td>
                <td>${row.id_barang}</td>
                <td>${row.nama_barang}</td>
                <td>${row.stok}</td>
            </tr>`;
        });
        $('#tabelTidakLaku tbody').html(rows || '<tr><td colspan="4" class="text-center text-muted">Tidak ada barang tidak laku.</td></tr>');
    }, 'json');
}


$(function(){
    loadBarangTidakLaku();
    $('#filterForm').submit(function(e){
        e.preventDefault();
        loadBarangTidakLaku();
    });
});
</script>
<?php include '../views/layouts/footer.php'; ?>
