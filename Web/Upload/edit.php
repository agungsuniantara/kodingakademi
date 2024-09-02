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
            html,
            body {
                height: 120%;
            }

            body {
                background-color: rgb(165, 215, 232);
                font-family: Arial, sans-serif;
                display: flex;
                align-items: center;
            }

            .container {
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.2);
                padding: 20px;
                max-width: 500px;
                margin: 0 auto;
            }

            .form-group {
                margin-bottom: 20px;
            }

            .text {
                margin-bottom: 20px;
            }

            .text a {
                text-decoration: none;
            }

            .navbar-header {
                float: none;
            }

            .navbar-fixed-top {
                top: 0;
                border-width: 0 0 1px;
            }

            .navbar {
                background-color: rgb(25, 55, 109);
            }

            .navbar-brand {
                color: white !important;
                display: flex;
                align-items: center;
            }

            .img-responsive {
                width: 40px;
                padding-bottom: 10px;
            }

            .footer {
                background-color: rgb(25, 55, 109);
                bottom: 0;
                position: fixed;
                width: 100%;
                padding-top: 10px;
                padding-bottom: 10px;
                z-index: 999999;
            }

            @media (max-width: 767px) {
                .container {
                    padding: 10px;
                }

                .form-group {
                    margin-bottom: 20px;
                }

                .text {
                    margin-bottom: 20px;
                    font-size: 10px;
                }
            }
        </style>
    </head>

    <body>
        <?php
        include "koneksi.php";
        $KodeOrder = $_GET['KodeOrder'];
        $sql = "select * from coba.db_order where id_order = '$KodeOrder'";
        $query = mysqli_query($koneksi, $sql);
        $data = mysqli_fetch_assoc($query);
        ?>
        <nav class="navbar navbar-default navbar-fixed-top">
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
                    <a class="navbar-brand" style="float: right;">

                    </a>
                    <a class="navbar-brand" href="logout.php" style="float: right;"> Logout</a>

                </div>
            </div>
        </nav>

        <div class="container">
            <h4 style="text-align: center;"><b>EDIT</b></h4>
            <hr>
            <form action="edituser.php" method="post" enctype="multipart/form-data" id="form">
                <div class="form-group">
                    <input type="hidden" name="id_order" value="<?php echo $data['id_order'] ?>">
                    <label>Nama :</label>
                    <div class="input-group">
                        <span class="input-group-addon"></span>
                        <input type="text" class="form-control" name="customer_name" value="<?php echo $data['customer_name'] ?>" required>
                    </div>
                </div>
                <div class="form-group">
                    <label>Nama produk :</label>
                    <div class="input-group">
                        <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                        <select class="form-control" name="product_name" id="product" required>
                            <option><?php echo $data['product_name'] ?></option>
                            <option>nasi goreng</option>
                            <option>pisang goreng</option>
                            <option>bakso</option>
                        </select>
                        <script>
                            document.getElementById("product").oninput = () => {
                                const product = document.getElementById('product');
                                if (product.value == "nasi goreng") {
                                    const harga = document.getElementById('harga');
                                    harga.value = 15000;
                                } else if (product.value == "pisang goreng") {
                                    const harga = document.getElementById('harga');
                                    harga.value = 5000;
                                } else if (product.value == "bakso") {
                                    const harga = document.getElementById('harga');
                                    harga.value = 20000;
                                }
                            };
                        </script>
                    </div>
                </div>
                <div class="form-group">
                    <label>Gambar produk baru :</label>
                    <div class="input-group">
                        <input type="file" class="form-control" name="image" value="" required>
                    </div>
                </div>
                <div class="form-group">
                    <label>Tanggal :</label>
                    <div class="input-group">
                        <span class="input-group-addon"></span>
                        <input type="date" class="form-control" name="date" value="<?php echo $data['date'] ?>">
                    </div>
                </div>
                <div class="form-group">
                    <label>Banyak produk :</label>
                    <div class="input-group">
                        <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                        <input type="text" class="form-control" name="number" value="<?php echo $data['number'] ?>" id="jumlah" required>
                    </div>
                </div>
                <div class="form-group">
                    <label>Harga :</label>
                    <div class="input-group">
                        <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                        <input type="text" class="form-control" name="price" value="<?php echo $data['price'] ?>" id="harga" readonly>
                    </div>
                </div>
                <script>
                    document.getElementById("jumlah").oninput = () => {
                        const jumlah = document.getElementById('jumlah');
                        const harga = document.getElementById('harga');
                        const total = document.getElementById('total');
                        total.value = harga.value * jumlah.value;
                    };
                </script>
                <div class="form-group">
                    <label>Total harga :</label>
                    <div class="input-group">
                        <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                        <input type="text" class="form-control" name="total_price" value="<?php echo $data['total_price'] ?>" id="total" readonly>
                    </div>
                </div>
                <button type="submit" class="btn btn-primary mt-3">Submit</button>
            </form>
        </div>

        <footer class="footer">
            <div style="text-align: center; color:white">
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