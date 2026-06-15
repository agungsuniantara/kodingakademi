-- Membuat database baru
CREATE DATABASE IF NOT EXISTS toko_online_db;

-- Menggunakan database yang baru dibuat
USE toko_online_db;

-- 1. Tabel pelanggan
CREATE TABLE pelanggan (
    id_pelanggan INT PRIMARY KEY AUTO_INCREMENT,
    nama_pelanggan VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    alamat TEXT,
    tanggal_daftar TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Tabel produk
CREATE TABLE produk (
    id_produk INT PRIMARY KEY AUTO_INCREMENT,
    nama_produk VARCHAR(100) NOT NULL,
    kategori VARCHAR(50),
    harga DECIMAL(10, 2) NOT NULL CHECK (harga >= 0),
    stok INT NOT NULL DEFAULT 0 CHECK (stok >= 0)
);

-- 3. Tabel pesanan
CREATE TABLE pesanan (
    id_pesanan INT PRIMARY KEY AUTO_INCREMENT,
    id_pelanggan INT NOT NULL,
    tanggal_pesanan TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status_pesanan ENUM('Menunggu Pembayaran', 'Diproses', 'Dikirim', 'Selesai', 'Dibatalkan') DEFAULT 'Menunggu Pembayaran',
    total_harga DECIMAL(12, 2) DEFAULT 0.00,
    FOREIGN KEY (id_pelanggan) REFERENCES pelanggan(id_pelanggan)
);

-- 4. Tabel detail_pesanan
CREATE TABLE detail_pesanan (
    id_detail INT PRIMARY KEY AUTO_INCREMENT,
    id_pesanan INT NOT NULL,
    id_produk INT NOT NULL,
    jumlah INT NOT NULL CHECK (jumlah > 0),
    harga_satuan DECIMAL(10, 2) NOT NULL, -- Harga barang saat dipesan
    FOREIGN KEY (id_pesanan) REFERENCES pesanan(id_pesanan),
    FOREIGN KEY (id_produk) REFERENCES produk(id_produk)
);

-- --- Isi Data Contoh ---

-- Data untuk tabel pelanggan
INSERT INTO pelanggan (nama_pelanggan, email, alamat) VALUES
('Budi Santoso', 'budi.s@example.com', 'Jl. Merdeka No. 10, Jakarta'),
('Siti Aminah', 'siti.a@example.com', 'Jl. Pahlawan No. 5, Surabaya'),
('Agus Wijaya', 'agus.w@example.com', 'Jl. Sudirman No. 25, Bandung'),
('Dewi Lestari', 'dewi.l@example.com', 'Jl. Gatot Subroto No. 15, Yogyakarta');

-- Data untuk tabel produk
INSERT INTO produk (nama_produk, kategori, harga, stok) VALUES
('Laptop ABC Model X', 'Elektronik', 12000000.00, 15),
('Smartphone XYZ Pro', 'Elektronik', 8500000.00, 30),
('Buku Sejarah Indonesia', 'Buku', 75000.00, 50),
('Meja Belajar Minimalis', 'Furnitur', 1500000.00, 10),
('Keyboard Mekanik RGB', 'Aksesoris Komputer', 750000.00, 25);

-- Data untuk tabel pesanan
-- Pesanan 1: Budi Santoso
INSERT INTO pesanan (id_pelanggan, status_pesanan, total_harga) VALUES
(1, 'Selesai', 12750000.00);
-- Detail Pesanan 1 (untuk Pesanan ID 1)
INSERT INTO detail_pesanan (id_pesanan, id_produk, jumlah, harga_satuan) VALUES
(1, 1, 1, 12000000.00), -- Laptop ABC Model X
(1, 3, 10, 7500.00);    -- Buku Sejarah Indonesia (harga satuan disesuaikan jika ada promo)

-- Pesanan 2: Siti Aminah
INSERT INTO pesanan (id_pelanggan, status_pesanan, total_harga) VALUES
(2, 'Dikirim', 8500000.00);
-- Detail Pesanan 2 (untuk Pesanan ID 2)
INSERT INTO detail_pesanan (id_pesanan, id_produk, jumlah, harga_satuan) VALUES
(2, 2, 1, 8500000.00); -- Smartphone XYZ Pro

-- Pesanan 3: Budi Santoso
INSERT INTO pesanan (id_pelanggan, status_pesanan, total_harga) VALUES
(1, 'Diproses', 750000.00);
-- Detail Pesanan 3 (untuk Pesanan ID 3)
INSERT INTO detail_pesanan (id_pesanan, id_produk, jumlah, harga_satuan) VALUES
(3, 5, 1, 750000.00); -- Keyboard Mekanik RGB

-- Pesanan 4: Agus Wijaya
INSERT INTO pesanan (id_pelanggan, status_pesanan, total_harga) VALUES
(3, 'Menunggu Pembayaran', 1500000.00);
-- Detail Pesanan 4 (untuk Pesanan ID 4)
INSERT INTO detail_pesanan (id_pesanan, id_produk, jumlah, harga_satuan) VALUES
(4, 4, 1, 1500000.00); -- Meja Belajar Minimalis

-- Pesanan 5: Siti Aminah (Pesanan yang akan dibatalkan)
INSERT INTO pesanan (id_pelanggan, status_pesanan, total_harga) VALUES
(2, 'Dibatalkan', 0.00);
-- Detail Pesanan 5 (untuk Pesanan ID 5) - Kosong karena dibatalkan sebelum ada barang

-- Pesanan 6: Dewi Lestari (akan diproses)
INSERT INTO pesanan (id_pelanggan, status_pesanan, total_harga) VALUES
(4, 'Diproses', 1650000.00);
-- Detail Pesanan 6 (untuk Pesanan ID 6)
INSERT INTO detail_pesanan (id_pesanan, id_produk, jumlah, harga_satuan) VALUES
(6, 3, 2, 75000.00); -- Buku Sejarah Indonesia
INSERT INTO detail_pesanan (id_pesanan, id_produk, jumlah, harga_satuan) VALUES
(6, 5, 1, 750000.00); -- Keyboard Mekanik RGB

-- jawaban

