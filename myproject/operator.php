<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $x = 10;
        $y = 2;
        echo $x + $y; // output: 12
        echo $x - $y; // output: 8
        echo $x * $y; // output: 20
        echo $x / $y; // output : 5
        echo $x % $y; // output : 0

        echo "<br>";
        
        $x = 5; 
        echo $x; // output: 5   
        $x += 3;   
        echo $x; // output: 8  
        $x *= 2;   
        echo $x; // output: 16    

        echo "<br>";

        $x = 10;
        $y = 20;
        var_dump($x == $y); // Output: bool(false)
        var_dump($x != $y); // Output: bool(true)
        var_dump($x < $y); // Output: bool(true)
        var_dump($x > $y); // Output: bool(false)

        // $x = true;
        // $y = false;
        // var_dump($x && $y); // Output: bool(false)
        // var_dump($x || $y); // Output: bool(true)
        // var_dump(!$x); // Output: bool(false)

        // $z = 10;
        // echo $z; // output: 10  
        // $z++;
        // echo $z; // output: 11  


?>
</body>
</html>