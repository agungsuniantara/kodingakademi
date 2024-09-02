<?php
    $koneksi = mysqli_connect("localhost", "root", "", "miniproject");

    $id = 1;
    $nama = "bagus";
    $alamat = "canggu";

    $sql = "update coba set nama='$nama', alamat = '$alamat' where id='$id'";

    $ganti = mysqli_query($koneksi, $sql);

    if($ganti){
        print("data berhasil diganti");
    }
    else{
        print("data gagal diganti");
    }
?>