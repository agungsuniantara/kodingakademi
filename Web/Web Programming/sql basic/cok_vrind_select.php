<?php
    $conn = mysqli_connect("localhost","root","root","student");

    $sql = "SELECT * FROM employee";
    $result = mysqli_query($conn, $sql);
    $data = mysqli_fetch_all($result, MYSQLI_ASSOC);
    print_r(json_encode($data));

    echo "<br>";

    foreach ($data as $row) {
        echo "Nama : " . $row["Name"] . ", Alamat : " . $row["Address"]. "<br>";
    }
?>