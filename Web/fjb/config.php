<?php
$host = 'localhost';
$db = 'forum_jual_beli';
$user = 'root';
$pass = '';

$conn = mysqli_connect($host, $user, $pass, $db);
if (!$conn) {
    header("HTTP/1.0 404 Not Found");
    exit;
}