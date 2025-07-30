<?php
include "koneksi.php";

$name = $_POST['name'];
$username = $_POST['username'];   
$password = $_POST['password'];

$sql = "insert into project.user values('', '$name', '$username', '$password')";

$query = mysqli_query($conn, $sql);

if ($query) {
    echo "
    <script>
        alert('New Account');
        location.href = 'login.php';
    </script>
    ";
} else {
    echo "
    <script>
        alert('Failed');
        location.href = 'register.php';
    </script>
    ";
}
?>