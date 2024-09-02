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
            <h1>Sign Up</h1>
            <form name="form-login" method="post" action="prosesregistrasi.php">
                <input type="text" name="nama" placeholder="Nama" required>
                <input type="text" name="alamat" placeholder="Alamat" required>
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <input type="submit" value="Submit">
            </form>
            <p>Already have an account ? <a href="login.php">Login here</a></p>
        </div>
    </div>
</body>

</html>