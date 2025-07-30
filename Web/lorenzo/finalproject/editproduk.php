<?php
    session_start();
    include "koneksi.php";

    if(!isset($_SESSION['Name_user'])) {
        echo "
            <script>
                alert('Lakukan login terlebih dahulu');
                location.href = 'login.php';
            </script>
        ";
        session_destroy();
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
            body{
        background-image: url(https://png.pngtree.com/thumb_back/fw800/background/20230615/pngtree-landscape-landscape-photo-image_2902263.jpg);
        background-repeat: no-repeat;
        background-size: cover;
    }
    .wrapper{
        width: 414px;
        height: 500px;
        margin-left: 700px;
        margin-top: 250px;
        padding: 2px 20px 0px 20px;
        background-color: rgba(255, 255, 255, 0.69);
        border-radius: 10px;
    }
    input {
      width: 400px;
      margin-top: 5px;
      margin-bottom: 20px;
      padding: 5px 0px 5px 10px;
    }
    textarea {
      width: 694px;
      height: 100px;
      margin-top: 5px;
      margin-bottom: 5px;
      outline: none;
      border: none;
      border-bottom: 1px solid rgb(82, 78, 78);
      padding: 5px 0px 5px 0px;
    }
    h1 {
      text-align: center;
    }
    </style>
</head>
<body>
<?php
	include "koneksi.php";
    $KodeOrder = $_GET['KodeOrder'];
	$sql="select * from project.order where id_order = '$KodeOrder'";
	$query=mysqli_query($koneksi,$sql); 
    $data=mysqli_fetch_assoc($query);
?>
  <div class="wrapper">
    <h1>Tambah Produk</h1>
    <form method="post" enctype="multipart/form-data" action="editproses.php">
    <input type="hidden" name="id_order" value="<?php echo $data['id_order']?>">
      <label for="Name">Name</label>
      <input type="text" id="Name" name="Name" value="<?php echo $data['Name']?> placeholder="Masukkan Name"> 
      <label for="Image">Image</label>
      <input type="File" id="Image" name="Image" placeholder="Masukkan Image"> 
      <label for="Product">Product</label>
      <input type="text" id="Product" name="Product" placeholder="Masukkan Product"> 
      <label for="Price">Price</label>
      <input type="text" id="Price" name="Price" placeholder="Masukkan Price"> 
      <label for="Quantity">Quantity</label>
      <input type="text" id="Quantity" name="Quantity" placeholder="Masukkan Quantity"> 
      <input type="submit" value="Submit" style="margin-left: 6px;"> 
    </form>
  </div>
</body>
</html>