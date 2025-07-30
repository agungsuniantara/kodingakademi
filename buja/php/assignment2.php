<?php
    $arr = array("PHP", "Javascript", "Python");
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
        <?php
            foreach ($arr as $value) {
                echo "<tr>";
                echo "<td>" . $value . "</td>";
                echo "</tr>";
            }
        ?>
    </table>
</body>
</html>