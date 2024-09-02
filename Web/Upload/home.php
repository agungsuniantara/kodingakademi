<?php
session_start();
if (isset($_SESSION['nama_depan'])) {
?>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        <style>
            * {
                outline: none !important;
            }

            body {
                background-color: rgb(165, 215, 232);
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
            }

            .container {
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.2);
                padding: 20px;
                margin: 0 auto;
            }

            .navbar-header {
                float: none;
            }

            .navbar {
                position: sticky;
                top: 0;
                z-index: 1000;
                background-color: rgb(25, 55, 109);
            }

            .navbar-brand {
                color: white !important;
                display: flex;
                align-items: center;
            }

            .warna:hover {
                color: grey !important;
            }

            .img-responsive {
                width: 40px;
                padding-bottom: 10px;
            }

            table {
                border-collapse: collapse;
                margin: 0 auto;
                font-size: 1.3rem;
                line-height: 1.5;
            }

            table th,
            table td {
                background-color: white;
                padding: 0.8rem;
            }

            table th {
                background-color: #eee;
                font-weight: bold;
            }

            .footer {
                background-color: rgb(25, 55, 109);
                bottom: 0;
                position: fixed;
                width: 100%;
                padding-top: 10px;
                padding-bottom: 10px;
                text-align: center;
                color: white;
            }

            @media (max-width: 767px) {

                table,
                thead,
                tbody,
                th,
                td,
                tr {
                    display: block;
                }

                body {
                    height: 155%;
                }
            }
        </style>

    </head>

    <body>
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <div class="navbar-header">
                    <a class="navbar-brand" style="float:left">
                        <img src="logobaru.png" class="img-responsive">
                        Welcome
                        <?php
                        $NamaDepan = $_SESSION['nama_depan'];
                        echo $NamaDepan;
                        ?>
                    </a>
                    <a class="navbar-brand" style="float: right;"></a>
                    <a class="navbar-brand" href="logout.php" style="float: right;"> Logout</a>
                </div>
            </div>
        </nav>

        <div class="container">
            <table>
                <thead>
                    <tr>
                        <th>No</th>
                        <th>Nama</th>
                        <th>Gambar</th>
                        <th>Pesanan</th>
                        <th>Harga</th>
                        <th>Jumlah</th>
                        <th>Total harga</th>
                        <th>
                            <a href="neworder.php">Tambah order + </a>
                        </th>
                    </tr>
                </thead>
                <?php
                include "koneksi.php";
                $sql = "select * from coba.db_order";
                $query = mysqli_query($koneksi, $sql);
                $no = 1;
                while ($data = mysqli_fetch_assoc($query)) {
                ?>
                    <tbody>
                        <tr>
                            <td><?php echo $no; ?></td>
                            <td><?php echo $data['customer_name']; ?></td>
                            <td><img src="<?php echo $data['image']; ?>" style="width:100px;height:100px"></td>
                            <td><?php echo $data['product_name']; ?></td>
                            <td><?php echo $data['price']; ?></td>
                            <td><?php echo $data['number']; ?></td>
                            <td><?php echo $data['total_price']; ?></td>
                            <td>
                                <a href="edit.php?KodeOrder=<?php echo $data['id_order'] ?>"><button type="submit" class="btn btn-success">Edit</button></a>
                                <a href="hapusdata.php?KodeOrder=<?php echo $data['id_order'] ?>"><button type="submit" class="btn btn-danger">Hapus</button></a>

                            </td>
                        </tr>
                    <?php
                    $no++;
                }
                    ?>
                    <tr>
                        <td colspan="8" style="height:60px;">

                        </td>
                    </tr>
                    </tbody>
            </table>
        </div>

        <footer class="footer">
            <div>
                &#169 Agung Suniantara 2023
            </div>
        </footer>
    </body>

    </html>
<?php
} else {
    echo "<script>
		alert ('Maaf anda tidak bisa akses halaman ini');
		location.href='index.php';
			
		</script>";
}
?>