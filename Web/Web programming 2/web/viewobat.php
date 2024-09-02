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
                    $sql = "SELECT * FROM dbklinik.obat ORDER BY nama";
                    if (!empty($nama)) {
                        $sql = $sql . " WHERE nama LIKE '%" . $nama . "%'";
                    }
                    $result = $conn->query($sql);

                    if (isset($_GET['message'])) {
                        echo '<script>alert("' . $_GET['message'] . '");</script>';
                    }
                ?>

                    <a href="viewobat.php?action=tambah" class="button">Tambah</a>
                    <table id="mydata">
                        <tr>
                            <th>Nama obat</th>
                            <th>harga</th>
                            <th>Aksi</th>
                        </tr>
                        <?php
                        while ($row = $result->fetch_assoc()) {
                            echo '<tr>
                            <td>' . $row["nama"] . '</td>
                            <td>' . $row["harga"] . '</td>
                            <td>
                                <a href="viewobat.php?action=ubah&id=' . $row["id"] . '&nama=' . $row["nama"] . '&harga=' . $row["harga"] . '" class="button">Ubah</a>
                                <a id="delete" href="#" data-id="' . $row["id"] . '" class="button delete-button">Hapus</a>
                            </td>
                        </tr>';
                        }
                        ?>
                    </table>

                <?php elseif ($_GET['action'] == "ubah") : ?>

                    <h3>Ubah obat</h3>

                    <div>
                        <form id="form-obat1" method="post" action="">
                            <label for="id">ID</label>
                            <input type="text" id="id" name="id" value="<?php echo $_GET['id']; ?>" disabled>
                            <label for="nama">Nama</label>
                            <input type="text" id="nama" name="nama" value="<?php echo $_GET['nama']; ?>">
                            <label for="harga">harga</label>
                            <input type="text" id="harga" name="harga" value="<?php echo $_GET['harga']; ?>">
                            <input type="submit" value="Submit">
                        </form>
                    </div>

                <?php else : ?>

                    <h3>Tambah obat</h3>

                    <div>
                        <form id="form-obat2" method="post" action="">
                            <label for="nama">Nama</label>
                            <input type="text" id="nama" name="nama" placeholder="Nama obat..">

                            <label for="harga">harga</label>
                            <input type="text" id="harga" name="harga" placeholder="harga..">

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
                $("#form-obat2").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        nama: $("#nama").val(),
                        harga: $("#harga").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-obat.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewobat.php");
                        }
                    });

                    $("#form-obat2")[0].reset(); // Reset the form
                });

                $("#form-obat1").submit(function(event) {
                    event.preventDefault(); // Prevent form submission
                    var formData = {
                        id: $("#id").val(),
                        nama: $("#nama").val(),
                        harga: $("#harga").val()
                    };

                    $.ajax({
                        type: "POST",
                        url: "admin-obat.php",
                        data: formData,
                        success: function(data) {
                            alert(data);
                            window.location.replace("viewobat.php");
                        }
                    });

                    $("#form-obat1")[0].reset(); // Reset the form
                });

                // Delete button click event handler
                $(document).on('click', '.delete-button', function(event) {
                    event.preventDefault(); // Prevent form submission
                    var id = $(this).data('id');
                    if (confirm('Are you sure you want to delete this item?')) {
                        $.ajax({
                            type: "GET",
                            url: "admin-obat.php?action=hapus&id=" + id,
                            success: function(data) {
                                window.location.replace("viewobat.php");
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