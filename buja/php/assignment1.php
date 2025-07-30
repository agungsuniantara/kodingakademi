<?php
    $nilai = 50;

    if ($nilai > 0 && $nilai <= 50){
        echo "<h5>nilai D</h5>";
    }
    else if($nilai > 50 && $nilai <= 70){
        echo "<h5>nilai C</h5>";
    }
    else if($nilai > 70 && $nilai <= 90){
        echo "<h5>nilai B</h5>";
    }
    else if($nilai > 90 && $nilai <= 100){
        echo "<h5>nilai A</h5>";
    }
    else{
        echo "<h5>Inputkan nilai dengan benar !!!</h5>";
    }

    $angka1 = 10;
    $angka2 = 20;
    $operator = "+";

    if ($operator == "+"){
        $hasil = $angka1 + $angka2;
        echo "<h5> hasil = $hasil </h5>";
    }
    else if($operator == "-"){
        $hasil = $angka1 - $angka2;
        echo "<h5> hasil = $hasil </h5>";
    }
    else if($operator == "*"){
        $hasil = $angka1 * $angka2;
        echo "<h5> hasil = $hasil </h5>";
    }
    else if($operator == "/"){
        $hasil = $angka1 / $angka2;
        echo "<h5> hasil = $hasil </h5>";
    }
    else if($operator == "%"){
        $hasil = $angka1 % $angka2;
        echo "<h5> hasil = $hasil </h5>";
    }
    else{
        echo "<h5> operator tidak diketahui </h5>";
    }
?>
