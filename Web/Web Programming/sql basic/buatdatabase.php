<?php
    $koneksi = mysqli_connect("localhost", "root", "", "");

    $db = "create database sistem_informasi_karyawan";

    $data = mysqli_query($koneksi,$db);

    if($data){
        echo "buat database berhasil";
    }
    else{
        echo "buat database gagal";
    }
?>