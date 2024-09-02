<?php
    $a = 10;
    $b = 20;

    if ($a == $b){ // false
        echo "a sama dengan b";
    }
    elseif ($a > $b){ // false
        echo "a lebih besar b";
    }
    elseif ($a < $b){ // true
        echo "a lebih kecil b";
    }
    else{
        echo "tidak ada";
    }

    if ($a > 0 && $a < 50){ // && = true and false = false
        echo "nilai D";
    }
?>