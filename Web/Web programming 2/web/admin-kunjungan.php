<?php

include "dbkoneksi.php";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    if (!isset($_POST['id'])) {
        //tambah kunjungan baru
        addNewkunjungan($conn, $_POST);
    } else {
        updatekunjungan($conn, $_POST);
    }
}
if ($_SERVER['REQUEST_METHOD'] === 'GET') {

    if (isset($_GET['action'])) {
        switch ($_GET['action']) {
            case "hapus":
                deletekunjungan($conn, $_GET);
                break;
            default:
                findAllkunjungan($conn);
        }
    } else {
        findAllkunjungan($conn);
    }
}


function addNewkunjungan($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'INSERT INTO dbklinik.kunjungan (nama_pasien, tgl_kunjungan, keluhan_pasien, hasil_diagnosa) 
    VALUES ("' . $params['nama_pasien'] . '", "' . $params['tgl_kunjungan'] . '", "' . $params['keluhan_pasien'] . '", "' . $params['hasil_diagnosa'] . '")';


    if ($conn->query($sql) === TRUE) {
        echo "kunjungan baru berhasil ditambah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function updatekunjungan($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'UPDATE dbklinik.kunjungan 
    SET nama_pasien ="' . $params['nama_pasien'] . '", tgl_kunjungan ="' . $params['tgl_kunjungan'] . '", keluhan_pasien ="' . $params['keluhan_pasien'] . '", hasil_diagnosa ="' . $params['hasil_diagnosa'] . '" WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        echo "kunjungan berhasil diubah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function deletekunjungan($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'DELETE FROM dbklinik.kunjungan WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        $msg = 'kunjungan berhasil dihapus';
    } else {
        $msg = "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    header("Location: viewkunjungan.php?message=" . $msg);
    exit();
}

function findAllkunjungan($conn)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM dbklinik.kunjungan ORDER BY nama_kunjungan";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo '<a href="viewkunjungan.php?action=tambah" class="button">Tambah</a>';
        echo '<table id="mydata">';
        echo '<tr>
        <th>Nama pasien</th>
        <th>tanggal kunjungan</th>
        <th>keluhan pasien</th>
        <th>hasil diagnosa</th>
        <th>Aksi</th>
        </tr>';

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

        echo '</table>';
    } else {
        echo "Tidak ada data kunjungan";
    }

    $conn->close();
}
