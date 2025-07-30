-- GROUP BY
-- GROUP BY digunakan untuk mengelompokkan baris data berdasarkan nilai pada satu atau beberapa kolom, 
-- sehingga Aggregate Functions bisa dihitung untuk setiap kelompok.

-- HAVING
-- HAVING adalah klausa yang digunakan untuk memfilter hasil agregat setelah proses GROUP BY.
-- HAVING digunakan jika ingin memfilter berdasarkan hasil fungsi agregat.

-- Perbedaan HAVING dan WHERE:
-- WHERE: memfilter sebelum proses pengelompokan/aggregasi
-- HAVING: memfilter setelah pengelompokan/aggregasi (GROUP BY)

-- DATABASE

CREATE DATABASE toko_modern;
USE toko_modern;

CREATE TABLE produk (
    id_produk INT PRIMARY KEY AUTO_INCREMENT,
    nama_produk VARCHAR(50),
    kategori VARCHAR(30),
    harga INT
);

CREATE TABLE penjualan (
    id_penjualan INT PRIMARY KEY AUTO_INCREMENT,
    id_produk INT,
    jumlah INT,
    total_harga INT,
    tanggal DATE,
    FOREIGN KEY (id_produk) REFERENCES produk(id_produk)
);

-- INSERT DATA 

INSERT INTO produk (nama_produk, kategori, harga) VALUES
('Laptop', 'Elektronik', 8000000),
('Mouse', 'Elektronik', 150000),
('Buku Tulis', 'ATK', 5000),
('Pulpen', 'ATK', 3000),
('Monitor', 'Elektronik', 2000000),
('Printer', 'Elektronik', 1200000),
('Penggaris', 'ATK', 7000);

INSERT INTO penjualan (id_produk, jumlah, total_harga, tanggal) VALUES
(1, 2, 16000000, '2024-06-01'),
(2, 5, 750000, '2024-06-01'),
(3, 10, 50000, '2024-06-01'),
(4, 8, 24000, '2024-06-01'),
(5, 1, 2000000, '2024-06-01'),
(6, 2, 2400000, '2024-06-02'),
(3, 7, 35000, '2024-06-02'),
(2, 3, 450000, '2024-06-02'),
(4, 12, 36000, '2024-06-02'),
(1, 1, 8000000, '2024-06-03'),
(5, 2, 4000000, '2024-06-03');

SELECT * FROM penjualan;

-- GROUP BY

-- menampilkan jumlah barang per kategori
SELECT kategori, COUNT(*) AS jumlah_barang
FROM produk
GROUP BY kategori;

-- menampilkan jumlah barang terjual per tanggal
SELECT tanggal, SUM(jumlah) AS total_barang_terjual
FROM penjualan
GROUP BY tanggal;

-- menampilkan banyak data dan jumlah terjual per id produk
SELECT id_produk, COUNT(*) AS Banyak_data, SUM(jumlah) AS Terjual
FROM penjualan 
GROUP BY id_produk;


-- HAVING

SELECT id_produk, SUM(total_harga) AS total_penjualan
FROM penjualan
GROUP BY id_produk
HAVING total_penjualan > 500000;

-- Perbedaan HAVING & WHERE

SELECT id_produk, SUM(total_harga) AS total_penjualan
FROM penjualan
WHERE tanggal >= '2024-06-02'
GROUP BY id_produk;

SELECT id_produk, SUM(total_harga) AS total_penjualan
FROM penjualan
WHERE tanggal >= '2024-06-02'
GROUP BY id_produk
HAVING total_penjualan > 500000;


-- GROUP BY JOIN

-- menampilkan total penjualan berdasarkan nama produk
SELECT produk.nama_produk, SUM(penjualan.total_harga) AS total_penjualan
FROM penjualan 
INNER JOIN produk ON penjualan.id_produk = produk.id_produk
GROUP BY produk.nama_produk;

-- Jumlah barang terjual per kategori per tanggal ( multi kolom group by )
SELECT produk.kategori, penjualan.tanggal, SUM(penjualan.jumlah) AS total_terjual
FROM penjualan
INNER JOIN produk ON penjualan.id_produk = produk.id_produk
GROUP BY produk.kategori, penjualan.tanggal;

-- Menampilkan rata-rata dan total harga jual per produk
SELECT produk.nama_produk, AVG(penjualan.total_harga) AS rata_rata, MAX(penjualan.total_harga) AS harga_tertinggi
FROM penjualan 
INNER JOIN produk ON penjualan.id_produk = produk.id_produk
GROUP BY produk.nama_produk;


-- GROUP BY JOIN & HAVING

SELECT produk.nama_produk, SUM(penjualan.total_harga) AS total_penjualan
FROM penjualan 
INNER JOIN produk ON penjualan.id_produk = produk.id_produk
GROUP BY produk.nama_produk
HAVING total_penjualan > 3000000;







