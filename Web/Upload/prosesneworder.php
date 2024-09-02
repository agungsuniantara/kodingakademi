<?php
session_start();
include "koneksi.php";

$CustomerName = $_POST['customer_name'];
$ProductName = $_POST['product_name'];
$Price = $_POST['price'];
$Number = $_POST['number'];
$TotalPrice = $_POST['total_price'];
$date = $_POST['date'];

$image = $_FILES['image'];
$imagefilename = $image['name'];
$imagefiletmp = $image['tmp_name'];
$filename_separate = explode('.', $imagefilename);
$file_extension = strtolower(end($filename_separate));
$extension = array('jpeg', 'jpg', 'png');
if (in_array($file_extension, $extension)) {
    $upload_image = 'image/' . $imagefilename;
    move_uploaded_file($imagefiletmp, $upload_image);

    $sql = "insert into coba.db_order values('', '$CustomerName', '$ProductName', '$date', '$Number', '$Price', '$TotalPrice', '$upload_image')";

    $query = mysqli_query($koneksi, $sql);

    if ($query) {
        echo "<script>
            alert ('Order berhasil');
            location.href='home.php';
            </script>";
    } else {
        echo "<script>
            alert ('Order gagal');
            location.href='home.php';
            </script>";
    }
}
