<?php
$koneksi = mysqli_connect("localhost", "root", "", "ajax");

$name = $_POST['name'];
$email = $_POST['email'];
$number = $_POST['number'];
$phone = $_POST['phone'];
$password = $_POST['password'];
$file = $_FILES['file'];
$uploadfolder = "upload/";

if (!file_exists($uploadfolder)) {
    mkdir($uploadfolder, 0777, true);
}

$targetPath = $uploadfolder . basename($file['name']);
$move = move_uploaded_file($file['tmp_name'], $targetPath);

$sql = "insert into ajax.user (name, email, number, phone, file, password) values ('$name','$email','$number','$phone','$targetPath','$password')";

$query = mysqli_query($koneksi, $sql);

if ($query) {
    $response = "berhasil upload data";
} else {
    $response = "gagal upload data";
}

echo json_encode($response);
