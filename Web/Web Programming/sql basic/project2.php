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
        $database = mysqli_connect("localhost", "root", "", "sistem_informasi_karyawan");

        $table = "select * from identitas";

        $sql = mysqli_query($database, $table);

        while($data = mysqli_fetch_assoc($sql)){

    ?>
    id_karyawan : <?php echo $data['id_karyawan']?><br>
    nama_depan : <?php echo $data['nama_depan']?><br>
    nama_belakang : <?php echo $data['nama_belakang']?><br>
    jenis_kelamin : <?php echo $data['jenis_kelamin']?><br>
    tanggal_lahir : <?php echo $data['tanggal_lahir']?><br>
    alamat : <?php echo $data['alamat']?><br>
    <br>

    <?php
        }
    ?>
</body>
</html>