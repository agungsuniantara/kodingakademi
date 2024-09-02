<?php
session_start();

if (isset($_SESSION["username"]) && isset($_SESSION["password"])) {
    $username = $_SESSION["username"];
} else {
    header('Location: login.php');
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <p>Halo <?php echo $username; ?></p>
    <a href="logout.php">logout</a>
</body>

</html>