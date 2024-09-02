<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    abstract class orang
    {
        public $nama;
        public $umur;
        public $alamat;

        public function __construct($a, $b, $c)
        {
            $this->nama = $a;
            $this->umur = $b;
            $this->alamat = $c;
        }

        abstract public function tampil_umur(): float;

        abstract public function tampil_nama(): string;

        abstract public function tampil_alamat(): string;
    }

    class tampil extends orang
    {
        public function tampil_umur(): float
        {
            return $this->umur;
        }

        public function tampil_nama(): string
        {
            return "nama = $this->nama";
        }
        public function tampil_alamat(): string
        {
            return "alamat = $this->alamat";
        }

        public function hoby()
        {
            echo "hobi = berenang";
        }
    }

    $tampil = new tampil("mang agus", 50, "denpasar");
    $umur = $tampil->tampil_umur();
    $nama = $tampil->tampil_nama();
    $alamat = $tampil->tampil_alamat();

    echo "$nama";
    echo "<br>";
    echo "umur = $umur";
    echo "<br>";
    echo "$alamat";
    echo "<br>";
    $tampil->hoby();
    ?>
</body>

</html>