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
    </style>
</head>
<body>
    <div class="parent">
        <h1 style="text-align: center;">NEW ORDER</h1>
        <div class="parent2">
            <form name="formorder" method="POST" action="prosesneworder.php" enctype="multipart/form-data">
                <label>Nama :</label>
                <input type="text" name="customer_name">
                <label>Nama Produk :</label>
                <input type="text" name="product_name">
                <label>Gambar Produk :</label><br><br>
                <input type="file" name="image" value=""><br><br>
                <label>Tanggal :</label>
                <input type="text" name="date">
                <label>Harga :</label>
                <input type="text" name="price">
                <label>Banyak Produk :</label>
                <input type="text" name="number">
                <label>Total Harga :</label>
                <input type="text" name="total_price">
                <div class="button">
                    <input type="submit" value="ORDER">
                </div>
            </form>
        </div>
    </div>
</body>
</html>
<?php
    }
?>