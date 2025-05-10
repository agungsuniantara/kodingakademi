CREATE DATABASE megastore;
USE megastore;

-- Tabel Produk
CREATE TABLE Produk (
    id_produk INT PRIMARY KEY AUTO_INCREMENT,
    nama_produk VARCHAR(100),
    kategori VARCHAR(50),
    harga DECIMAL(10,2),
    stok INT
);

-- Tabel Pelanggan
CREATE TABLE Pelanggan (
    id_pelanggan INT PRIMARY KEY AUTO_INCREMENT,
    nama_pelanggan VARCHAR(100),
    kontak VARCHAR(50),
    alamat TEXT
);

-- Tabel Pegawai
CREATE TABLE Pegawai (
    id_pegawai INT PRIMARY KEY AUTO_INCREMENT,
    nama_pegawai VARCHAR(100),
    posisi VARCHAR(50)
);

-- Tabel Transaksi
CREATE TABLE Transaksi (
    id_transaksi INT PRIMARY KEY AUTO_INCREMENT,
    id_pelanggan INT,
    id_produk INT,
    id_pegawai INT,
    jumlah INT,
    tanggal DATE,
    FOREIGN KEY (id_pelanggan) REFERENCES Pelanggan(id_pelanggan),
    FOREIGN KEY (id_produk) REFERENCES Produk(id_produk),
    FOREIGN KEY (id_pegawai) REFERENCES Pegawai(id_pegawai)
);

INSERT INTO Produk (id_produk, nama_produk, kategori, harga, stok) VALUES
(1, 'Laptop ASUS', 'Elektronik', 8000000, 10),     -- cocok untuk analisis #2
(2, 'Printer Canon', 'Elektronik', 1500000, 20),   -- stok cukup, tapi harga < 2jt
(3, 'Meja Kantor', 'Furniture', 1200000, 8),
(4, 'Speaker JBL', 'Elektronik', 2500000, 12),     -- cocok untuk analisis #2
(5, 'Kursi Gaming', 'Furniture', 3000000, 5);

INSERT INTO Pelanggan (id_pelanggan, nama_pelanggan, kontak, alamat) VALUES
(1, 'Siti Aminah', '081234567890', 'Jakarta'),    -- cocok untuk analisis #3 & #5
(2, 'Budi Santoso', '081212121212', 'Denpasar'),
(3, 'Andi Wijaya', '082298765432', 'Surabaya'),   -- cocok untuk LIKE '%ja%'
(4, 'Rahma Putri', '085612345678', 'Bandung'),
(5, 'Agus Salim', '081888888888', 'Yogyakarta');  -- cocok untuk LIKE '%ja%'

INSERT INTO Pegawai (id_pegawai, nama_pegawai, posisi) VALUES
(1, 'Dewi Lestari', 'Kasir'),
(2, 'Rizky Pratama', 'Sales'),
(3, 'Intan Ayu', 'Sales'),       -- cocok untuk analisis #5
(4, 'Wahyu Hadi', 'Admin');

INSERT INTO Transaksi (id_transaksi, id_pelanggan, id_produk, id_pegawai, jumlah, tanggal) VALUES
(1, 1, 1, 2, 1, '2025-04-01'),   -- transaksi oleh "Siti", cocok untuk analisis #5
(2, 3, 4, 1, 2, '2025-04-02'),   -- pelanggan dari "Surabaya", cocok untuk analisis #3
(3, 5, 1, 3, 1, '2025-04-03'),   -- pegawai "Intan Ayu", cocok untuk analisis #5
(4, 2, 3, 4, 3, '2025-05-01'),   -- di luar bulan April, jumlah > 1 → analisis #4
(5, 4, 5, 1, 2, '2025-03-15'),   -- di luar April, jumlah > 1 → analisis #4
(6, 1, 4, 3, 1, '2025-04-10');   -- Siti beli speaker, cocok juga untuk analisis tambahan

-- Tampilkan semua transaksi yang terjadi antara tanggal 2025-04-01 dan 2025-04-03, 
-- dan jumlah pembelian lebih dari 1.

SELECT * FROM Transaksi
WHERE tanggal BETWEEN '2025-04-01' AND '2025-04-03'
AND jumlah > 1;

-- Tampilkan semua produk dari kategori 'Elektronik' 
-- yang stok-nya di bawah 15 dan harga di atas 2.000.000

SELECT * FROM Produk
WHERE kategori = 'Elektronik'
AND stok < 15
AND harga > 2000000;

-- Tampilkan pelanggan yang berasal dari kota yang mengandung kata "ja".
SELECT * FROM Pelanggan
WHERE alamat LIKE '%ja%';

-- Tampilkan semua pelanggan yang pernah melakukan transaksi
SELECT nama_pelanggan
FROM Pelanggan p
WHERE EXISTS (
  SELECT * FROM Transaksi t
  WHERE t.id_pelanggan = p.id_pelanggan
);



