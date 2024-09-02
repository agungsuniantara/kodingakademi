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
    <h1>Class display : </h1>

    <table id="myDataTable1" class="display"></table>

    <h1>No class</h1>

    <table id="myDataTable2" class=""></table>

    <h1>Cell border : </h1>

    <table id="myDataTable3" class="cell-border"></table>

    <h1>Compact : </h1>

    <table id="myDataTable4" class="display compact"></table>

    <h1>Hover : </h1>

    <table id="myDataTable5" class="hover"></table>

    <h1>Order-column : </h1>

    <table id="myDataTable6" class="order-column"></table>

    <h1>Stripe : </h1>

    <table id="myDataTable7" class="stripe"></table>

    <script>
        $(document).ready(function() {
            $("#myDataTable1").DataTable({
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

    <script>
        $(document).ready(function() {
            $("#myDataTable2").DataTable({
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

    <script>
        $(document).ready(function() {
            $("#myDataTable3").DataTable({
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

    <script>
        $(document).ready(function() {
            $("#myDataTable4").DataTable({
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

    <script>
        $(document).ready(function() {
            $("#myDataTable5").DataTable({
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

    <script>
        $(document).ready(function() {
            $("#myDataTable6").DataTable({
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

    <script>
        $(document).ready(function() {
            $("#myDataTable7").DataTable({
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