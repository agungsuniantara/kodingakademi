<?php
session_start();
require "config.php";

$username = $_SESSION['username'];
$password = $_POST['password'];

$sql = "update project.user set password = '$password' where username = '$username'";

$query = mysqli_query($conn, $sql);

if ($query) {
    echo "
        <script>
            alert('berhasil mengganti password');
            location.href = 'login.php';
        </script>
    ";
} else {
    echo "
        <script>
            alert('berhasil mengganti password');
            location.href = 'forgotpassword.php';
        </script>
    ";
}
