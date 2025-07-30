<?php
  session_start();
  include "koneksi.php";

  if($_SERVER['REQUEST_METHOD'] == "POST"){
    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "SELECT * from project.user where username='$username' and password='$password'";
    $query = mysqli_query($koneksi, $sql);
    $row = mysqli_num_rows($query);

    if($row){
       $data = mysqli_fetch_assoc($query);
       $nama = $data['name'];
       
       $_SESSION['Name_user'] = $nama;

        echo "
        <script>
            alert('Login berhasil');
            location.href = 'index.php';
        </script>
        ";
    }else{
        echo "
        <script>
            alert('Login gagal');
            location.href = 'login.php';
        </script>
        ";
    }
  }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
            body{
        background-image: url(https://png.pngtree.com/thumb_back/fw800/background/20230615/pngtree-landscape-landscape-photo-image_2902263.jpg);
        background-repeat: no-repeat;
        background-size: cover;
    }
    .wrapper{
        width: 414px;
        height: 350px;
        margin-left: 700px;
        margin-top: 250px;
        padding: 2px 20px 0px 20px;
        background-color: rgba(255, 255, 255, 0.69);
        border-radius: 10px;
    }
    input {
      width: 400px;
      margin-top: 5px;
      margin-bottom: 20px;
      padding: 5px 0px 5px 10px;
    }
    textarea {
      width: 694px;
      height: 100px;
      margin-top: 5px;
      margin-bottom: 5px;
      outline: none;
      border: none;
      border-bottom: 1px solid rgb(82, 78, 78);
      padding: 5px 0px 5px 0px;
    }
    h1 {
      text-align: center;
    }
    </style>
</head>
<body>
  <div class="wrapper">
    <h1>LOGIN</h1>
    <form method="post">
      <label for="name">Username</label>
      <input type="text" id="name" name="username" placeholder="Masukkan Username"> 
      <label for="password">Password</label>
      <input type="text" id="name" name="password" placeholder="Masukkan Password"> 
      <input type="submit" value="Login" style="margin-left: 6px;"> 
      Don't have account ? <a href="register.php">Register</a>
    </form>
  </div>
</body>
</html>