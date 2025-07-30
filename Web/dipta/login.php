<?php
    session_start();
    include "koneksi.php";
    include "alert.php";
    
    if ($_SERVER["REQUEST_METHOD"] == "POST"){
        $username = $_POST['username'];
        $password = $_POST['password'];

        $sql = "select * from db_project.user where username = '$username' and password = '$password'";
        $query = mysqli_query($koneksi, $sql);
        $row = mysqli_num_rows($query);

        if ($row){
            $data = mysqli_fetch_assoc($query);
            $nama = $data["nama"];
            $level = $data["level"];
            $id = $data["id_user"];

            $_SESSION["Nama_user"] = $nama; 

            if ($level == "user"){
                $_SESSION["user"] = $level;
                $_SESSION["id_user"] = $id;
            }
            elseif($level == "admin"){
                $_SESSION["admin"] = $level;
            }
            
            showAlert('Login berhasil', 'success', 'index.php');
            exit();
        }
        else{
            showAlert('Username atau password salah', 'error', 'login.php');
            exit();
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - E-Commerce</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <!-- SweetAlert2 CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css">
    <style>
        body {
            background: linear-gradient(135deg, #4e73df 0%, #224abe 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .login-container {
            background: white;
            border-radius: 1rem;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            width: 100%;
            max-width: 400px;
        }
        .login-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .login-header h1 {
            color: #224abe;
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        .login-header p {
            color: #6c757d;
            margin-bottom: 0;
        }
        .form-floating {
            margin-bottom: 1rem;
        }
        .form-floating > .form-control {
            padding: 1rem 0.75rem;
        }
        .btn-login {
            background: #224abe;
            border: none;
            padding: 0.8rem;
            font-weight: 500;
            width: 100%;
            margin-top: 1rem;
        }
        .btn-login:hover {
            background: #1a3a8f;
        }
        .register-link {
            text-align: center;
            margin-top: 1.5rem;
        }
        .register-link a {
            color: #224abe;
            text-decoration: none;
            font-weight: 500;
        }
        .register-link a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-header">
            <h1>Welcome Back!</h1>
            <p>Please login to your account</p>
        </div>
    <form method="POST">
            <div class="form-floating">
                <input type="text" class="form-control" id="username" name="username" placeholder="Username" required>
                <label for="username">Username</label>
            </div>
            <div class="form-floating">
                <input type="password" class="form-control" id="password" name="password" placeholder="Password" required>
                <label for="password">Password</label>
            </div>
            <button type="submit" class="btn btn-primary btn-login">
                <i class="fas fa-sign-in-alt me-2"></i>Login
            </button>
            <div class="register-link">
                Don't have an account? <a href="register.php">Register here</a>
            </div>
    </form>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- SweetAlert2 JS -->
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
</body>
</html>