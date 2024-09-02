<?php
    include "koneksi.php";

    $nama = $_POST['Nama'];
    $umur = $_POST['Umur'];
    $alamat = $_POST['Alamat'];
    $email= $_POST['Email'];
    $username = $_POST['Username'];
    $password = $_POST['Password'];

    $sql = "insert into user values('','$nama','$umur','$alamat','$email','$username','$password')";

    $masuk = mysqli_query($koneksi,$sql);

    if($masuk){
        echo"
            <script>
                alert('data berhasil di daftar');
                location.href='daftar.php';
            </script>
        ";
    }
    else{
        echo"
            <script>
                alert('data gagal di daftar');
            </script>
        ";
    }
?>