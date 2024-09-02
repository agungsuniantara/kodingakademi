<?php
    $lamborgini = array("suv" => "Urus", "sports" => "Huracan", "coupe" => "aventador");
    $size = count($lamborgini);
    $keys = array_keys($lamborgini);

    $suzuki["hatch"] = "swift";
    $suzuki["utility"] = "ertiga";
    $suzuki["suv"] = "vitara";

    echo "akses 2nd array \n";
    echo $suzuki["hatch"], "\n";
    echo $suzuki["utility"], "\n";
    echo $suzuki["suv"], "\n";
    echo "\n";

    echo "akses 1nd array \n";
    echo $lamborgini["suv"], "\n";
    echo $lamborgini["sports"], "\n";
    echo $lamborgini["coupe"], "\n";
    echo "\n";

    for ($i = 0; $i < $size; $i++){
        echo $lamborgini[$keys[$i]]. " is a/an ". $keys[$i]. " car \n";
    }
    
    foreach($lamborgini as $keys1 => $value){
        echo $value." is a ".$key1." car\n";
    }
?>