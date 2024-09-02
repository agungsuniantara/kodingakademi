<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $array = ['prabu', 'wayan', 'agus', 20];

        $jumlah = count($array);
        echo "<h5>jumlah data = $jumlah</h5>";
        echo "<h5>data 1 = $array[0]</h5>";
        echo "<h5>data 2 = $array[1]</h5>";

        for ($i = 0; $i < $jumlah; $i++){
            echo "$array[$i] <br>";
        }

        foreach($array as $data){
            echo $data;
        }

    ?>
</body>
</html>