<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form upload</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>

<body>
    <form id="myForm" enctype="multipart/form-data">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>

        <label for="number">Number :</label><br>
        <input type="text" id="number" name="number"><br><br>

        <label for="phone">Phone number :</label><br>
        <input type="text" id="phone" value="+62" name="phone"><br><br>

        <label for="file">File :</label><br>
        <input type="file" id="file" name="file"><br><br>

        <label for="password">Password :</label><br>
        <input type="password" id="password" name="password"><br><br>

        <label for="confirm">Confirm Password :</label><br>
        <input type="password" id="confirm" name="confirm"><br><br>

        <input type="submit" value="Submit">
    </form>

    <script src="ajax.js"></script>
</body>

</html>