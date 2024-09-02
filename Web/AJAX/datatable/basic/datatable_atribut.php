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

                ],
                searching: true,
                ordering: true,
                paging: true,
                info: true,
                lengthChange: true,
                autoWidth: true,
                lengthMenu: [5, 10, 25, 50],
                pageLength: 2,
                columnDefs: [{
                    width: "20%",
                    targets: 0
                }],
                language: {
                    lengthMenu: "Tampilkan _MENU_ data per halaman",
                    zeroRecords: "Tidak ada data yang ditemukan",
                    info: "Menampilkan _START_ sampai _END_ dari _TOTAL_ entri",
                    infoEmpty: "Menampilkan 0 sampai 0 dari 0 entri",
                    infoFiltered: "(disaring dari total _MAX_ entri)",
                    search: "Cari:",
                    paginate: {
                        next: "Selanjutnya",
                        previous: "Sebelumnya"
                    }
                }
            });
        });
    </script>

</body>

</html>