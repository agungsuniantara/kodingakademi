<?php
setcookie("user", "John Doe", time() + 3600, "/", null, true, true);

echo "Hallo " . $_COOKIE['user'];
