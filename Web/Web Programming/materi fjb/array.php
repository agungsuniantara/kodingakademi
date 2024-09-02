<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $fruits = ["Apple", "Orange", "Mango"];
        echo $fruits[0]; // Output: Apple

        $fruits = ["Apple" => 1.5, "Orange" => 1.2, "Mango" => 2.0];
        echo $fruits["Apple"]; // Output: 1.5

        $number = [
                [10, 5, 20, 3, 15],
                [30, 4, 5, 10, 25],
                [40, 2, 3, 15, 23]
            ];
        echo $number[0][2] ."<br> <br>"; // Output: 20

        $name = "Alexander";
        $usia = 18;
        $alamat = "Batanghari";
        $course = "Web Programming";

        $number = 10;
        

        echo "Name : $name <br>";
        echo "Age : $usia <br>";
        echo "Address : $alamat <br>";
        echo "Course : $course <br>";
    ?>
</body>
</html>