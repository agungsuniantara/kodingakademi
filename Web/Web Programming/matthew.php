<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <!-- tambah data -->
    <?php
    $koneksi = mysqli_connect("localhost", "root", "", "sistem_informasi_karyawan");

    $nama = "matthew";
    $alamat = "denpasar";
    $telp = 89;

    $sql = "insert into sistem_informasi_karyawan.user (id, nama, alamat, telp) values ('', '$nama', '$alamat', '$telp')";

    $query = mysqli_query($koneksi, $sql);

    if ($query) {
        echo "data berhasil ditambah";
    } else {
        echo "data gagal ditambah";
    }
    ?>

    <!-- tampil data -->
    <?php
    $koneksi = mysqli_connect("localhost", "root", "", "sistem_informasi_karyawan");

    $sql = "select * from sistem_informasi_karyawan.user";

    $query = mysqli_query($koneksi, $sql);

    foreach ($query as $data) {
    ?>
        <h5><?php echo $data['id'] ?></h5>
        <h5><?php echo $data['nama'] ?></h5>
        <h5><?php echo $data['alamat'] ?></h5>
        <h5><?php echo $data['telp'] ?></h5>
    <?php
    };
    ?>

    <!-- update data -->

    <?php
    $koneksi = mysqli_connect("localhost", "root", "", "sistem_informasi_karyawan");

    $nama = "agung";
    $alamat = "gianyar";
    $telp = 99;

    $sql = "update sistem_informasi_karyawan.user set nama = '$nama', alamat = '$alamat', telp = '$telp' where id = '1'";

    $query = mysqli_query($koneksi, $sql);

    if ($query) {
        echo "edit data berhasil";
    } else {
        echo "edit gagal";
    }
    ?>

    <!-- delete data -->
    <?php
    $koneksi = mysqli_connect("localhost", "root", "", "sistem_informasi_karyawan");

    $sql = "delete from sistem_informasi_karyawan.user where id = '3'";

    $query = mysqli_query($koneksi, $sql);

    if ($query) {
        echo "delete data berhasil";
    } else {
        echo "delete gagal";
    }
    ?>

</body>

</html>