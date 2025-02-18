<?php
    $conn = new mysqli("localhost", "user", "", "student");

    $sql = "update Employee set Name = 'wayan', Address = 'ubud' where EmpID = 1";
    $query = mysqli_query($conn, $sql);
?>