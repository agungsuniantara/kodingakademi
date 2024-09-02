<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$ajax</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>

<body>
    <script>
        $(document).ready(function() {
            $.post('proses.php', {
                nama: 'agus',
                alamat: 'denpasar'
            }, function(response) {
                alert("berhasil mengirim data");
                document.write(response);
            });
        });
    </script>
</body>

</html>