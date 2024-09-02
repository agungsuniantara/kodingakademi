<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    class tamu
    {
        public $nama;
        public $alamat;
        public $umur;

        function masuk_data($a, $b, $c)
        {
            $this->nama = $a;
            $this->alamat = $b;
            $this->umur = $c;
        }

        function tampil_data()
        {
            echo "nama = $this->nama <br>";
            echo "alamat = $this->alamat <br>";
            echo "umur = $this->umur <br>";
        }
    }

    $yani = new tamu();

    $yani->masuk_data("yani", "denpasar", "18 tahun");

    $yani->tampil_data();

    ?>

    <br><br>

    <?php
    class pelanggan
    {
        public $nama;
        public $alamat;
        public $umur;

        public function __construct($a, $b, $c)
        {
            $this->nama = $a;
            $this->alamat = $b;
            $this->umur = $c;
        }

        function tampil_data()
        {
            echo "nama = $this->nama <br>";
            echo "alamat = $this->alamat <br>";
            echo "umur = $this->umur <br>";
        }
    }

    class pembeli extends pelanggan
    {
        public $status;

        function id($a)
        {
            $this->status = $a;
        }

        function tampil_status()
        {
            echo "status = $this->status <br>";
        }
    }

    class penjual extends pelanggan
    {
        public $status;

        function id($a)
        {
            $this->status = $a;
        }

        function tampil_status()
        {
            echo "status = $this->status <br>";
        }
    }

    $pembeli = new pembeli("yani", "denpasar", "18 tahun");
    $pembeli->id("pembeli");
    $pembeli->tampil_data();
    $pembeli->tampil_status();

    echo "<br>";

    $penjual = new penjual("wayan", "denpasar", "16 tahun");
    $penjual->id("penjual");
    $penjual->tampil_data();
    $penjual->tampil_status();
    ?>
</body>

</html>