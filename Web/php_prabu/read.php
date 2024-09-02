<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <table border="1">
        <tr>
            <th>id</th>
            <th>nama</th>
            <th>alamat</th>
            <th>umur</th>
            <th>email</th>
        </tr>
        <?php
        $koneksi = mysqli_connect("localhost", "root", "", "dbprabu");
        $sql = "select * from dbprabu.user";
        $row = mysqli_query($koneksi, $sql);

        foreach ($row as $data) {
            echo "<tr>";
            echo "<td>$data[id]</td>";
            echo "<td>$data[nama]</td>";
            echo "<td>$data[alamat]</td>";
            echo "<td>$data[umur]</td>";
            echo "<td>$data[email]</td>";
            echo "</tr>";
        }
        ?>
    </table>
    <a href="create.php">register</a>


</body>

</html>