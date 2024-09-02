<?php
include "config.php";

$id = $_GET['id'];

$sql = "delete from kodingakademi.employees where id = '$id'";

$query = mysqli_query($conn, $sql);

if ($query) {
    echo "
            <script>
                alert('Delete Employee');
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
