<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
	<style>
		html,
		body {
			height: 120%;
		}

		body {
			background-color: rgb(165, 215, 232);
			font-family: Arial, sans-serif;
			display: flex;
			align-items: center;
		}

		.container {
			background-color: #fff;
			border-radius: 5px;
			box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.2);
			padding: 20px;
			max-width: 500px;
			margin: 0 auto;
		}

		.form-group {
			margin-bottom: 20px;
		}

		.text {
			margin-bottom: 20px;
		}

		.text a {
			text-decoration: none;
		}

		.navbar-header {
			float: none;
		}

		.navbar-fixed-top {
			top: 0;
			border-width: 0 0 1px;
		}

		.navbar {
			background-color: rgb(25, 55, 109);
		}

		.navbar-brand {
			color: white !important;
			display: flex;
			align-items: center;
		}

		.img-responsive {
			width: 40px;
			padding-bottom: 10px;
		}

		.footer {
			background-color: rgb(25, 55, 109);
			bottom: 0;
			position: fixed;
			width: 100%;
			padding-top: 10px;
			padding-bottom: 10px;
			z-index: 999999;
		}

		@media (max-width: 767px) {
			.container {
				padding: 10px;
			}

			.form-group {
				margin-bottom: 20px;
			}

			.text {
				margin-bottom: 20px;
				font-size: 10px;
			}
		}
	</style>
</head>

<body>
	<nav class="navbar navbar-default navbar-fixed-top">
		<div class="container-fluid">
			<div class="navbar-header">
				<a class="navbar-brand" href="#">
					<img src="logobaru.png" class="img-responsive">
				</a>
			</div>
		</div>
	</nav>

	<div class="container">
		<h4 style="text-align: center;"><b>REGISTER</b></h4>
		<hr>
		<form action="simpandaftar.php" method="post">
			<div class="form-group">
				<label>Nama depan :</label>
				<div class="input-group">
					<span class="input-group-addon"></span>
					<input type="text" class="form-control" placeholder="Nama depan" name="nama_depan" required>
				</div>
			</div>
			<div class="form-group">
				<label>Nama belakang :</label>
				<div class="input-group">
					<span class="input-group-addon"></span>
					<input type="text" class="form-control" placeholder="Nama belakang" name="nama_belakang" required>
				</div>
			</div>
			<div class="form-group">
				<label>Jenis kelamin :</label>
				<div class="input-group">
					<span class="input-group-addon"></span>
					<select class="form-control" name="jenis_kelamin" required>
						<option></option>
						<option>Laki - Laki</option>
						<option>Perempuan</option>
					</select>
				</div>
			</div>
			<div class="form-group">
				<label>Tanggal lahir :</label>
				<div class="input-group">
					<span class="input-group-addon"></span>
					<input type="date" class="form-control" name="tanggal_lahir" required>
				</div>
			</div>
			<div class="form-group">
				<label>Alamat :</label>
				<div class="input-group">
					<span class="input-group-addon"></span>
					<input type="text" class="form-control" placeholder="Alamat" name="alamat" required>
				</div>
			</div>
			<div class="form-group">
				<label>Email :</label>
				<div class="input-group">
					<span class="input-group-addon"></span>
					<input type="email" class="form-control" placeholder="Email" name="email" required>
				</div>
			</div>
			<div class="form-group">
				<label>Password :</label>
				<div class="input-group">
					<span class="input-group-addon"></span>
					<input type="password" class="form-control" placeholder="Passowrd" name="password" required>
				</div>
			</div>
			<div class="text">
				Have account ? <a href="index.php">Sign in</a>
			</div>
			<button type="submit" class="btn btn-primary mt-3">Submit</button>
		</form>
	</div>
	<footer class="footer">
		<div style="text-align: center; color:white">
			&#169 Agung Suniantara 2023
		</div>
	</footer>
</body>

</html>