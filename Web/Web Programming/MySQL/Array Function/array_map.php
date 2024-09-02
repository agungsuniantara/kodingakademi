<?php
    function addone($val){
        return ($val + 1);
    }

    $number = array(10,20,30,40,50);

    $number2 = array_map('addone', $number);

    print_r($number2);
?>