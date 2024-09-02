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
  <div class="div1">
    <form action="" method="post" name="form_register">
      <label for="nama">Nama :</label>
      <input type="text" id="nama" name="nama">
      <label for="alamat">alamat:</label>
      <input type="text" id="alamat" name="alamat">
      <label for="umur">umur :</label>
      <input type="umur" id="umur" name="umur">
      <label for="email">email :</label>
      <input type="text" id="email" name="email">
      <button name="submit">submit</button>

    </form>
  </div>

</body>



</html>

<?php
if (isset($_POST['submit'])) {

  $koneksi = mysqli_connect("localhost", "root", "", "dbprabu");
  $nama = $_POST['nama'];
  $alamat = $_POST['alamat'];
  $umur = $_POST['umur'];
  $email = $_POST['email'];

  $sql = "insert into dbprabu.user value('','$nama','$alamat','$umur','$email')";
  $query = mysqli_query($koneksi, $sql);

  if ($query) {
    echo "
  <script>
  alert('good boy');
  location.href='db.php';
</script>
  ";
  }
}

?>