<?php
    require 'config.php';
    session_start();
    
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $username = $_POST['username'];
        $password = $_POST['password'];
    
        $sql = "SELECT * FROM users WHERE username = '$username'";
        $query = mysqli_query($conn, $sql);
        $fetch = mysqli_fetch_assoc($query);
    
        if ($fetch) {
            $_SESSION['user_id'] = $fetch['id'];
            header("Location: index.php");
        } else {
            header("Location: login.php");
        }
    }
?>