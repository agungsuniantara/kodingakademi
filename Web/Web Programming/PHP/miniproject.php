<!DOCTYPE html>
<html>
    <head>
        <style>
            .table {
                font-family: sans-serif;
                color: #232323;
                border-collapse: collapse;
                text-align: center;
                width:100%;
            }
            .table tr td{
                padding: 8px 20px;
            }
        </style>
    </head>
    <body>
    <?php
    $array = array("ID","NAME","EMAIL","POSITION","PHONE");
    $array1 = array("001","agung","agungsuniantara@gmail.com","CEO","090909090");
    $array2 = array("002","salsa","salsa@gmail.com","Karyawan","07787878");
    ?>
    <div>
    <div></div>
    <table class="table" align="center">
        <tr style="background-color: red;">
            <?php foreach($array as $id):?>
                <td><?php echo $id ?></td>
            <?php endforeach; ?>
        </tr>
        <tr>
            <?php foreach($array1 as $data1):?>
                <td><?php echo $data1?></td>
            <?php endforeach; ?>
        </tr>
        <tr>
            <?php foreach($array2 as $data2):?>
                <td><?php echo $data2?></td>
            <?php endforeach; ?>
        </tr>
    </table>
    </div>
    </body>
</html>