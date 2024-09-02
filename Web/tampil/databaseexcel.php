<?php
require 'SimpleXLSXGen.php';
require 'koneksi.php';

$header = [
    ['id_karyawan', 'nama_depan', 'nama_belakang', 'jenis_kelamin', 'tanggal_lahir', 'alamat', 'email', 'password']
];

$sql = "select * from coba.db_coba";
$query = mysqli_query($koneksi, $sql);

while (mysqli_fetch_assoc($query)) {
    foreach ($query as $row) {
        $header = array_merge($header, array(array($row['id_karyawan'], $row['nama_depan'], $row['nama_belakang'], $row['jenis_kelamin'], $row['tanggal_lahir'], $row['alamat'], $row['email'], $row['password'])));
    }
}

$write = Shuchkin\SimpleXLSXGen::fromArray($header);
$write->saveAs('database.xlsx');
