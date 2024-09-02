<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AJAX Event</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <style>
        #loading {
            display: none;
        }
    </style>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>

<body>
    <div id="loading">
        <i class="fa-solid fa-spinner fa-spin-pulse"></i> loading data...
    </div>

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
                    $("#loading").show();
                },
                success: function(response) {
                    setTimeout(() => {
                        $("#loading").hide();
                        document.write(response + "<br>");
                    }, 1500);
                },
            });
        });
    </script>
</body>

</html>