<?php
session_start();
if (isset($_SESSION['email'])) {
?>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body>
        <form action="" method="POST">
            <input type="submit" name="logout" value="logout">
        </form>
    </body>

    </html>

    <?php
    if ($_POST['logout']) {
        $tutup = session_destroy();

        if ($tutup) {
            echo "
      <script>
        alert('logout berhasil');
        location.href = 'login.php';
      </script>
      ";
        } else {
            echo "
      <script>
        alert('logout gagal');
        location.href = 'home.php';
      </script>
      ";
        }
    }
    ?>
<?php
} else {
    echo "
      <script>
        alert('silahkan melakukan login');
        location.href = 'login.php';
      </script>
      ";
}
?>