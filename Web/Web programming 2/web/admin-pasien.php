<?php

include "dbkoneksi.php";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    if (!isset($_POST['id'])) {
        //tambah pasien baru
        addNewpasien($conn, $_POST);
    } else {
        updatepasien($conn, $_POST);
    }
}
if ($_SERVER['REQUEST_METHOD'] === 'GET') {

    if (isset($_GET['action'])) {
        switch ($_GET['action']) {
            case "hapus":
                deletepasien($conn, $_GET);
                break;
            default:
                findAllpasien($conn);
        }
    } else {
        findAllpasien($conn);
    }
}


function addNewpasien($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'INSERT INTO dbklinik.pasien (nama, jenis_kelamin, usia) 
    VALUES ("' . $params['nama'] . '", "' . $params['jenis_kelamin'] . '", "' . $params['usia'] . '")';


    if ($conn->query($sql) === TRUE) {
        echo "pasien baru berhasil ditambah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function updatepasien($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'UPDATE dbklinik.pasien 
    SET nama ="' . $params['nama'] . '", jenis_kelamin ="' . $params['jenis_kelamin'] . '", usia ="' . $params['usia'] . '" WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        echo "pasien berhasil diubah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function deletepasien($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'DELETE FROM dbklinik.pasien WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        $msg = 'pasien berhasil dihapus';
    } else {
        $msg = "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    header("Location: viewpasien.php?message=" . $msg);
    exit();
}

function findAllpasien($conn)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM dbklinik.pasien ORDER BY nama";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo '<a href="viewpasien.php?action=tambah" class="button">Tambah</a>';
        echo '<table id="mydata">';
        echo '<tr>
            <th>Nama pasien</th>
            <th>Jenis kelamin</th>
            <th>Usia</th>
            <th>Aksi</th>
        </tr>';

        while ($row = $result->fetch_assoc()) {
            echo '<tr>
                <td>' . $row["nama"] . '</td>
                <td>' . $row["jenis_kelamin"] . '</td>
                <td>' . $row["usia"] . '</td>
                <td>
                <a href="viewpasien.php?action=ubah&id=' . $row["id"] .
                '&nama=' . $row["nama"] .
                '&jenis_kelamin=' . $row["jenis_kelamin"] .
                '&usia=' . $row["usia"] .
                '" class="button">Ubah</a>
                <a id="delete" href="viewpasien.php?action=hapus&id=' . $row["id"] . '" class="button">Hapus</a></td>
                </tr>';
        }

        echo '</table>';
    } else {
        echo "Tidak ada data pasien";
    }

    $conn->close();
}
