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
        function data1($nama = "Ben", $course = "Coding"){
            echo "
                <tr>
                    <td>1</td>
                    <td>$nama</td>
                    <td>$course</td>
                </tr>
            ";
        }
    ?>

    <table border="1">
        <tr>
            <td>No</td>
            <td>Nama</td>
            <td>Course</td>
        </tr>
        <?php
            data1();
        ?>
    </table>
</body>
</html>