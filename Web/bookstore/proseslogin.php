<?php
    session_start();
    include "koneksi.php";

    $Username = $_POST['username'];
    $Password = $_POST['password'];

    $sql = "select * from user where Username = '$Username' and Password = '$Password'";
    $query = mysqli_query($koneksi, $sql);
    $row = mysqli_num_rows($query);
    if($row > 0)
    {
        $data=mysqli_fetch_assoc($query);
        $NamaDepan = $data['Nama'];
        $_SESSION['Nama'] = $NamaDepan;

        echo "<script>
        alert ('Login berhasil');
        location.href='home.php';
        </script>";
    }
    else{
        echo "<script>
        alert ('Login gagal');
        location.href='home.php';
        </script>";
    }
?>