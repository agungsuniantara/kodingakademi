<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .body, html{
            height: 100%;
            margin: 0;
        }
        .table{
            border-collapse: collapse;
        }
        .table,tr,td{
            border: 2px solid black;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <?php
        include "koneksi.php";

        $sql="select * from db_coba";

        $query=mysqli_query($koneksi, $sql);
		while ($data=mysqli_fetch_array($query)){
    ?>
    <table class="table">
        <tr>
            <td>id karyawan</td>
            <td>nama depan</td>
            <td>nama belakang</td>
            <td>jenis kelamin</td>
            <td>tanggal lahir</td>
            <td>alamat</td>
        </tr>
        <tr>
            <td><?php echo $data['id_karyawan']; ?></td>
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