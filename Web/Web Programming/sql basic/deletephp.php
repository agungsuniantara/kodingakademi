<?php
    $koneksi = mysqli_connect('localhost', 'root', '', 'miniproject');

    $id = 1;

    $sql = "delete from identitas where id = '$id'";

    $hapus = mysqli_query($koneksi, $sql);

    if($hapus){
        print("data berhasil di hapus");
    }
    else{
        print("data gagal di hapus");
    }
