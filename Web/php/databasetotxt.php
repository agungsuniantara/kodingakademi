<?php
include "koneksi.php";

$sql = "select * from coba.db_coba";
$query = mysqli_query($koneksi, $sql);

$filename = "users.txt";
$file = fopen($filename, "w");

$header = [
    ['id_karyawan', 'nama_depan', 'nama_belakang', 'jenis_kelamin', 'tanggal_lahir', 'alamat', 'email', 'password']
];

while (mysqli_fetch_assoc($query)) {
    foreach ($query as $row) {
        $line = $row['id_karyawan'] . $row['nama_depan'] . $row['nama_belakang'] . $row['jenis_kelamin'] . $row['tanggal_lahir'] . $row['alamat'] . $row['email'] . $row['password'];

        fwrite($file, $line);
    }
}

fclose($file);
$koneksi->close();
