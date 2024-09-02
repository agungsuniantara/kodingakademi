<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post">
        Nama : <input type="text" placeholder="masukkan nama" name="nama">
        Umur : <input type="number" placeholder="masukkan umur" name="umur">
        Alamat : <input type="text" placeholder="masukkan alamat" name="alamat">
        <input type="submit">
    </form>
    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $nama = isset($_POST['nama']) ? $_POST['nama'] : '';
        $umur = isset($_POST['umur']) ? $_POST['umur'] : '';
        $alamat = isset($_POST['alamat']) ? $_POST['alamat'] : '';

        $filename = 'assignment.txt';
        $content = 'Nama : ' . $nama . PHP_EOL . 'Umur : ' . $umur . PHP_EOL . 'Alamat : ' . $alamat;

        if (file_put_contents($filename, $content)) {
            echo '<br> File written successfully.';
        } else {
            echo '<br> Error: Unable to create file ' . $filename;
        }
    }
    ?>
</body>

</html>