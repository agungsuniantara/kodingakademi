<?php
session_start();
include "koneksi.php";
include "alert.php";

if(!isset($_SESSION["user"])){
    showAlert('Silahkan login terlebih dahulu', 'warning', 'login.php');
    exit();
}

$id_user = $_SESSION["id_user"];

// Get cart items for display
$sql = "SELECT k.*, p.nama, p.harga, p.temp 
        FROM db_project.cart k 
        JOIN db_project.product p ON k.id_product = p.id_product 
        WHERE k.id_user = '$id_user'";
$query = mysqli_query($koneksi, $sql);

if(mysqli_num_rows($query) == 0) {
    showAlert('Keranjang belanja kosong', 'warning', 'produk.php');
    exit();
}

// Handle checkout process
if(isset($_POST['checkout'])) {
    $total = $_POST['total'];
    $status = "pending";
    
    // Get cart items
    $cart_sql = "SELECT k.*, p.nama, p.harga 
                FROM db_project.cart k 
                JOIN db_project.product p ON k.id_product = p.id_product 
                WHERE k.id_user = '$id_user'";
    $cart_query = mysqli_query($koneksi, $cart_sql);
    
    if(mysqli_num_rows($cart_query) > 0) {
        // Insert into orders table
        $order_sql = "INSERT INTO db_project.orders (id_user, total_amount, status, order_date) 
                     VALUES ('$id_user', '$total', '$status', NOW())";
        $order_query = mysqli_query($koneksi, $order_sql);
        
        if($order_query) {
            $id_order = mysqli_insert_id($koneksi);
            
            // Insert order items
            while($cart_item = mysqli_fetch_assoc($cart_query)) {
                $id_product = $cart_item['id_product'];
                $quantity = $cart_item['quantity'];
                $harga = $cart_item['harga'];
                
                $order_item_sql = "INSERT INTO db_project.order_details (id_order, id_product, quantity, price) 
                                 VALUES ('$id_order', '$id_product', '$quantity', '$harga')";
                mysqli_query($koneksi, $order_item_sql);
                
                // Update product stock
                $update_stock_sql = "UPDATE db_project.product 
                                   SET stock = stock - '$quantity' 
                                   WHERE id_product = '$id_product'";
                mysqli_query($koneksi, $update_stock_sql);
            }
            
            // Clear cart
            $clear_cart_sql = "DELETE FROM db_project.cart WHERE id_user = '$id_user'";
            mysqli_query($koneksi, $clear_cart_sql);
            
            showAlert('Checkout berhasil!', 'success', 'riwayat_pesanan.php');
        } else {
            showAlert('Gagal melakukan checkout', 'error', 'checkout.php');
        }
    } else {
        showAlert('Keranjang belanja kosong', 'error', 'keranjang.php');
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout - E-Commerce</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .navbar {
            background: linear-gradient(135deg, #4e73df 0%, #224abe 100%);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .navbar-brand {
            font-weight: 600;
            color: white !important;
        }
        .nav-link {
            color: rgba(255,255,255,0.9) !important;
            transition: all 0.3s ease;
        }
        .nav-link:hover {
            color: white !important;
            transform: translateY(-1px);
        }
        .checkout-container {
            background: white;
            border-radius: 1rem;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
            padding: 2rem;
            margin-bottom: 2rem;
        }
        .order-summary {
            background: #f8f9fa;
            border-radius: 0.5rem;
            padding: 1.5rem;
        }
        .btn-checkout {
            background: #28a745;
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            border-radius: 0.5rem;
            transition: all 0.3s ease;
            font-weight: 600;
        }
        .btn-checkout:hover {
            background: #218838;
            color: white;
            transform: translateY(-2px);
        }
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
                    <li class="nav-item">
                        <a class="nav-link" href="index.php">
                            <i class="fas fa-home me-1"></i> Home
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="produk.php">
                            <i class="fas fa-box me-1"></i> Produk
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="keranjang.php">
                            <i class="fas fa-shopping-cart me-1"></i> Cart
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="logout.php">
                            <i class="fas fa-sign-out-alt me-1"></i> Logout
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container">
        <div class="checkout-container">
            <h2 class="mb-4">Checkout</h2>
            
            <?php if(mysqli_num_rows($query) > 0): ?>
                <div class="row">
                    <div class="col-lg-8">
                        <div class="order-items mb-4">
                            <h4 class="mb-3">Pesanan Anda</h4>
                            <?php 
                                $total = 0;
                                while($data = mysqli_fetch_assoc($query)): 
                                    $subtotal = $data['harga'] * $data['quantity'];
                                    $total += $subtotal;
                            ?>
                                <div class="card mb-3">
                                    <div class="card-body">
                                        <div class="row align-items-center">
                                            <div class="col-md-2">
                                                <img src="<?php echo $data['temp']; ?>" alt="<?php echo $data['nama']; ?>" class="img-fluid rounded">
                                            </div>
                                            <div class="col-md-4">
                                                <h5 class="card-title"><?php echo $data['nama']; ?></h5>
                                                <p class="card-text">Rp <?php echo number_format($data['harga'], 0, ',', '.'); ?></p>
                                            </div>
                                            <div class="col-md-3">
                                                <p class="card-text">Jumlah: <?php echo $data['quantity']; ?></p>
                                            </div>
                                            <div class="col-md-3">
                                                <p class="card-text fw-bold">Subtotal: Rp <?php echo number_format($subtotal, 0, ',', '.'); ?></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            <?php endwhile; ?>
                        </div>
                    </div>
                    
                    <div class="col-lg-4">
                        <div class="order-summary">
                            <h4 class="mb-3">Ringkasan Pesanan</h4>
                            <div class="d-flex justify-content-between mb-2">
                                <span>Total Item</span>
                                <span><?php echo mysqli_num_rows($query); ?> item</span>
                            </div>
                            <div class="d-flex justify-content-between mb-3">
                                <span>Total Harga</span>
                                <span class="fw-bold">Rp <?php echo number_format($total, 0, ',', '.'); ?></span>
                            </div>
                            <form method="POST">
                                <input type="hidden" name="total" value="<?php echo $total; ?>">
                                <button type="submit" name="checkout" class="btn btn-checkout w-100">
                                    <i class="fas fa-shopping-bag me-2"></i>Proses Checkout
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            <?php else: ?>
                <div class="text-center py-5">
                    <i class="fas fa-shopping-cart fa-3x text-muted mb-3"></i>
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
</body>
</html> 