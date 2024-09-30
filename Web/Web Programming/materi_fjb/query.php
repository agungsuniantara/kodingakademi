<?php
require "config.php";
$sql = "SELECT * FROM employee";
$result = mysqli_query($conn, $sql);
print_r($result);
