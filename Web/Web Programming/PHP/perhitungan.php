<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="" method="post">
        angka 1 : <input type="number" name="angka1">
        angka 2 : <input type="number" name="angka2">
        pilih :   
        <select name="mode" id="">
            <option>plus</option>
            <option>minus</option>
            <option>subtract</option>
        </select>
        <input type="submit">
    </form>
    <?php
        $angka1 = $_POST['angka1'];
        $angka2 = $_POST['angka2'];
        $mode = $_POST['mode'];

        switch($mode){
            case "plus":
                $hasil = $angka1 + $angka2;
                echo $hasil;
                break;
            case "minus":
                $hasil = $angka1 - $angka2;
                echo $hasil;
                break;
            case "subtract":
                $hasil = $angka1 * $angka2;
                echo $hasil;
                break;
            default:
                echo "angka tidak dikenal";
        }
    ?>
</body>
</html>