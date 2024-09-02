<?php
    $array = array("Jaguar", "Audi", "Mercedes", "BMW");
    $ukuran = count($array);

    for($i = 0; $i < $ukuran; $i++){
        echo $array[$i], "\n";
    }

    foreach($array as $var){
        echo "\n$var";
    }

?>