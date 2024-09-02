<?php

include "dbkoneksi.php";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    if (!isset($_POST['id'])) {
        //tambah dokter baru
        addNewDokter($conn, $_POST);
    } else {
        updateDokter($conn, $_POST);
    }
}
if ($_SERVER['REQUEST_METHOD'] === 'GET') {

    if (isset($_GET['action'])) {
        switch ($_GET['action']) {
            case "hapus":
                deleteDokter($conn, $_GET);
                break;
            default:
                findAllDokter($conn);
        }
    } else {
        findAllDokter($conn);
    }
}


function addNewDokter($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'INSERT INTO dbklinik.dokter (nama_dokter, spesialis) 
    VALUES ("' . $params['nama_dokter'] . '", "' . $params['spesialis'] . '")';


    if ($conn->query($sql) === TRUE) {
        echo "Dokter baru berhasil ditambah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function updateDokter($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'UPDATE dbklinik.dokter 
    SET nama_dokter ="' . $params['nama_dokter'] . '", spesialis ="' . $params['spesialis'] . '" WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        echo "Dokter berhasil diubah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function deleteDokter($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'DELETE FROM dbklinik.dokter WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        $msg = 'Dokter berhasil dihapus';
    } else {
        $msg = "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    header("Location: viewdokter.php?message=" . $msg);
    exit();
}

function findAllDokter($conn)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM dbklinik.dokter ORDER BY nama_dokter";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo '<a href="viewdokter.php?action=tambah" class="button">Tambah</a>';
        echo '<table id="mydata">';
        echo '<tr>
            <th>Nama Dokter</th>
            <th>Spesialisasi</th>
            <th>Aksi</th>
        </tr>';

        while ($row = $result->fetch_assoc()) {
            echo '<tr>
                <td>' . $row["nama_dokter"] . '</td>
                <td>' . $row["spesialis"] . '</td>
                <td>
                <a href="viewdokter.php?action=ubah&id=' . $row["id"] .
                '&nama_dokter=' . $row["nama_dokter"] .
                '&spesialis=' . $row["spesialis"] .
                '" class="button">Ubah</a>
                <a id="delete" href="viewdokter.php?action=hapus&id=' . $row["id"] . '" class="button">Hapus</a></td>
                </tr>';
        }

        echo '</table>';
    } else {
        echo "Tidak ada data dokter";
    }

    $conn->close();
}
