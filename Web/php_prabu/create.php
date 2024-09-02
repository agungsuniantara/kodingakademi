<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        <?php include "style.css" ?>
    </style>
</head>

<body>
    <form action="" method="post" name="form_register">
        <label for="nama">nama : </label>
        <input type="text" name="nama" id="nama">
        <label for="alamat">alamat : </label>
        <input type="text" name="alamat" id="alamat">
        <label for="umur">umur : </label>
        <input type="text" name="umur" id="umur">
        <label for="email">email : </label>
        <input type="text" name="email" id="email">
        <input type="submit" value="register" name="submit">
    </form>

</body>

</html>

<?php
if (isset($_POST['submit'])) {
    $koneksi = mysqli_connect("localhost", "root", "", "dbprabu");
    $nama = $_POST['nama'];
    $alamat = $_POST['alamat'];
    $umur = $_POST['umur'];
    $email = $_POST['email'];

    $sql = "insert into dbprabu.user values('','$nama','$alamat', '$umur', '$email')";
    $query = mysqli_query($koneksi, $sql);

    if ($query) {
        echo "
            <script>
            alert('berhasil register');
            location.href = 'read.php';
            </script>
        ";
    }
}
?>