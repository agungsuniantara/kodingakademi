<?php
require "config.php";

$sql = "SELECT * FROM employee WHERE `Name` = 'admin'";
$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_assoc($result);

if($row){
    print_r($row);
    echo "<br>";
    echo "EmpID : " . $row["EmpID"] . "<br>";
    echo "Name : " . $row["Name"] . "<br>";
    echo "Address : " . $row["Address"] . "<br>";
    echo "Mobile Number : " . $row["Mobile Number"] . "<br>";
    echo "Gender : " . $row["Gender"] . "<br>";
}

