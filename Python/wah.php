<?php
    function nilai($uts, $uas){
        if (($uts > 60) && ($uas > 60)){
            return "Lulus";
        }
        else{
            return "Tidak lulus";
        }
    }

    $siswa1 = nilai(70, 90);
    echo $siswa1 . "<br>";
?>