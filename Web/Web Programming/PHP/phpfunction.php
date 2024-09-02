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
   function printName(){
      echo"Hello It is a Function";
   }
   printName();

   echo "<hr>";

   printName();
?>

<br>


<?php
   function Greetings($name){
     echo "Hello, ".$name." Welcome to Koding Akademi!";
   }

   Greetings("Robert");
   $name = "Lyla";
   echo"</br>";
   Greetings($name)
?>

<br>


<?php   
   function Greeting($name, $place="Koding Akademi"){
     echo "Hello, ".$name." Welcome to ".$place;
   }

   Greeting("Robert","denpasar");
   $name = "Lyla";
   echo"</br>";
   Greeting($name)
?>

<br>


<?php
   function hitungLua($panjang, $lebar){
     $luas = 2*($panjang + $lebar);
     return $luas;
   }

   echo "Luas Persegi adalah ". hitungLua(20, 30);
?>

<br>


<?php

  function hitungLuas($panjang, $lebar){
    $luas = 2*($panjang + $lebar);
    return $luas;
  }
  function Greetin($name){
    echo "Hello, ".$name." Welcome to Koding Akademi!";
    echo "<br>";
    echo "Luas Persegi adalah ". hitungLuas(20, 30);
  }

  // memanggil fungsi perkenalan
  Greetin("Robert");

?>

<br>


<?php

function faktorial($angka) {
  if ($angka < 2) {
    return 1;
  } else {
  return ($angka * faktorial($angka-1));
  }
}

echo "faktorial 5 adalah " . faktorial(5);


function data($arr1, $arr2, $arr3){
    echo "
      <table>
          <tr>
            <td>No</td>
            <td>Nama</td>
            <td>Course</td>
          </tr>
          <tr>
            <td>$arr1[0]</td>
            <td>$arr1[1]</td>
            <td>$arr1[2]</td>
          </tr>
          <tr>
            <td>$arr2[0]</td>
            <td>$arr2[1]</td>
            <td>$arr2[2]</td>
          </tr>
          <tr>
            <td>$arr3[0]</td>
            <td>$arr3[1]</td>
            <td>$arr3[2]</td>
          </tr>
      </table>
    ";
}

$arr1 = array(1, "ben", "web design");
$arr2 = array(2, "ben", "web design");
$arr3 = array(3, "ben", "web design");

data($arr1, $arr2, $arr3);

?>
</body>
</html>