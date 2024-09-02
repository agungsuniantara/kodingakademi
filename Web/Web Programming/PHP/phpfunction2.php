<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="" method="post">
        <input type="text" name="angka1">
        <input type="text" name="angka2">
        <select name="kondisi" id="">
            <option value="plus">tambah</option>
            <option value="multiply">kali</option>
        </select>
        <input type="submit">
    </form>

    <?php
    $angka1 = $_POST['angka1'];
    $angka2 = $_POST['angka2'];
    $kondisi = $_POST['kondisi'];

    if ($kondisi == "plus") {
        $hasil = $angka1 + $angka2;
        echo "<h1>hasil = $hasil </h1>";
    } elseif ($kondisi == "multiply") {
        $hasil = $angka1 * $angka2;
        echo "<h1> hasil = $hasil </h1>";
    }
    ?>
</body>

</html>