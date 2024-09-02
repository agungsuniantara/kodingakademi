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
        $nilai = 50;

        if($nilai < 50){
            echo "nilai D";
        }
        elseif($nilai >= 50 && $nilai < 70){
            echo "nilai C";
        }
        elseif($nilai >= 70 && $nilai <= 80){
            echo "nilai B";
        }
        else{
            echo "nilai A";
        }
    ?>
</body>
</html>