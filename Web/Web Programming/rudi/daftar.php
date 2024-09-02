<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
    .div1{
        width: 150px;
        height: 300px;
        margin: auto;
        margin-top: 100px;
    }
    input{
        padding: 8px 40px;
        border-radius: 10px;
    }
    button{
        padding: 5px 8px;
        background-color: black;
        color: orange;
        border-radius: 5px;
        font-size: 15px;
    }
    a{
        color: blue;
    }
    </style>
</head>
<body>
<div class="div1">
        <form action="procesdaftar.php" method="post">
        <h3> surename </h3> <input type="text" name="surename"> <br>
        <h3> name </h3> <input type="text" name="name"> <br>
        <h3> date of birth </h3> <input type="text" name="birth"> <br>
        <h3> username </h3> <input type="text" name="username"> <br>
        <h3> password </h3> <input type="text" name="password"><br><br>
        <input type="submit"> Sign Up
        <a href="login.php"><h3> Back to sign in </h3></a>
     </form>
</body>
</html>
