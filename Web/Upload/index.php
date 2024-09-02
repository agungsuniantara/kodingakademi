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
			height: 100%;
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
				margin-bottom: 10px;
			}

			.text {
				margin-bottom: 10px;
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
		<h4 style="text-align: center;"><b>LOGIN</b></h4>
		<hr>
		<form action="proseslogin.php" method="post">
			<div class="form-group">
				<label for="email">Email:</label>
				<div class="input-group">
					<span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
					<input type="email" class="form-control" id="email" placeholder="Enter email" name="email">
				</div>
			</div>
			<div class="form-group">
				<label for="pwd">Password:</label>
				<div class="input-group">
					<span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
					<input type="password" class="form-control" id="pwd" placeholder="Enter password" name="password">
				</div>
			</div>
			<div class="text">
				Dont have account ? <a href="registration.php">Sign up</a>
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