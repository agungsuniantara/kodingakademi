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
        <td>Name</td>
        <td>Course</td>
    </tr>
    <?php
        function table($a, $b , $c){
        for ($i = 0; $i < 3; $i++) {
                echo "
                    <tr>
                        <td>$a[$i]</td>
                        <td>$b[$i]</td>
                        <td>$c[$i]</td>
                    </tr>
                
                ";
            }
        }
        $no = array("1","2","3");
        $name = array("ben","tom","george");
        $course = array("web design","web programming","python basic");

        table($no, $name, $course);
    ?>
    </table>
</body>
</html>