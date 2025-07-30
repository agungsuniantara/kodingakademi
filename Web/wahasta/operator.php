<?php
    $a = 5; // 0101
    $b = 3; // 0011

    var_dump($a & $b); // 0101 and 0011 = 0001, 5 & 3 = 1
    var_dump($a | $b); // 0101 or 0011 = 0111, 5 | 3 = 7

    $umur = 20;
    $result = ($umur >= 18) ? "dewasa" : "anak-anak"; // true : false

    $nilai = 80;

    $hasil = ($nilai >= 90) ? "A" : (($nilai >= 75) ? "B" : "C");

    for ($i = 6; $i <= 5; $i++){
        echo "iterasi ke " . $i;
    }
?>