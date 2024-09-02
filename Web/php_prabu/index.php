<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $nama = "prabu";
    $umur = 20;
    $alamat = "denpasar";

    echo "<h1>nama = $nama, umur = $umur, alamat = $alamat</h1>";

    $data = [1, 2, 3, 4, 5];

    echo "$data[0]";

    for ($i = 0; $i < 5; $i++) {
        echo "<h1>$i</h1>";
    }

    foreach ($ambil as $data) {
        echo "$data";
    }

    foreach ($data as $a) {
        echo "$a";
    }

    if ($umur == 10) {
        echo "angka = 10";
    } else {
        echo "angka selain 10";
    }

    if ($umur == 10) {
        echo "angka = 10";
    } else if ($umur == 20) {
        echo "angka = 20";
    } else {
        echo "angka tidak tersedia";
    }

    $data1 = "baru";
    $data2 = "lama";

    if ($data1 == "salah" || $data2 == "lama") {
        echo "<h1>ini or</h1>";
    }
    if ($data1 == "benar" && $data2 == "lama") {
        echo "<h1>ini and</h1>";
    }
    ?>


</body>

</html>