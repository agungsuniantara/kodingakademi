<?php
    $conn = new mysqli("localhost", "root", "", "student");
    if ($conn){
        echo "berhasil tekoneksi";
    }
    else{
        echo "gagal terkoneksi";
    }
?>  