<?php
    include "koneksi.php";

    $sql = "UPDATE db_coba  SET nama_depan='Putu' WHERE id_karyawan=1";

    if(mysqli_query($koneksi, $sql)){ 
        echo "data berhasil di update"; 
        }else{ 
        echo "data tidak berhasil di update"; 
        }
?>