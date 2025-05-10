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

CREATE TABLE Jurusan(
    ID INT PRIMARY KEY,                 
    Nama_Jurusan VARCHAR(50) NOT NULL,   
    Fakultas VARCHAR(50) NOT NULL     
);

CREATE TABLE Mahasiswa(
	NIM INT PRIMARY KEY,
    Nama VARCHAR(50) NOT NULL,
    Email VARCHAR(50) UNIQUE,
    Umur INT CHECK (Umur >= 17),
    Jurusan_id INT,
    CONSTRAINT fk_jurusan FOREIGN KEY (Jurusan_id) REFERENCES Jurusan(ID)
);

-- Menambah data ke tabel Mahasiswa  
INSERT INTO Jurusan (ID, Nama_Jurusan, Fakultas)  
VALUES (1, "Sistem informasi", 'teknik');  

INSERT INTO Mahasiswa (NIM, Nama, Email, Umur, Jurusan_ID)  
VALUES (20220005, 'Eko Pratama', 'eko@email.com', 19, 1);

INSERT INTO Mahasiswa (NIM, Nama, Email, Umur, Jurusan_ID)  
VALUES (20220006, 'Eko Pratama', 'ekoo@email.com', 19, 1);

-- Menampilkan data / membaca data

SELECT * FROM Mahasiswa;  

-- Update

UPDATE Mahasiswa
SET 
    Email = 'budi.baru@email.com',
    Umur = 21
WHERE NIM = '20220006';

-- Hapus

DELETE FROM Mahasiswa  
WHERE NIM = '20220006'; 

DROP DATABASE kampus;
