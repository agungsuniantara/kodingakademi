<?php
$host = 'localhost';
$db = 'student';
$user = 'root';
$pass = 'root';

$conn = mysqli_connect($host, $user, $pass, $db);

if (!$conn) {
    echo "Failed connection";
}
