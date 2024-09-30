<?php
require "config.php";

$sql = "SELECT * FROM employee";
$result = mysqli_query($conn, $sql);
$data = mysqli_fetch_all($result, MYSQLI_ASSOC);

print_r($data);

echo "<br>";

foreach ($data as $row) { 
    echo "<br>";
    echo "EmpID : " . $row["EmpID"] . "<br>";
    echo "Name : " . $row["Name"] . "<br>";
    echo "Address : " . $row["Address"] . "<br>";
    echo "Mobile Number : " . $row["Mobile Number"] . "<br>";
    echo "Gender : " . $row["Gender"] . "<br>";
}