<?php
session_start();
if (isset($_SESSION['namalengkap'])) {
?>
    <!DOCTYPE html>
    <html>

    <head>
        <title>Website Klinik Sejahtera</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="mytable.css">
        <link rel="stylesheet" href="mystyle.css">
        <link rel="stylesheet" href="myform.css">
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    </head>

    <body>
        <section>
            <div id="mymenu" class="vertical-menu">
                <a class="active" href="admin.php">Home</a>
                <a id="menuDokter" href="viewdokter.php">Dokter</a>
                <a id="menuPasien" href="viewpasien.php">Pasien</a>
                <a id="menuObat" href="viewobat.php">Obat</a>
                <a id="menuKunjungan" href="viewkunjungan.php">Kunjungan</a>
                <a id="jadwalDokter" href="viewjadwal.php">Jadwal Dokter</a>
            </div>
            <div id="content" class="rightContent">
                <?php
                include "dbkoneksi.php";
                if (!isset($_GET['action'])) :
                    $sql = "SELECT * FROM dbklinik.dokter ORDER BY nama_dokter";
                    if (!empty($nama)) {
                        $sql = $sql . " WHERE nama_dokter LIKE '%" . $nama . "%'";
                    }
                    $result = $conn->query($sql);

                    if (isset($_GET['message'])) {
                        echo '<script>alert("' . $_GET['message'] . '");</script>';
                    }
                ?>

                    <a href="viewdokter.php?action=tambah" class="button">Tambah</a>
                    <table id="mydata">
                        <tr>
                            <th>Nama Dokter</th>
                            <th>Spesialisasi</th>
                            <th>Aksi</th>
                        </tr>
                        <?php
                        while ($row = $result->fetch_assoc()) {
                            echo '<tr>
                            <td>' . $row["nama_dokter"] . '</td>
                            <td>' . $row["spesialis"] . '</td>
                            <td>
                                <a href="viewdokter.php?action=ubah&id=' . $row["id"] . '&nama_dokter=' . $row["nama_dokter"] . '&spesialis=' . $row["spesialis"] . '" class="button">Ubah</a>
                                <a id="delete" href="#" data-id="' . $row["id"] . '" class="button delete-button">Hapus</a>
                            </td>
                        </tr>';
                        }
                        ?>
                    </table>

                <?php elseif ($_GET['action'] == "ubah") : ?>

                    <h3>Ubah Dokter</h3>

                    <div>
                        <form id="form-dokter1" method="post" action="">
                            <label for="id">ID</label>
                            <input type="text" id="id" name="id" value="<?php echo $_GET['id']; ?>" disabled>
                            <label for="nama">Nama</label>
                            <input type="text" id="nama_dokter" name="nama_dokter" value="<?php echo $_GET['nama_dokter']; ?>">

                            <label for="spesialis">Spesialis</label>
                            <input type="text" id="spesialis" name="spesialis" value="<?php echo $_GET['spesialis']; ?>">

                            <input type="submit" value="Submit">
                        </form>
                    </div>

                <?php else : ?>

                    <h3>Tambah Dokter</h3>

                    <div>
                        <form id="form-dokter2" method="post" action="">
                            <label for="nama">Nama</label>
                            <input type="text" id="nama_dokter" name="nama_dokter" placeholder="Nama dokter..">

                            <label for="spesialis">Spesialis</label>
                            <input type="text" id="spesialis" name="spesialis" placeholder="Spesialis..">

                            <input type="submit" value="Submit">
                        </form>
                    </div>

                <?php
                endif;
                $conn->close();
                ?>
            </div>
        </section>

        <footer>
            <p>&copy; Klinik Sehat Sejahtera 2022</p>
        </footer>

        <script>
            $(document).ready(function() {
                $("#form-dokter2").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        nama_dokter: $("#nama_dokter").val(),
                        spesialis: $("#spesialis").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-dokter.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewdokter.php");
                        }
                    });

                    $("#form-dokter2")[0].reset(); // Reset the form
                });

                $("#form-dokter1").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        id: $("#id").val(),
                        nama_dokter: $("#nama_dokter").val(),
                        spesialis: $("#spesialis").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-dokter.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewdokter.php");
                        }
                    });

                    $("#form-dokter1")[0].reset(); // Reset the form
                });

                // Delete button click event handler
                $(document).on('click', '.delete-button', function(event) {
                    event.preventDefault(); // Prevent form submission
                    var id = $(this).data('id');
                    if (confirm('Are you sure you want to delete this item?')) {
                        $.ajax({
                            type: "GET",
                            url: "admin-dokter.php?action=hapus&id=" + id,
                            success: function(data) {
                                window.location.replace("viewdokter.php");
                            }
                        });
                    }
                });
            });
        </script>
    </body>

    </html>

<?php
} else {
    echo "<script>
		alert ('Maaf anda tidak bisa akses halaman ini');
		location.href='login.php';
			
		</script>";
}
?>