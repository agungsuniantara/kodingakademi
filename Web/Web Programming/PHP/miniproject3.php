<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $data = array(
        array(1, "william smith", "william smith", "william smith"),
        array(2, "william smith", "william smith", "william smith"),
        array(3, "william smith", "william smith", "william smith"),
        array(4, "william smith", "william smith", "william smith")
    );

    $key = count($data);
    ?>
    <table border="1">
        <tr>
            <td>No</td>
            <td>Nama</td>
            <td>Alamat</td>
            <td>Umur</td>
        </tr>
        <?php
        for ($row = 0; $row < $key; $row++) {
            echo "<tr>";
            for ($col = 0; $col < 4; $col++) {
                echo "<td>" . $data[$row][$col] . "</td>";
            }
            echo "</tr>";
        }
        ?>
    </table>

</body>

</html>