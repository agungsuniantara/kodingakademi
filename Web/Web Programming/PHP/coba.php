<?php
$nilai=80;

if($nilai >= 0 && $nilai <= 50){
    echo"nilai D";
}
elseif($nilai > 50 && $nilai <= 70){
    echo"nilai C";
}
elseif($nilai > 70 && $nilai <= 80) {
    echo "nilai B";
}
elseif($nilai > 80 && $nilai <= 100)
{
    echo "nilai A";
}
else{
    echo "nilai tidak dikenal";
}
?>