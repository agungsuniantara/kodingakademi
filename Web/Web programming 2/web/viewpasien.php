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
                    $sql = "SELECT * FROM dbklinik.pasien ORDER BY nama";
                    if (!empty($nama)) {
                        $sql = $sql . " WHERE nama LIKE '%" . $nama . "%'";
                    }
                    $result = $conn->query($sql);

                    if (isset($_GET['message'])) {
                        echo '<script>alert("' . $_GET['message'] . '");</script>';
                    }
                ?>

                    <a href="viewpasien.php?action=tambah" class="button">Tambah</a>
                    <table id="mydata">
                        <tr>
                            <th>Nama Pasien</th>
                            <th>Jenis kelamin</th>
                            <th>Usia</th>
                            <th>Aksi</th>
                        </tr>
                        <?php
                        while ($row = $result->fetch_assoc()) {
                            echo '<tr>
                            <td>' . $row["nama"] . '</td>
                            <td>' . $row["jenis_kelamin"] . '</td>
                            <td>' . $row["usia"] . '</td>
                            <td>
                                <a href="viewpasien.php?action=ubah&id=' . $row["id"] . '&nama=' . $row["nama"] . '&jenis_kelamin=' . $row["jenis_kelamin"] . '&usia=' . $row["usia"] . '" class="button">Ubah</a>
                                <a id="delete" href="#" data-id="' . $row["id"] . '" class="button delete-button">Hapus</a>
                            </td>
                        </tr>';
                        }
                        ?>
                    </table>

                <?php elseif ($_GET['action'] == "ubah") : ?>

                    <h3>Ubah Pasien</h3>

                    <div>
                        <form id="form-pasien1" method="post" action="">
                            <label for="id">ID</label>
                            <input type="text" id="id" name="id" value="<?php echo $_GET['id']; ?>" disabled>
                            <label for="nama">Nama</label>
                            <input type="text" id="nama" name="nama" value="<?php echo $_GET['nama']; ?>">
                            <label for="jenis_kelamin">Jenis kelamin</label>
                            <input type="text" id="jenis_kelamin" name="jenis_kelamin" value="<?php echo $_GET['jenis_kelamin']; ?>">
                            <label for="usia">Usia</label>
                            <input type="text" id="usia" name="usia" value="<?php echo $_GET['usia']; ?>">
                            <input type="submit" value="Submit">
                        </form>
                    </div>

                <?php else : ?>

                    <h3>Tambah Pasien</h3>

                    <div>
                        <form id="form-pasien2" method="post" action="">
                            <label for="nama">Nama</label>
                            <input type="text" id="nama" name="nama" placeholder="Nama pasien..">

                            <label for="jenis_kelamin">Jenis kelamin</label>
                            <input type="text" id="jenis_kelamin" name="jenis_kelamin" placeholder="Jenis kelamin..">

                            <label for="usia">Usia</label>
                            <input type="text" id="usia" name="usia" placeholder="Usia..">

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
                $("#form-pasien2").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        nama: $("#nama").val(),
                        jenis_kelamin: $("#jenis_kelamin").val(),
                        usia: $("#usia").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-pasien.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewpasien.php");
                        }
                    });

                    $("#form-pasien2")[0].reset(); // Reset the form
                });

                $("#form-pasien1").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        id: $("#id").val(),
                        nama: $("#nama").val(),
                        jenis_kelamin: $("#jenis_kelamin").val(),
                        usia: $("#usia").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-pasien.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewpasien.php");
                        }
                    });

                    $("#form-pasien1")[0].reset(); // Reset the form
                });

                // Delete button click event handler
                $(document).on('click', '.delete-button', function(event) {
                    event.preventDefault(); // Prevent form submission
                    var id = $(this).data('id');
                    if (confirm('Are you sure you want to delete this item?')) {
                        $.ajax({
                            type: "GET",
                            url: "admin-pasien.php?action=hapus&id=" + id,
                            success: function(data) {
                                window.location.replace("viewpasien.php");
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