<?php
    require 'php/php_register.php';
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
