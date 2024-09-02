<?php
// Memulai session
session_start();

// Menyimpan nilai pada session
$_SESSION["username"] = "JohnDoe";
$_SESSION["password"] = "123";

// Mendapatkan nilai dari session
echo "username: " . $_SESSION["username"] . "<br>";
echo "password: " . $_SESSION["password"] . "<br>";

// Menghapus session
session_destroy();

echo "setelah session destroy : <br>";

// Mendapatkan nilai session setelah session destroy
echo "username: " . $_SESSION["username"] . "<br>";
echo "password: " . $_SESSION["password"] . "<br><br>";
?>

<html>
<button><a href="index_session.php">index</a></button>
</html>