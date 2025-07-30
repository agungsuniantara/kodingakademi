// ---- AJAX CRUD Barang ----
function loadBarang(keyword = '') {
    $.get('ajax/BarangAjax.php', {action: 'list', search: keyword}, function(res){
        let rows = '';
        res.data.forEach(b => {
            rows += `
            <tr>
                <td>${b.id_barang}</td>
                <td>${b.nama_barang}</td>
                <td>${b.kategori}</td>
                <td>Rp ${parseInt(b.harga_beli).toLocaleString('id')}</td>
                <td>Rp ${parseInt(b.harga_jual).toLocaleString('id')}</td>
                <td>${b.stok}</td>
                <td>
                    <button class="btn btn-edit btn-sm" data-id="${b.id_barang}"><i class="bi bi-pencil-square"></i></button>
                    <button class="btn btn-delete btn-sm" data-id="${b.id_barang}"><i class="bi bi-trash"></i></button>
                </td>
            </tr>`;
        });
        $('#tabelBarang tbody').html(rows);
    }, 'json');
}
loadBarang();

$('#btnTambahBarang').click(function(){
    $('#formBarang')[0].reset();
    $('#id_barang').val('');
    $('#modalBarangLabel').text('Tambah Barang');
});

$('#formBarang').submit(function(e){
    e.preventDefault();
    let action = $('#id_barang').val() ? 'edit' : 'create';
    let formData = $(this).serialize() + '&action=' + action;

    $.post('ajax/BarangAjax.php', formData, function(res){
        console.log('Response:', res);
        if(res.status === 'success'){
            $('#modalBarang').modal('hide');
            loadBarang();
        } else {
            alert('Gagal menyimpan data!');
        }
    }, 'json').fail(function(xhr, status, error){
        alert('AJAX Error: ' + error + "\nResponse: " + xhr.responseText);
    });
});

$(document).on('click', '.btn-edit', function(){
    let id = $(this).data('id');
    $.get('ajax/BarangAjax.php', {action: 'get', id_barang: id}, function(res){
        if(res.status === 'success'){
            let b = res.data;
            $('#modalBarang').modal('show');
            $('#modalBarangLabel').text('Edit Barang');
            $('#id_barang').val(b.id_barang);
            $('#nama_barang').val(b.nama_barang);
            $('#kategori').val(b.kategori);
            $('#harga_beli').val(b.harga_beli);
            $('#harga_jual').val(b.harga_jual);
            $('#stok').val(b.stok);
        }
    }, 'json');
});

$(document).on('click', '.btn-delete', function(){
    if(confirm('Hapus barang ini?')) {
        let id = $(this).data('id');
        $.post('ajax/BarangAjax.php', {action: 'delete', id_barang: id}, function(res){
            if(res.status === 'success'){
                loadBarang();
            } else {
                alert('Gagal menghapus!');
            }
        }, 'json');
    }
});

// Search barang
$('#inputSearch').on('input', function(){
    let keyword = $(this).val();
    loadBarang(keyword);
});