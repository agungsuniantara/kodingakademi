<!DOCTYPE html>
<html lang="id">

<head>
    <meta charset="UTF-8">
    <title>DataTables Contoh</title>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.css">
    <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.js"></script>
</head>

<body>
    <table id="myDataTable"></table>

    <script>
        $(document).ready(function() {
            $("#myDataTable").DataTable({
                columns: [{
                        data: "nama",
                        title: "Nama"
                    },
                    {
                        data: "email",
                        title: "Email"
                    },
                    {
                        data: "telepon",
                        title: "Telepon"
                    },
                ],
                data: [{
                        nama: "John Doe",
                        email: "john@example.com",
                        telepon: "12345"
                    },
                    {
                        nama: "Jane Doe",
                        email: "jane@example.com",
                        telepon: "67890"
                    },
                    {
                        nama: "Jane Doe",
                        email: "jane@example.com",
                        telepon: "67890"
                    },
                ],
            });
        });
    </script>

</body>

</html>