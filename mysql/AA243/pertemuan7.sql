-- Operator dalam MySQL adalah simbol atau kata kunci 
-- yang digunakan untuk melakukan operasi terhadap satu atau lebih nilai atau ekspresi dalam perintah SQL.

-- Jenis-Jenis Operator dalam MySQL
-- 1. aritmatika (+, -, *, /, %)
-- 2. logika ( AND, OR, NOT )
-- 3. perbandingan ( =, !=, <, >, <=, >= )
-- 4. khusus : 
	-- LIKE	-> Mencocokkan pola string 
    -- IN -> Memeriksa apakah nilai termasuk dalam daftar
    -- BETWEEN, AND -> Memeriksa apakah nilai berada dalam rentang
    -- IS NULL / IS NOT NULL -> Mengecek apakah data NULL
    -- EXISTS -> Memeriksa apakah subquery menghasilkan hasil
    -- ANY / ALL -> Membandingkan dengan hasil subquery
    
CREATE DATABASE sistem_kampus;
USE sistem_kampus;

-- CREATE TABLE

CREATE TABLE mahasiswa (
    id_mahasiswa INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100),
    jurusan VARCHAR(50),
    umur INT,
    email VARCHAR(100)
);

CREATE TABLE dosen (
    id_dosen INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100),
    keahlian VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE mata_kuliah (
    id_mk INT AUTO_INCREMENT PRIMARY KEY,
    nama_mk VARCHAR(100),
    sks INT,
    id_dosen INT,
    FOREIGN KEY (id_dosen) REFERENCES dosen(id_dosen)
);

-- INSERT DATA

INSERT INTO mahasiswa (nama, jurusan, umur, email) VALUES
('Ayu Lestari', 'Teknik Informatika', 20, 'ayu@gmail.com'),
('Budi Prasetyo', 'Sistem Informasi', 22, 'budi@kampus.ac.id'),
('Citra Dewi', 'Manajemen', 19, NULL),
('Doni Saputra', 'Teknik Informatika', 23, 'doni@kampus.ac.id'),
('Eka Wahyuni', 'Manajemen', 18, NULL);

INSERT INTO dosen (nama, keahlian, email) VALUES
('Dr. Andi', 'Data Science', 'andi@kampus.ac.id'),
('Prof. Rina', 'Jaringan Komputer', NULL),
('Dra. Sari', 'Manajemen SDM', 'sari@kampus.ac.id'),
('Bapak Anwar', 'Basis Data', 'anwar@kampus.ac.id');

INSERT INTO mata_kuliah (nama_mk, sks, id_dosen) VALUES
('Pemrograman Python', 3, 1),
('Jaringan Komputer', 3, 2),
('Manajemen Bisnis', 2, 3),
('Basis Data', 4, 4);

-- ARITMATIKA

SELECT nama, umur, umur + 2 AS umur_ditambah
FROM mahasiswa;

SELECT nama_mk, sks, 24 - sks AS sisa_sks
FROM mata_kuliah;

-- PERBANDINGAN

SELECT * FROM mahasiswa
WHERE umur > 20;

SELECT * FROM mata_kuliah
WHERE sks != 3;

-- LOGIKA

SELECT * FROM mahasiswa
WHERE jurusan = 'Teknik Informatika' AND umur > 20; -- TRUE AND TRUE = TRUE

SELECT * FROM mahasiswa
WHERE jurusan = 'Sistem Informasi' OR umur < 20;

-- KHUSUS

-- LIKE

SELECT * FROM mahasiswa
WHERE nama LIKE 'a%';

SELECT * FROM mahasiswa
WHERE nama LIKE '%o';

SELECT * FROM mahasiswa
WHERE nama LIKE '%tari%';

-- IN 

SELECT * FROM mahasiswa
WHERE jurusan IN ('Teknik Informatika', 'Sistem Informasi');

-- BETWEEN

SELECT * FROM mahasiswa
WHERE umur BETWEEN 19 AND 22;

-- IS NULL

SELECT * FROM mahasiswa
WHERE email IS NULL;

-- EXIST ( SUBQUERY )

SELECT nama FROM dosen d
WHERE EXISTS (
  SELECT * FROM mata_kuliah mk
  WHERE mk.id_dosen = d.id_dosen
);

-- ALL / ANY

SELECT * FROM mahasiswa
WHERE umur > ALL (
    SELECT umur FROM mahasiswa WHERE jurusan = 'Manajemen'
);

SELECT * FROM mahasiswa
WHERE umur > ANY (
    SELECT umur FROM mahasiswa WHERE jurusan = 'Teknik Informatika'
);



















    