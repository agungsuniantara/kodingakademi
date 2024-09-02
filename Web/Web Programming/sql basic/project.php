<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="tengah">
        <div>
        <form action="" method="post">
        ID Karyawan : <input type="text" name="id_karyawan" style="margin-left: 20px;"><br>
        Nama Depan : <input type="text" name="nama_depan" style="margin-left: 20px;"><br>
        Nama Belakang: <input type="text" name="nama_belakang" style="margin-left: 10px;"><br>
        Jenis Kelamin : <input type="text" name="jenis_kelamin" style="margin-left: 20px;"><br>
        Tanggal Lahir : <input type="date" name="tanggal_lahir" style="margin-left: 20px;"><br>
        Alamat : <input type="text" name="alamat" style="margin-left: 20px;"><br>
        <input type="submit">
        <a href="project2.php">tampil data</a>
    </form>
    <?php
        $id_karyawan = $_POST['id_karyawan'];
        $nama_depan = $_POST['nama_depan'];
        $nama_belakang = $_POST['nama_belakang'];
        $jenis_kelamin = $_POST['jenis_kelamin'];
        $tanggal_lahir = $_POST['tanggal_lahir'];
        $alamat = $_POST['alamat'];

        $koneksi = mysqli_connect("localhost", "root", "", "sistem_informasi_karyawan");
        $input = "insert into identitas values('$id_karyawan','$nama_depan','$nama_belakang','$jenis_kelamin','$tanggal_lahir','$alamat')";
        $data = mysqli_query($koneksi,$input);

        if($data){
            echo "
                <script>
                    alert('data berhasil disimpan');
                </script>
            ";
        }else{
            echo "
                <script>
                    alert('data gagal disimpan');
                </script>
            ";
        }
    ?>
</body>
</html>