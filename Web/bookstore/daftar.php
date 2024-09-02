<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Halaman login</title>
    <style>
        body{
            margin: 0;
            background-image: url(https://img.freepik.com/free-photo/grunge-paint-background_1409-1337.jpg?w=2000);
            height: 100%;
            background-repeat: no-repeat;
            background-size: cover;
        }
        .parent{
            margin: auto;
            margin-top: 80px;
            width: 500px;
            height: 400px;
            overflow: auto;
            background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBOdkcUtDlUIP--MZ60TTJKnULcE2lNomunQ&usqp=CAU);
            background-repeat: no-repeat;
            background-size: cover;
            border-radius: 10px;
        }
        .child{
            width: 350px;
            height: 300px;
            margin: auto;
            margin-top: 40px;
            background-color: rgba(255, 255, 255, 0.035);
        }
        .text{
            text-align: center;
            font-family:cursive;
        }
        label{
            font-family:cursive;
        }
        input[type=text], input[type=password]{
            width: 100%;
            margin-top: 10px;
            margin-bottom: 10px;
            box-sizing: border-box;
            padding: 10px;
            font-family:cursive;
        }
        input[type=submit]{
            padding: 10px 40px; 
            margin-top: 20px;
            margin-bottom: 10px;
            border: none;
            cursor:pointer;
            border-radius: 5px;
            background-color: antiquewhite;
            font-family:cursive;
        }
    </style>
</head>
<body>
    <div class="parent">
        <div class="child">
            <h2 class="text">DAFTAR</h2>
            <hr style="margin-bottom: 30px;  border: 6px solid rgb(168, 171, 168); border-radius: 5px;">
            <form name="formlogin" method="POST" action="prosesdaftar.php">
                <label>Nama :</label>
                <input type="text" placeholder="masukkan nama" name="Nama">
                <label>Umur :</label>
                <input type="text" placeholder="masukkan umur" name="Umur">
                <label>Alamat :</label>
                <input type="text" placeholder="masukkan alamat" name="Alamat">
                <label>Email :</label>
                <input type="text" placeholder="masukkan email" name="Email">
                <label>Username :</label>
                <input type="text" placeholder="masukkan username" name="Username">
                <label>Password :</label>
                <input type="password" placeholder="masukkan password" name="Password">
                <center><input type="submit" value="Daftar"></center>
            </form>
            <center><a href="login.php">login</a></center>
        </div>
    </div>
</body>
</html>