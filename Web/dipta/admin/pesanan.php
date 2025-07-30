<?php
    session_start();
    include "../koneksi.php";
    include "../alert.php";

    if(!isset($_SESSION["admin"])){
        showAlert('Lakukan login terlebih dahulu', 'error', 'login.php');
        session_destroy();
        exit;
    }

    // Handle payment confirmation
    if(isset($_POST['confirm_payment'])) {
        $order_id = $_POST['order_id'];
        $payment_status = $_POST['payment_status']; // 'success' or 'failed'
        
        // Update payment status
        $payment_sql = "UPDATE payments SET payment_status = '$payment_status' WHERE id_order = $order_id";
        $payment_query = mysqli_query($koneksi, $payment_sql);
        
        if($payment_query) {
            // Update order status based on payment status
            if($payment_status == 'success') {
                $order_sql = "UPDATE orders SET status = 'paid' WHERE id_order = $order_id";
            } else {
                $order_sql = "UPDATE orders SET status = 'cancelled' WHERE id_order = $order_id";
            }
            mysqli_query($koneksi, $order_sql);
            
            $status_message = $payment_status == 'success' ? 'Pembayaran berhasil dikonfirmasi' : 'Pembayaran ditolak';
            showAlert($status_message, 'success', 'pesanan.php');
        } else {
            showAlert('Gagal mengupdate status pembayaran', 'error', 'pesanan.php');
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kelola Pesanan - Admin Dashboard</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <!-- SweetAlert2 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css">
    <style>
        .sidebar {
            min-height: 100vh;
            background: #343a40;
            color: white;
        }
        .sidebar .nav-link {
            color: rgba(255,255,255,.8);
            padding: 1rem;
            margin: 0.2rem 0;
            border-radius: 0.25rem;
        }
        .sidebar .nav-link:hover {
            background: rgba(255,255,255,.1);
            color: white;
        }
        .sidebar .nav-link.active {
            background: #0d6efd;
            color: white;
        }
        .sidebar .nav-link.text-danger {
            color: #dc3545 !important;
            font-weight: 600;
        }
        .sidebar .nav-link.text-danger:hover {
            background: rgba(220, 53, 69, 0.1);
            color: #dc3545 !important;
        }
        .main-content {
            padding: 2rem;
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
        .order-details {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 0.5rem;
            margin-top: 1rem;
        }
        .btn-action {
            margin: 0 0.25rem;
        }
        .payment-proof-modal img {
            max-width: 100%;
            height: auto;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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
    </style>
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <!-- Sidebar -->
            <div class="col-md-3 col-lg-2 px-0 sidebar">
                <div class="p-3">
                    <h4 class="text-center mb-4">Admin Panel</h4>
                    <div class="nav flex-column">
                        <a href="../index.php" class="nav-link">
                            <i class="fas fa-home me-2"></i> Dashboard
                        </a>
                        <a href="produk.php" class="nav-link">
                            <i class="fas fa-box me-2"></i> Kelola Produk
                        </a>
                        <a href="pesanan.php" class="nav-link active">
                            <i class="fas fa-clipboard-list me-2"></i> Kelola Pesanan
                        </a>
                        <a href="../logout.php" class="nav-link text-danger">
                            <i class="fas fa-sign-out-alt me-2"></i> Logout
                        </a>
                    </div>
                </div>
            </div>

            <!-- Main Content -->
            <div class="col-md-9 col-lg-10 main-content">
                <div class="row mb-4">
                    <div class="col-12">
                        <h2 class="mb-4">Kelola Pesanan</h2>
                    </div>
                </div>

                <?php
                // Get all orders with user and payment information
                $sql = "SELECT o.*, u.nama as customer_name, p.payment_status, p.payment_proof, p.amount as payment_amount 
                        FROM orders o 
                        JOIN user u ON o.id_user = u.id_user 
                        LEFT JOIN payments p ON o.id_order = p.id_order 
                        ORDER BY o.order_date DESC";
                $query = mysqli_query($koneksi, $sql);
                ?>

                <?php if(mysqli_num_rows($query) > 0): ?>
                    <?php while($row = mysqli_fetch_assoc($query)): ?>
                        <div class="card mb-4">
                            <div class="card-header d-flex justify-content-between align-items-center">
                                <h5 class="mb-0">Pesanan #<?php echo $row['id_order']; ?></h5>
                                <span class="status <?php echo $row['status']; ?>">
                                    <?php echo ucfirst($row['status']); ?>
                                </span>
                            </div>
                            <div class="card-body">
                                <div class="row mb-3">
                                    <div class="col-md-6">
                                        <p><strong>Tanggal:</strong> <?php echo date('d/m/Y H:i', strtotime($row['order_date'])); ?></p>
                                        <p><strong>Pelanggan:</strong> <?php echo $row['customer_name']; ?></p>
                                        <p><strong>Total:</strong> Rp <?php echo number_format($row['total_amount'], 0, ',', '.'); ?></p>
                                    </div>
                                    <div class="col-md-6">
                                        <p><strong>Status Pembayaran:</strong> 
                                            <?php if($row['payment_status']): ?>
                                                <span class="payment-status <?php echo $row['payment_status']; ?>">
                                                    <?php echo ucfirst($row['payment_status']); ?>
                                                </span>
                                            <?php else: ?>
                                                <span class="payment-status pending">Pending</span>
                                            <?php endif; ?>
                                        </p>
                                        <?php if($row['payment_proof']): ?>
                                            <p><strong>Bukti Pembayaran:</strong></p>
                                            <button type="button" class="btn btn-info btn-sm" data-bs-toggle="modal" data-bs-target="#proofModal<?php echo $row['id_order']; ?>">
                                                <i class="fas fa-eye"></i> Lihat Bukti Pembayaran
                                            </button>
                                        <?php endif; ?>
                                    </div>
                                </div>

                                <div class="order-details">
                                    <h6 class="mb-3">Detail Pesanan</h6>
                                    <div class="table-responsive">
                                        <table class="table table-sm">
                                            <thead>
                                                <tr>
                                                    <th>Produk</th>
                                                    <th>Jumlah</th>
                                                    <th>Harga</th>
                                                    <th>Subtotal</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <?php
                                                $sql_items = "SELECT od.*, p.nama as product_name 
                                                            FROM order_details od 
                                                            JOIN product p ON od.id_product = p.id_product 
                                                            WHERE od.id_order = " . $row['id_order'];
                                                $query_items = mysqli_query($koneksi, $sql_items);
                                                while($item = mysqli_fetch_assoc($query_items)):
                                                ?>
                                                <tr>
                                                    <td><?php echo $item['product_name']; ?></td>
                                                    <td><?php echo $item['quantity']; ?></td>
                                                    <td>Rp <?php echo number_format($item['price'], 0, ',', '.'); ?></td>
                                                    <td>Rp <?php echo number_format($item['price'] * $item['quantity'], 0, ',', '.'); ?></td>
                                                </tr>
                                                <?php endwhile; ?>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>

                                <?php if($row['status'] == 'pending' && $row['payment_proof']): ?>
                                    <div class="mt-3">
                                        <form method="post" class="form-confirm d-inline">
                                            <input type="hidden" name="order_id" value="<?php echo $row['id_order']; ?>">
                                            <input type="hidden" name="payment_status" value="success">
                                            <input type="hidden" name="confirm_payment" value="1">
                                            <button type="button" class="btn btn-success btn-action btn-confirm">
                                                <i class="fas fa-check"></i> Konfirmasi Pembayaran
                                            </button>
                                        </form>
                                        <form method="post" class="form-tolak d-inline">
                                            <input type="hidden" name="order_id" value="<?php echo $row['id_order']; ?>">
                                            <input type="hidden" name="payment_status" value="failed">
                                            <input type="hidden" name="confirm_payment" value="1">
                                            <button type="button" class="btn btn-danger btn-action btn-tolak">
                                                <i class="fas fa-times"></i> Tolak Pembayaran
                                            </button>
                                        </form>
                                    </div>
                                <?php endif; ?>
                            </div>
                        </div>

                        <!-- Payment Proof Modal -->
                        <?php if($row['payment_proof']): ?>
                        <div class="modal fade" id="proofModal<?php echo $row['id_order']; ?>" tabindex="-1">
                            <div class="modal-dialog modal-lg">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title">Bukti Pembayaran - Pesanan #<?php echo $row['id_order']; ?></h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                                    </div>
                                    <div class="modal-body payment-proof-modal text-center">
                                        <img src="<?php echo '../'.$row['payment_proof']; ?>" alt="Bukti Pembayaran">
                                        <div class="mt-3">
                                            <p><strong>Jumlah Pembayaran:</strong> Rp <?php echo number_format($row['payment_amount'], 0, ',', '.'); ?></p>
                                            <p><strong>Status:</strong> 
                                                <span class="payment-status <?php echo $row['payment_status'] ? $row['payment_status'] : 'pending'; ?>">
                                                    <?php echo ucfirst($row['payment_status'] ? $row['payment_status'] : 'pending'); ?>
                                                </span>
                                            </p>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <?php endif; ?>
                    <?php endwhile; ?>
                <?php else: ?>
                    <div class="alert alert-info">
                        <i class="fas fa-info-circle me-2"></i>Belum ada pesanan.
                    </div>
                <?php endif; ?>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- SweetAlert2 -->
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script>
        // Konfirmasi pembayaran
        document.querySelectorAll('.btn-confirm').forEach(function(btn) {
            btn.addEventListener('click', function() {
                Swal.fire({
                    title: 'Konfirmasi Pembayaran?',
                    text: "Apakah Anda yakin ingin mengkonfirmasi pembayaran ini?",
                    icon: 'question',
                    showCancelButton: true,
                    confirmButtonColor: '#28a745',
                    cancelButtonColor: '#aaa',
                    confirmButtonText: 'Ya, Konfirmasi!',
                    cancelButtonText: 'Batal'
                }).then((result) => {
                    if (result.isConfirmed) {
                        btn.closest('form').submit();
                    }
                });
            });
        });
        // Tolak pembayaran
        document.querySelectorAll('.btn-tolak').forEach(function(btn) {
            btn.addEventListener('click', function() {
                Swal.fire({
                    title: 'Tolak Pembayaran?',
                    text: "Apakah Anda yakin ingin menolak pembayaran ini?",
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#dc3545',
                    cancelButtonColor: '#aaa',
                    confirmButtonText: 'Ya, Tolak!',
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
