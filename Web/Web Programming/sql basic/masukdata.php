<?php
$koneksi = mysqli_connect("localhost", "root", "", "coba10");

$sql = 'insert into isi values ("dode","denpasar")';

if (mysqli_query($koneksi, $sql)) {
    echo "Record inserted successfully";
} else {
    echo "Could not insert record: ";
}
