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
    <table id="myDataTable1" class="display"></table>

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
                    {
                        data: null,
                        title: "Action",
                        render: function() {
                            return (
                                "<button>Delete</button>" +
                                "<button>Edit</button>"
                            );
                        },
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
                        nama: "Bob Smith",
                        email: "bob@example.com",
                        telepon: "98765"
                    },
                    {
                        nama: "Alice Johnson",
                        email: "alice@example.com",
                        telepon: "45678"
                    },
                ],
            });

            // Tambahkan tombol di bawah kolom pencarian
            var button = $("<div class='custom-buttons'></div>").insertAfter(
                ".dataTables_wrapper .dataTables_filter input"
            );

            // Tambahkan tombol di sini
            button.append("<button>Tambah</button>");

            // Gaya CSS tambahan (opsional)
            button.css({
                "margin-top": "20px",
            });
        });
    </script>

</body>

</html>