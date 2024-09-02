<?php
    include "koneksi.php";

    $sql = "delete from db_coba where id_karyawan=1";

    if(mysqli_query($koneksi, $sql)){ 
        echo "data berhasil dihapus"; 
        }else{ 
        echo "data tidak berhasil dihapus"; 
        }
?>