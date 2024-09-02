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

  echo "<h1>nama =$nama,umur=$umur,alamat=$alamat</h1>";
  
  $data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  for ($i = 0; $i < 10; $i++) {
    echo "<h1>$data[$i]</h1>";
  }
  foreach ($data as $g) {
    echo "$g";
  }

  if ($umur == 20) {
    echo "<h1>angka = 10</h1>";
  } else {
    echo "<h1>angka selain 10</h1>";
  }

  if ($umur == 20) {
    echo "angka=10";
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
    echo "<h1>ini and </h1>";
  }

  ?>


</body>

</html>