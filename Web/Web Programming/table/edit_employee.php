<?php
include "config.php";

$id = $_POST['id'];
$name = $_POST['name'];
$email = $_POST['email'];
$address = $_POST['address'];
$phone = $_POST['phone'];

$sql = "update kodingakademi.employees set name = '$name', email = '$email', address = '$address', phone = '$phone' where id = '$id' ";

$query = mysqli_query($conn, $sql);

if ($query) {
    echo "
            <script>
                alert('Edit Employee');
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
