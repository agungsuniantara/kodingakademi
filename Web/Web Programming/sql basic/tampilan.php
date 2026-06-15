<?php
    include "koneksi_baru.php";

    $query = "SELECT * FROM users";
    $result = mysqli_query($koneksi, $query);
    $data = mysqli_fetch_all($result, MYSQLI_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <h1>Data Users</h1>
    </div>
    <div>
        <?php foreach($data as $row): ?>
            <p>ID: <?php echo $row['id_nama']; ?></p>
            <p>Nama: <?php echo $row['nama']; ?></p>
            <p>Email: <?php echo $row['email']; ?></p>
            <p>Password: <?php echo $row['password']; ?></p>
            <hr>
        <?php endforeach; ?>
    </div>
</body>
</html>