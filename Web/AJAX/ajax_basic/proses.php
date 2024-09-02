<?php
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $nama = $_GET['nama'];
    $alamat = $_GET['alamat'];
    echo "nama : " . $nama . "<br> alamat : " . $alamat;
} 
elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nama = $_POST['nama'];
    $alamat = $_POST['alamat'];
    echo "nama : " . $nama . "<br> alamat : " . $alamat;
} 
else {
    echo "Invalid Request";
}
