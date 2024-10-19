<?php
$host = 'localhost';
$db = 'forum';
$user = 'root';
$pass = 'root';

$conn = mysqli_connect($host, $user, $pass, $db);
if (!$conn) {
    header("HTTP/1.0 404 Not Found");
    exit;
}