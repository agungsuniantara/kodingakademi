<?php
include "config.php";

$name = $_POST['name'];
$email = $_POST['email'];
$address = $_POST['address'];
$phone = $_POST['phone'];

$sql = "insert into kodingakademi.employees values('', '$name', '$email', '$address', '$phone')";

$query = mysqli_query($conn, $sql);

if ($query) {
    echo "
            <script>
                alert('New Employee');
                location.href = 'index.php';
            </script>
        ";
} else {
    echo "
            <script>
                alert('Failed');
                location.href = 'index.php';
            </script>
        ";
}
