<?php
    $arr = array("Jaguar", "BMW", "Mercedes", "Toyota");
    echo $arr[0];
    echo $arr[1];
    echo $arr[2];
    echo $arr[3];

    $arr2 = array(); 
    $arr2[0] = "satu";
    $arr2[1] = "dua";
    $arr2[2] = "tiga";
    $arr2[3] = "empat";

    echo $arr2[0];
    echo $arr2[1];

    for ($i = 0; $i < count($arr2); $i++) {
        echo $arr2[$i] . "<br/>";
    }

    foreach ($arr2 as $value) {
        echo $value . "<br/>";
    }
    
?>