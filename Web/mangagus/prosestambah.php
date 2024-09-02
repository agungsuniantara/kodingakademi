<?php
session_start();
include "koneksi.php";

$Nama_barang = $_POST['nama_barang'];
$jumlah_barang = $_POST['jumlah_barang'];
$harga_barang = $_POST['harga_barang'];

$sql = "insert into finalproject.barang values('', '$Nama_barang', '$jumlah_barang', '$harga_barang')";

$query = mysqli_query($koneksi, $sql);

if ($query) {
    echo "<script>
        alert ('Order berhasil');
        location.href='home.php';
        </script>";
} else {
    echo "<script>
        alert ('Order gagal');
        location.href='home.php';
        </script>";
}
