-- OBJEK : 
-- 1. DATABASE
-- 2. TABEL
-- 3. KOLOM

-- TIPE DATA SQL : 
-- 1. INT (INTEGER / BILANGAN BULAT)
-- 2. VARCHAR (BISA MENYIMPAN TEKS DAN ANGKA)
-- 3. DECIMAL (MENYIMPAN BILANGAN DESIMAL)
-- 4. DATE (MENYIMPAN TANGGAL / YYYY-MM-DD)

-- OPERATOR : 

-- ARITMATIKA : 
-- +, -, /, *, % (MODULUS)

-- PERBANDINGAN : 
-- >, <, >= , <= , !=

-- LOGIKA : 
-- AND, OR, NOT

CREATE DATABASE usaha;

CREATE TABLE usaha.karyawan(
	id_karyawan INT,
    nama VARCHAR(30), 
    umur INT, 
    gaji DECIMAL,
    tanggal DATE
);

SELECT * FROM usaha.karyawan;

-- DDL , DML

