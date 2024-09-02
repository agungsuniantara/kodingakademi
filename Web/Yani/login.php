<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .pembungkus {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: red;
        }

        .login {
            width: 70vh;
            height: 70vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: green;
            
        }
        .konten{
            width: 40vh;
            height: 40vh;
            color: white;
            background-color: blue;
        }
    </style>
</head>

<body>
    <div class="pembungkus">
        <div class="login">
            <div class="konten">
            <form action="">
                <label for="username">Username</label>
                <input type="text" name="username" id="username"><br>
                <label for="password">Password</label>
                <input type="text" name="password" id="password">
                <input type="submit" value="submit">
            </form>
            </div>
        </div>
    </div>
</body>

</html>