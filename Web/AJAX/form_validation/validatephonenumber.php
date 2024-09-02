<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phone Number Validation</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>

<body>
    <form id="myForm">
        <label for="name">Name :</label><br>
        <input type="text" id="name"><br><br>

        <label for="email">Email :</label><br>
        <input type="text" id="email"><br><br>

        <label for="number">Number :</label><br>
        <input type="text" id="number"><br><br>

        <label for="phone">Phone number :</label><br>
        <input type="text" id="phone" value="+62"><br><br>

        <label for="file">File :</label><br>
        <input type="file" id="file"><br><br>

        <label for="password">Password :</label><br>
        <input type="password" id="password"><br><br>

        <label for="confirm">Confirm Password :</label><br>
        <input type="password" id="confirm"><br><br>

        <input type="submit" value="Submit">
    </form>

    <script>
        $(document).ready(function() {
            $("#myForm").submit(function(event) {
                event.preventDefault();

                var phoneNumber = $("#phone").val().trim();

                if (!validatePhoneNumber(phoneNumber)) {
                    alert("Data nomor telepon tidak sesuai");
                } else {
                    alert("Proses AJAX akan berjalan");
                }
            });

            function validatePhoneNumber(phoneNumber) {
                const phoneNumberPattern = /^\+62\d{9,15}$/;
                return phoneNumberPattern.test(phoneNumber);
            }
        });
    </script>
</body>

</html>