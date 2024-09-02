<?php
    include "conn.php";

    $sql = 'insert into cobatable(id, nama_depan, nama_belakang, jenis_kelamin, tanggal_lahir, alamat) values (1, "Topan", "permana", "laki-laki", "20 Juni 1999", "Jl.Raya Diponegoror gang 6 No 7")';

    if(mysqli_query($conn, $sql)){
    echo "berhasil";
    }else{
    echo "gagal";
    }
?>