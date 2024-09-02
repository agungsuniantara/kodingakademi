<?php
session_start();

if (isset($_SESSION['nama'])) {

?>

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body>
        <?php
        $nama = $_SESSION['nama'];
        echo "<h1>Welcome $nama</h1>";
        ?>
        <a href="logout.php">Logout</a>
    </body>

    </html>

<?php
} else {
    echo "
        <script>
            alert('silahkan login terlebih dahulu');
            location.href = 'login.php';
        </script>";
}
?>