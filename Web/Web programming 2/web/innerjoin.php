<?php
    $koneksi = mysqli_connect("localhost", "root", "", "dbklinik");

    $table = "SELECT kunjungan.id, pasien.id, dokter.id
    FROM ((kunjungan
    INNER JOIN pasien ON kunjungan.id_pasien = pasien.id)
    INNER JOIN dokter ON kunjungan.id_dokter = dokter.id);";

    $data = mysqli_query($koneksi,$table);

    if($data){
        echo "data berhasil terhubung";
    }
    else{
        echo "data gagal terhubung";
    }
