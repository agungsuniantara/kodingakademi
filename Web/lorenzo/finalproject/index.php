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
        <a href="tambahproduk.php" class="nav-btn">Tambah Data</a>
        <a href="logout.php" class="nav-btn">Logout</a>
    </nav>

    <div class="wrapper">
        <div class="form-table">
            <table>
                <tr>
                    <th>Name</th>
                    <th>Image's Product</th>
                    <th>product's Name</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                    <th>Action</th>
                </tr>
                
            </table>
        </div>
    </div>
</body>
</html>

