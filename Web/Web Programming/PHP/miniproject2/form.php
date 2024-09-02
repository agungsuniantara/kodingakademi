<?php
    session_start();
    $koneksi=mysqli_connect('localhost','root','','miniproject');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet"type="text/css" href="miniprojecttable.css?<?php echo time(); ?>" />
    <title>Mini Project</title>
</head>
<body>  
    <div id="latar">
        <div class="parent">
        <div class="input">
            <div class="form">
                <form action="" method="post">
                    <input type="text" name="nama" placeholder="Nama barang" class="isiform"><br>
                    <input type="number" name="harga" placeholder="Harga" class="isiform"><br>
                    <input type="date" name="tanggal" class="isiform"><br>
                    <input type="submit" name="submit" class="submit" value="Submit">
                </form>
                <?php
                    $nama = $_POST['nama'];
                    $harga = $_POST['harga'];
                    $tanggal = $_POST['tanggal'];

                    $sqlinput = "insert into databarang values('$nama', '$harga', '$tanggal')";
                    mysqli_query($koneksi, $sqlinput);
                ?>
            </div>
        </div>
        </div>
    </div>
</body>
</html>