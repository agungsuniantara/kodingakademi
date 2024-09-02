<?php
session_start();
include "koneksi.php";

$id = $_POST['id'];
$nama_barang = $_POST['nama_barang'];
$jumlah_barang = $_POST['jumlah_barang'];
$harga_barang = $_POST['harga_barang'];

$sql = "update finalproject.barang set nama_barang='$nama_barang', jumlah_barang='$jumlah_barang',harga_barang='$harga_barang' where id='$id'";

$query = mysqli_query($koneksi, $sql);

if ($query) {
    echo "<script>
        alert ('Edit berhasil');
        location.href='home.php';
        </script>";
} else {
    echo "<script>
        alert ('Edit gagal');
        location.href='home.php';
        </script>";
}
