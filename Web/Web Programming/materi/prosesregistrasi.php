<?php
include "config.php";

$nama = $_POST['nama'];
$alamat = $_POST['alamat'];
$username = $_POST['username'];
$password = $_POST['password'];

$sql = "insert into project.user values('', '$nama', '$alamat', '$username', '$password')";

if (mysqli_query($conn, $sql)) {
    echo "
    <script>
        alert('berhasil mendaftar !');
        location.href = 'login.php';
    </script>";
} else {
    echo "
    <script>
    alert('Terjadi kesalahan');
    location.href = 'register.php';
    </script>";
}

mysqli_close($conn);
