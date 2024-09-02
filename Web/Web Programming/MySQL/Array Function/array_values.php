<?php
    $lamborgini = array("suv" => "Urus", "sports" => "Huracan", "coupe" => "aventador");
    $honda = array("suru", "uracanaaaa", "aventadorsssss");

    $merged = array_merge($lamborgini, $honda);

    $merged2 = array_values($merged);

    print_r($merged2);
?>