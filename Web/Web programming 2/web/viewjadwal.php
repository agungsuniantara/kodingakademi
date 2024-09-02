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
                <a id="menukunjungan" href="viewkunjungan.php">Kunjungan</a>
                <a id="jadwalDokter" href="viewjadwal.php">Jadwal Dokter</a>
            </div>
            <div id="content" class="rightContent">
                <?php
                include "dbkoneksi.php";
                if (!isset($_GET['action'])) :
                    $sql = "SELECT * FROM dbklinik.jadwal_dokter ORDER BY nama_dokter";
                    if (!empty($nama)) {
                        $sql = $sql . " WHERE nama_dokter LIKE '%" . $nama . "%'";
                    }
                    $result = $conn->query($sql);

                    if (isset($_GET['message'])) {
                        echo '<script>alert("' . $_GET['message'] . '");</script>';
                    }
                ?>

                    <a href="viewjadwal.php?action=tambah" class="button">Tambah</a>
                    <table id="mydata">
                        <tr>
                            <th>Nama dokter</th>
                            <th>hari</th>
                            <th>jam</th>
                            <th>Aksi</th>
                        </tr>
                        <?php
                        while ($row = $result->fetch_assoc()) {
                            echo '<tr>
                            <td>' . $row["nama_dokter"] . '</td>
                            <td>' . $row["hari"] . '</td>
                            <td>' . $row["jam"] . '</td>
                            <td>
                                <a href="viewjadwal.php?action=ubah&id=' . $row["id"] . '&nama_dokter=' . $row["nama_dokter"] . '&hari=' . $row["hari"] . '&jam=' . $row["jam"] . '" class="button">Ubah</a>
                                <a id="delete" href="#" data-id="' . $row["id"] . '" class="button delete-button">Hapus</a>
                            </td>
                        </tr>';
                        }
                        ?>
                    </table>

                <?php elseif ($_GET['action'] == "ubah") : ?>

                    <h3>Ubah Jadwal</h3>

                    <div>
                        <form id="form-jadwal1" method="post" action="">
                            <label for="id">ID</label>
                            <input type="text" id="id" name="id" value="<?php echo $_GET['id']; ?>" disabled>
                            <label for="nama_dokter">Nama dokter</label>
                            <input type="text" id="nama_dokter" name="nama_dokter" value="<?php echo $_GET['nama_dokter']; ?>" readonly>
                            <label for="hari">Hari</label>
                            <input type="date" id="hari" name="hari" value="<?php echo $_GET['hari']; ?>" style="margin-bottom: 10px;">
                            <label for="jam">Jam</label>
                            <input type="time" id="jam" name="jam" value="<?php echo $_GET['jam']; ?>" style="margin-bottom: 10px;"><br>

                            <input type="submit" value="Submit">
                        </form>
                    </div>

                <?php else : ?>

                    <h3>Tambah jadwal</h3>

                    <div>
                        <form id="form-jadwal2" method="post" action="">
                            <label for="nama_dokter">Nama dokter</label>
                            <select id="nama_dokter" name="nama_dokter" style="padding:2px 20px; margin-bottom: 5px;">
                                <option></option>
                                <?php
                                $sql_pasien = "select * from dbklinik.dokter";
                                $query_pasien = $conn->query($sql_pasien);

                                while ($row = $query_pasien->fetch_assoc()) {
                                ?>
                                    <option><?php echo $row['nama_dokter'] ?></option>
                                <?php } ?>
                            </select>
                            <label for="hari">Hari</label>
                            <input type="date" id="hari" name="hari" style="margin-bottom: 10px;">
                            <label for="jam">Jam</label>
                            <input type="time" id="jam" name="jam" style="margin-bottom: 10px;"><br>
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
                $("#form-jadwal2").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        nama_dokter: $("#nama_dokter").val(),
                        hari: $("#hari").val(),
                        jam: $("#jam").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-jadwal.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewjadwal.php");
                        }
                    });

                    $("#form-jadwal2")[0].reset(); // Reset the form
                });

                $("#form-jadwal1").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        id: $("#id").val(),
                        nama_dokter: $("#nama_dokter").val(),
                        hari: $("#hari").val(),
                        jam: $("#jam").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-jadwal.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewjadwal.php");
                        }
                    });

                    $("#form-jadwal1")[0].reset(); // Reset the form
                });

                // Delete button click event handler
                $(document).on('click', '.delete-button', function(event) {
                    event.preventDefault(); // Prevent form submission
                    var id = $(this).data('id');
                    if (confirm('Are you sure you want to delete this item?')) {
                        $.ajax({
                            type: "GET",
                            url: "admin-jadwal.php?action=hapus&id=" + id,
                            success: function(data) {
                                window.location.replace("viewjadwal.php");
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