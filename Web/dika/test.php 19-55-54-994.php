<?php

$data = [10,20,30,40,50];
$genap = []; 
$ganjil = [];

for ($i = 0; $i < count($data); $i++) {
    if ($data[$i] % 2 == 0) {
        array_push($genap, $data[$i]);
    } else {
        array_push($ganjil, $data[$i]);
    }
}

echo "Jumlah angka genap : ".(count($genap));
echo "Jumlah angka ganjil : ".(count($ganjil));
?>