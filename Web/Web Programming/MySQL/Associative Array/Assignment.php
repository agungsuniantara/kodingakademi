<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .table,tr,td{
            border: 3px solid rgb(2, 2, 2);
            padding: 8px;
        }
        .table{
            border-collapse: collapse;
            text-align: center;
        }
    </style>
    <title>Document</title>
</head>
<body>
    <table class="table" align="center">
    <?php
        $admin = array("username" => "user_admin", "password" => "admin123", "role" => "admin");
        $pengguna = array("username" => "user_pengguna", "password" => "pengguna123", "role" => "pengguna");
    ?>
        <tr>
            <td><b>No</b></td>
            <td><b>Nama Array</b></td>
            <td><b>Label Index</b></td>
            <td><b>Nilai / Value</b></td>
        </tr>
        <tr>
            <td rowspan="4">1</td>
            <td rowspan="4">Admin</td>
            <?php foreach($pengguna as $key => $value): ?>
                <tr>
                    <td><?php echo $key?></td>
                    <td><?php echo $value?></td>
                </tr>
            <?php endforeach; ?>
        </tr>
        <tr>
            <td rowspan="4">2</td>
            <td rowspan="4">Pengguna</td>
            <?php foreach($admin as $key => $value): ?>
                <tr>
                    <td><?php echo $key?></td>
                    <td><?php echo $value?></td>
                </tr>
            <?php endforeach; ?>
        </tr>
    </table>
</body>
</html>