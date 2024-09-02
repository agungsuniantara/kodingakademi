<?php
    include "config.php";
    $sql = "SELECT 'EmpID', 'Name', 'Address', 'Mobile Number', 'Gender' 
            FROM employee";
    $result = mysqli_query($conn, $sql);
    print_r($result);
