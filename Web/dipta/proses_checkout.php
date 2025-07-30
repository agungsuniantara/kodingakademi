<?php
session_start();
include "koneksi.php";

if(!isset($_SESSION["user"]) || empty($_SESSION['cart'])) {
    header("Location: login.php");
    exit;
}

if(isset($_POST['checkout'])) {
    // Get form data
    $shipping_address = $_POST['shipping_address'];
    $payment_method = $_POST['payment_method'];
    
    // Calculate total
    $total = 0;
    foreach($_SESSION['cart'] as $item) {
        $sql = "SELECT harga FROM product WHERE id_product = " . $item['id_product'];
        $query = mysqli_query($koneksi, $sql);
        $data = mysqli_fetch_assoc($query);
        $total += $data['harga'] * $item['quantity'];
    }

    // Start transaction
    mysqli_begin_transaction($koneksi);
    
    try {
        // Insert into orders table
        $sql = "INSERT INTO orders (id_user, total_amount, payment_method, shipping_address) 
                VALUES (" . $_SESSION['id_user'] . ", " . $total . ", '" . $payment_method . "', '" . $shipping_address . "')";
        mysqli_query($koneksi, $sql);
        
        $order_id = mysqli_insert_id($koneksi);

        // Insert order details
        foreach($_SESSION['cart'] as $item) {
            $sql = "SELECT harga FROM product WHERE id_product = " . $item['id_product'];
            $query = mysqli_query($koneksi, $sql);
            $data = mysqli_fetch_assoc($query);
            
            $sql = "INSERT INTO order_details (id_order, id_product, quantity, price) 
                    VALUES (" . $order_id . ", " . $item['id_product'] . ", " . $item['quantity'] . ", " . $data['harga'] . ")";
            mysqli_query($koneksi, $sql);
        }

        // Handle payment proof upload
        if(isset($_FILES['payment_proof'])) {
            $file = $_FILES['payment_proof'];
            $file_name = time() . '_' . $file['name'];
            $file_tmp = $file['tmp_name'];
            $filesize = $file['size'];
            $upload_dir = 'payment_proofs/';

            // Check if file size is more than 5MB (5MB = 5242880 bytes)
            if($filesize > 5242880) {
                echo "<script>
                    alert('Ukuran file terlalu besar. Maksimal 5MB');
                    location.href='checkout.php';
                    </script>";
                exit();
            }
            
            if(!file_exists($upload_dir)) {
                mkdir($upload_dir, 0777, true);
            }
            
            if(move_uploaded_file($file_tmp, $upload_dir . $file_name)) {
                // Insert payment record
                $sql = "INSERT INTO payments (id_order, amount, payment_proof) 
                        VALUES (" . $order_id . ", " . $total . ", '" . $file_name . "')";
                mysqli_query($koneksi, $sql);
            }
        }

        // Commit transaction
        mysqli_commit($koneksi);
        
        // Clear cart from database
        $sql = "DELETE FROM cart WHERE id_user = " . $_SESSION['id_user'];
        mysqli_query($koneksi, $sql);
        
        // Clear cart from session
        unset($_SESSION['cart']);
        
        echo "
            <script>
                alert('Pesanan berhasil dibuat! Silahkan tunggu konfirmasi pembayaran.');
                location.href = 'riwayat_pesanan.php';
            </script>
        ";
        
    } catch (Exception $e) {
        // Rollback transaction on error
        mysqli_rollback($koneksi);
        echo "
            <script>
                alert('Terjadi kesalahan: " . $e->getMessage() . "');
                location.href = 'checkout.php';
            </script>
        ";
    }
}
?> 