<?php
session_start();
include "koneksi.php";
include "alert.php";

if(!isset($_SESSION["user"])){
    showAlert('Silahkan login terlebih dahulu', 'warning', 'login.php');
    exit();
}

// Initialize cart if it doesn't exist
if(!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = array();
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id_product = $_POST['id_product'];
    $quantity = $_POST['kuantitas'];
    $id_user = $_SESSION["id_user"];

    // Check if product already exists in cart
    $check_sql = "SELECT * FROM db_project.cart WHERE id_product = '$id_product' AND id_user = '$id_user'";
    $check_query = mysqli_query($koneksi, $check_sql);

    if(mysqli_num_rows($check_query) > 0) {
        // Update quantity if product exists
        $cart_data = mysqli_fetch_assoc($check_query);
        $new_quantity = $cart_data['quantity'] + $quantity;
        
        $update_sql = "UPDATE db_project.cart SET quantity = '$new_quantity' WHERE id_product = '$id_product' AND id_user = '$id_user'";
        $update_query = mysqli_query($koneksi, $update_sql);
        
        if($update_query) {
            showAlert('Produk berhasil ditambahkan ke keranjang', 'success', 'keranjang.php');
        } else {
            showAlert('Gagal menambahkan produk ke keranjang', 'error', 'produk.php');
        }
    } else {
        // Insert new product to cart
        $insert_sql = "INSERT INTO db_project.cart (id_user, id_product, quantity) VALUES ('$id_user', '$id_product', '$quantity')";
        $insert_query = mysqli_query($koneksi, $insert_sql);
        
        if($insert_query) {
            showAlert('Produk berhasil ditambahkan ke keranjang', 'success', 'keranjang.php');
        } else {
            showAlert('Gagal menambahkan produk ke keranjang', 'error', 'produk.php');
        }
    }
} else {
    showAlert('Invalid request', 'error', 'produk.php');
}

// Redirect back to cart page
header("Location: keranjang.php");
exit;
?> 