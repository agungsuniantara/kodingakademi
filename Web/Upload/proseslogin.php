<?php
session_start();
include "koneksi.php";

$Email = $_POST['email'];
$Password = $_POST['password'];

$sql = "select * from coba.db_coba where email = '$Email' and password = '$Password'";
$query = mysqli_query($koneksi, $sql);
$row = mysqli_num_rows($query);
if ($row > 0) {
    $data = mysqli_fetch_assoc($query);
    $NamaDepan = $data['nama_depan'];
    $_SESSION['nama_depan'] = $NamaDepan;

    echo "<script>
        alert ('Login berhasil');
        location.href='home.php';
        </script>";
} else {
    echo "<script>
        alert ('Akun tidak ditemukan');
        location.href='index.php';
        </script>";
}
