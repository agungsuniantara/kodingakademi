<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$.getJSON()</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>

<body>
    <script>
        $(document).ready(function() {
            $.getJSON('data.json', function(data) {
                document.write("nama = " + data.nama + "<br>");
                document.write("alamat = " + data.alamat);
            });
        });
    </script>
</body>

</html>