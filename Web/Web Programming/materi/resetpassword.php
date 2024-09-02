<?php
session_start();

if (isset($_SESSION['username'])) {
?>

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reset Password</title>
        <style>
            <?php include "style.css" ?>
        </style>
    </head>

    <body>
        <?php
        require "config.php";
        $username = $_SESSION['username'];
        $sql = "select * from project.user where username = '$username'";
        $query = mysqli_query($conn, $sql);
        $data = mysqli_fetch_assoc($query);
        ?>
        <div class="wrapper">
            <div class="login">
                <h1>Reset Password</h1>
                <form action="gantipassword.php" method="post">
                    <input type="text" name="username" value="<?php echo $username ?>" disabled>
                    <input type="text" name="password" value="<?php echo $data['password'] ?>" required>
                    <input type="submit" value="Continue">
                </form>
            </div>
        </div>
    </body>

    </html>

<?php
} else {
    echo "
            <script>
                alert('silahkan masukan username terlebih dahulu');
                location.href = 'forgotpassword.php';
            </script>
        ";
}
?>