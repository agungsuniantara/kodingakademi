<?php
    $angka1 = $_POST["angka1"]; 
    $angka2 = $_POST["angka2"];
    $operator = $_POST["operator"];

    if ($operator == "tambah"){
        $hasil = $angka1 + $angka2;
        echo "
            <h1> HASIL : $hasil </h1>
        ";
    }
    else if ($operator == "kurang"){
        $hasil = $angka1 + $angka2;
        echo "
            <h1> HASIL : $hasil </h1>
        ";
    }
?>