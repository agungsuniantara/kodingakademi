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
   class Books {
      
      var $price;
      var $title;
      
      function setPrice($par){
         $this->price = $par;
      }
      
      function getPrice(){
         echo $this->price ."<br/>";
      }
      
      function setTitle($par){
         $this->title = $par;
      }
      
      function getTitle(){
         echo $this->title ." <br/>";
      }
   }
?>
<?php
    $physics = new Books;
    $maths = new Books;
    $chemistry = new Books;

    $physics->setTitle( "Physics for High School" );
    $chemistry->setTitle( "Advanced Chemistry" );
    $maths->setTitle( "Algebra" );

    $physics->setPrice( 10 );
    $chemistry->setPrice( 15 );
    $maths->setPrice( 7 );

    $physics->getTitle();
    $chemistry->getTitle();
    $maths->getTitle();

    $physics->getPrice();
    $chemistry->getPrice();
    $maths->getPrice();
?>

<?php
class Fruit {
  public $nama;
  public $warna;
  public $kalori;
  
  public function __construct($name, $color,$calories) {
    $this->nama = $name;
    $this->warna = $color; 
    $this->kalori = $calories; 
  }
  
  public function getName() {
    echo "Nama buah : $this->nama <br>"; 
  }
}

class Apple extends Fruit {
  public function myDetails() {
    echo "Nama buah : {$this->nama} , Warna :  {$this->warna}, Kalori : {$this->kalori}"; 
  }
}

$apple = new Apple("Apple Malang", "hijau", 100);
$apple->getName();
$apple->myDetails();

?>
</body>
</html>