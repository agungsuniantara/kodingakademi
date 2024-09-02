<?php
$koneksi = mysqli_connect("localhost", "root", "", "ajax");

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action'])) {

    // Delete action

    if ($_POST['action'] === 'delete' && isset($_POST['id'])) {
        $idToDelete = $_POST['id'];

        $deleteQuery = "DELETE FROM ajax.user WHERE id = '$idToDelete'";
        mysqli_query($koneksi, $deleteQuery);

        echo json_encode(array("berhasil"));
        exit;
    }

    // Fetch action

    elseif ($_POST['action'] === 'fetch' && isset($_POST['id'])) {
        $id = $_POST['id'];

        $fetchQuery = "SELECT * FROM ajax.user WHERE id = '$id'";
        $query = mysqli_query($koneksi, $fetchQuery);
        $array = mysqli_fetch_assoc($query);

        echo json_encode($array);
        exit;
    }

    // Edit action

    elseif ($_POST['action'] === 'edit' && isset($_POST['id'])) {
        $id = $_POST['id'];
        $name = $_POST['name'];
        $email = $_POST['email'];
        $number = $_POST['number'];
        $phone = $_POST['phone'];
        $password = $_POST['password'];
        $file = $_FILES['file'];
        $uploadfolder = "upload/";

        if (!file_exists($uploadfolder)) {
            mkdir($uploadfolder, 0777, true);
        }

        $targetPath = $uploadfolder . basename($file['name']);
        $move = move_uploaded_file($file['tmp_name'], $targetPath);

        if ($move) {
            $updateQuery = "UPDATE ajax.user SET 
                name='$name', email='$email', number='$number', 
                phone='$phone', password='$password', file='$targetPath' 
                WHERE id = '$id'";

            mysqli_query($koneksi, $updateQuery);
            echo json_encode(array("berhasil"));
            exit;
        } else {
            echo json_encode(array("gagal"));
            exit;
        }
    }

    // Tambah action

    elseif ($_POST['action'] === 'tambah') {

        $name = $_POST['name'];
        $email = $_POST['email'];
        $number = $_POST['number'];
        $phone = $_POST['phone'];
        $password = $_POST['password'];
        $file = $_FILES['file'];
        $uploadfolder = "upload/";

        if (!file_exists($uploadfolder)) {
            mkdir($uploadfolder, 0777, true);
        }

        $targetPath = $uploadfolder . basename($file['name']);
        $move = move_uploaded_file($file['tmp_name'], $targetPath);

        if ($move) {
            $insertQuery = "INSERT INTO ajax.user (name, email, number, phone, file, password) VALUES ('$name', '$email', '$number', '$phone', '$targetPath', '$password')";
            mysqli_query($koneksi, $insertQuery);
            echo json_encode(array("berhasil"));
            exit;
        } else {
            echo json_encode(array("gagal"));
            exit;
        }
    }
} else {

    // Tampil semua data

    $query = "SELECT * FROM ajax.user";
    $result = mysqli_query($koneksi, $query);

    $data = array();

    while ($row = mysqli_fetch_assoc($result)) {
        $data[] = $row;
    }

    echo json_encode(array("data" => $data));
}
