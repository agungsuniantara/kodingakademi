<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    function datadiri()
    {
        $nama2 = "wayan";
        $umur = 30;
        $alamat = "amerika";

        echo "<h1>Nama : $nama2</h1>";
        echo "<h1>Umur : $umur</h1>";
        echo "<h1>Alamat : $alamat</h1>";
    }

    function datadiriint()
    {
        $hasil = 1 + 1;
        return $hasil;
    }
    ?>

    <?php
    $nama = "agung";
    $umur = 23;
    $alamat = "denpasar";

    echo "<h1>Nama : $nama</h1>";
    echo "<h1>Umur : $umur</h1>";
    echo "<h1>Alamat : $alamat</h1>";

    datadiri();

    $coba = datadiriint();

    echo "<h1>function return : $coba</h1>";

    $data = [1, 2, 3, 4, 5];
    $jumlah = count($data);
    $total = 0;

    for ($i = 0; $i < 5; $i++) {
        echo "<h1>$data[$i]</h1>";
    }

    foreach ($data as $a) {
        echo "<h1>$a</h1>";
    }

    echo "<h1>$jumlah</h1>";

    for ($i = 0; $i < $jumlah; $i++) {
        $total += $data[$i];
    }

    $rata = $total / $jumlah;

    echo "<h1>rata - rata = $rata</h1>";
    ?>
</body>

</html>