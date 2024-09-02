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
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <title>Document</title>
    <style>
        .body, html{
            flex: 1;
            margin: 0;
        }
        img{
            width: 150px;
            height: 100px;
        }
        .button {
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 14px;
            text-decoration: none; 
            color:white;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  	    <a class="navbar-brand" href="#" style="font-family: Cursive;">
        <img src="logobaru.png" alt="logo" style="width:60px; height:60px"> Gungsun mart
  	    </a>
        <ul class="navbar-nav ml-auto">
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown" style="font-family: Cursive;">
                    MENU
                </a>
                <div class="dropdown-menu">
                    <a class="dropdown-item" href="#"></a>
                    <a class="dropdown-item" href="#"></a>
                    <a class="dropdown-item" href="#"></a>
                    <a class="dropdown-item" href="#"></a>
                </div>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#" style="font-family: Cursive;">
                Welcome    
                <?php
      	            $NamaDepan=$_SESSION['nama_depan'];
		            echo $NamaDepan;
	            ?>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="logout.php" style="font-family: Cursive;">LOGOUT</a>
            </li>
        </ul>
    </nav>
    <div class="container mt-5">
        <table class="table" >
            <thead>
                <tr>
                    <th scope="col">No</th>
                    <th scope="col">Nama</th>
                    <th scope="col">Gambar Produk</th>
                    <th scope="col">Nama Produk</th>
                    <th scope="col">Harga</th>
                    <th scope="col">Banyak Produk</th>
                    <th scope="col">Total Harga</th>
                    <th scope="col">Action</th>
                </tr>
            </thead>
            <?php
                include "koneksi.php";
                $sql="select * from db_order";
                $query=mysqli_query($koneksi, $sql);
                $no = 1;
	            while ($data=mysqli_fetch_assoc($query)){
            ?>
            <tbody>
                <tr>
                    <td><?php echo $no; ?></td>
                    <td><?php echo $data['customer_name']; ?></td>
                    <td><img src="<?php echo $data['image']; ?>"></td>
                    <td><?php echo $data['product_name']; ?></td>
                    <td><?php echo $data['price']; ?></td>
                    <td><?php echo $data['number']; ?></td>
                    <td><?php echo $data['total_price']; ?></td>
                    <td>
                        <a href="edit.php?KodeOrder=<?php echo $data['id_order']?>"><button class="button" style="background-color: #4CAF50;">Edit</button></a>
                        <a href="hapusdata.php?KodeOrder=<?php echo $data['id_order']?>"><button class="button" style="background-color: #f44336;">Hapus</button></a>
                    </td>
                </tr>
            </tbody>
            <?php
                $no++;
                }
            ?>
            <tbody>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td><a href="neworder.php"><button class="button" style="background-color: #008CBA;">+ New Order</button></a></td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
<?php
	}
	else
	{
		echo "<script>
		alert ('Maaf anda tidak bisa akses halaman ini');
		location.href='login.php';
			
		</script>";	
	}
?>