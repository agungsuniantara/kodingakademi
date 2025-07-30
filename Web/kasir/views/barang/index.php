<?php include '../views/layouts/header.php'; ?>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

<div class="content">
    <h2 class="fw-bold mb-4">Kelola Barang</h2>
    <div class="d-flex justify-content-between mb-3">
        <button class="btn btn-tambah-barang" data-bs-toggle="modal" data-bs-target="#modalBarang" id="btnTambahBarang">
            <i class="bi bi-plus-lg me-1"></i> Tambah Barang
        </button>
        <form class="d-flex" method="get" action="">
            <input type="text" class="form-control input-search-barang" id="inputSearch" placeholder="Cari barang...">
        </form>
    </div>
    <div class="card shadow-sm">
        <div class="card-body">
            <h5 class="fw-bold mb-3">Daftar Barang</h5>
            <div class="table-responsive">
                <table class="table table-barang align-middle mb-0" id="tabelBarang">
                    <thead>
                        <tr>
                            <th>ID</th><th>NAMA BARANG</th><th>KATEGORI</th>
                            <th>HARGA BELI</th><th>HARGA JUAL</th><th>STOK</th><th>AKSI</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Data barang akan diisi dengan JS/AJAX -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<!-- Modal Tambah/Edit Barang -->
<div class="modal fade" id="modalBarang" tabindex="-1" aria-labelledby="modalBarangLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <form id="formBarang">
        <div class="modal-header">
          <h5 class="modal-title" id="modalBarangLabel">Tambah Barang</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="id_barang" name="id_barang">
            <div class="mb-3">
                <label for="nama_barang" class="form-label">Nama Barang</label>
                <input type="text" class="form-control" id="nama_barang" name="nama_barang" required>
            </div>
            <div class="mb-3">
                <label for="kategori" class="form-label">Kategori</label>
                <input type="text" class="form-control" id="kategori" name="kategori" required>
            </div>
            <div class="mb-3">
                <label for="harga_beli" class="form-label">Harga Beli</label>
                <input type="number" class="form-control" id="harga_beli" name="harga_beli" required>
            </div>
            <div class="mb-3">
                <label for="harga_jual" class="form-label">Harga Jual</label>
                <input type="number" class="form-control" id="harga_jual" name="harga_jual" required>
            </div>
            <div class="mb-3">
                <label for="stok" class="form-label">Stok</label>
                <input type="number" class="form-control" id="stok" name="stok" required>
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-light" data-bs-dismiss="modal">Batal</button>
          <button type="submit" class="btn btn-tambah-barang">Simpan</button>
        </div>
      </form>
    </div>
  </div>
</div>
<!-- End Modal -->

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
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
</script>
<?php include '../views/layouts/footer.php'; ?>
