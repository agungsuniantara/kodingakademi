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
        include "conn.php";

        $sql="select * from cobatable";

        $query=mysqli_query($conn, $sql);
        while ($data=mysqli_fetch_array($query)){
    ?>
    <table border="1">
        <tr>
            <td>id</td>
            <td>nama depan</td>
            <td>nama belakang</td>
            <td>jenis kelamin</td>
            <td>tanggal lahir</td>
            <td>alamat</td>
        </tr>
        <tr>
            <td><?php echo $data['id']; ?></td>
            <td><?php echo $data['nama_depan']; ?></td>
            <td><?php echo $data['nama_belakang']; ?></td>
            <td><?php echo $data['jenis_kelamin']; ?></td>
            <td><?php echo $data['tanggal_lahir']; ?></td>
            <td><?php echo $data['alamat']; ?></td>
        </tr>
    </table>
    <?php
    }
    ?>
</body>
</html>
