<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    class orang
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

    class mang_agus extends orang
    {
        public $hobi;

        function hobii($a)
        {
            $this->hobi = $a;
        }

        function tampil_hobi()
        {
            echo "hobi = $this->hobi";
        }
    }

    class wah_asta extends orang
    {
        public $hobi;

        function hobii($a)
        {
            $this->hobi = $a;
        }
        function tampil_hobi()
        {
            echo "hobi = $this->hobi";
        }
    }

    $mang_agus = new mang_agus("mang agus", "denpasar", "18 tahun");
    $mang_agus->hobii("renang");
    $mang_agus->tampil_data();
    $mang_agus->tampil_hobi();

    echo "<br><br>";

    $wah_asta = new wah_asta("wah asta", "denpasar", "50 tahun");
    $wah_asta->hobii("taekwondo");
    $wah_asta->tampil_data();
    $wah_asta->tampil_hobi();
    ?>
</body>

</html>