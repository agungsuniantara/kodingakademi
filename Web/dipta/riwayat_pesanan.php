<?php
session_start();
include "koneksi.php";
include "alert.php";

if(!isset($_SESSION["user"])){
    showAlert('Silahkan login terlebih dahulu', 'warning', 'login.php');
    exit();
}

// Handle payment proof upload
if(isset($_POST['upload_bukti'])) {
    $id_order = $_POST['id_order'];
    $image = $_FILES['bukti_pembayaran'];
    
    // Cek apakah sudah pernah upload bukti
    $cek_bukti_sql = "SELECT payment_proof FROM db_project.payments WHERE id_order = '$id_order'";
    $cek_bukti_query = mysqli_query($koneksi, $cek_bukti_sql);
    $cek_bukti = mysqli_fetch_assoc($cek_bukti_query);

    if($cek_bukti) {
        showAlert('Bukti pembayaran sudah diupload, tidak dapat upload lagi.', 'warning', 'riwayat_pesanan.php');
        exit();
    }

    // Check for upload errors
    if ($image['error'] !== UPLOAD_ERR_OK) {
        $error_message = match($image['error']) {
            UPLOAD_ERR_INI_SIZE, UPLOAD_ERR_FORM_SIZE => 'Ukuran file terlalu besar. Maksimal 1MB',
            UPLOAD_ERR_PARTIAL => 'File hanya terupload sebagian',
            UPLOAD_ERR_NO_FILE => 'Tidak ada file yang diupload',
            UPLOAD_ERR_NO_TMP_DIR => 'Folder temporary tidak ditemukan',
            UPLOAD_ERR_CANT_WRITE => 'Gagal menulis file ke disk',
            UPLOAD_ERR_EXTENSION => 'Upload dihentikan oleh ekstensi PHP',
            default => 'Terjadi kesalahan saat upload'
        };
        showAlert($error_message, 'error', 'riwayat_pesanan.php');
        exit();
    }

    $imagefilename = $image['name'];
    $imagefiletmp = $image['tmp_name'];
    $filesize = $image['size'];
    
    // Check if file size is more than 1MB
    if($filesize > 1048576) {
        showAlert('Ukuran file terlalu besar. Maksimal 1MB', 'error', 'riwayat_pesanan.php');
        exit();
    }
    
    $filename_separate = explode('.', $imagefilename);
    $file_extension = strtolower(end($filename_separate));
    $extension = array('jpeg', 'jpg', 'png');
    
    if(in_array($file_extension, $extension)) {
        $upload_image = 'payment_proofs/'.$imagefilename;
        move_uploaded_file($imagefiletmp, $upload_image);
        
        // Update order status dan tandai bukti_uploaded
        $update_sql = "UPDATE db_project.orders SET 
                          status = 'pending'
                       WHERE id_order = '$id_order'";
        $update_query = mysqli_query($koneksi, $update_sql);
        
        if($update_query) {
            // Get order total amount
            $amount_sql = "SELECT total_amount FROM db_project.orders WHERE id_order = '$id_order'";
            $amount_query = mysqli_query($koneksi, $amount_sql);
            $order_data = mysqli_fetch_assoc($amount_query);
            $amount = $order_data['total_amount'];

            // Insert payment record
            $payment_sql = "INSERT INTO db_project.payments (id_order, payment_date, amount, payment_status, payment_proof) 
                            VALUES ('$id_order', NOW(), '$amount', 'pending', '$upload_image')";
            $payment_query = mysqli_query($koneksi, $payment_sql);
            
            if($payment_query) {
                showAlert('Bukti pembayaran berhasil diupload', 'success', 'riwayat_pesanan.php');
            } else {
                showAlert('Gagal menyimpan data pembayaran', 'error', 'riwayat_pesanan.php');
            }
        } else {
            showAlert('Gagal mengupdate status pesanan', 'error', 'riwayat_pesanan.php');
        }
    } else {
        showAlert('Format file tidak didukung. Gunakan JPG, JPEG, atau PNG', 'error', 'riwayat_pesanan.php');
    }
}

$id_user = $_SESSION["id_user"];
$sql = "SELECT o.*, u.nama as nama_user 
        FROM db_project.orders o 
        JOIN db_project.user u ON o.id_user = u.id_user 
        WHERE o.id_user = '$id_user' 
        ORDER BY o.id_order DESC";
$query = mysqli_query($koneksi, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Riwayat Pesanan - E-Commerce</title>
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
        .history-container {
            background: white;
            border-radius: 1rem;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
            padding: 2rem;
            margin-bottom: 2rem;
        }
        .order-card {
            background: white;
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border: 1px solid #e9ecef;
            transition: all 0.3s ease;
        }
        .order-card:hover {
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            transform: translateY(-2px);
        }
        .order-header {
            border-bottom: 2px solid #e9ecef;
            padding-bottom: 1rem;
            margin-bottom: 1rem;
        }
        .order-number {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2c3e50;
        }
        .order-date {
            color: #6c757d;
            font-size: 0.9rem;
        }
        .order-status {
            padding: 0.5rem 1rem;
            border-radius: 2rem;
            font-size: 0.9rem;
            font-weight: 500;
        }
        .status-pending {
            background: #fff3cd;
            color: #856404;
        }
        .status-processing {
            background: #cce5ff;
            color: #004085;
        }
        .status-completed {
            background: #d4edda;
            color: #155724;
        }
        .status-cancelled {
            background: #f8d7da;
            color: #721c24;
        }
        .status-paid {
            background: #d4edda;
            color: #155724;
        }
        .order-total {
            font-size: 1.2rem;
            font-weight: 700;
            color: #224abe;
        }
        .order-items {
            margin-top: 1rem;
        }
        .item-card {
            background: #f8f9fa;
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 0.5rem;
        }
        .item-name {
            font-weight: 500;
            color: #2c3e50;
        }
        .item-price {
            color: #6c757d;
        }
        .item-quantity {
            color: #6c757d;
            font-size: 0.9rem;
        }
        .empty-history {
            text-align: center;
            padding: 3rem;
            color: #6c757d;
        }
        .empty-history i {
            font-size: 4rem;
            color: #dee2e6;
            margin-bottom: 1rem;
        }
        .order-card {
            background: white;
            border-radius: 1rem;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            margin-bottom: 1.5rem;
        }
        .order-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        .order-header {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 1rem 1rem 0 0;
            border-bottom: 1px solid #e9ecef;
        }
        .order-body {
            padding: 1.5rem;
        }
        .order-footer {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 0 0 1rem 1rem;
            border-top: 1px solid #e9ecef;
        }
        .product-image {
            width: 80px;
            height: 80px;
            object-fit: cover;
            border-radius: 0.5rem;
        }
        .status {
            padding: 0.5rem 1rem;
            border-radius: 0.25rem;
            font-size: 0.875rem;
            font-weight: 500;
        }
        .status.pending {
            background-color: #fff3cd;
            color: #856404;
        }
        .status.paid {
            background-color: #d4edda;
            color: #155724;
        }
        .status.cancelled {
            background-color: #f8d7da;
            color: #721c24;
        }
        .payment-status {
            padding: 0.5rem 1rem;
            border-radius: 0.25rem;
            font-size: 0.875rem;
            font-weight: 500;
        }
        .payment-status.pending {
            background-color: #fff3cd;
            color: #856404;
        }
        .payment-status.success {
            background-color: #d4edda;
            color: #155724;
        }
        .payment-status.failed {
            background-color: #f8d7da;
            color: #721c24;
        }
        .empty-orders {
            text-align: center;
            padding: 3rem;
            color: #6c757d;
        }
        .empty-orders i {
            font-size: 4rem;
            color: #dee2e6;
            margin-bottom: 1rem;
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
                        <a class="nav-link active" href="riwayat_pesanan.php">
                            <i class="fas fa-history me-1"></i> Riwayat
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
        <div class="history-container">
            <h2 class="mb-4">Riwayat Pesanan</h2>
            
            <?php if(mysqli_num_rows($query) > 0): ?>
                <?php while($order = mysqli_fetch_assoc($query)): ?>
                    <div class="order-card">
                        <div class="order-header d-flex justify-content-between align-items-center">
                            <div>
                                <div class="order-number">Order #<?php echo $order['id_order']; ?></div>
                                <div class="order-date"><?php echo date('d F Y H:i', strtotime($order['order_date'])); ?></div>
                            </div>
                            <div>
                                <span class="order-status status-<?php echo strtolower($order['status']); ?>">
                                    <?php echo ucfirst($order['status']); ?>
                                </span>
                            </div>
                        </div>
                        
                        <div class="order-items">
                            <?php
                                $items_sql = "SELECT oi.*, p.nama, p.temp 
                                            FROM db_project.order_details oi 
                                            JOIN db_project.product p ON oi.id_product = p.id_product 
                                            WHERE oi.id_order = " . $order['id_order'];
                                $items_query = mysqli_query($koneksi, $items_sql);
                                while($item = mysqli_fetch_assoc($items_query)):
                            ?>
                                <div class="item-card">
                                    <div class="row align-items-center">
                                        <div class="col-md-2">
                                            <img src="<?php echo $item['temp']; ?>" alt="<?php echo $item['nama']; ?>" class="img-fluid rounded">
                                        </div>
                                        <div class="col-md-6">
                                            <div class="item-name"><?php echo $item['nama']; ?></div>
                                            <div class="item-price">Rp <?php echo number_format($item['price'], 0, ',', '.'); ?></div>
                                        </div>
                                        <div class="col-md-2">
                                            <div class="item-quantity">Jumlah: <?php echo $item['quantity']; ?></div>
                                        </div>
                                        <div class="col-md-2 text-end">
                                            <div class="item-total">Rp <?php echo number_format($item['price'] * $item['quantity'], 0, ',', '.'); ?></div>
                                        </div>
                                    </div>
                                </div>
                            <?php endwhile; ?>
                        </div>
                        
                        <div class="d-flex justify-content-between align-items-center mt-3">
                            <div class="order-total">
                                Total: Rp <?php echo number_format($order['total_amount'], 0, ',', '.'); ?>
                            </div>
                            <?php if($order['status'] == 'pending'): ?>
                                <?php if(isset($order['bukti_uploaded']) && $order['bukti_uploaded'] == 1): ?>
                                    <button type="button" class="btn btn-success" disabled style="pointer-events:none;">
                                        <i class="fas fa-check-circle me-2"></i>Centang Upload Bukti
                                    </button>
                                <?php else: ?>
                                    <button type="button" class="btn btn-primary" 
                                            data-bs-toggle="modal" 
                                            data-bs-target="#uploadModal<?php echo $order['id_order']; ?>">
                                        <i class="fas fa-upload me-2"></i>Upload Bukti Pembayaran
                                    </button>
                                <?php endif; ?>
                            <?php endif; ?>
                        </div>
                    </div>

                    <!-- Upload Modal -->
                    <div class="modal fade" id="uploadModal<?php echo $order['id_order']; ?>" tabindex="-1">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title">Upload Bukti Pembayaran</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                                </div>
                                <form method="POST" enctype="multipart/form-data">
                                    <div class="modal-body">
                                        <input type="hidden" name="id_order" value="<?php echo $order['id_order']; ?>">
                                        <div class="mb-3">
                                            <label class="form-label">Pilih File Bukti Pembayaran</label>
                                            <input type="file" class="form-control" name="bukti_pembayaran" required>
                                            <div class="form-text">Format: JPG, JPEG, PNG. Maksimal 1MB</div>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Batal</button>
                                        <button type="submit" name="upload_bukti" class="btn btn-primary">
                                            <i class="fas fa-upload me-2"></i>Upload
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                <?php endwhile; ?>
            <?php else: ?>
                <div class="empty-history">
                    <i class="fas fa-history"></i>
                    <h3>Belum Ada Pesanan</h3>
                    <p>Anda belum memiliki riwayat pesanan</p>
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
