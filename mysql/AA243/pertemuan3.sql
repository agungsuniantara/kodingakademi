-- DDL ( Database Definition Language )
-- sekumpulan perintah yang dapat membuat, mengubah dan menghapus
-- struktur atau skema basis data dan constraint ( primary key, foreign key ).

-- Fungsi utama DDL : 
-- 1. Membuat objek dalam basis data (CREATE)
-- 2. Mengubah struktur objek (ALTER)
-- 3. Menghapus objek dari basis data (DROP)
-- 4. Menghapus semua data dalam tabel tanpa menghapus strukturnya (TRUNCATE)

-- CREATE 

CREATE DATABASE toko_online;
USE toko_online;

CREATE TABLE karyawan(
	id_karyawan INT, 
    nama VARCHAR(40),
    alamat VARCHAR(40),
    Status VARCHAR(30),
    Tanggal DATE
);

-- ALTER 

-- ADD ( menambah )
ALTER TABLE karyawan
ADD gaji DECIMAL,
ADD jabatan VARCHAR(20);

DESC karyawan;

-- MODIFY ( MENGUBAH )
ALTER TABLE karyawan
MODIFY Tanggal VARCHAR(20);

-- CHANGE ( MENGEDIT )
ALTER TABLE karyawan
CHANGE Tanggal Date DATE;

-- DROP ( MENGHAPUS )
ALTER TABLE karyawan
DROP jabatan;

-- DDL DROP 

DROP TABLE karyawan;
DROP DATABASE toko_online;




