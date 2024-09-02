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
$hatchbacks = array("Suzuki" => "Baleno","Skoda" => "Fabia","Hyundai" => "i20","Tata" => "Tigor");
$hatchbacks2 = array("Suzu" => "Baleno","Sko" => "Fabia","Hyun" => "i20","Ta" => "Tigor");
$merged = array_merge($hatchbacks, $hatchbacks2);
print_r($merged);

$contoh1 = array("coba1");
$contoh2 = array("coba2");
$contoh3 = array("coba3");

$gabung = array_merge($contoh1, $contoh2,$contoh3);

foreach($gabung as $n => $key){
    echo $key;
}
?>

<br>

<?php
$hatchbacks = array(
        "Suzuki" => "Baleno",
        "Skoda" => "Fabia",
        "Hyundai" => "i20",
        "Tata" => "Tigor"
    );
print_r(array_flip($hatchbacks));
?>
</body>
</html>