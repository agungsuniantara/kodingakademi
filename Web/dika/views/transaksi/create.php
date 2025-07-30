<?php
$page = 'transaksi';
$pageTitle = 'Transaksi Baru';

ob_start();
?>

<div class="row">
    <!-- Form Transaksi -->
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h5 class="card-title mb-0">
                    <i class="fas fa-shopping-cart"></i> Transaksi Baru
                </h5>
            </div>
            <div class="card-body">
                <!-- Search Barang -->
                <div class="mb-3">
                    <label class="form-label">Cari Barang</label>
                    <div class="input-group">
                        <input type="text" class="form-control" id="searchBarang" placeholder="Cari nama barang...">
                        <button class="btn btn-outline-secondary" type="button" id="btnSearchBarang">
                            <i class="fas fa-search"></i>
                        </button>
                    </div>
                </div>

                <!-- Hasil Pencarian -->
                <div id="searchResults" class="mb-3" style="display: none;">
                    <div class="card">
                        <div class="card-body">
                            <h6>Hasil Pencarian:</h6>
                            <div id="searchResultsList"></div>
                        </div>
                    </div>
                </div>

                <!-- Daftar Item Transaksi -->
                <div class="table-responsive">
                    <table class="table table-striped" id="transaksiTable">
                        <thead class="table-dark">
                            <tr>
                                <th>Nama Barang</th>
                                <th>Harga</th>
                                <th>Qty</th>
                                <th>Diskon</th>
                                <th>Subtotal</th>
                                <th>Aksi</th>
                            </tr>
                        </thead>
                        <tbody id="transaksiItems">
                            <tr id="emptyRow">
                                <td colspan="6" class="text-center text-muted">Belum ada item yang dipilih</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <!-- Summary dan Pembayaran -->
    <div class="col-md-4">
        <div class="card sticky-top">
            <div class="card-header">
                <h5 class="card-title mb-0">
                    <i class="fas fa-calculator"></i> Total Transaksi
                </h5>
            </div>
            <div class="card-body">
                <div class="mb-3">
                    <label class="form-label">Tanggal Transaksi</label>
                    <input type="date" class="form-control" id="tanggalTransaksi" value="<?= date('Y-m-d') ?>">
                </div>

                <hr>

                <div class="d-flex justify-content-between mb-2">
                    <span>Subtotal:</span>
                    <span id="subtotalAmount">Rp 0</span>
                </div>
                
                <div class="mb-3">
                    <label class="form-label">Diskon Transaksi</label>
                    <div class="input-group">
                        <span class="input-group-text">Rp</span>
                        <input type="number" class="form-control" id="diskonTransaksi" value="0" min="0">
                    </div>
                </div>

                <div class="d-flex justify-content-between mb-3">
                    <strong>Total:</strong>
                    <strong id="totalAmount">Rp 0</strong>
                </div>

                <hr>

                <div class="mb-3">
                    <label class="form-label">Uang Bayar</label>
                    <div class="input-group">
                        <span class="input-group-text">Rp</span>
                        <input type="number" class="form-control" id="uangBayar" min="0">
                    </div>
                </div>

                <div class="d-flex justify-content-between mb-3">
                    <span>Kembalian:</span>
                    <span id="kembalian">Rp 0</span>
                </div>

                <div class="d-grid gap-2">
                    <button type="button" class="btn btn-success btn-lg" id="btnBayar" disabled>
                        <i class="fas fa-money-bill"></i> Proses Pembayaran
                    </button>
                    <a href="index.php?page=transaksi" class="btn btn-secondary">
                        <i class="fas fa-arrow-left"></i> Kembali
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

<?php
$content = ob_get_clean();

// JavaScript untuk functionality kasir
ob_start();
?>
<script>
let transaksiItems = [];
let itemCounter = 0;

$(document).ready(function() {
    // Search barang
    $('#searchBarang, #btnSearchBarang').on('click keyup', function(e) {
        if (e.type === 'click' || (e.type === 'keyup' && e.keyCode === 13)) {
            searchBarang();
        }
    });

    // Event listeners
    $('#diskonTransaksi, #uangBayar').on('input', updateTotals);
    $('#btnBayar').on('click', prosesTransaksi);
});

function searchBarang() {
    const keyword = $('#searchBarang').val().trim();
    if (keyword.length < 2) {
        $('#searchResults').hide();
        return;
    }

    // Show loading state
    $('#searchResultsList').html('<div class="text-center"><i class="fas fa-spinner fa-spin"></i> Mencari...</div>');
    $('#searchResults').show();

    // Debug logging
    console.log('Searching for:', keyword);

    $.ajax({
        url: 'index.php?page=barang&action=search',
        method: 'GET',
        data: { keyword: keyword },
        dataType: 'json',
        success: function(response) {
            console.log('Search response:', response);
            if (response.error) {
                $('#searchResultsList').html(`<div class="alert alert-danger">${response.error}</div>`);
            } else {
                displaySearchResults(response);
            }
        },
        error: function(xhr, status, error) {
            console.error('Search error:', {xhr, status, error});
            $('#searchResultsList').html(`<div class="alert alert-danger">Error: ${error}</div>`);
        }
    });
}

function displaySearchResults(barang) {
    console.log('Displaying results:', barang);
    let html = '';
    if (!barang || barang.length === 0) {
        html = '<p class="text-muted">Barang tidak ditemukan</p>';
    } else {
        barang.forEach(function(item) {
            html += `
                <div class="d-flex justify-content-between align-items-center border-bottom py-2">
                    <div>
                        <strong>${item.nama_barang}</strong><br>
                        <small class="text-muted">${item.kategori} | Stok: ${item.stok}</small><br>
                        <small>Rp ${parseInt(item.harga_jual).toLocaleString('id-ID')}</small>
                    </div>
                    <button class="btn btn-sm btn-primary" onclick="addToTransaction(${JSON.stringify(item).replace(/"/g, '&quot;')})">
                        <i class="fas fa-plus"></i> Tambah
                    </button>
                </div>
            `;
        });
    }
    
    $('#searchResultsList').html(html);
    $('#searchResults').show();
}

function addToTransaction(barang) {
    // Check if item already exists
    const existingIndex = transaksiItems.findIndex(item => item.id_barang === barang.id_barang);
    
    if (existingIndex !== -1) {
        // Increase quantity
        transaksiItems[existingIndex].quantity += 1;
        updateItemRow(existingIndex);
    } else {
        // Add new item
        const newItem = {
            id: ++itemCounter,
            id_barang: barang.id_barang,
            nama_barang: barang.nama_barang,
            harga_satuan: parseFloat(barang.harga_jual),
            quantity: 1,
            diskon_item: 0,
            subtotal: parseFloat(barang.harga_jual)
        };
        
        transaksiItems.push(newItem);
        addItemRow(newItem);
    }
    
    updateTotals();
    $('#searchBarang').val('');
    $('#searchResults').hide();
}

function addItemRow(item) {
    $('#emptyRow').hide();
    
    const row = `
        <tr id="item-${item.id}">
            <td>${item.nama_barang}</td>
            <td>Rp ${item.harga_satuan.toLocaleString('id-ID')}</td>
            <td>
                <div class="input-group input-group-sm" style="width: 100px;">
                    <button class="btn btn-outline-secondary" type="button" onclick="updateQuantity(${item.id}, -1)">-</button>
                    <input type="number" class="form-control text-center" value="${item.quantity}" min="1" 
                           onchange="updateQuantity(${item.id}, 0, this.value)">
                    <button class="btn btn-outline-secondary" type="button" onclick="updateQuantity(${item.id}, 1)">+</button>
                </div>
            </td>
            <td>
                <input type="number" class="form-control form-control-sm" value="${item.diskon_item}" min="0" 
                       style="width: 80px;" onchange="updateDiskon(${item.id}, this.value)">
            </td>
            <td id="subtotal-${item.id}">Rp ${item.subtotal.toLocaleString('id-ID')}</td>
            <td>
                <button class="btn btn-sm btn-danger" onclick="removeItem(${item.id})">
                    <i class="fas fa-trash"></i>
                </button>
            </td>
        </tr>
    `;
    
    $('#transaksiItems').append(row);
}

function updateItemRow(index) {
    const item = transaksiItems[index];
    $(`#item-${item.id} input[type="number"]`).first().val(item.quantity);
    updateSubtotal(item.id);
}

function updateQuantity(itemId, change, newValue = null) {
    const index = transaksiItems.findIndex(item => item.id === itemId);
    if (index === -1) return;
    
    if (newValue !== null) {
        transaksiItems[index].quantity = Math.max(1, parseInt(newValue));
    } else {
        transaksiItems[index].quantity = Math.max(1, transaksiItems[index].quantity + change);
    }
    
    updateSubtotal(itemId);
    updateTotals();
}

function updateDiskon(itemId, diskon) {
    const index = transaksiItems.findIndex(item => item.id === itemId);
    if (index === -1) return;
    
    transaksiItems[index].diskon_item = Math.max(0, parseFloat(diskon) || 0);
    updateSubtotal(itemId);
    updateTotals();
}

function updateSubtotal(itemId) {
    const index = transaksiItems.findIndex(item => item.id === itemId);
    if (index === -1) return;
    
    const item = transaksiItems[index];
    item.subtotal = (item.harga_satuan * item.quantity) - item.diskon_item;
    
    $(`#subtotal-${itemId}`).text('Rp ' + item.subtotal.toLocaleString('id-ID'));
}

function removeItem(itemId) {
    transaksiItems = transaksiItems.filter(item => item.id !== itemId);
    $(`#item-${itemId}`).remove();
    
    if (transaksiItems.length === 0) {
        $('#emptyRow').show();
    }
    
    updateTotals();
}

function updateTotals() {
    const subtotal = transaksiItems.reduce((sum, item) => sum + item.subtotal, 0);
    const diskonTransaksi = parseFloat($('#diskonTransaksi').val()) || 0;
    const total = subtotal - diskonTransaksi;
    const uangBayar = parseFloat($('#uangBayar').val()) || 0;
    const kembalian = uangBayar - total;
    
    $('#subtotalAmount').text('Rp ' + subtotal.toLocaleString('id-ID'));
    $('#totalAmount').text('Rp ' + total.toLocaleString('id-ID'));
    $('#kembalian').text('Rp ' + Math.max(0, kembalian).toLocaleString('id-ID'));
    
    // Enable/disable bayar button
    $('#btnBayar').prop('disabled', transaksiItems.length === 0 || uangBayar < total);
}

function prosesTransaksi() {
    if (transaksiItems.length === 0) {
        alert('Belum ada item yang dipilih!');
        return;
    }
    
    const subtotal = transaksiItems.reduce((sum, item) => sum + item.subtotal, 0);
    const diskonTransaksi = parseFloat($('#diskonTransaksi').val()) || 0;
    const total = subtotal - diskonTransaksi;
    const uangBayar = parseFloat($('#uangBayar').val()) || 0;
    
    if (uangBayar < total) {
        alert('Uang bayar tidak mencukupi!');
        return;
    }
    
    const transaksiData = {
        tanggal_transaksi: $('#tanggalTransaksi').val(),
        total_harga: total,
        diskon: diskonTransaksi,
        items: JSON.stringify(transaksiItems.map(item => ({
            id_barang: item.id_barang,
            quantity: item.quantity,
            harga_satuan: item.harga_satuan,
            subtotal: item.subtotal,
            diskon_item: item.diskon_item
        })))
    };
    
    $.ajax({
        url: 'index.php?page=transaksi&action=store',
        method: 'POST',
        data: transaksiData,
        success: function(response) {
            const result = JSON.parse(response);
            if (result.success) {
                alert('Transaksi berhasil disimpan!');
                window.location.href = 'index.php?page=transaksi';
            } else {
                alert('Error: ' + result.error);
            }
        },
        error: function() {
            alert('Terjadi kesalahan saat menyimpan transaksi!');
        }
    });
}
</script>
<?php
$scripts = ob_get_clean();

include 'views/layout/template.php';
?>