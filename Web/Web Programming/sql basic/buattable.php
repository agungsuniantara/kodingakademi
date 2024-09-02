<?php
    $koneksi = mysqli_connect("localhost", "root", "", "coba10");

    $table = "create table isi(nama VARCHAR(20) NOT NULL, nama VARCHAR(20) NOT NULL)";

    $data = mysqli_query($koneksi,$table);

    if($data){
        echo "buat table berhasil";
    }
    else{
        echo "buat table gagal";
    }
?>