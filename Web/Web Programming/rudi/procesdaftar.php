<?php
    $koneksi = mysqli_connect("localhost", "root", "", "sistem_informasi_karyawan");

    $surename = $_POST['surename'];
    $name = $_POST['name'];
    $birth = $_POST['birth'];
    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "insert into id3 values('','$surename','$name','$birth','$username','$password')";

    $masuk = mysqli_query($koneksi,$sql);

    if($masuk){
        echo"
            <script>
                alert('data berhasil di daftar');
                location.href='login.php';
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