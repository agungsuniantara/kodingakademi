<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $data = [1, "prabu", "denpasar", "087765564453", "prabu@gmail.com"];
    $data2 = [1, "prabu", "denpasar", "087765564453", "prabu@gmail.com"];
    ?>

    <table border="1">
        <tr>
            <th>No</th>
            <th>Nama</th>
            <th>Alamat</th>
            <th>No Telp</th>
            <th>Email</th>
        </tr>
        <tr>
            <td><?php echo $data[0] ?></td>
            <td><?php echo $data[1] ?></td>
            <td><?php echo $data[2] ?></td>
            <td><?php echo $data[3] ?></td>
            <td><?php echo $data[4] ?></td>
        </tr>
    </table>

    <br>

    <table border="1">
        <tr>
            <th>No</th>
            <th>Nama</th>
            <th>Alamat</th>
            <th>No Telp</th>
            <th>Email</th>
        </tr>
        <tr>
            <?php
            foreach ($data as $a) {
                echo "<td>$a</td>";
            }
            ?>
        </tr>
        <tr>
            <?php
            foreach ($data as $a) {
                echo "<td>$a</td>";
            }
            ?>
        </tr>
        <tr>
            <?php
            foreach ($data as $a) {
                echo "<td>$a</td>";
            }
            ?>
        </tr>
    </table>
</body>

</html>