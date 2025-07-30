<?php include '../views/layouts/header.php'; ?>
<link rel="stylesheet" href="../assets/css/transaksi.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

<div class="content">
    <div class="row">
        <!-- Kiri: Panel Barang -->
        <div class="col-lg-8 mb-4">
            <div class="card shadow-sm mb-4">
                <div class="card-body">
                    <h5 class="fw-bold mb-3"><i class="bi bi-receipt me-2"></i> Transaksi Baru</h5>
                    <div class="mb-3">
                        <label class="form-label fw-bold">Cari Barang</label>
                        <div class="input-group">
                            <input type="text" id="searchBarang" class="form-control" placeholder="Cari nama barang...">
                            <button class="btn btn-outline-secondary" type="button" id="btnCariBarang"><i class="bi bi-search"></i></button>
                        </div>
                        <!-- Dropdown hasil search -->
                        <div id="dropdownHasilBarang" class="list-group position-absolute z-3 w-50" style="display:none;max-height:220px;overflow:auto;"></div>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-barang align-middle" id="tabelKeranjang">
                            <thead>
                                <tr>
                                    <th>NAMA BARANG</th>
                                    <th>HARGA</th>
                                    <th>QTY</th>
                                    <th>DISKON</th>
                                    <th>SUBTOTAL</th>
                                    <th>AKSI</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr id="rowKosong"><td colspan="6" class="text-center text-muted">Belum ada item yang dipilih</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <!-- Kanan: Panel Total -->
        <div class="col-lg-4 mb-4">
            <div class="card shadow-sm">
                <div class="card-body">
                    <h5 class="fw-bold mb-3"><i class="bi bi-calculator me-2"></i> Total Transaksi</h5>
                    <form id="formPembayaran">
                        <div class="mb-3">
                            <label class="form-label">Tanggal Transaksi</label>
                            <input type="date" id="tanggal_transaksi" name="tanggal_transaksi" class="form-control" value="<?= date('Y-m-d') ?>">
                        </div>
                        <div class="mb-2">
                            <label>Subtotal:</label>
                            <span class="float-end fw-bold" id="txtSubtotal">Rp 0</span>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Diskon Transaksi</label>
                            <div class="input-group">
                                <span class="input-group-text">Rp</span>
                                <input type="number" class="form-control" id="diskonTransaksi" name="diskon" value="0" min="0">
                            </div>
                        </div>
                        <div class="mb-2">
                            <label>Total:</label>
                            <span class="float-end fw-bold fs-5 text-success" id="txtTotal">Rp 0</span>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Uang Bayar</label>
                            <div class="input-group">
                                <span class="input-group-text">Rp</span>
                                <input type="number" class="form-control" id="uangBayar" min="0">
                            </div>
                        </div>
                        <div class="mb-2">
                            <label>Kembalian:</label>
                            <span class="float-end fw-bold" id="txtKembalian">Rp 0</span>
                        </div>
                        <button class="btn btn-success w-100 my-3" type="submit"><i class="bi bi-cash-coin me-1"></i> Proses Pembayaran</button>
                        <a href="index.php?page=transaksi" class="btn btn-secondary w-100"><i class="bi bi-arrow-left me-1"></i> Kembali</a>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
let keranjang = [];
let barangList = [];
// Ambil data barang dari server sekali saja
function loadBarangList(callback) {
    if (barangList.length > 0) return callback(barangList);
    $.get('ajax/barang.php', {action: 'list'}, function(res){
        barangList = res.data || [];
        callback(barangList);
    }, 'json');
}

// Search barang
$('#searchBarang').on('input', function(){
    let keyword = $(this).val().toLowerCase();
    loadBarangList(function(list){
        let hasil = list.filter(b => b.nama_barang.toLowerCase().includes(keyword));
        let dropdown = $('#dropdownHasilBarang');
        dropdown.empty();
        if(keyword && hasil.length > 0){
            hasil.forEach(b => {
                dropdown.append(`<button type="button" class="list-group-item list-group-item-action" data-id="${b.id_barang}">${b.nama_barang} <span class="text-muted float-end">Rp ${parseInt(b.harga_jual).toLocaleString('id')}</span></button>`);
            });
            dropdown.show();
        } else {
            dropdown.hide();
        }
    });
});
// Tambahkan barang ke keranjang jika dipilih di hasil search
$(document).on('click', '#dropdownHasilBarang button', function(){
    let id = $(this).data('id');
    let barang = barangList.find(b => b.id_barang == id);
    if(!barang) return;
    // Cek double
    if(keranjang.some(k => k.id_barang == id)) return;
    keranjang.push({
        id_barang: barang.id_barang,
        nama_barang: barang.nama_barang,
        harga_jual: barang.harga_jual,
        quantity: 1,
        diskon_item: 0
    });
    renderKeranjang();
    $('#dropdownHasilBarang').hide();
    $('#searchBarang').val('');
});
$(document).click(function(e){
    if (!$(e.target).closest('#searchBarang, #dropdownHasilBarang').length) {
        $('#dropdownHasilBarang').hide();
    }
});

// Render keranjang ke tabel
function renderKeranjang(){
    let tbody = $('#tabelKeranjang tbody');
    tbody.empty();
    if(keranjang.length == 0){
        tbody.html(`<tr id="rowKosong"><td colspan="6" class="text-center text-muted">Belum ada item yang dipilih</td></tr>`);
        hitungRingkasan();
        return;
    }
    keranjang.forEach((item, i) => {
        tbody.append(`
            <tr>
                <td>${item.nama_barang}</td>
                <td>
                    <input type="number" class="form-control harga-barang" value="${item.harga_jual}" min="0" data-idx="${i}">
                </td>
                <td>
                    <input type="number" class="form-control qty-barang" value="${item.quantity}" min="1" data-idx="${i}">
                </td>
                <td>
                    <input type="number" class="form-control diskon-barang" value="${item.diskon_item||0}" min="0" data-idx="${i}">
                </td>
                <td class="subtotal-barang" id="subtotal-barang-${i}">Rp 0</td>
                <td>
                    <button class="btn btn-danger btn-sm btn-hapus-barang" data-idx="${i}"><i class="bi bi-trash"></i></button>
                </td>
            </tr>
        `);
    });
    hitungRingkasan();
}

// Update quantity, harga, diskon per item
$(document).on('input', '.qty-barang, .harga-barang, .diskon-barang', function(){
    let idx = $(this).data('idx');
    let qty = parseInt($(`.qty-barang[data-idx=${idx}]`).val()) || 0;
    let harga = parseInt($(`.harga-barang[data-idx=${idx}]`).val()) || 0;
    let diskon = parseInt($(`.diskon-barang[data-idx=${idx}]`).val()) || 0;
    keranjang[idx].quantity = qty;
    keranjang[idx].harga_jual = harga;
    keranjang[idx].diskon_item = diskon;
    hitungRingkasan();
});

// Hapus item
$(document).on('click', '.btn-hapus-barang', function(){
    let idx = $(this).data('idx');
    keranjang.splice(idx,1);
    renderKeranjang();
});

// Hitung subtotal, total, kembalian
function hitungRingkasan(){
    let subtotal = 0, total = 0;
    keranjang.forEach((item,i) => {
        let sub = (item.harga_jual * item.quantity) - (item.diskon_item || 0);
        subtotal += sub;
        $(`#subtotal-barang-${i}`).text('Rp ' + sub.toLocaleString('id'));
    });
    $('#txtSubtotal').text('Rp ' + subtotal.toLocaleString('id'));
    let diskonTransaksi = parseInt($('#diskonTransaksi').val()) || 0;
    total = subtotal - diskonTransaksi;
    $('#txtTotal').text('Rp ' + total.toLocaleString('id'));
    $('#totalTransaksi').val(total);
    // Hitung kembalian
    let bayar = parseInt($('#uangBayar').val()) || 0;
    let kembali = bayar - total;
    $('#txtKembalian').text('Rp ' + (kembali > 0 ? kembali.toLocaleString('id') : 0));
}

// Update total saat diskon/uang bayar diubah
$('#diskonTransaksi, #uangBayar').on('input', function(){
    hitungRingkasan();
});

// Proses pembayaran
$('#formPembayaran').submit(function(e){
    e.preventDefault();
    if(keranjang.length == 0){
        alert('Keranjang masih kosong!');
        return;
    }
    let tanggal_transaksi = $('#tanggal_transaksi').val();
    let diskon = parseInt($('#diskonTransaksi').val()) || 0;
    let total_harga = keranjang.reduce((sum, item) => sum + (item.harga_jual * item.quantity - (item.diskon_item || 0)), 0) - diskon;
    let bayar = parseInt($('#uangBayar').val()) || 0;
    let kembali = bayar - total_harga;
    if(bayar < total_harga){
        alert('Uang bayar kurang!');
        return;
    }
    // Siapkan detail untuk backend
    let detail = keranjang.map(item => ({
        id_barang: item.id_barang,
        quantity: item.quantity,
        harga_satuan: item.harga_jual,
        subtotal: (item.harga_jual * item.quantity) - (item.diskon_item || 0),
        diskon_item: item.diskon_item || 0
    }));

    $.post('ajax/transaksi.php', {
        action: 'create',
        tanggal_transaksi: tanggal_transaksi,
        total_harga: total_harga,
        diskon: diskon,
        detail: JSON.stringify(detail)
    }, function(res){
        if(res.status == 'success'){
            alert('Transaksi berhasil!');
            window.location = 'index.php?page=transaksi';
        }else{
            alert('Gagal menyimpan transaksi!');
        }
    }, 'json');
});

</script>
<?php include '../views/layouts/footer.php'; ?>
