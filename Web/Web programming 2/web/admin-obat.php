<?php

include "dbkoneksi.php";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    if (!isset($_POST['id'])) {
        //tambah obat baru
        addNewobat($conn, $_POST);
    } else {
        updateobat($conn, $_POST);
    }
}
if ($_SERVER['REQUEST_METHOD'] === 'GET') {

    if (isset($_GET['action'])) {
        switch ($_GET['action']) {
            case "hapus":
                deleteobat($conn, $_GET);
                break;
            default:
                findAllobat($conn);
        }
    } else {
        findAllobat($conn);
    }
}


function addNewobat($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'INSERT INTO dbklinik.obat (nama, harga) 
    VALUES ("' . $params['nama'] . '", "' . $params['harga'] . '")';


    if ($conn->query($sql) === TRUE) {
        echo "obat baru berhasil ditambah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function updateobat($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'UPDATE dbklinik.obat 
    SET nama ="' . $params['nama'] . '", harga ="' . $params['harga'] . '" WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        echo "obat berhasil diubah";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function deleteobat($conn, $params)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = 'DELETE FROM dbklinik.obat WHERE id=' . $params['id'];


    if ($conn->query($sql) === TRUE) {
        $msg = 'obat berhasil dihapus';
    } else {
        $msg = "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    header("Location: viewobat.php?message=" . $msg);
    exit();
}

function findAllobat($conn)
{
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM dbklinik.obat ORDER BY nama";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo '<a href="viewobat.php?action=tambah" class="button">Tambah</a>';
        echo '<table id="mydata">';
        echo '<tr>
            <th>Nama obat</th>
            <th>harga</th>
            <th>Aksi</th>
        </tr>';

        while ($row = $result->fetch_assoc()) {
            echo '<tr>
                <td>' . $row["nama"] . '</td>
                <td>' . $row["harga"] . '</td>
                <td>
                <a href="viewobat.php?action=ubah&id=' . $row["id"] .
                '&nama=' . $row["nama"] .
                '&harga=' . $row["harga"] .
                '" class="button">Ubah</a>
                <a id="delete" href="viewobat.php?action=hapus&id=' . $row["id"] . '" class="button">Hapus</a></td>
                </tr>';
        }

        echo '</table>';
    } else {
        echo "Tidak ada data obat";
    }

    $conn->close();
}
