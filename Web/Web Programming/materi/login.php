<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        <?php include "style.css" ?>
    </style>
</head>

<body>
    <div class="wrapper">
        <div class="login">
            <h1>Log in</h1>
            <form action="proseslogin.php" method="post">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <input type="submit" value="Login">
            </form>
            <a href="register.php" class="register">Register</a>
            <p>Forgot Password ? <a href="forgotpassword.php">Click here</a></p>
        </div>
    </div>
</body>

</html>