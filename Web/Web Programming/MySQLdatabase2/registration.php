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
            background-size: 100%;
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
            margin-top: 10px;
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
            padding: 10px;
            height: 700px;
            width: 500px;
            background-color: white;
        }
        .parent2{
            margin-left: 50px;
            margin-right: 50px;
        }
    </style>
</head>
<body>
    <div class="parent">
        <h1 style="text-align: center;">DAFTAR</h1>
        <div class="parent2">
            <form name="formlogin" method="POST" action="simpandaftar2.php">
                <label>Nama depan :</label>
                <input type="text" name="nama_depan" required>
                <label>Nama belakang :</label>
                <input type="text" name="nama_belakang" required>
                <label>Jenis kelamin</label>
                <input type="text" name="jenis_kelamin" required>
                <label>Tanggal lahir :</label>
                <input type="text" name="tanggal_lahir" required>
                <label>Alamat :</label>
                <input type="text" name="alamat" required>
                <label>Email</label>
                <input type="text" name="email" required>
                <label>Password :</label>
                <input type="password" name="password" required>
                <div class="button">
                    <input type="submit" value="daftar">
                </div>
                <p style="text-align: center; margin-top: 30px;">Sudah punya akun ? <a href="login.php" style="text-decoration: none;">LOGIN</a></p>
            </form>
        </div>
    </div>
</body>
</html>