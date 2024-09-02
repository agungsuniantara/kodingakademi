<?php

include "dbkoneksi.php";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    if (!isset($_POST['id'])) {
        //tambah jadwal baru
        addNewjadwal($conn, $_POST);
    } else {
        updatejadwal($conn, $_POST);
    }
}
if ($_SERVER['REQUEST_METHOD'] === 'GET') {

    if (isset($_GET['action'])) {
        switch ($_GET['action']) {
            case "hapus":
                deletejadwal($conn, $_GET);
                break;
            default:
                findAlljadwal($conn);
        }
    } else {
        findAlljadwal($conn);
    }
}


function addNewjadwal($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'INSERT INTO dbklinik.jadwal_dokter (nama_dokter, hari, jam) 
    VALUES ("' . $params['nama_dokter'] . '", "' . $params['hari'] . '", "' . $params['jam'] . '")';

    if ($conn->query($sql) === TRUE) {
        echo "jadwal baru berhasil ditambah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function updatejadwal($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'UPDATE dbklinik.jadwal_dokter 
    SET nama_dokter ="' . $params['nama_dokter'] . '", hari ="' . $params['hari'] . '", jam ="' . $params['jam'] . '" WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        echo "jadwal berhasil diubah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function deletejadwal($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'DELETE FROM dbklinik.jadwal_dokter WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        $msg = 'jadwal berhasil dihapus';
    } else {
        $msg = "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    header("Location: viewjadwal.php?message=" . $msg);
    exit();
}

function findAlljadwal($conn)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM dbklinik.jadwal_dokter ORDER BY nama_dokter";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo '<a href="viewjadwal.php?action=tambah" class="button">Tambah</a>';
        echo '<table id="mydata">';
        echo '<tr>
        <th>Nama pasien</th>
        <th>tanggal jadwal</th>
        <th>keluhan pasien</th>
        <th>hasil diagnosa</th>
        <th>Aksi</th>
        </tr>';

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

        echo '</table>';
    } else {
        echo "Tidak ada data jadwal";
    }

    $conn->close();
}
