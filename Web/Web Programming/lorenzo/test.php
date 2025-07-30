<?php
    session_start();
    if(!isset($_SESSION['Name_user'])) {
        echo "
        <script>
            alert('Lakukan login terlebih dahulu');
            location.href = 'login.php';
        </script>
        ";
    }
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style><?php include "style.css" ?></style>
</head>

<body>
    <nav class="navbar">
        <a href="index.php" class="nav-btn">Home</a>
        <a href="tambahproduk.php" class="nav-btn">Tambah Produk</a>
        <a href="logout.php" class="nav-btn">Logout</a>
    </nav>

    <div class="wrapper">
        <div class="form-table">
            <table>
                <tr>
                    <th>No</th>
                    <th>Name</th>
                    <th>Image's Product</th>
                    <th>product's Name</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                    <th>Action</th>
                </tr>
                <?php
                    include "koneksi.php";
                    $sql="select * from order";
                    $query=mysqli_query($koneksi, $sql);
                    $no = 1;
                    while ($data=mysqli_fetch_assoc($query)):
                ?>
                <tr>
                    <td><?php echo $no; ?></td>
                    <td><?php echo $data['Name']; ?></td>
                    <td><img src="<?php echo $data['Image']; ?>"></td>
                    <td><?php echo $data['Product']; ?></td>
                    <td><?php echo $data['Price']; ?></td>
                    <td><?php echo $data['Quantity']; ?></td>
                    <td><?php echo $data['Total']; ?></td>
                    <td>
                        <a href="edit.php?KodeOrder=<?php echo $data['id_order']?>"><button class="button" style="background-color: #4CAF50;">Edit</button></a>
                        <a href="hapusdata.php?KodeOrder=<?php echo $data['id_order']?>"><button class="button" style="background-color: #f44336;">Hapus</button></a>
                    </td>
                </tr>
                <?php
                    $no++;
                    endwhile;
                ?>
            </table>
        </div>
    </div>
</body>
</html>
