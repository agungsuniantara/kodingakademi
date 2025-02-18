CREATE DATABASE supermarket;
USE supermarket;

/*
CREATE TABLE karyawan_tetap(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50),
    gaji DECIMAL(10,2)
);
*/

/*
CREATE TABLE karyawan_kontrak(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50),
    gaji DECIMAL(10,2)
);
*/

/*
CREATE TABLE pelanggan_online(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50),
    jumlah_transaksi DECIMAL(10,2)
);
*/

/*
CREATE TABLE pelanggan_offline(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50),
    jumlah_transaksi DECIMAL(10,2)
);
*/

/*
CREATE TABLE produk(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nama_produk VARCHAR(50),
    harga DECIMAL(10,2),
    stok INT
);
*/

/*
INSERT INTO karyawan_tetap(nama, gaji)
VALUES
("Andi", 8000000),
("Budi", 7500000),
("Citra", 9000000),
("Dewi", 8500000)
*/

/*
INSERT INTO karyawan_kontrak(nama, gaji)
VALUES
("Feri", 5000000),
("Gita", 5500000),
("Hendra", 6000000),
("Ika", 4500000)
*/

/*
INSERT INTO pelanggan_online(nama, jumlah_transaksi)
VALUES 
("Alfa", 1500000),
("Beta", 2000000),
("Charlie", 2500000),
("Delta", 1800000)
*/

/*
INSERT INTO pelanggan_offline(nama, jumlah_transaksi)
VALUES 
("Fox", 3000000),
("Juliet", 2500000),
("Saha", 1900000),
("Golf", 2200000)
*/

/*
INSERT INTO produk(nama_produk, harga, stok)
VALUES 
("Laptop", 15000000, 20),
("Smartphone", 8000000, 50),
("Tablet", 5000000, 30),
("Headset", 250000, 100)
*/

-- UNION ( hasil query data nya masing-masing harus sama dan akan menampilkan data yang tidak duplikat )

/*
SELECT nama FROM karyawan_tetap
UNION 
SELECT nama FROM karyawan_kontrak;
*/

-- SUB QUERIES

/*
SELECT nama, gaji FROM karyawan_tetap 
WHERE gaji > (SELECT AVG(gaji) FROM karyawan_tetap);
*/

/*
SELECT nama, jumlah_transaksi FROM pelanggan_offline
WHERE jumlah_transaksi > (SELECT MAX(jumlah_transaksi) FROM pelanggan_online);
*/

-- UNION & SUB QUERIES

SELECT nama FROM karyawan_tetap
WHERE gaji > (SELECT AVG(gaji) FROM karyawan_tetap)
UNION
SELECT nama FROM karyawan_kontraks
WHERE gaji > (SELECT AVG(gaji) FROM karyawan_kontrak);

-- LATIHAN

-- 1. Tampilkan nama produk dan harga produk yang lebih besar dari rata-ratanya
-- 2. Tampilkan jumlah transaksi pelanggan online yang lebih besar dari rata-ratanya dan jumlah transaksi pelanggan offline yang lebih besar dari rata-ratanya juga.

-- jawaban 1
SELECT nama_produk, harga FROM produk
WHERE harga > (SELECT AVG(harga) FROM produk);

-- jawaban 2 
SELECT nama, jumlah_transaksi FROM pelanggan_offline
WHERE jumlah_transaksi > (SELECT AVG(jumlah_transaksi) FROM pelanggan_offline)
UNION
SELECT nama, jumlah_transaksi FROM pelanggan_online
WHERE jumlah_transaksi > (SELECT AVG(jumlah_transaksi) FROM pelanggan_online);




