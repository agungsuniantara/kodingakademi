<?php
session_start();

if (isset($_SESSION['username']) || isset($_SESSION['password'])) {
    echo "session tersedia <br>";
    echo "username : " . $_SESSION['username'] . "<br>";
    echo "password : " . $_SESSION['password'];
} else {
    echo "session tidak tersedia";
}
