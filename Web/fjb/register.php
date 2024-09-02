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
    $query_register = mysqli_query($conn, $sql);

    if ($query_register){
        header("Location: login.php");
    }
    else {
        header("Location: register.php");
    }
}
?>
<!DOCTYPE html>
<html>

<head>
    <title>Register</title>
    <link rel="stylesheet" href="./styles/style.css">
    <style>
        <?php include "styles/style.css"?>
    </style>
</head>

<body>
    <header>
        <div class="container">
            <h1>Register</h1>
        </div>
    </header>

    <div class="container">
        <form method="post" class="register-form">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>

            <div class="container-btn">
                <button type="submit">Register</button>
                <a href="login.php">Back to login</a>
            </div>
        </form>
    </div>
</body>

</html>
