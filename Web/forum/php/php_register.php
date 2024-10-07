<?php
    require 'config.php';

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $username = $_POST['username'];
        $email = $_POST['email'];
        $password = password_hash($_POST['password'], PASSWORD_BCRYPT);
        
        $check_existing = "SELECT * FROM users WHERE username = '$username' OR email = '$email'";
        $query_existing = mysqli_query($conn, $check_existing);
        $existing_user = mysqli_fetch_assoc($query_existing);
        
        if ($existing_user) {
            header("Location: register.php");
            exit;
        }
        
        $sql_register = "INSERT INTO users (username, email, password) VALUES ('$username', '$email', '$password')";
        $query_register = mysqli_query($conn, $sql_register);
    
        if ($query_register){
            header("Location: login.php");
        }
        else {
            header("Location: register.php");
        }
    }
?>