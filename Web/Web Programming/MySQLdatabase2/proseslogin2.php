<?php
  session_start();
  include "koneksi.php";

  // Validate input: make sure email and password are not empty
  if (empty($_POST['email']) || empty($_POST['password'])) {
    echo "<script>
      alert ('Email dan password tidak boleh kosong');
      location.href='login.php';
      </script>";
    exit();
  }

  // Sanitize input: remove potentially harmful characters from email and password
  $email = mysqli_real_escape_string($koneksi, $_POST['email']);
  $password = mysqli_real_escape_string($koneksi, $_POST['password']);

  // Hash the password for additional security
  $hashed_password = hash('sha256', $password);

  // Prepare and execute the SQL query using parameterized statements
  $stmt = mysqli_prepare($koneksi, "SELECT * FROM coba.db_coba WHERE email = ? AND password = ?");
  mysqli_stmt_bind_param($stmt, "ss", $email, $hashed_password);
  mysqli_stmt_execute($stmt);
  $result = mysqli_stmt_get_result($stmt);

  // Check if the query returned any rows
  if (mysqli_num_rows($result) > 0) {
    // Store the user's first name in a session variable and redirect to the home page
    $data = mysqli_fetch_assoc($result);
    $namaDepan = $data['nama_depan'];
    $_SESSION['nama_depan'] = $namaDepan;

    echo "<script>
      alert ('Login berhasil');
      location.href='home.php';
      </script>";
  } else {
    // If the query did not return any rows, display an error message and redirect to the login page
    echo "<script>
      alert ('Email atau password salah');
      location.href='login.php';
      </script>";
  }

  mysqli_close($koneksi);
?>
