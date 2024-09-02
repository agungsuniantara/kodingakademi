<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .body, html{
            height: 100%;
            margin: 0;
            background-image: url(https://img.freepik.com/free-vector/hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg?w=2000);
            background-repeat: no-repeat;
            background-size: cover;
        }
        input[type=text], input[type=password] {
            width: 100%;
            padding: 7px;
            margin-bottom: 20px;
            border: none;
            border-bottom: 2px solid red;
            box-sizing: border-box;
        }
        input[type=submit]{
            padding: 10px 100px;
            margin-top: 20px;
            background-color: red;
            color: white;
            border: none;
            text-decoration: none;
            cursor: pointer;
        }
        .button{
            text-align: center;
        }
        .parent{
            margin: auto;
            margin-top: 10%;
            padding: 10px;
            height: 350px;
            width: 500px;
            background-color: white;
        }
        .parent2{
            margin-left: 50px;
            margin-right: 50px;
        }
    </style>
</head>
<body oncontextmenu="return false;">
    <div class="parent">
        <h1 style="text-align: center; margin-bottom: 40px;">LOGIN</h1>
        <div class="parent2">
            <form name="formlogin" method="POST" action="proseslogin.php">
                <label>Email :</label>
                <input type="text" name="email">
                <label>Password :</label>
                <input type="password" name="password">
                <div class="button">
                    <input type="submit" value="login">
                </div>
                <p style="text-align: center; margin-top: 30px;">Belum punya akun ? <a href="registration.php" style="text-decoration: none;">DAFTAR</a></p>
            </form>
        </div>
    </div>
</body>
</html>