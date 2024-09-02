<?php
    include "koneksi.php";

    $Nama_depan = $_POST['nama_depan'];
    $Nama_belakang = $_POST['nama_belakang'];
    $Jenis_kelamin = $_POST['jenis_kelamin'];
    $Tanggal_lahir = $_POST['tanggal_lahir'];
    $Alamat = $_POST['alamat'];
    $Email = $_POST['email'];
    $Password = $_POST['password'];

    $sql = "insert into coba.db_coba values('', '$Nama_depan', '$Nama_belakang', '$Jenis_kelamin', '$Tanggal_lahir', '$Alamat', '$Email', '$Password')";

    $query = mysqli_query($koneksi, $sql);
    if($query){
        echo "<script>
        alert ('Data berhasil disimpan');
        location.href='registration.php';
        </script>";
    }else{
        echo "<script>
        alert ('Data gagal disimpan');
        location.href='registration.php';
        </script>";
    }
?>