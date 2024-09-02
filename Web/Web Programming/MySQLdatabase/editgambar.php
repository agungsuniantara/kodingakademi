<?php
	session_start();
	if (isset($_SESSION['nama_depan']))
	{
?>
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
            background-image: url(https://img.freepik.com/free-vector/hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg?w=2000);
            background-repeat: no-repeat;
            background-size: 100%;
        }
        input[type=text], input[type=password] {
            width: 100%;
            padding: 7px;
            margin-bottom: 20px;
            border: none;
            border-bottom: 2px solid red;
            box-sizing: border-box;
        }
        input[type=submit]{
            padding: 10px 100px;
            margin-top: 10px;
            background-color: red;
            color: white;
            border: none;
            text-decoration: none;
            cursor: pointer;
        }
        .button{
            text-align: center;
        }
        .parent{
            margin: auto;
            padding: 10px;
            height: 700px;
            width: 500px;
            background-color: white;
        }
        .parent2{
            margin-left: 50px;
            margin-right: 50px;
        }
        img{
            width: 150px;
            height: 100px;
        }
    </style>
</head>
<body>
<?php
	include "koneksi.php";
    $KodeOrder = $_GET['KodeOrder'];
	$sql="select * from db_order where id_order = '$KodeOrder'";
	$query=mysqli_query($koneksi,$sql); 
    $data=mysqli_fetch_assoc($query);
?>
    <div class="parent">
        <h1 style="text-align: center;">GAMBAR</h1>
        <div class="parent2">
            <form name="formuser" method="POST" action="uploadgambar.php" enctype="multipart/form-data">
                <input type="hidden" name="id_order" value="<?php echo $data['id_order']?>">
                <label>Gambar Produk :</label><br><br>
                <img src="<?php echo $data['image']; ?>"><br><br>
                <label>Gambar Produk Baru : </label><br><br>
                <input type="file" name="image" value="" required><br><br>
                <div class="button">
                    <input type="submit" value="UPLOAD">
                </div>
            </form>
        </div>
    </div>
</body>
</html>
<?php
    }
?>