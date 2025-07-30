<?php
    function faktor($a){
        if ($a == 0){
            return 1;
        }
        else{
            return $a * faktor($a - 1);
        }
    }

    $nilai = faktor(5);

    // 5 * faktor(4);
    // 5 * 4 * faktor(3);
    // 5 * 4 * 3 * faktor(2);
    // 5 * 4 * 3 * 2 * 1 * 1;
?>