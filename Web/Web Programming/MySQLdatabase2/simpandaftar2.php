<?php
    include "koneksi.php";
    
    $Nama_depan = mysqli_real_escape_string($koneksi, $_POST['nama_depan']);
    $Nama_belakang = mysqli_real_escape_string($koneksi, $_POST['nama_belakang']);
    $Jenis_kelamin = mysqli_real_escape_string($koneksi, $_POST['jenis_kelamin']);
    $Tanggal_lahir = mysqli_real_escape_string($koneksi, $_POST['tanggal_lahir']);
    $Alamat = mysqli_real_escape_string($koneksi, $_POST['alamat']);
    $Email = mysqli_real_escape_string($koneksi, $_POST['email']);
    $Password = password_hash($_POST['password'], PASSWORD_DEFAULT); // Hash password

    // Prepare statement
    $stmt = $koneksi->prepare("INSERT INTO coba.db_coba (Nama_depan, Nama_belakang, Jenis_kelamin, Tanggal_lahir, Alamat, Email, Password) VALUES (?, ?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("sssssss", $Nama_depan, $Nama_belakang, $Jenis_kelamin, $Tanggal_lahir, $Alamat, $Email, $Password);

    // Execute statement
    if($stmt->execute()){
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

    // Close statement and database connection
    $stmt->close();
    $koneksi->close();
?>
