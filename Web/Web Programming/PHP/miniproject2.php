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
        $judul = array("ID", "NAMA", "UMUR", "EMAIL", "POSITION", "PHONE");
        $isi1 = array("E001", "Agung", "18 tahun", "agung@gmail.com", "karyawan", "rahasia");
    ?>
    <table border="1">
        <tr>
        <?php
            foreach($judul as $value){
                echo 
                "<td>$value</td>";
            }
        ?>
        </tr>
        <tr>
        <?php
            foreach($isi1 as $value){
                echo 
                "<td>$value</td>";
            }
        ?>
        </tr>
    </table>
</body>
</html>