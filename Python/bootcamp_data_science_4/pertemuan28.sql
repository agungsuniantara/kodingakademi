CREATE DATABASE wedding_db;
USE wedding_db;

-- buat tabel

CREATE TABLE pelanggan (
    id_pelanggan INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    no_hp VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    kota VARCHAR(50) DEFAULT 'Denpasar',
    tanggal_lahir DATE
);

CREATE TABLE vendor (
    id_vendor INT AUTO_INCREMENT PRIMARY KEY,
    nama_vendor VARCHAR(100) NOT NULL,
    kategori ENUM('Katering', 'Dekorasi', 'Foto', 'MC', 'Musik', 'Venue') NOT NULL,
    kota VARCHAR(50),
    rating DECIMAL(2,1) DEFAULT 4.5
);

CREATE TABLE paket (
    id_paket INT AUTO_INCREMENT PRIMARY KEY,
    nama_paket VARCHAR(100) NOT NULL,
    harga DECIMAL(12,2) NOT NULL,
    durasi_jam INT DEFAULT 8,
    kapasitas_tamu INT DEFAULT 300
);

CREATE TABLE pemesanan (
    id_pemesanan INT AUTO_INCREMENT PRIMARY KEY,
    id_pelanggan INT NOT NULL,
    id_paket INT NOT NULL,
    id_vendor INT NOT NULL,
    tanggal_acara DATE NOT NULL,
    jumlah_tamu INT,
    status ENUM('Pending', 'Konfirmasi', 'Selesai', 'Batal') DEFAULT 'Pending',
    FOREIGN KEY (id_pelanggan) REFERENCES pelanggan(id_pelanggan),
    FOREIGN KEY (id_paket) REFERENCES paket(id_paket),
    FOREIGN KEY (id_vendor) REFERENCES vendor(id_vendor)
);

DESCRIBE pelanggan;

-- edit tabel

ALTER TABLE pelanggan ADD COLUMN pekerjaan VARCHAR(50);

ALTER TABLE pelanggan MODIFY COLUMN no_hp VARCHAR(50) NOT NULL;

ALTER TABLE pelanggan DROP COLUMN pekerjaan;

ALTER TABLE vendor RENAME TO vendor_wedding;
ALTER TABLE vendor_wedding RENAME TO vendor;

-- insert tabel

INSERT INTO pelanggan (nama, no_hp, email, kota, tanggal_lahir)
VALUES ('Gede Mahendra', '081234567890', 'gede@email.com', 'Denpasar', '1994-03-12');

INSERT INTO pelanggan (nama, no_hp, email, kota, tanggal_lahir) VALUES
('Putu Ayu Lestari', '081298765432', 'putu@email.com', 'Badung', '1996-07-25'),
('Ni Komang Sari', '081377788899', 'sari@email.com', 'Gianyar', '1998-01-30'),
('I Made Wirawan', '081555123456', 'made@email.com', 'Denpasar', '1992-11-08'),
('Kadek Dwi Putra', '081666987654', NULL, 'Tabanan', '1995-05-17'),
('Luh Gede Pratiwi', '081777654321', 'luh@email.com', 'Badung', '1997-09-02'),
('Nyoman Adi Saputra', '081888111222', 'nyoman@email.com', 'Klungkung', '1993-12-21'),
('Wayan Sari Dewi', '081999333444', 'wayan@email.com', 'Denpasar', '1999-04-14');

INSERT INTO vendor (nama_vendor, kategori, kota, rating) VALUES
('Bali Boga Catering', 'Katering', 'Denpasar', 4.8),
('Taman Ubud Garden', 'Venue', 'Gianyar', 4.7),
('Lensata Wedding Photography', 'Foto', 'Badung', 4.9),
('Dekorasi Anggrek Bali', 'Dekorasi', 'Denpasar', 4.6),
('MC Agus Production', 'MC', 'Badung', 4.5),
('Gamelan Semar Pegulingan', 'Musik', 'Gianyar', 4.8);

INSERT INTO paket (nama_paket, harga, durasi_jam, kapasitas_tamu) VALUES
('Paket Intim 50', 25000000, 6, 50),
('Paket Sederhana 100', 40000000, 8, 100),
('Paket Keluarga 200', 65000000, 8, 200),
('Paket Premium 300', 95000000, 10, 300),
('Paket Mewah 500', 150000000, 12, 500),
('Paket Eksklusif 800', 250000000, 12, 800);

INSERT INTO pemesanan (id_pelanggan, id_paket, id_vendor, tanggal_acara, jumlah_tamu, status) VALUES
(1,3,1,'2026-06-14',180,'Selesai'),
(2,2,2,'2026-07-19',95,'Selesai'),
(3,5,4,'2026-08-02',480,'Konfirmasi'),
(4,1,3,'2026-08-16',45,'Pending'),
(5,4,1,'2026-09-06',280,'Konfirmasi'),
(6,3,2,'2026-09-20',210,'Pending'),
(7,6,5,'2026-10-11',750,'Konfirmasi'),
(8,2,3,'2026-10-25',100,'Pending'),
(1,4,6,'2026-11-08',300,'Pending'),
(3,3,2,'2026-11-22',190,'Pending');

-- update data

UPDATE pelanggan SET kota = 'Denpasar' WHERE id_pelanggan = 5;

UPDATE pemesanan SET status = 'Selesai', jumlah_tamu = 50 WHERE id_pemesanan = 4;

UPDATE vendor SET rating = rating + 0.1 WHERE kategori = 'Katering';

UPDATE pemesanan SET status = 'Selesai';

-- delete data

DELETE FROM pemesanan WHERE id_pemesanan = 10;

DELETE FROM pelanggan WHERE id_pelanggan = 1;

-- select data

SELECT * FROM pelanggan;

SELECT nama, kota FROM pelanggan;

SELECT nama AS nama_pelanggan, no_hp AS hp FROM pelanggan;

SELECT DISTINCT kota FROM pelanggan;

SELECT nama_paket, harga, harga * 0.9 AS harga_diskon FROM paket;

SELECT nama_paket, harga / kapasitas_tamu AS harga_per_tamu FROM paket;

SELECT nama, kota FROM pelanggan WHERE kota = 'Denpasar';
SELECT nama_paket, harga FROM paket WHERE harga >= 95000000;
SELECT nama, tanggal_lahir FROM pelanggan WHERE tanggal_lahir < '1995-01-01';
SELECT nama, kota FROM pelanggan WHERE kota <> 'Badung';

SELECT nama, kota, tanggal_lahir FROM pelanggan
WHERE kota = 'Denpasar' AND tanggal_lahir > '1995-01-01';

SELECT nama_paket, harga FROM paket
WHERE harga < 40000000 OR kapasitas_tamu > 300;

SELECT nama, kota FROM pelanggan WHERE NOT kota = 'Gianyar';

SELECT nama_vendor, kategori FROM vendor WHERE kategori IN ('Katering', 'Musik');

SELECT nama_paket, harga FROM paket WHERE harga BETWEEN 40000000 AND 100000000;

SELECT nama, tanggal_lahir FROM pelanggan
WHERE tanggal_lahir BETWEEN '1995-01-01' AND '1997-12-31';

SELECT nama FROM pelanggan WHERE nama LIKE 'Luh%';
SELECT nama FROM pelanggan WHERE nama LIKE '%Made%';
SELECT nama FROM pelanggan WHERE nama LIKE '%Dewi%';
SELECT nama FROM pelanggan WHERE nama LIKE '%Lestari';

SELECT nama, email FROM pelanggan WHERE email IS NULL;
SELECT nama, email FROM pelanggan WHERE email IS NOT NULL;

SELECT nama_paket, harga FROM paket ORDER BY harga ASC;
SELECT nama_vendor, rating FROM vendor ORDER BY rating DESC;

SELECT nama_paket, harga FROM paket ORDER BY harga ASC LIMIT 3;
SELECT nama_paket, harga FROM paket ORDER BY harga ASC LIMIT 3 OFFSET 2;

-- agregasi data

SELECT COUNT(*) AS jumlah_pemesanan FROM pemesanan;

SELECT COUNT(DISTINCT kota) AS jumlah_kota FROM pelanggan;

SELECT AVG(jumlah_tamu) AS rata_rata_tamu FROM pemesanan;

SELECT MIN(harga) AS harga_termurah, MAX(harga) AS harga_termahal FROM paket;

-- group by

SELECT status, COUNT(*) AS jumlah FROM pemesanan GROUP BY status;

SELECT kategori, AVG(rating) AS rata_rata_rating FROM vendor GROUP BY kategori;

SELECT kota, COUNT(*) AS jumlah_pelanggan FROM pelanggan GROUP BY kota;

-- having 

SELECT kategori, AVG(rating) AS rata_rata_rating
FROM vendor
GROUP BY kategori
HAVING AVG(rating) > 4.6;

-- join

SELECT p.nama, ps.tanggal_acara, ps.status
FROM pemesanan AS ps
JOIN pelanggan AS p ON ps.id_pelanggan = p.id_pelanggan;

SELECT p.nama, ps.tanggal_acara, ps.status
FROM pemesanan ps
INNER JOIN pelanggan p ON ps.id_pelanggan = p.id_pelanggan;

SELECT p.nama, ps.tanggal_acara
FROM pelanggan AS p
LEFT JOIN pemesanan AS ps ON p.id_pelanggan = ps.id_pelanggan;

SELECT p.nama, ps.tanggal_acara
FROM pelanggan AS p
RIGHT JOIN pemesanan AS ps ON p.id_pelanggan = ps.id_pelanggan;

SELECT ps.id_pemesanan, pl.nama AS nama_pelanggan, v.nama_vendor, pk.nama_paket, ps.tanggal_acara, ps.status
FROM pemesanan AS ps
JOIN pelanggan AS pl ON ps.id_pelanggan = pl.id_pelanggan
JOIN vendor AS v ON ps.id_vendor = v.id_vendor
JOIN paket AS pk ON ps.id_paket = pk.id_paket
ORDER BY ps.tanggal_acara;

SELECT v.nama_vendor, COUNT(*) AS jumlah_pesanan, SUM(pk.harga) AS total_pendapatan
FROM pemesanan ps
JOIN vendor v ON ps.id_vendor = v.id_vendor
JOIN paket pk ON ps.id_paket = pk.id_paket
WHERE ps.status <> 'Batal'
GROUP BY v.id_vendor, v.nama_vendor
ORDER BY total_pendapatan DESC;

-- subquery

SELECT nama_paket, harga FROM paket
WHERE harga > (SELECT AVG(harga) FROM paket);

SELECT id_paket FROM paket ORDER BY harga DESC LIMIT 1;

SELECT id_pelanggan FROM pemesanan WHERE id_paket = 6;

SELECT nama FROM pelanggan WHERE id_pelanggan IN (7);

SELECT nama FROM pelanggan
WHERE id_pelanggan IN (
    SELECT id_pelanggan FROM pemesanan
    WHERE id_paket = (
        SELECT id_paket FROM paket ORDER BY harga DESC LIMIT 1
    )
);














