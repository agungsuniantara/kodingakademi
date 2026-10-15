DROP DATABASE wedding_db;

CREATE DATABASE wedding_db;
USE wedding_db;

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

ALTER TABLE pelanggan ADD COLUMN pekerjaan VARCHAR(50);

ALTER TABLE pelanggan MODIFY COLUMN no_hp VARCHAR(20) NOT NULL;

ALTER TABLE pelanggan DROP COLUMN pekerjaan;

ALTER TABLE vendor RENAME TO vendor_wedding;

ALTER TABLE vendor_wedding RENAME TO vendor;

DROP TABLE pemesanan;
DROP DATABASE wedding_db;

INSERT INTO pelanggan (nama, no_hp, email, kota, tanggal_lahir)
VALUES ('Gede Mahendra', '081234567890', '[EMAIL]', 'Denpasar', '1994-03-12');

INSERT INTO pelanggan (nama, no_hp, email, kota, tanggal_lahir) VALUES
('Putu Ayu Lestari', '081298765432', '[EMAIL]', 'Badung', '1996-07-25'),
('Ni Komang Sari', '081377788899', '[EMAIL]', 'Gianyar', '1998-01-30'),
('I Made Wirawan', '081555123456', '[EMAIL]', 'Denpasar', '1992-11-08'),
('Kadek Dwi Putra', '081666987654', NULL, 'Tabanan', '1995-05-17'),
('Luh Gede Pratiwi', '081777654321', '[EMAIL]', 'Badung', '1997-09-02'),
('Nyoman Adi Saputra', '081888111222', '[EMAIL]', 'Klungkung', '1993-12-21'),
('Wayan Sari Dewi', '081999333444', '[EMAIL]', 'Denpasar', '1999-04-14');

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
(1, 3, 1, '2026-06-14', 180, 'Selesai'),
(2, 2, 2, '2026-07-19', 95, 'Selesai'),
(3, 5, 4, '2026-08-02', 480, 'Konfirmasi'),
(4, 1, 3, '2026-08-16', 45, 'Pending'),
(5, 4, 1, '2026-09-06', 280, 'Konfirmasi'),
(6, 3, 2, '2026-09-20', 210, 'Pending'),
(7, 6, 5, '2026-10-11', 750, 'Konfirmasi'),
(8, 2, 3, '2026-10-25', 100, 'Pending'),
(1, 4, 6, '2026-11-08', 300, 'Pending'),
(3, 3, 2, '2026-11-22', 190, 'Pending');

UPDATE pelanggan
SET kota = 'Tabanan'
WHERE id_pelanggan = 5;

UPDATE pemesanan
SET status = 'Selesai', jumlah_tamu = 50
WHERE id_pemesanan = 4;

UPDATE vendor
SET rating = rating + 0.1
WHERE kategori = 'Katering';

UPDATE pemesanan SET status = 'Selesai';

DELETE FROM pemesanan WHERE id_pemesanan = 9;










