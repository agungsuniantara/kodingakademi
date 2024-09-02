<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css.css">
    <title>Document</title>
    <style>
        .wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100%;
        }

        .table {
            width: 100vh;
            height: 50vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            gap: 2vh;
        }

        .konten {
            display: flex;
            align-items: center;
        }

        .konten-item {
            width: 28vh;
            height: auto;
            text-align: center;
        }

        .button {
            width: 8.4vh;
            height: 5vh;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <div class="wrapper">
        <div class="table">
            <h1>DATA BARANG</h1>
            <div class="konten">
                <div class="konten-item">No</div>
                <div class="konten-item">Nama Barang</div>
                <div class="konten-item">Jumlah Barang</div>
                <div class="konten-item">Harga Barang</div>
                <div class="konten-item">Action</div>
            </div>

            <?php
            include "koneksi.php";
            $sql = "select * from finalproject.barang";
            $query = mysqli_query($koneksi, $sql);
            $no = 1;
            while ($data = mysqli_fetch_assoc($query)) {
            ?>

                <div class="konten">
                    <div class="konten-item"><?php echo $no; ?></div>
                    <div class="konten-item"><?php echo $data['nama_barang']; ?></div>
                    <div class="konten-item"><?php echo $data['jumlah_barang']; ?></div>
                    <div class="konten-item"><?php echo $data['harga_barang']; ?></div>
                    <div class="konten-item">
                        <a href="tambah.php?id=<?php echo $data['id'] ?>"><button class="button" style="background-color: #4CAF50;">Tambah</button></a>
                        <a href="edit.php?id=<?php echo $data['id'] ?>"><button class="button" style="background-color: #4CAF50;">Edit</button></a>
                        <a href="hapusdata.php?id=<?php echo $data['id'] ?>"><button class="button" style="background-color: #f44336;">Hapus</button></a>
                    </div>
                </div>
            <?php
                $no++;
            }
            ?>
        </div>
    </div>
</body>

</html>