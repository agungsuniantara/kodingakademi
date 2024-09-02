<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $data = array(
            array("agustus", "2020"),
            array("januari","2024")
        );

        foreach ($data as $item){
            foreach ($item as $name){
    ?>

    <div>
        <h1><?php echo $name?></h1>
    </div>

    <?php
        }
    }
    ?>
</body>
</html>