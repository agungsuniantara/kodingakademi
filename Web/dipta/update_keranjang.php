<?php
session_start();
include "koneksi.php";
include "alert.php";

if(!isset($_SESSION["user"])){
    showAlert('Silahkan login terlebih dahulu', 'warning', 'login.php');
    exit();
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id_cart = $_POST['id_keranjang'];
    $quantity = $_POST['quantity'];
    $id_user = $_SESSION["id_user"];

    // Update quantity in cart
    $update_sql = "UPDATE db_project.cart SET quantity = '$quantity' WHERE id_cart = '$id_cart' AND id_user = '$id_user'";
    $update_query = mysqli_query($koneksi, $update_sql);
    
    if($update_query) {
        // showAlert('Kuantitas berhasil diperbarui', 'success', 'keranjang.php');
    } else {
        showAlert('Gagal memperbarui kuantitas', 'error', 'keranjang.php');
    }
} else {
    showAlert('Invalid request', 'error', 'keranjang.php');
}
?>
