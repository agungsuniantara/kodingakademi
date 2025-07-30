<?php
    $data1 = array("satu", "dua", "tiga"); # array
    $data2 = array("nama" => "buja", "alamat" => "denpasar"); # asosiatif array

    echo "<h1>$data1[0]</h1>";
    echo "<h1>".$data2["nama"]."</h1>";

    $data1[0] = "halo"; # array
    $data2["alamat"] = "tabanan"; # asosiatif array

    echo "<h1>$data1[0]</h1>";
    echo "<h1>".$data2["alamat"]."</h1>";

    # looping array

    $size_data1 = count($data1); 
    $size_data2 = count($data2); 

    echo "<h1>$size_data1</h1>";
    echo "<h1>$size_data2</h1>";

    for ($i = 0; $i < $size_data1; $i++){ # array
        echo "<h1>$data1[$i]</h1>";
    }

    $keys = array_keys($data2); // keys = ["nama", "alamat"]
    
    for ($i = 0; $i < $size_data2; $i++){
        echo "<h1>".$data2[$keys[$i]]."</h1>";
        echo "<h1>".$keys[$i]."</h1>";
    }

    # looping foreach

    foreach ($data1 as $value){ // array
        echo "<h1>$value</h1>";
    }

    foreach ($data2 as $key => $value){ // asosiatif array
        echo "<h1>key = $key value = $value</h1>";
    }

    $admin = array("username" => "user_admin", "password" => "admin123", "role" => "admin");
    $user = array("username" => "user_pengguna", "password" => "pengguna123", "role" => "pengguna");
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
            <td>No</td>
            <td>Nama array</td>
            <td>Label</td>
            <td>Value</td>
        </tr>
        <?php
            foreach ($admin as $key => $value){
                echo "<tr>";
                echo "<td>1</td>";
                echo "<td>Admin</td>";
                echo "<td>$key</td>";
                echo "<td>$value</td>";
                echo "</tr>";
            };
        ?>
    </table>
</body>
</html>