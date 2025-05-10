-- Constraint adalah aturan yang diterapkan pada kolom atau tabel untuk membatasi jenis data yang dapat dimasukkan, 
-- sehingga menjaga integritas data.

-- Jenis-Jenis Constraint dalam SQL
-- 1. PRIMARY KEY → Menandakan kolom sebagai kunci utama (unik & tidak boleh NULL).
-- 2. FOREIGN KEY → Menghubungkan dua tabel (referensi ke PRIMARY KEY tabel lain).
-- 3. UNIQUE → Memastikan nilai dalam kolom unik (tidak ada duplikat).
-- 4. NOT NULL → Memastikan kolom tidak boleh kosong (NULL).
-- 5. CHECK → Memberikan kondisi tertentu pada nilai kolom.
-- 6. DEFAULT → Memberikan nilai default jika tidak diisi.

-- DML adalah kumpulan perintah SQL untuk memodifikasi data dalam tabel, meliputi:

-- 1. INSERT → Menambah data
-- 2. SELECT → Membaca data
-- 3. UPDATE → Mengubah data
-- 4. DELETE → Menghapus data

CREATE DATABASE kampus;
USE kampus;

CREATE TABLE jurusan(
	ID INT PRIMARY KEY,
    Nama_jurusan VARCHAR(30) NOT NULL,
    Fakultas VARCHAR(30) NOT NULL
);

-- id : 1, nama jurusan : sistem informasi, fakultas : teknik
-- 1 to many

CREATE TABLE mahasiswa(
	NIM INT PRIMARY KEY,
    Nama VARCHAR(30) NOT NULL,
    Alamat VARCHAR(30) NOT NULL,
    Email VARCHAR(30) UNIQUE,
    Umur INT CHECK (Umur > 16),
    ID_jurusan INT,
    CONSTRAINT fk_jurusan FOREIGN KEY(ID_jurusan) REFERENCES jurusan(ID)
);

-- NIM : 200200, Nama : wahyu, Alamat : denpasar, email : test, umur : 20, id jurusan : 1

-- INSERT ( masukkan data ) 

INSERT INTO jurusan (ID, Nama_jurusan, Fakultas)
VALUES (1, "Sistem informasi", "Teknik");

INSERT INTO mahasiswa (NIM, Nama, Alamat, Email ,Umur, ID_jurusan)
VALUES (200200, "wahyu", "denpasar", "wahyu@gmail.com", 20, 1);

-- SELECT ( melihat data ) 

SELECT * FROM jurusan;
SELECT NIM, Nama, ID_jurusan FROM mahasiswa;

-- UPDATE ( mengubah data )

UPDATE Mahasiswa 
SET 
	Nama = "agung",
    Alamat = "ubud"
WHERE NIM = 200200;

-- DELETE ( menghapus data ) 

DELETE FROM Mahasiswa
WHERE NIM = 200200;
