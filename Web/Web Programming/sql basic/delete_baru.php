<?php
    $koneksi = mysqli_connect("localhost","root","root","test");
    
    $sql = "DELETE FROM emp5 WHERE id = 2";
    $result = mysqli_query($koneksi, $sql);
    
    if ($result) {
        echo "berhasil delete";
    }
    else{
        echo "gagal delete";
    }
?>