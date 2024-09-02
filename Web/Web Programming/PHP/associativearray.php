<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $lamborghinis = array("suv"=>"Urus", "sports"=>"Huracan", "coupe"=>"Aventador");

        $suzuki["hatch"] = "Swift";
        $suzuki["utility"] = "Ertiga";
        $suzuki["suv"] = "Vitara";

        echo "Accessing the 2nd array... <br>";
        echo $suzuki["hatch"], "<br>";
        echo $suzuki["utility"], "<br>";
        echo $suzuki["suv"], "<br>";

        echo "<br>";
        
        echo "Accessing the 1st array... <br>";
        echo $lamborghinis["suv"], "<br>";
        echo $lamborghinis["sports"], "<br>";
        echo $lamborghinis["coupe"], "<br>";
    ?>
    <br>
    <?php
        $lamborghinis = array("suv"=>"Urus", "sports"=>"Huracan", "coupe"=>"Aventador");

        $size = count($lamborghinis);
        
        $keys = array_keys($lamborghinis);
        
        for($i = 0; $i < $size; $i++)
        {
            echo $lamborghinis[$keys[$i]] ." is a/an ". $keys[$i] ." car <br>";
        }
    ?>

<?php

$lamborghinis = array("Urus", "Huracan", "Aventador");

foreach($lamborghinis as $key => $value)
{
    echo $value ."is a/an ". $key ." car <br>";
}

?>

<br>

<?php
    $admin = array("username"=>"user_admin", "password"=>"admin123", "role"=>"admin");
    $pengguna = array("username"=>"user_pengguna", "password"=>"pengguna123", "role"=>"pengguna");
    $keysadmin = array_keys($admin);
    $keyspengguna = array_keys($pengguna);
?>
<table border="1">
    <tr>
        <td>No</td>
        <td>Nama array</td>
        <td>Label index</td>
        <td>Nilai / value</td>
    </tr>
    <tr>
        <td rowspan="3">1</td>
        <td rowspan="3">admin</td>
        <td><?php echo $keysadmin[0]?></td>
        <td><?php echo $admin["username"]?></td>
    </tr>
    <tr>
        <td><?php echo $keysadmin[1]?></td>
        <td><?php echo $admin["password"]?></td>
    </tr>
    <tr>
        <td><?php echo $keysadmin[2]?></td>
        <td><?php echo $admin["role"]?></td>
    </tr>
    <tr>
        <td rowspan="3">2</td>
        <td rowspan="3">pengguna</td>
        <td><?php echo $keyspengguna[0]?></td>
        <td><?php echo $pengguna["username"]?></td>
    </tr>
    <tr>
        <td><?php echo $keyspengguna[1]?></td>
        <td><?php echo $pengguna["password"]?></td>
    </tr>
    <tr>
        <td><?php echo $keyspengguna[2]?></td>
        <td><?php echo $pengguna["role"]?></td>
    </tr>
</table>
</body>
</html>