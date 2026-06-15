<?php
    $koneksi = mysqli_connect("localhost","root","root","test");

    $id = 1;
    $name = "wayan";
    $salary = 140000;

    $sql = "UPDATE emp5 SET `name` = '$name', emp_salary = '$salary' WHERE id = '$id'";
    $result = mysqli_query($koneksi, $sql);

    if ($result) {
        echo "berhasil update";
    }
    else{
        echo "gagal update";
    }
?>