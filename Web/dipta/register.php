<?php
    include "koneksi.php";
    include "alert.php";

    if ($_SERVER["REQUEST_METHOD"] == "POST"){
        $nama = $_POST["nama"];
        $alamat = $_POST["alamat"];
        $no_telp = $_POST["no_telp"];
        $username = $_POST["username"];
        $password = $_POST["password"];

        $sql = "INSERT INTO db_project.user (nama, alamat, no_telp, username, password, level) 
        VALUES ('$nama', '$alamat', '$no_telp', '$username', '$password', 'user')";

        $query = mysqli_query($koneksi, $sql);

        if ($query){
            showAlert('Registrasi berhasil! Silahkan login.', 'success', 'login.php');
        }
        else{
            showAlert('Registrasi gagal. Silahkan coba lagi.', 'error', 'register.php');
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - E-Commerce</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body {
            background: linear-gradient(135deg, #4e73df 0%, #224abe 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem 0;
        }
        .register-container {
            background: white;
            border-radius: 1rem;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            width: 100%;
            max-width: 600px;
        }
        .register-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .register-header h1 {
            color: #224abe;
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        .register-header p {
            color: #6c757d;
            margin-bottom: 0;
        }
        .form-floating {
            margin-bottom: 1rem;
        }
        .form-floating > .form-control {
            padding: 1rem 0.75rem;
        }
        .btn-register {
            background: #224abe;
            border: none;
            padding: 0.8rem;
            font-weight: 500;
            width: 100%;
            margin-top: 1rem;
        }
        .btn-register:hover {
            background: #1a3a8f;
        }
        .login-link {
            text-align: center;
            margin-top: 1.5rem;
        }
        .login-link a {
            color: #224abe;
            text-decoration: none;
            font-weight: 500;
        }
        .login-link a:hover {
            text-decoration: underline;
        }
        .form-row {
            display: flex;
            gap: 1rem;
        }
        .form-row .form-floating {
            flex: 1;
        }
        @media (max-width: 768px) {
            .form-row {
                flex-direction: column;
                gap: 0;
            }
        }
    </style>
</head>
<body>
    <div class="register-container">
        <div class="register-header">
            <h1>Create Account</h1>
            <p>Join our e-commerce platform today</p>
        </div>
        <form method="POST">
            <div class="form-floating">
                <input type="text" class="form-control" id="nama" name="nama" placeholder="Nama" required>
                <label for="nama">Nama Lengkap</label>
            </div>
            <div class="form-floating">
                <input type="text" class="form-control" id="alamat" name="alamat" placeholder="Alamat" required>
                <label for="alamat">Alamat</label>
            </div>
            <div class="form-floating">
                <input type="tel" class="form-control" id="no_telp" name="no_telp" placeholder="No. Telepon" required>
                <label for="no_telp">No. Telepon</label>
            </div>
            <div class="form-row">
                <div class="form-floating">
                    <input type="text" class="form-control" id="username" name="username" placeholder="Username" required>
                    <label for="username">Username</label>
                </div>
                <div class="form-floating">
                    <input type="password" class="form-control" id="password" name="password" placeholder="Password" required>
                    <label for="password">Password</label>
                </div>
            </div>
            <button type="submit" class="btn btn-primary btn-register">
                <i class="fas fa-user-plus me-2"></i>Register
            </button>
            <div class="login-link">
                Already have an account? <a href="login.php">Login here</a>
            </div>
    </form>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>