<?php
session_start();
include "koneksi.php";

$username = $_POST['username'];
$password = $_POST['password'];

$sql = "select * from finalproject.user where username = '$username' and password = '$password'";
$query = mysqli_query($koneksi, $sql);
$row = mysqli_num_rows($query);

if ($row > 0) {
    $data = mysqli_fetch_assoc($query);
    $username = $data['username'];
    $_SESSION['username'] = $username;

    echo "<script>
        alert ('Login berhasil');
        location.href='home.php';
        </script>";
} else {
    echo "<script>
        alert ('Akun tidak ditemukan');
        location.href='login.php';
        </script>";
}
