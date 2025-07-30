<?php
    $data = array("satu", "dua", "tiga", "empat");

    // sizeof
    echo "<h1>". sizeof($data)."</h1>";

    // is_array
    echo is_array($data) ? "<h1>Array</h1>" : "<h1>Not array</h1>"; // true : false

    // in_array
    echo in_array("dua", $data) ? "<h1>iya</h1>" : "<h1>tidak</h1>";

    // print_r 
    print_r($data);

    // array_merge

    echo "<br>";
    $data2 = array("lima", "enam", "tujuh");
    $merge = array_merge($data, $data2);
    print_r($merge);

    // array_value
    echo "<br>";
    $value = array_values($merge);
    
    foreach($value as $data){
        echo $data." ";
    }

    // array_keys
    echo "<br>";
    $keys = array_keys($merge);
    
    foreach($keys as $data){
        echo $data." ";
    }

    // array_pop
    echo "<br>";
    array_pop($merge);
    print_r($merge);

    // array_push
    echo "<br>";
    array_push($merge, "haloha");
    print_r($merge);

    // array_shift
    echo "<br>";
    array_shift($merge);
    print_r($merge);

    // sort
    echo "<br>";
    sort($merge);
    print_r($merge);

    // map

    function add($a){
        return ($a + 1);
    }

    echo "<br>";
    $angka = array(1,2,3,4);
    $hasil = array_map('add', $angka);
    print_r($hasil);

    // array flip

    echo "<br>";
    $data_baru = array("nama" => "buja", "alamat" => "denpasar");
    $baru = array_flip($data_baru);
    print_r($baru);

    // array reverse

    echo "<br>";
    $angka = array(10,20,30,40);
    print_r(array_reverse($angka));

    // array_rand

    echo "<br>";
    $test = $merge[array_rand($merge)];
    echo $test;

    // array slice
    echo "<br>";
    print_r($merge);
    echo "<br>";
    $baru = array_slice($merge, 1, 3);
    print_r($baru);

?>