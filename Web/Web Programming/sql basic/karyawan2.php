<?php
    $database = mysqli_connect('localhost','root','','sistem_informasi_karyawan');
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
        $table = "select * from identitas";

        $gabung = mysqli_query($database, $table);

        while($data = mysqli_fetch_assoc($gabung))
        {
    ?>
    <table border="1">
        <tr>
            <td><?php echo $data['id_karyawan']?></td>
        </tr>
        <tr>
            <td><?php echo $data['nama_depan']?></td>
        </tr>
        <tr>
            <td><?php echo $data['nama_belakang']?></td>
        </tr>
        <tr>
            <td><?php echo $data['jenis_kelamin']?></td>
        </tr>
        <tr>
            <td><?php echo $data['tanggal_lahir']?></td>
        </tr>
        <tr>
            <td><?php echo $data['alamat']?></td>
        </tr>
    </table>
    <?php
        }
    ?>
</body>
</html>