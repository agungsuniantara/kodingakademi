<?php
session_start();
if (isset($_SESSION['namalengkap'])) {
?>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <title>Website Klinik Sejahtera</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="mystyle.css">
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <style>
            .clock-container {
                position: relative;
                width: 200px;
                height: 200px;
            }

            .clock-image {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-image: url('jam.png');
                /* Ganti 'jam.png' dengan nama file gambar jam Anda */
                background-size: cover;
            }

            .hour-hand,
            .minute-hand,
            .second-hand {
                position: absolute;
                top: 50%;
                left: 50%;
                transform-origin: bottom center;
                background-color: black;
            }

            .hour-hand {
                width: 6px;
                height: 60px;
                z-index: 3;
            }

            .minute-hand {
                width: 4px;
                height: 80px;
                z-index: 2;
            }

            .second-hand {
                width: 2px;
                height: 90px;
                z-index: 1;
            }

            .logout{
                background-color: green;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }

            .logout > a{
                color: white;
                text-decoration: none;
            }
        </style>
    </head>

    <body>

        <section>
            <div id="mymenu" class="vertical-menu">
                <a href="admin.php" class="active">Home</a>
                <a id="menuDokter" href="viewdokter.php">Dokter</a>
                <a id="menuPasien" href="viewpasien.php">Pasien</a>
                <a id="menuObat" href="viewobat.php">Obat</a>
                <a id="menuKunjungan" href="viewkunjungan.php">Kunjungan</a>
                <a id="jadwalDokter" href="viewjadwal.php">Jadwal Dokter</a>
            </div>

            <div id="content" class="rightContent">
                <h2>Selamat Datang di Klinik Sehat Sejahtera</h2>
                <button class="logout"><a href="logout.php">logout</a></button>
            </div>

        </section>

        <footer>
            <p>Copyright Klinik Sehat Sejahtera 2022</p>
        </footer>

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