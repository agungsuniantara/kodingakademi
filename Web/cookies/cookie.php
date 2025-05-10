<?php
setcookie("user", "John Doe", time() + 3600, "/");

echo "Hallo " . $_COOKIE['user'];
