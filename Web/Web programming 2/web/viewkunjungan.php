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
                    $sql = "SELECT * FROM dbklinik.kunjungan ORDER BY nama_pasien";
                    if (!empty($nama)) {
                        $sql = $sql . " WHERE nama LIKE '%" . $nama . "%'";
                    }
                    $result = $conn->query($sql);

                    if (isset($_GET['message'])) {
                        echo '<script>alert("' . $_GET['message'] . '");</script>';
                    }
                ?>

                    <a href="viewkunjungan.php?action=tambah" class="button">Tambah</a>
                    <table id="mydata">
                        <tr>
                            <th>Nama pasien</th>
                            <th>tanggal kunjungan</th>
                            <th>keluhan pasien</th>
                            <th>hasil diagnosa</th>
                            <th>Aksi</th>
                        </tr>
                        <?php
                        while ($row = $result->fetch_assoc()) {
                            echo '<tr>
                            <td>' . $row["nama_pasien"] . '</td>
                            <td>' . $row["tgl_kunjungan"] . '</td>
                            <td>' . $row["keluhan_pasien"] . '</td>
                            <td>' . $row["hasil_diagnosa"] . '</td>
                            <td>
                                <a href="viewkunjungan.php?action=ubah&id=' . $row["id"] . '&nama_pasien=' . $row["nama_pasien"] . '&tgl_kunjungan=' . $row["tgl_kunjungan"] . '&keluhan_pasien=' . $row["keluhan_pasien"] . '&hasil_diagnosa=' . $row["hasil_diagnosa"] . '" class="button">Ubah</a>
                                <a id="delete" href="#" data-id="' . $row["id"] . '" class="button delete-button">Hapus</a>
                            </td>
                        </tr>';
                        }
                        ?>
                    </table>

                <?php elseif ($_GET['action'] == "ubah") : ?>

                    <h3>Ubah kunjungan</h3>

                    <div>
                        <form id="form-kunjungan1" method="post" action="">
                            <label for="id">ID</label>
                            <input type="text" id="id" name="id" value="<?php echo $_GET['id']; ?>" disabled>
                            <label for="nama_pasien">Nama pasien</label>
                            <input type="text" id="nama_pasien" name="nama_pasien" value="<?php echo $_GET['nama_pasien']; ?>" readonly>
                            <label for="tgl_kunjungan">Tanggal kunjungan</label>
                            <input type="datetime-local" id="tgl_kunjungan" name="tgl_kunjungan" value="<?php echo $_GET['tgl_kunjungan']; ?>">
                            <label for="keluhan_pasien">Keluhan pasien</label>
                            <input type="text" id="keluhan_pasien" name="keluhan_pasien" value="<?php echo $_GET['keluhan_pasien']; ?>">
                            <label for="hasil_diagnosa">Hasil diagnosa</label>
                            <input type="text" id="hasil_diagnosa" name="hasil_diagnosa" value="<?php echo $_GET['hasil_diagnosa']; ?>">
                            <input type="submit" value="Submit">
                        </form>
                    </div>

                <?php else : ?>

                    <h3>Tambah kunjungan</h3>

                    <div>
                        <form id="form-kunjungan2" method="post" action="">
                            <label for="nama_pasien">Nama pasien</label>
                            <select id="nama_pasien" name="nama_pasien" style="padding:2px 20px; margin-bottom: 5px;">
                                <option></option>
                                <?php
                                $sql_pasien = "select * from dbklinik.pasien";
                                $query_pasien = $conn->query($sql_pasien);

                                while ($row = $query_pasien->fetch_assoc()) {
                                ?>
                                    <option><?php echo $row['nama'] ?></option>
                                <?php } ?>
                            </select>
                            <label for="tgl_kunjungan">Tanggal kunjungan</label>
                            <input type="datetime-local" id="tgl_kunjungan" name="tgl_kunjungan" style="margin-bottom: 5px;">
                            <label for="keluhan_pasien">Keluhan pasien</label>
                            <input type="text" id="keluhan_pasien" name="keluhan_pasien" placeholder="keluhan pasien..">
                            <label for="hasil_diagnosa">Hasil diagnosa</label>
                            <input type="text" id="hasil_diagnosa" name="hasil_diagnosa" placeholder="hasil diagnosa..">
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
                $("#form-kunjungan2").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        nama_pasien: $("#nama_pasien").val(),
                        tgl_kunjungan: $("#tgl_kunjungan").val(),
                        keluhan_pasien: $("#keluhan_pasien").val(),
                        hasil_diagnosa: $("#hasil_diagnosa").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-kunjungan.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewkunjungan.php");
                        }
                    });

                    $("#form-kunjungan2")[0].reset(); // Reset the form
                });

                $("#form-kunjungan1").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        id: $("#id").val(),
                        nama_pasien: $("#nama_pasien").val(),
                        tgl_kunjungan: $("#tgl_kunjungan").val(),
                        keluhan_pasien: $("#keluhan_pasien").val(),
                        hasil_diagnosa: $("#hasil_diagnosa").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-kunjungan.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewkunjungan.php");
                        }
                    });

                    $("#form-kunjungan1")[0].reset(); // Reset the form
                });

                // Delete button click event handler
                $(document).on('click', '.delete-button', function(event) {
                    event.preventDefault(); // Prevent form submission
                    var id = $(this).data('id');
                    if (confirm('Are you sure you want to delete this item?')) {
                        $.ajax({
                            type: "GET",
                            url: "admin-kunjungan.php?action=hapus&id=" + id,
                            success: function(data) {
                                window.location.replace("viewkunjungan.php");
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