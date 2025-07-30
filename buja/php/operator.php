<?php
    $angka1 = 10;
    $angka2 = 20;
    $angka3 = 30;

    // operator aritmatika
    $tambah = $angka1 + $angka2;
    $kurang = $angka1 - $angka2;
    $kali = $angka1 * $angka2;
    $bagi = $angka1 / $angka2;
    $pangkat = $angka1 ** $angka2;
    $modulus = $angka1 % $angka2;

    // operator perbandingan
    $lebih_besar = $angka2 > $angka3;
    $lebih_kecil = $angka2 < $angka3;
    $sama_dengan = $angka2 == $angka3;
    $lebih_besar_sama_dengan = $angka2 >= $angka3;
    $lebih_kecil_sama_dengan = $angka2 <= $angka3;
    $tidak_sama_dengan = $angka2 != $angka3;

    // operator logika
    $and = $angka2 > $angka3 && $angka1 < $angka3;
    $or = $angka2 > $angka3 || $angka1 < $angka3;
    $not = !($angka2 > $angka3) || $angka1 < $angka3;
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Operator aritmatika</h2>
    <h5><?php echo $tambah;?></h5>
    <h5><?php echo $kurang;?></h5>
    <h5><?php echo $kali;?></h5>
    <h5><?php echo $bagi;?></h5>
    <h5><?php echo $pangkat;?></h5>
    <h5><?php echo $modulus;?></h5>

    <h2>Operator assignment</h2>
    <h5><?php echo $angka1 += 1; ?></h5>
    <h5><?php echo $angka1 -= 1; ?></h5>
    <h5><?php echo $angka1 /= 1; ?></h5>
    <h5><?php echo $angka1 %= 1; ?></h5>

    <h2>Operator perbandingan</h2>
    <h5><?php echo $lebih_besar; ?></h5>
    <h5><?php echo $lebih_kecil; ?></h5>
    <h5><?php echo $sama_dengan; ?></h5>
    <h5><?php echo $lebih_besar_sama_dengan; ?></h5>
    <h5><?php echo $lebih_kecil_sama_dengan; ?></h5>
    <h5><?php echo $tidak_sama_dengan; ?></h5>

    <h2>Operator logika</h2>
    <h5><?php echo $and; ?></h5>
    <h5><?php echo $or; ?></h5>
    <h5><?php echo $not; ?></h5>
</body>
</html>