<?php
session_start();

$username = $_POST['username'];
$password = $_POST['password'];

if ($username == "admin" && $password == "123") {
    $_SESSION["username"] = $username;
    $_SESSION["password"] = $password;
    header('Location: home.php');
} else {
    header('Location: login.php');
}
