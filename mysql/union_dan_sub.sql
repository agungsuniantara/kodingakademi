CREATE DATABASE kantor;
USE kantor;

CREATE TABLE karyawan_tetap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50),
    gaji DECIMAL(10, 2)
);

CREATE TABLE karyawan_kontrak (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50),
    gaji DECIMAL(10, 2)
);

CREATE TABLE pelanggan_online (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50),
    jumlah_transaksi DECIMAL(10, 2)
);

CREATE TABLE pelanggan_offline (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50),
    jumlah_transaksi DECIMAL(10, 2)
);

CREATE TABLE produk (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_produk VARCHAR(50),
    harga DECIMAL(10, 2),
    stok INT
);

INSERT INTO produk (nama_produk, harga, stok)
VALUES
('Laptop', 15000000, 20),
('Smartphone', 8000000, 50),
('Tablet', 5000000, 30),
('Headset', 250000, 100),
('Charger', 150000, 200);


INSERT INTO pelanggan_offline (nama, jumlah_transaksi)
VALUES
('Foxtrot', 3000000),
('Golf', 2200000),
('Hotel', 1900000),
('India', 2700000),
('Juliet', 2500000);


INSERT INTO pelanggan_online (nama, jumlah_transaksi)
VALUES
('Alfa', 1500000),
('Beta', 2000000),
('Charlie', 2500000),
('Delta', 1800000),
('Echo', 1700000);


INSERT INTO karyawan_kontrak (nama, gaji)
VALUES
('Feri', 5000000),
('Gita', 5500000),
('Hendra', 6000000),
('Ika', 4500000),
('Joko', 4800000);


INSERT INTO karyawan_tetap (nama, gaji)
VALUES
('Andi', 8000000),
('Budi', 7500000),
('Citra', 9000000),
('Dewi', 8500000),
('Eko', 7000000);

-- UNION

SELECT nama 
FROM karyawan_tetap
UNION
SELECT nama
FROM karyawan_kontrak;

-- UNION ALL

SELECT nama 
FROM karyawan_tetap
UNION ALL
SELECT nama
FROM karyawan_kontrak;

-- SUB QUERIES

SELECT nama, gaji
FROM karyawan_tetap
WHERE gaji > (SELECT AVG(gaji) FROM karyawan_tetap);

SELECT nama_produk, harga
FROM produk
WHERE harga > (SELECT AVG(harga) FROM produk);

SELECT nama, jumlah_transaksi
FROM pelanggan_offline
WHERE jumlah_transaksi > (SELECT MAX(jumlah_transaksi) FROM pelanggan_online);

-- UNION & SUB QUERIES

SELECT nama 
FROM karyawan_tetap
WHERE gaji > (SELECT AVG(gaji) FROM karyawan_tetap)
UNION
SELECT nama
FROM karyawan_kontrak
WHERE gaji > (SELECT AVG(gaji) FROM karyawan_kontrak);









