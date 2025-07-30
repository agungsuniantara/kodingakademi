<?php include '../views/layouts/header.php'; ?>
<link rel="stylesheet" href="../assets/css/transaksi.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />

<div class="content">
    <h2 class="fw-bold mb-4">Daftar Transaksi</h2>
    <div class="card shadow-sm mb-3">
        <div class="card-body">
            <h5 class="fw-bold mb-3"><i class="bi bi-journal-text me-2"></i> Daftar Transaksi</h5>
            <div class="row mb-3">
                <div class="col-md-3 mb-2">
                    <label class="form-label">Tanggal Dari</label>
                    <input type="date" id="filterTanggalDari" class="form-control" value="<?= date('Y-m-01') ?>">
                </div>
                <div class="col-md-3 mb-2">
                    <label class="form-label">Tanggal Sampai</label>
                    <input type="date" id="filterTanggalSampai" class="form-control" value="<?= date('Y-m-d') ?>">
                </div>
                <div class="col-md-3 mb-2">
                    <label class="form-label">Total Minimum</label>
                    <input type="number" id="filterTotalMin" class="form-control" placeholder="Minimal total">
                </div>
                <div class="col-md-3 mb-2 d-flex align-items-end">
                    <button class="btn btn-primary w-100" id="btnFilter"><i class="bi bi-funnel-fill me-2"></i>Filter</button>
                </div>
            </div>
            <div class="d-flex gap-3 flex-wrap mb-4">
                <div class="card-summary card-blue flex-fill">
                    <div class="p-3">
                        <div class="fw-bold mb-1">Total Transaksi</div>
                        <div class="fs-2 fw-bold" id="summaryTransaksi">0</div>
                        <div class="icon-bg"><i class="bi bi-cart2"></i></div>
                    </div>
                </div>
                <div class="card-summary card-green flex-fill">
                    <div class="p-3">
                        <div class="fw-bold mb-1">Total Pendapatan</div>
                        <div class="fs-2 fw-bold" id="summaryPendapatan">Rp 0</div>
                        <div class="icon-bg"><i class="bi bi-cash-stack"></i></div>
                    </div>
                </div>
                <div class="card-summary card-cyan flex-fill">
                    <div class="p-3">
                        <div class="fw-bold mb-1">Rata-rata Transaksi</div>
                        <div class="fs-2 fw-bold" id="summaryRata2">Rp 0</div>
                        <div class="icon-bg"><i class="bi bi-graph-up"></i></div>
                    </div>
                </div>
                <div class="card-summary card-yellow flex-fill">
                    <div class="p-3">
                        <div class="fw-bold mb-1">Total Diskon</div>
                        <div class="fs-2 fw-bold" id="summaryDiskon">Rp 0</div>
                        <div class="icon-bg"><i class="bi bi-percent"></i></div>
                    </div>
                </div>
                <div class="ms-auto">
                    <button class="btn btn-tambah-barang" id="btnTambahTransaksi"><i class="bi bi-plus-lg me-1"></i> Transaksi Baru</button>
                </div>
            </div>
            <div class="table-responsive">
                <table class="table table-transaksi align-middle mb-0" id="tabelTransaksi">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>TANGGAL</th>
                            <th>TOTAL ITEM</th>
                            <th>SUBTOTAL</th>
                            <th>DISKON</th>
                            <th>TOTAL</th>
                            <th>AKSI</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="loadingTransaksi">
                            <td colspan="7" class="spinner">
                                <div class="spinner-border text-primary" role="status">
                                    <span class="visually-hidden">Loading...</span>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <!-- Modal Tambah/Edit Transaksi -->
            <div class="modal fade" id="modalTransaksi" tabindex="-1" aria-labelledby="modalTransaksiLabel" aria-hidden="true">
                <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                        <form id="formTransaksi">
                            <div class="modal-header">
                                <h5 class="modal-title" id="modalTransaksiLabel">Tambah Transaksi</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button>
                            </div>
                            <div class="modal-body">
                                <input type="hidden" id="id_transaksi" name="id_transaksi">
                                <div class="row mb-3">
                                    <div class="col-md-6">
                                    <label for="tanggal_transaksi" class="form-label">Tanggal Transaksi</label>
                                    <input type="date" class="form-control" id="tanggal_transaksi" name="tanggal_transaksi" required>
                                    </div>
                                </div>
                            <hr>
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-2">
                                    <label class="fw-bold">Daftar Barang</label>
                                    <button type="button" class="btn btn-sm btn-secondary" id="btnTambahBarangDetail">
                                        <i class="bi bi-plus-lg"></i> Tambah Barang
                                    </button>
                                </div>
                                <div class="table-responsive">
                                    <table class="table table-bordered" id="tableDetailBarang">
                                        <thead>
                                        <tr>
                                            <th style="width:35%">Nama Barang</th>
                                            <th style="width:10%">Qty</th>
                                            <th style="width:20%">Harga</th>
                                            <th style="width:15%">Diskon</th>
                                            <th style="width:20%">Subtotal</th>
                                            <th style="width:10%"></th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        <!-- Baris detail barang dinamis -->
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div class="mt-3 d-flex justify-content-end">
                                <div>
                                    <label class="fw-bold me-2">Total Harga: </label>
                                    <span id="totalHargaText" class="fw-bold text-success">Rp 0</span>
                                    <input type="hidden" name="total_harga" id="total_harga" value="0">
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-light" data-bs-dismiss="modal">Batal</button>
                                <button type="submit" class="btn btn-primary">Simpan</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>
<script>
let daftarBarang = [];
function getDaftarBarang(callback){
    if(daftarBarang.length > 0) return callback(daftarBarang);
    $.get('ajax/BarangAjax.php', {action: 'list'}, function(res){
        daftarBarang = res.data || [];
        callback(daftarBarang);
    }, 'json');
}

// === TABLE TRANSAKSI ===
function loadTransaksi() {
    let tanggal_dari = $('#filterTanggalDari').val();
    let tanggal_sampai = $('#filterTanggalSampai').val();
    let total_min = $('#filterTotalMin').val();
    $('#tabelTransaksi tbody').html(`
        <tr id="loadingTransaksi">
            <td colspan="7" class="spinner">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </td>
        </tr>
    `);

    $.get('ajax/TransaksiAjax.php', {
        action: 'list',
        tanggal_dari: tanggal_dari,
        tanggal_sampai: tanggal_sampai,
        total_min: total_min
    }, function(res){
        $('#summaryTransaksi').text(res.summary.total_transaksi);
        $('#summaryPendapatan').text('Rp ' + parseInt(res.summary.total_pendapatan).toLocaleString('id'));
        $('#summaryRata2').text('Rp ' + parseInt(res.summary.rata2).toLocaleString('id'));
        $('#summaryDiskon').text('Rp ' + parseInt(res.summary.total_diskon).toLocaleString('id'));
        let rows = '';
        if (res.data.length > 0) {
            res.data.forEach(t => {
                rows += `
                <tr>
                    <td>${t.id_transaksi}</td>
                    <td>${t.tanggal_transaksi}</td>
                    <td>${t.total_item}</td>
                    <td>Rp ${parseInt(t.subtotal).toLocaleString('id')}</td>
                    <td>Rp ${parseInt(t.diskon).toLocaleString('id')}</td>
                    <td>Rp ${parseInt(t.total_harga).toLocaleString('id')}</td>
                    <td>
                        <button class="btn btn-edit btn-sm" data-id="${t.id_transaksi}">
                            <i class="bi bi-pencil-square"></i>
                        </button>
                        <button class="btn btn-delete btn-sm" data-id="${t.id_transaksi}">
                            <i class="bi bi-trash"></i>
                        </button>
                        <button class="btn btn-cetak btn-sm btn-success" data-id="${t.id_transaksi}">
                            <i class="bi bi-printer"></i> Cetak
                        </button>
                    </td>
                </tr>`;
            });
        } else {
            rows = `<tr><td colspan="7" class="text-center text-muted">Tidak ada data transaksi.</td></tr>`;
        }
        $('#tabelTransaksi tbody').html(rows);
    }, 'json');
}
loadTransaksi();
$('#btnFilter').click(loadTransaksi);

// === MODAL TAMBAH/EDIT ===

function formatRupiah(angka) {
    return 'Rp ' + parseInt(angka || 0).toLocaleString('id');
}

function hitungTotalDanSubtotal() {
    let total = 0;
    $('#tableDetailBarang tbody tr').each(function(){
        let qty = parseInt($(this).find('.qty-barang').val()) || 0;
        let harga = parseInt($(this).find('.harga-barang').val()) || 0;
        let diskonItem = parseInt($(this).find('.diskon-barang').val()) || 0;
        let subtotal = (qty * harga) - diskonItem;
        $(this).find('.subtotal-barang').val(subtotal);
        $(this).find('.subtotal-barang-text').text(formatRupiah(subtotal));
        total += subtotal;
    });
    $('#total_harga').val(total);
    $('#totalHargaText').text(formatRupiah(total));
}


function tambahBarisBarang(barang = {}) {
    getDaftarBarang(function(barangList){
        let options = '<option value="">-- Pilih Barang --</option>';
        barangList.forEach(b => {
            options += `<option value="${b.id_barang}" data-harga="${b.harga_jual}">${b.nama_barang}</option>`;
        });
        let tr = $(`
        <tr>
            <td>
                <select class="form-select nama-barang" name="id_barang[]" style="width: 100%;">${options}</select>
            </td>
            <td>
                <input type="number" name="quantity[]" class="form-control qty-barang" value="${barang.quantity||1}" min="1">
            </td>
            <td>
                <input type="number" name="harga_satuan[]" class="form-control harga-barang" value="${barang.harga_satuan||''}" min="0">
            </td>
            <td>
                <input type="number" name="diskon_item[]" class="form-control diskon-barang" value="${barang.diskon_item||0}" min="0">
            </td>
            <td>
                <span class="subtotal-barang-text">Rp 0</span>
                <input type="hidden" class="subtotal-barang" name="subtotal[]" value="0">
            </td>
            <td>
                <button type="button" class="btn btn-danger btn-sm btn-hapus-barang"><i class="bi bi-x"></i></button>
            </td>
        </tr>
        `);

        // Event2 seperti sebelumnya...
        tr.find('.nama-barang').change(function(){
            let harga = $(this).find('option:selected').data('harga') || 0;
            tr.find('.harga-barang').val(harga);
            hitungTotalDanSubtotal();
        });
        tr.find('.qty-barang, .harga-barang, .diskon-barang').on('input', hitungTotalDanSubtotal);
        tr.find('.btn-hapus-barang').click(function(){
            tr.remove();
            hitungTotalDanSubtotal();
        });
        if(barang.id_barang) tr.find('.nama-barang').val(barang.id_barang).trigger('change');
        if(barang.harga_satuan) tr.find('.harga-barang').val(barang.harga_satuan);
        if(barang.quantity) tr.find('.qty-barang').val(barang.quantity);

        $('#tableDetailBarang tbody').append(tr);

        // === SELECT2
        tr.find('.nama-barang').select2({
            dropdownParent: $('#modalTransaksi'),
            placeholder: '-- Pilih Barang --',
            allowClear: true,
            width: 'resolve'
        });

        hitungTotalDanSubtotal();
    });
}

// Tambah baris baru saat klik tombol
$('#btnTambahBarangDetail').click(function(){ tambahBarisBarang(); });
// Reset form/modal
$('#btnTambahTransaksi').click(function(){
    $('#formTransaksi')[0].reset();
    $('#tableDetailBarang tbody').html('');
    tambahBarisBarang();
    $('#modalTransaksiLabel').text('Tambah Transaksi');
    $('#modalTransaksi').modal('show');
});
$('#diskon').on('input', hitungTotalDanSubtotal);

// EDIT transaksi
$(document).on('click', '.btn-edit', function(){
    let id = $(this).data('id');
    $.get('ajax/TransaksiAjax.php', {action: 'get', id_transaksi: id}, function(res){
        if(res.status === 'success'){
            let t = res.data;
            $('#modalTransaksiLabel').text('Edit Transaksi');
            $('#id_transaksi').val(t.id_transaksi);
            $('#tanggal_transaksi').val(t.tanggal_transaksi);
            $('#diskon').val(t.diskon);
            $('#total_harga').val(t.total_harga);

            // detail barang
            $('#tableDetailBarang tbody').html('');
            if (t.detail && t.detail.length > 0) {
                t.detail.forEach(function(det) {
                    tambahBarisBarang({
                        id_barang: det.id_barang,
                        quantity: det.quantity,
                        harga_satuan: det.harga_satuan
                    });
                });
            } else {
                tambahBarisBarang();
            }
            $('#modalTransaksi').modal('show');
        }
    }, 'json');
});
// Submit transaksi (create/edit)
$('#formTransaksi').submit(function(e){
    e.preventDefault();
    let detail = [];
    $('#tableDetailBarang tbody tr').each(function(){
        detail.push({
            id_barang: $(this).find('.nama-barang').val(),
            quantity: $(this).find('.qty-barang').val(),
            harga_satuan: $(this).find('.harga-barang').val(),
            diskon_item: $(this).find('.diskon-barang').val(), 
            subtotal: $(this).find('.subtotal-barang').val()
        });
    });
    if(detail.length == 0 || detail.some(d => !d.id_barang || d.quantity <= 0)){
        alert('Isi detail barang dengan benar!');
        return;
    }
    let formData = $(this).serializeArray();
    formData.push({name: 'detail', value: JSON.stringify(detail)});

    let action = $('#id_transaksi').val() ? 'edit' : 'create';
    formData.push({name: 'action', value: action});
    $.post('ajax/TransaksiAjax.php', formData, function(res){
        if(res.status === 'success'){
            $('#modalTransaksi').modal('hide');
            loadTransaksi();
        } else {
            alert('Gagal menyimpan transaksi!');
        }
    }, 'json').fail(function(xhr, status, error){
        alert('AJAX Error: ' + error + "\nResponse: " + xhr.responseText);
    });
});

// Hapus transaksi
$(document).on('click', '.btn-delete', function(){
    if(confirm('Hapus transaksi ini?')) {
        let id = $(this).data('id');
        $.post('ajax/TransaksiAjax.php', {action: 'delete', id_transaksi: id}, function(res){
            if(res.status === 'success'){
                loadTransaksi();
            } else {
                alert('Gagal menghapus transaksi!');
            }
        }, 'json');
    }
});

// Cetak transaksi
$(document).on('click', '.btn-cetak', function(){
    let id = $(this).data('id');
    // Buka halaman cetak di tab baru (atau bisa popup/print window)
    window.open('index.php?page=cetak_transaksi&id=' + id, '_blank');
});

</script>
<?php include '../views/layouts/footer.php'; ?>
