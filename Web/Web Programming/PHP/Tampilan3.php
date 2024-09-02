<!DOCTYPE html>
<html>
<head>
<title>tabel</title>
</head>
<body>
<?php
    $array[0] = "PHP";
    $array[1] = "Javascript";
    $array[2] = "Python";
    $array[3] = "C";
    $array[4] = "C++";
    $array[5] = "C#";
?>
<table border="1">
    <tr>
        <td><?php echo $array[0] ?></td>
    </tr>
    <tr>
        <td><?php echo $array[1] ?></td>
    </tr>
    <tr>
        <td><?php echo $array[2] ?></td>
    </tr>
    <tr>
        <td><?php echo $array[3] ?></td>
    </tr>
    <tr>
        <td><?php echo $array[4] ?></td>
    </tr>
    <tr>
        <td><?php echo $array[5] ?></td>
    </tr>
</table>
</body>
</html>