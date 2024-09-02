<?php
session_start();
include "dbkoneksi.php";

$username = $_POST['username'];
$password = $_POST['password'];

$sql = "select * from dbklinik.users where username = '$username' and password = '$password'";
$query = mysqli_query($conn, $sql);
$row = mysqli_num_rows($query);
if ($row > 0) {
    $data = mysqli_fetch_assoc($query);
    $nama = $data['namalengkap'];
    $_SESSION['namalengkap'] = $nama;

    echo "<script>
        alert ('Login berhasil');
        location.href='admin.php';
        </script>";
} else {
    echo "<script>
        alert ('Akun tidak ditemukan');
        location.href='login.php';
        </script>";
}
