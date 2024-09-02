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
    $list = array('html', 'css', 'javascript');
    $no = 1; 
    foreach($list as $isi){
        echo $no.". ". $isi . "<br>";
        $no++; 
    }
    
    echo "<br>";

    $web = array('php', 'javascript', 'C++');
    foreach ($web as $key => $value) {
        echo "array : " . $value . " index ke " . $key . "<br>";
    }


    echo "<br>";

    $web = array("HTML", "CSS", "Javascript");
    foreach($web as $data){
        echo "$data \n";
    }

    echo "<br>";

    for($i = 1; $i <= 4; $i++){
        echo "<h1>heading HTML $i </h1><br>";
    }
?>

    <table border="1">
        <?php
            $array1 = array("ID", "NAMA", "UMUR");
            foreach($array1 as $value){
                echo 
                "<tr>
                    <td>$value</td>
                </tr>";
            }
        ?>
    </table>

    <br>
    
    <?php
        $contoh1 = array("array", "array2");
        $panjang = count($contoh1);

        echo "panjang dari array adalah $panjang";
    ?>
</body>
</html>
