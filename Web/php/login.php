<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="style.css" />


</head>

<body>
  <nav class="wrapper-navbar">
    <section class="navbar-1">
      <div class="navbar1-kiri">
        <a href="index.html"><img src="asset/heker.png" alt="" class="gambarlogo1" /></a>
        <a href="index.html"><img src="asset/close.png" alt="" class="gambarlogooo" /></a>
      </div>
    </section>
  </nav>

  <section id="main-content">
    <div class="login">
      <div class="border">
        <h2>Log in</h2>
        <div class="login-email">
          <ul>
            <li><b>email</b></li>
            <li>
              Need an account? <a href="Sign up.html"><b>Sign up</b></a>
            </li>
          </ul>
          <form action="" method="POST">
            <input type="text" placeholder="masukan email" name="email" />
        </div>

        <div class="login-email2">
          <ul>
            <li style="margin-right: 27vh"><b>password</b></li>
            <li style="margin-right: 1vh">
              <img src="asset/mata.png" alt="" />
            </li>
            <li><b>show</b></li>
          </ul>

          <input type="text" placeholder="masukan password" name="password" />
        </div>

        <div class="atas-google">
          <input type="submit" class="button1" name="submit">
        </div>
        </form>

        <div class="bawah">
          <p>OR</p>
        </div>
        <div class="bawah-google">
          <button class="button23">
            <img src="asset/fesbook.png" alt="" /><a href="#">Continue width Fesbook</a>
          </button>
        </div>

        <div class="bawah-google">
          <button class="button2">
            <img src="asset/google.png" alt="" /><a href="#">Continue width google</a>
          </button>
        </div>

        <div class="bawah-google">
          <button class="button2">
            <img src="asset/twitter.png" alt="" /><a href="#">Continue width Twitter</a>
          </button>
        </div>
      </div>
    </div>
  </section>
</body>

</html>

<?php
if (isset($_POST["submit"])) {
  $koneksi = mysqli_connect("localhost", "root", "", "contoh");

  $email = $_POST['email'];
  $password = $_POST['password'];

  $sql = "select * from contoh.user where email = '$email' and password = '$password'";

  $query = mysqli_query($koneksi, $sql);

  foreach ($query as $data) {
    $email = $data['email'];

    $_SESSION['email'] = $email;

    if ($email) {
      echo "
      <script>
        alert('login berhasil');
        location.href = 'home.php';
      </script>
      ";
    } else {
      echo "
      <script>
        alert('login gagal');
        location.href = 'login.php';
      </script>
      ";
    }
  }
}
?>