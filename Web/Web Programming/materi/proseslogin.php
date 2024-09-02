<?php
session_start();
require "config.php";

$username = $_POST['username'];
$password = $_POST['password'];

$sql = "select * from project.user where username = '$username' and password = '$password'";

$query = mysqli_query($conn, $sql);
$baris = mysqli_num_rows($query);

if ($baris > 0) {
    $data = mysqli_fetch_assoc($query);
    $nama = $data['nama'];
    $_SESSION['nama'] = $nama;

    echo "<script>
        alert ('Berhasil login !');
        location.href='home.php';
        </script>";
} else {
    echo "<script>
        alert ('Akun tidak ditemukan');
        location.href='login.php';
        </script>";
}
