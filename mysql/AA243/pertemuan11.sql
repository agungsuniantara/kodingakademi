-- Agregat / agregasi
-- Agregasi adalah fungsi yang melakukan perhitungan terhadap kumpulan data (bukan satu baris saja). 
-- Fungsi agregat sering digunakan untuk menganalisis data, misal menghitung rata-rata, jumlah, nilai terbesar/terkecil.

-- | Fungsi   | Keterangan                                                                 |
-- | -------- | -------------------------------------------------------------------------- |
-- | COUNT()  | Menghitung jumlah baris/data                                               |
-- | SUM()    | Menjumlahkan semua nilai pada kolom numerik                                |
-- | AVG()    | Menghitung nilai rata-rata kolom numerik                                   |
-- | MIN()    | Mengambil nilai terkecil                                                   |
-- | MAX()    | Mengambil nilai terbesar                                                   |
-- | ROUND()  | Membulatkan hasil perhitungan ke jumlah angka di belakang koma tertentu    |

-- UNION
-- UNION digunakan untuk menggabungkan hasil dari dua atau lebih query SELECT menjadi satu hasil.
-- Hasil gabungan akan menghapus baris duplikat secara default.
-- Untuk menampilkan semua baris (termasuk duplikat), gunakan UNION ALL.

-- SUBQUERY
-- Subquery adalah query di dalam query lain.
-- Subquery dapat berada di bagian SELECT, FROM, WHERE, atau HAVING.

-- PRAKTEK --

CREATE DATABASE kampusku;
USE kampusku;

CREATE TABLE mahasiswa_fisika (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(50)
);

CREATE TABLE mahasiswa_matematika (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(50)
);

CREATE TABLE nilai_mahasiswa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(50),
    matkul VARCHAR(30),
    nilai INT
);

INSERT INTO mahasiswa_fisika (nama) VALUES
('Andi'), ('Budi'), ('Citra');

INSERT INTO mahasiswa_matematika (nama) VALUES
('Dina'), ('Budi'), ('Eko');

INSERT INTO nilai_mahasiswa (nama, matkul, nilai) VALUES
('Andi', 'Fisika', 80),
('Budi', 'Fisika', 85),
('Citra', 'Fisika', 90),
('Dina', 'Matematika', 70),
('Budi', 'Matematika', 75),
('Eko', 'Matematika', 95);

-- AGREGASI --

-- COUNT

SELECT COUNT(*) AS jumlah_fisika FROM mahasiswa_fisika;

-- SUM 

SELECT SUM(nilai) AS total_nilai_fisika
FROM nilai_mahasiswa
WHERE matkul = 'Fisika';

-- AVG & ROUND

SELECT AVG(nilai) AS rata_rata_nilai
FROM nilai_mahasiswa;

SELECT ROUND(AVG(nilai),2) AS rata_rata_nilai
FROM nilai_mahasiswa;

-- MIN dan MAX

SELECT MIN(nilai) AS nilai_terendah, MAX(nilai) AS nilai_tertinggi
FROM nilai_mahasiswa;

-- UNION & UNION ALL --

-- UNION
-- Menggabungkan semua nama mahasiswa (tanpa duplikat)
SELECT nama FROM mahasiswa_fisika
UNION
SELECT nama FROM mahasiswa_matematika;

-- Menggabungkan nama & asal jurusan
SELECT nama, 'Fisika' AS jurusan FROM mahasiswa_fisika
UNION
SELECT nama, 'Matematika' AS jurusan FROM mahasiswa_matematika;

-- UNION ALL
-- Menggabungkan semua nama mahasiswa (dengan duplikat)
SELECT nama FROM mahasiswa_fisika
UNION ALL
SELECT nama FROM mahasiswa_matematika;

-- SUBQUERY -- 

-- Mahasiswa dengan nilai tertinggi
SELECT nama, nilai
FROM nilai_mahasiswa
WHERE nilai = (SELECT MAX(nilai) FROM nilai_mahasiswa);

-- Mahasiswa dengan nilai di atas rata-rata
SELECT nama, nilai
FROM nilai_mahasiswa
WHERE nilai > (SELECT AVG(nilai) FROM nilai_mahasiswa);

-- Mahasiswa yang memiliki nilai di atas rata-rata mata kuliah
SELECT nama, matkul, nilai
FROM nilai_mahasiswa n1
WHERE nilai > (
    SELECT AVG(nilai) 
    FROM nilai_mahasiswa n2
    WHERE n2.matkul = n1.matkul
);

-- Hitung jumlah seluruh mahasiswa unik (gabungan fisika & matematika, tanpa duplikat)
SELECT COUNT(*) AS jumlah_mahasiswa
FROM (
  SELECT nama FROM mahasiswa_fisika
  UNION
  SELECT nama FROM mahasiswa_matematika
) AS semua_mahasiswa;





