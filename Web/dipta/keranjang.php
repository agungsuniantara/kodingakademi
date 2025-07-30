<?php
    session_start();
    include "koneksi.php";
    include "alert.php";

    if(!isset($_SESSION["user"])){
        showAlert('Silahkan login terlebih dahulu', 'warning', 'login.php');
        exit();
    }

    // Handle delete cart item
    if(isset($_GET['delete'])) {
        $id_cart = $_GET['delete'];
        $id_user = $_SESSION["id_user"];

        $check_sql = "SELECT * FROM db_project.cart WHERE id_cart = '$id_cart' AND id_user = '$id_user'";
        $check_query = mysqli_query($koneksi, $check_sql);

        if(mysqli_num_rows($check_query) > 0) {
            $delete_sql = "DELETE FROM db_project.cart WHERE id_cart = '$id_cart' AND id_user = '$id_user'";
            $delete_query = mysqli_query($koneksi, $delete_sql);

            if($delete_query) {
                showAlert('Item berhasil dihapus dari keranjang', 'success', 'keranjang.php');
            } else {
                showAlert('Gagal menghapus item dari keranjang', 'error', 'keranjang.php');
            }
        } else {
            showAlert('Item tidak ditemukan', 'error', 'keranjang.php');
        }
    }

    // Handle add to cart
    if(isset($_POST['add_to_cart'])) {
        $id_product = $_POST['id_product'];
        $quantity = $_POST['quantity'];
        $id_user = $_SESSION["id_user"];
        
        $stock_sql = "SELECT stock FROM db_project.product WHERE id_product = '$id_product'";
        $stock_query = mysqli_query($koneksi, $stock_sql);
        $product = mysqli_fetch_assoc($stock_query);
        if(!$product || $product['stock'] <= 0) {
            showAlert('Stok produk habis, tidak dapat menambahkan ke keranjang', 'error', 'produk.php');
            exit();
        }
        
        $check_sql = "SELECT * FROM db_project.cart WHERE id_product = '$id_product' AND id_user = '$id_user'";
        $check_query = mysqli_query($koneksi, $check_sql);
        
        if(mysqli_num_rows($check_query) > 0) {
            showAlert('Produk sudah ada di keranjang', 'warning', 'keranjang.php');
        } else {
            $insert_sql = "INSERT INTO db_project.cart (id_user, id_product, quantity) VALUES ('$id_user', '$id_product', '$quantity')";
            $insert_query = mysqli_query($koneksi, $insert_sql);
            if(!$insert_query) {
                showAlert('Gagal menambahkan ke keranjang', 'error', 'produk.php');
            } else {
                showAlert('Produk berhasil ditambahkan ke keranjang', 'success', 'keranjang.php');
            }
        }
    }

    // Handle quantity update
    if(isset($_POST['update_quantity'])) {
        $id_cart = $_POST['id_cart'];
        $quantity = $_POST['quantity'];
        $id_user = $_SESSION["id_user"];

        $update_sql = "UPDATE db_project.cart SET quantity = '$quantity' WHERE id_cart = '$id_cart' AND id_user = '$id_user'";
        $update_query = mysqli_query($koneksi, $update_sql);

        if(!$update_query) {
            showAlert('Gagal memperbarui kuantitas', 'error', 'keranjang.php');
        }
    }

    // --- AMBIL DATA KERANJANG ---
    $id_user = $_SESSION["id_user"];
    $sql = "SELECT k.*, p.nama, p.harga, p.temp, p.stock
            FROM db_project.cart k 
            JOIN db_project.product p ON k.id_product = p.id_product 
            WHERE k.id_user = '$id_user'";
    $query = mysqli_query($koneksi, $sql);

    $cart_items = [];
    $total = 0;
    $has_zero_stock = false;
    if(mysqli_num_rows($query) > 0) {
        while($data = mysqli_fetch_assoc($query)){
            $cart_items[] = $data;
            $subtotal = $data['harga'] * $data['quantity'];
            $total += $subtotal;
            if($data['stock'] == 0) {
                $has_zero_stock = true;
            }
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keranjang - E-Commerce</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background-color: #f8f9fa; }
        .navbar {
            background: linear-gradient(135deg, #4e73df 0%, #224abe 100%);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .navbar-brand { font-weight: 600; color: white !important; }
        .nav-link { color: rgba(255,255,255,0.9) !important; transition: all 0.3s ease; }
        .nav-link:hover { color: white !important; transform: translateY(-1px); }
        .cart-container { background: white; border-radius: 1rem; box-shadow: 0 0 15px rgba(0,0,0,0.05); padding: 2rem; margin-bottom: 2rem; }
        .cart-item { background: white; border-radius: 0.5rem; padding: 1rem; margin-bottom: 1rem; transition: all 0.3s ease; border: 1px solid #e9ecef; }
        .cart-item:hover { box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
        .product-image { width: 100px; height: 100px; object-fit: cover; border-radius: 0.5rem; }
        .product-title { font-size: 1.1rem; font-weight: 600; color: #2c3e50; margin-bottom: 0.5rem; }
        .product-price { font-size: 1.1rem; font-weight: 700; color: #224abe; }
        .quantity-input { width: 80px; text-align: center; border: 2px solid #e9ecef; border-radius: 0.5rem; padding: 0.5rem; }
        .btn-remove { background: #dc3545; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.5rem; transition: all 0.3s ease; }
        .btn-remove:hover { background: #c82333; color: white; transform: translateY(-2px); }
        .btn-checkout { background: #28a745; color: white; border: none; padding: 0.8rem 2rem; border-radius: 0.5rem; transition: all 0.3s ease; font-weight: 600; }
        .btn-checkout:hover { background: #218838; color: white; transform: translateY(-2px); }
        .cart-summary { background: #f8f9fa; border-radius: 0.5rem; padding: 1.5rem; margin-top: 2rem; }
        .summary-title { font-size: 1.2rem; font-weight: 600; color: #2c3e50; margin-bottom: 1rem; }
        .summary-item { display: flex; justify-content: space-between; margin-bottom: 0.5rem; color: #6c757d; }
        .summary-total { font-size: 1.3rem; font-weight: 700; color: #224abe; border-top: 2px solid #e9ecef; padding-top: 1rem; margin-top: 1rem; }
        .empty-cart { text-align: center; padding: 3rem; color: #6c757d; }
        .empty-cart i { font-size: 4rem; color: #dee2e6; margin-bottom: 1rem; }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="index.php">
                <i class="fas fa-store me-2"></i>E-Commerce
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="index.php"><i class="fas fa-home me-1"></i> Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="produk.php"><i class="fas fa-box me-1"></i> Produk</a></li>
                    <li class="nav-item"><a class="nav-link active" href="keranjang.php"><i class="fas fa-shopping-cart me-1"></i> Cart</a></li>
                    <li class="nav-item"><a class="nav-link" href="riwayat_pesanan.php"><i class="fas fa-history me-1"></i> Riwayat</a></li>
                    <li class="nav-item"><a class="nav-link" href="logout.php"><i class="fas fa-sign-out-alt me-1"></i> Logout</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container">
        <div class="cart-container">
            <h2 class="mb-4">Keranjang Belanja</h2>
            
            <?php if(count($cart_items) > 0): ?>
                <div class="row">
                    <div class="col-lg-8">
                    <?php foreach($cart_items as $data): 
                        $subtotal = $data['harga'] * $data['quantity'];
                    ?>
                        <div class="cart-item">
                            <div class="row align-items-center">
                                <div class="col-md-2">
                                    <img src="<?php echo $data['temp']; ?>" alt="<?php echo $data['nama']; ?>" class="product-image">
                                </div>
                                <div class="col-md-4">
                                    <h5 class="product-title"><?php echo $data['nama']; ?></h5>
                                    <div class="product-price">Rp <?php echo number_format($data['harga'], 0, ',', '.'); ?></div>
                                    <?php if($data['stock'] == 0): ?>
                                        <div class="text-danger small mt-1">Stok habis! Silakan hapus produk ini.</div>
                                    <?php endif; ?>
                                </div>
                                <div class="col-md-3">
                                    <form method="POST" class="d-flex align-items-center">
                                        <input type="hidden" name="id_cart" value="<?php echo $data['id_cart']; ?>">
                                        <input type="number" name="quantity" value="<?php echo $data['quantity']; ?>" 
                                               min="1" max="<?php echo $data['stock']; ?>" class="quantity-input me-2" 
                                               onchange="this.form.submit()" <?php echo $data['stock'] == 0 ? 'disabled' : ''; ?>>
                                        <input type="hidden" name="update_quantity" value="1">
                                    </form>
                                </div>
                                <div class="col-md-2">
                                    <div class="product-price">
                                        Rp <?php echo number_format($subtotal, 0, ',', '.'); ?>
                                    </div>
                                </div>
                                <div class="col-md-1">
                                    <form method="GET" class="d-inline form-delete-cart">
                                        <input type="hidden" name="delete" value="<?php echo $data['id_cart']; ?>">
                                        <button type="button" class="btn btn-remove btn-showalert-delete">
                                            <i class="fas fa-trash"></i>
                                        </button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    <?php endforeach; ?>
                    </div>
                    <div class="col-lg-4">
                        <div class="cart-summary">
                            <h5 class="summary-title">Ringkasan Belanja</h5>
                            <div class="summary-item">
                                <span>Total Item</span>
                                <span><?php echo count($cart_items); ?> item</span>
                            </div>
                            <div class="summary-item">
                                <span>Total Harga</span>
                                <span class="summary-total">Rp <?php echo number_format($total, 0, ',', '.'); ?></span>
                            </div>
                            <?php if($has_zero_stock): ?>
                                <button class="btn btn-checkout w-100 mt-3" disabled>
                                    <i class="fas fa-shopping-bag me-2"></i>Checkout
                                </button>
                                <div class="alert alert-danger mt-3">
                                    Ada produk di keranjang yang stoknya habis.<br>
                                    Silakan hapus produk tersebut sebelum checkout.
                                </div>
                            <?php else: ?>
                                <a href="checkout.php" class="btn btn-checkout w-100 mt-3">
                                    <i class="fas fa-shopping-bag me-2"></i>Checkout
                                </a>
                            <?php endif; ?>
                        </div>
                    </div>
                </div>
            <?php else: ?>
                <div class="empty-cart">
                    <i class="fas fa-shopping-cart"></i>
                    <h3>Keranjang Belanja Kosong</h3>
                    <p>Anda belum menambahkan produk ke keranjang</p>
                    <a href="produk.php" class="btn btn-primary mt-3">
                        <i class="fas fa-shopping-bag me-2"></i>Belanja Sekarang
                    </a>
                </div>
            <?php endif; ?>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- SweetAlert2 -->
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script>
    // ShowAlert2 konfirmasi hapus item
    document.querySelectorAll('.btn-showalert-delete').forEach(function(btn){
        btn.addEventListener('click', function(e){
            Swal.fire({
                title: 'Hapus Item?',
                text: "Yakin ingin menghapus produk dari keranjang?",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#dc3545',
                cancelButtonColor: '#aaa',
                confirmButtonText: 'Ya, Hapus!',
                cancelButtonText: 'Batal'
            }).then((result) => {
                if (result.isConfirmed) {
                    btn.closest('form').submit();
                }
            });
        });
    });
    </script>
</body>
</html>
