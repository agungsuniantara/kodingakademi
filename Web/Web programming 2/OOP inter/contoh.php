<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    abstract class shape
    {
        public $color;
        public $angka1;
        public $angka2;
        public $hasil;

        public function __construct($angka1, $angka2, $color)
        {
            $this->angka1 = $angka1;
            $this->angka2 = $angka2;
            $this->color = $color;
        }

        abstract public function getArea(): float;

        abstract public function toString(): string;
    }

    class rectangle extends shape
    {
        public function getArea(): float
        {
            $this->hasil = $this->angka1 * $this->angka2;

            return $this->hasil;
        }

        public function toString(): string
        {
            return "panjang = $this->angka1, lebar = $this->angka2, warna = $this->color";
        }
    }

    class triangle extends shape
    {
        public function getArea(): float
        {
            $this->hasil = 0.5 * $this->angka1 * $this->angka2;

            return $this->hasil;
        }

        public function toString(): string
        {
            return "alas = $this->angka1, tinggi = $this->angka2, warna = $this->color";
        }
    }

    $rectangle = new rectangle(10, 20, "red");
    echo "Rectangle : ";
    echo "<br>";
    echo $rectangle->toString();
    echo "<br>";
    echo "Luas: " . $rectangle->getArea();
    echo "<br>";
    echo "<br>";

    $triangle = new triangle(10, 20, "blue");
    echo "Triangle : ";
    echo "<br>";
    echo $triangle->toString();
    echo "<br>";
    echo "Luas: " . $triangle->getArea();
    ?>
</body>

</html>