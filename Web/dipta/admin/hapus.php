<?php
    session_start();
    include "../koneksi.php";
    include "../alert.php";

    if(!isset($_SESSION["admin"])){
        showAlert('Lakukan login terlebih dahulu', 'error', 'login.php');
        session_destroy();
    }

    $id = $_GET['id'];
    $sql = "DELETE FROM product WHERE id_product = $id";
    $query = mysqli_query($koneksi, $sql);

    if($query){
        showAlert('Data berhasil dihapus', 'success', 'produk.php');
    }
    else{
        showAlert('Data gagal dihapus', 'error', 'produk.php');
    }
?>