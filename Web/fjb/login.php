<?php
    require 'php/php_login.php';
?>

<!DOCTYPE html>
<html>

<head>
    <title>Login</title>
    <style>
        <?php include "styles/style.css"?>
    </style>
</head>

<body>
    <header>
        <div class="container">
            <h1>Login</h1>
        </div>
    </header>

    <div class="container">
        <form method="post" class="login-form">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>

            <div class="container-btn">
                <button type="submit">Login</button>
                <a href="register.php">Register</a>
            </div>
        </form>
    </div>
</body>

</html>