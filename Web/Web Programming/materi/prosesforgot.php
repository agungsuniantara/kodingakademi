<?php
session_start();
require "config.php";

$username = $_POST['username'];

$sql = "select * from project.user where username = '$username'";

$query = mysqli_query($conn, $sql);
$row = mysqli_num_rows($query);

if ($row > 0) {
    $data = mysqli_fetch_assoc($query);
    $_SESSION['username'] = $data['username'];

    echo "
        <script>
        alert('username terdaftar');
        location.href = 'resetpassword.php';
        </script>
    ";
} else {
    echo "
        <script>
        alert('username tidak terdaftar');
        location.href = 'forgotpassword.php';
        </script>
    ";
}
