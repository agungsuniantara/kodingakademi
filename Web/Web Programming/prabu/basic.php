<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        // variabel
        $nama = "prabu";
        $angka = 20;

        echo "<h1>$nama</h1>";
        echo "<h1>$angka</h1>";
        
        // conditional statement
        // if
        if ($nama == "prabu"){
            echo "
                <script>
                    alert('berhasil');
                </script>
            ";
        }
        else{
            echo "gagal";
        }
        // for
        for ($i = 0; $i < 5; $i++){
            echo "<h1>$nama</h1>";
        }
    ?>
</body>
</html>