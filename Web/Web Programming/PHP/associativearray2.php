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
    $admin = array("username"=>"user_admin", "password"=>"admin123", "role"=>"admin");
    $pengguna = array("username"=>"user_pengguna", "password"=>"pengguna123", "role"=>"pengguna");
    $keysadmin = array_keys($admin);
    $keypengguna = array_keys($pengguna);
    $index = 0;
?>
<table border="1">
    <?php
        while($index < 1) {
    ?>
    <tr>
        <td>No</td>
        <td>Nama array</td>
        <td>Label index</td>
        <td>Nilai / value</td>
    </tr>
    <tr>
        <td rowspan="3">1</td>
        <td rowspan="3">admin</td>
        <td><?php echo $keysadmin[$index]?></td>
        <td><?php echo $admin[$keysadmin[$index]]?></td>
        <?php $index++; ?>
    </tr>
    <tr>
        <td><?php echo $keysadmin[$index]?></td>
        <td><?php echo $admin[$keysadmin[$index]]?></td>
        <?php $index++; ?>
    </tr>
    <tr>
        <td><?php echo $keysadmin[$index]?></td>
        <td><?php echo $admin[$keysadmin[$index]]?></td>
    </tr>
    <tr>
        <td rowspan="3">2</td>
        <td rowspan="3">pengguna</td>
        <td><?php echo $keysadmin[$index]?></td>
        <td><?php echo $admin[$keysadmin[$index]]?></td>
        <?php $index++; ?>
    </tr>
    <tr>
        <td><?php echo $keysadmin[$index]?></td>
        <td><?php echo $admin[$keysadmin[$index]]?></td>
        <?php $index++; ?>
    </tr>
    <tr>
        <td><?php echo $keysadmin[$index]?></td>
        <td><?php echo $admin[$keysadmin[$index]]?></td>
    </tr>
</table>
<?php 
    } 
?>
</body>
</html>