<?php
class Dokterr
{
    // Atribut (variabel)
    public $nomer = 1;
    public $nama_dokter;
    public $spesialisasi;

    // Metode (fungsi)
    public function tampil()
    {
        echo "$this->nomer. Nama dokter : $this->nama_dokter, Spesialisasi : $this->spesialisasi " . "<br>";
    }
}

// Membuat instance (object) dari class Mobil
$dokter1 = new Dokterr();
$dokter2 = new Dokterr();

// Mengatur nilai atribut untuk setiap object
$dokter1->nama_dokter = "Merah";
$dokter1->spesialisasi = "Toyota";

$dokter2->nomer = 2;
$dokter2->nama_dokter = "Biru";
$dokter2->spesialisasi = "Daihatsu";

// Memanggil atribut pada setiap object
echo "Nama dokter : $dokter1->nama_dokter <br>";
echo "Spesialisasi : $dokter1->spesialisasi <br>";

echo "Nama dokter : $dokter2->nama_dokter <br>";
echo "Spesialisasi : $dokter2->spesialisasi <br>";

// Memanggil metode pada setiap object
$dokter1->tampil();
$dokter2->tampil();
