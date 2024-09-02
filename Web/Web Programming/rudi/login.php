<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
background-image: url(sun.jpeg);
background-size:100%;
background-repeat: no-repeat;
        }
    .div1{
        width: 150px;
        height: 300px;
        margin: auto;
        margin-top: 150px;
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
        <h3> Sign in </h3> <input type="text"> <br>
        <h3> Your Password </h3> <input type="password"><br><br>
        <button> sign in </button><br>
        not member yet:
        <a href="daftar.php"><h2> Sign up here </h3></a>
     </form>
        
</body>
</html>