<?php
    $koneksi = mysqli_connect('localhost', 'root', '', 'miniproject')
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $koneksi = mysqli_connect("localhost", "root", "", "coba10");
        $sql = "select * from databarang";

        $query = mysqli_query($koneksi, $sql);
        while($data = mysqli_fetch_assoc($query)){
    ?>
    <table border="1">
        <tr>
            <td><?php echo $data['nama']?></td>
        </tr>
        <tr>
            <td><?php echo $data['harga']?></td>
        </tr>
        <tr>
            <td><?php echo $data['tanggal']?></td>
        </tr>
    </table>
    <?php
        }
    ?>
</body>
</html>
