<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    function tampil()
    {
        $array = array("Ben" => "Web Design", "Tom" => "Web programming", "George" => "Python basic");
        $angka = 0;

        foreach ($array as $key => $value) {
            $angka++;
            echo "<tr>";
            echo "<td>$angka</td>";
            echo "<td>$key</td>";
            echo "<td>$value</td>";
            echo "<tr>";
        }
    }
    ?>

    <table>
        <tr>
            <td>No</td>
            <td>Nama</td>
            <td>Alamat</td>
        </tr>
        <?php tampil(); ?>
    </table>
</body>

</html>