<?php
    $name = "wahasta";
    $alamat = "denpasar";
    $beli = "tidak";

    echo "Nama saya : " . $name . "<br>";

    $a = 10;
    $b = 20;
    $c = 30;

    $and = ($a < $b) && ($c < $b); // true && false = false
    $or = ($a < $b) || ($c < $b); // true || false = true

    var_dump($and);
    var_dump($or);
?>