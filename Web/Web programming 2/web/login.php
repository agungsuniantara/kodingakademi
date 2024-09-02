<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .body,
        html {
            height: 100%;
            margin: 0;
            background-image: url(https://e1.pxfuel.com/desktop-wallpaper/764/142/desktop-wallpaper-clinic.jpg);
            background-repeat: no-repeat;
            background-size: cover;
        }

        input[type=text],
        input[type=password] {
            width: 100%;
            padding: 7px;
            margin-bottom: 20px;
            border: none;
            border-bottom: 2px solid red;
            box-sizing: border-box;
            background-color: rgb(243, 248, 255);
            outline: none;
        }

        input[type=submit] {
            padding: 10px 100px;
            margin-top: 20px;
            background-color: red;
            color: white;
            border: none;
            text-decoration: none;
            cursor: pointer;
        }

        .button {
            text-align: center;
        }

        .parent {
            margin: auto;
            margin-top: 10%;
            padding: 10px;
            height: 350px;
            width: 500px;
            background-color: rgb(243, 248, 255);
            border-radius: 5px;
        }

        .parent2 {
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
                <label>Username :</label>
                <input type="text" name="username">
                <label>Password :</label>
                <input type="password" name="password">
                <div class="button">
                    <input type="submit" value="Login">
                </div>
            </form>
        </div>
    </div>
</body>

</html>