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
    class person
    {
        public $id;
        public $nama;
        public $nik;
        public $tgl_lahir;

        public function __construct($id, $nama, $nik, $tgl_lahir)
        {
            $this->id = $id;
            $this->nama = $nama;
            $this->nik = $nik;
            $this->tgl_lahir = $tgl_lahir;
        }

        public function getNama()
        {
            echo "Nama : $this->nama";
        }

        public function getNik()
        {
            echo "Nik : $this->nik";
        }

        public function getTglLahir()
        {
            echo "Tanggal lahir : $this->tgl_lahir";
        }
    }

    class pasien extends person
    {
        public $patientID;
        public $tgl_registrasi;
        public $usia;
        public $jenis_kelamin;
        public $alergi;

        public function data($tanggal, $usia, $jenis_kelamin, $alergi)
        {
            $this->patientID = $this->id;
            $this->tgl_registrasi = $tanggal;
            $this->usia = $usia;
            $this->jenis_kelamin = $jenis_kelamin;
            $this->alergi = $alergi;

            echo "id = {$this->patientID} <br>";
            echo "nama = {$this->nama} <br>";
            echo "tanggal registrasi = {$this->tgl_registrasi} <br>";
            echo "usia = {$this->usia} <br>";
            echo "jenis kelamin = {$this->jenis_kelamin} <br>";
            echo "alergi = {$this->alergi} <br>";
        }

        public function getPatientID()
        {
            echo $this->patientID;
        }

        public function getTglRegistrasi()
        {
            echo $this->tgl_registrasi;
        }
    }

    class dokter extends person
    {
        public $dokterID;
        public $spesialis;

        public function data($spesialis)
        {
            $this->dokterID = $this->id;
            $this->spesialis = $spesialis;

            echo "id = {$this->dokterID} <br>";
            echo "nama dokter = {$this->nama} <br>";
            echo "spesialis = {$this->spesialis} <br>";
        }

        public function getDokterID()
        {
            echo $this->dokterID;
        }
        public function getSpesialis()
        {
            echo $this->spesialis;
        }
    }

    $pasien = new pasien(1, 'agung', 123, '14 juni 1998');
    $dokter = new dokter(2, 'wayan', 123, '14 juni 1998');
    
    $pasien->data("23 april 2023", "23 tahun", "laki-laki", "bulu");

    $dokter->data("kandungan");
    ?>
</body>

</html>