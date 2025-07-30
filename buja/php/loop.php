<?php
    for ($i = 0; $i < 10; $i++) {
        echo "$i <br/>";
    }

    for ($i = 0; $i < 10; $i++) {
        for ($j = 0; $j < 10; $j++) {
            echo "$i $j <br/>";
        }
    }

    $i = 0;
    while ($i < 10) {
        echo "$i <br/>";
        $i++;
    }

    $i = 0;
    do {
        echo "$i <br/>";
        $i++;
    } while ($i < 10);

    $arr = array("Jaguar", "BMW", "Mercedes", "Toyota");
    foreach ($arr as $value) {
        echo "$value <br/>";
    }

    $arr = array("Jaguar", "BMW", "Mercedes", "Toyota");
    foreach ($arr as $key => $value) {
        echo "$key => $value <br/>";
    }
    
?>