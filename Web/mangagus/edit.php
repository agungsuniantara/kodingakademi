<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .edit {
            width: 60vh;
            height: 50vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            background-color: blue;
        }
        
        input[type=text] {
            width: 20vh;
            height: 5vh;
        }
    </style>
</head>

<body>
    <div class="wrapper">
        <div class="edit">
            <h1>NEW ORDER</h1>
            <?php
            include "koneksi.php";
            $id = $_GET['id'];
            $sql = "select * from finalproject.barang where id = '$id'";
            $query = mysqli_query($koneksi, $sql);
            $data = mysqli_fetch_assoc($query);
            ?>
            <form name="formorder" method="POST" action="prosesedit.php">
                <input type="hidden" name="id" value="<?php echo $data['id'] ?>">
                <label>Nama barang :</label>
                <input type="text" name="nama_barang" value="<?php echo $data['nama_barang'] ?>"><br>
                <label>Jumlah barang :</label>
                <input type="text" name="jumlah_barang" value="<?php echo $data['jumlah_barang'] ?>"><br>
                <label>Harga barang :</label>
                <input type="text" name="harga_barang" value="<?php echo $data['harga_barang'] ?>"><br>
                <input type="submit" value="edit">
            </form>
        </div>
    </div>


</body>

</html>