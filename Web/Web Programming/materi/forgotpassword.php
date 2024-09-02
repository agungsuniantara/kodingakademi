<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forgot Password</title>
    <style>
        <?php include "style.css" ?>
    </style>
</head>

<body>
    <div class="wrapper">
        <div class="login">
            <h1>Forgot Password</h1>
            <form action="prosesforgot.php" method="post">
                <input type="text" name="username" placeholder="Enter username" required>
                <input type="submit" value="Continue">
            </form>
        </div>
    </div>
</body>

</html>