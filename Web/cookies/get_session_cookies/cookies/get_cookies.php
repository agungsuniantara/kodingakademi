<?php
setcookie("user", "John Doe", time() + 5, "/", null, true, true);
echo "user : " . $_COOKIE['user'] . "<br><br>";
?>

<html>
<button><a href="index_cookie.php">Index</a></button>
</html>