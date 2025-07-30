<?php
    $arr1 = array("E001","Wiliiam Smith","Wiliiam_Smith@gmail.com","CEO","08112144");
    $arr2 = array("E002","WReza Dredd","Reza_fredd@gmail.com","Sr Manager","08112143");
    $arr3 = array("E003","Mohan Kumar","Mohan_Kumar@gmail.com","Web Developer","081126234");
    $arr4 = array("E004","Cindy Mac","Cindy_Mac@gmail.com","Senior HR","08536437");
    $arr5 = array("E005","Vince Jose","Vince_Jose@gmail.com","HR Consultant","08199465");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border="1">
        <tr>
            <th>No</th>
            <th>Name</th>
            <th>Email</th>
            <th>Position</th>
            <th>Phone</th>
        </tr>
        <tr>
            <?php
                foreach ($arr1 as $value) {
                    echo "<td>" . $value . "</td>";
                }
            ?>
        </tr>
        <tr>
            <?php
                foreach ($arr2 as $value) {
                    echo "<td>" . $value . "</td>";
                }
            ?>
        </tr>
        <tr>
            <?php
                foreach ($arr3 as $value) {
                    echo "<td>" . $value . "</td>";
                }
            ?>
        </tr>
        <tr>
            <?php
                foreach ($arr4 as $value) {
                    echo "<td>" . $value . "</td>";
                }
            ?>
        </tr>
        <tr>
            <?php
                foreach ($arr5 as $value) {
                    echo "<td>" . $value . "</td>";
                }
            ?>
        </tr>
    </table>
</body>
</html>