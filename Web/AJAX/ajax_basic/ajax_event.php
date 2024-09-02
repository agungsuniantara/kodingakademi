<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AJAX Event</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>

<body>
    <script>
        $(document).ready(function() {
            $.ajax({
                url: 'proses.php',
                method: 'GET',
                data: {
                    nama: 'agus',
                    alamat: 'denpasar'
                },
                beforeSend: function() {
                    alert("loading data...");
                },
                success: function(response) {
                    alert("data berhasil di load..");
                    document.write(response + "<br>")
                },
                error: function(error) {
                    alert("data gagal di load..");
                    document.write(error)
                },
                complete: function() {
                    document.write("proses ajax telah selesai");
                }
            });
        });
    </script>
</body>

</html>