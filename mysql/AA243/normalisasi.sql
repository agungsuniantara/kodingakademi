-- Active: 1772784578144@@127.0.0.1@3306@normalisasi_db

-- Tahap 0: UNF (Unnormalized Form / Data Mentah)
-- Ciri utamanya adalah ada kolom yang berisi banyak nilai sekaligus (Multivalue), 
-- misalnya daftar barang yang dibeli digabung dalam satu kolom menggunakan koma.
-- Tahap 1: 1NF (First Normal Form / Bentuk Normal Pertama)
-- Setiap kolom harus Atomik (hanya boleh berisi satu nilai tunggal). Tidak boleh ada koma-komaan atau array dalam satu sel.
-- Tahap 2: 2NF (Second Normal Form / Bentuk Normal Kedua)
-- Setiap kolom yang tidak merupakan bagian dari primary key harus bergantung penuh pada primary key.
-- Tahap 3: 3NF (Third Normal Form / Bentuk Normal Ketiga)
-- Tidak ada transitive dependency (kolom tidak boleh bergantung pada kolom lain yang bukan primary key).

-- Tahap 0: UNF (Unnormalized Form / Data Mentah)
-- Data mentah biasanya berasal dari catatan manual atau spreadsheet sederhana. 
-- Ciri utamanya adalah ada kolom yang berisi banyak nilai sekaligus (Multivalue), 
-- misalnya daftar barang yang dibeli digabung dalam satu kolom menggunakan koma.

CREATE TABLE nf0_penjualan_mentah (
    no_invoice VARCHAR(10),
    tanggal DATE,
    id_pelanggan VARCHAR(10),
    nama_pelanggan VARCHAR(50),
    kota_pelanggan VARCHAR(50),
    daftar_barang_dibeli VARCHAR(200)
);

INSERT INTO nf0_penjualan_mentah VALUES 
('INV-101', '2026-04-01', 'CUST-01', 'Budi Santoso', 'Dalung', 'BRG-1 (Mouse, 2x, 150000), BRG-2 (Keyboard, 1x, 300000)'),
('INV-102', '2026-04-02', 'CUST-02', 'Ayu Lestari', 'Denpasar', 'BRG-1 (Mouse, 1x, 150000)');

SELECT * FROM nf0_penjualan_mentah;

-- Masalah: Sangat sulit menggunakan fungsi SUM() atau JOIN karena data barang menyatu dengan teks lain.

-- Tahap 1: 1NF (First Normal Form / Bentuk Normal Pertama)
-- Aturan Utama 1NF: Setiap kolom harus Atomik (hanya boleh berisi satu nilai tunggal). 
-- Tidak boleh ada koma-komaan atau array dalam satu sel.
-- Solusi: Kita pecah kolom daftar_barang_dibeli menjadi baris-baris baru.

CREATE TABLE nf1_penjualan (
    no_invoice VARCHAR(10),
    tanggal DATE,
    id_pelanggan VARCHAR(10),
    nama_pelanggan VARCHAR(50),
    kota_pelanggan VARCHAR(50),
    kode_barang VARCHAR(10),
    nama_barang VARCHAR(50),
    harga INT,
    qty INT
);

-- Perhatikan: INV-101 sekarang menjadi dua baris
INSERT INTO nf1_penjualan VALUES 
('INV-101', '2026-04-01', 'CUST-01', 'Budi Santoso', 'Dalung', 'BRG-1', 'Mouse', 150000, 2),
('INV-101', '2026-04-01', 'CUST-01', 'Budi Santoso', 'Dalung', 'BRG-2', 'Keyboard', 300000, 1),
('INV-102', '2026-04-02', 'CUST-02', 'Ayu Lestari', 'Denpasar', 'BRG-1', 'Mouse', 150000, 1);

SELECT * FROM nf1_penjualan;

-- Masalah di 1NF: Data nama_pelanggan, kota, dan tanggal ditulis berulang-ulang untuk INV-101. 
-- Ini memboroskan ruang penyimpanan (Redundansi).

-- Tahap 2: 2NF (Second Normal Form / Bentuk Normal Kedua)
-- Aturan Utama 2NF: Sudah memenuhi 1NF, dan TIDAK ADA Ketergantungan Parsial.
-- Penjelasan: Di tabel 1NF, Primary Key-nya adalah gabungan (no_invoice, kode_barang). 
-- Namun, nama_barang dan harga hanya bergantung pada kode_barang, bukan no_invoice. 
-- Begitu juga data pelanggan yang hanya bergantung pada no_invoice.
-- Solusi: Pecah menjadi 3 tabel (Tabel Transaksi, Tabel Barang, Tabel Detail).

-- 1. Tabel Invoice (Transaksi Utama)
CREATE TABLE nf2_invoice (
    no_invoice VARCHAR(10) PRIMARY KEY,
    tanggal DATE,
    id_pelanggan VARCHAR(10),
    nama_pelanggan VARCHAR(50),
    kota_pelanggan VARCHAR(50)
);

INSERT INTO nf2_invoice VALUES 
('INV-101', '2026-04-01', 'CUST-01', 'Budi Santoso', 'Dalung'),
('INV-102', '2026-04-02', 'CUST-02', 'Ayu Lestari', 'Denpasar');

-- 2. Tabel Master Barang
CREATE TABLE nf2_barang (
    kode_barang VARCHAR(10) PRIMARY KEY,
    nama_barang VARCHAR(50),
    harga INT
);

INSERT INTO nf2_barang VALUES 
('BRG-1', 'Mouse', 150000),
('BRG-2', 'Keyboard', 300000);

-- 3. Tabel Detail Invoice (Junction Table)
CREATE TABLE nf2_detail_invoice (
    no_invoice VARCHAR(10),
    kode_barang VARCHAR(10),
    qty INT,
    FOREIGN KEY (no_invoice) REFERENCES nf2_invoice(no_invoice),
    FOREIGN KEY (kode_barang) REFERENCES nf2_barang(kode_barang)
);

INSERT INTO nf2_detail_invoice VALUES 
('INV-101', 'BRG-1', 2),
('INV-101', 'BRG-2', 1),
('INV-102', 'BRG-1', 1);

SELECT * FROM nf2_invoice;
SELECT * FROM nf2_barang;
SELECT * FROM nf2_detail_invoice;

-- Tahap 3: 3NF (Third Normal Form / Bentuk Normal Ketiga)
-- Aturan Utama 3NF: Sudah memenuhi 2NF, dan TIDAK ADA Ketergantungan Transitif.
-- Penjelasan: Kolom biasa tidak boleh bergantung pada kolom biasa lainnya. 
-- Semua kolom harus murni bergantung langsung ke Primary Key tabel tersebut.
-- Solusi: Keluarkan data Pelanggan dari tabel Invoice.

-- 1. Master Pelanggan
CREATE TABLE nf3_pelanggan (
    id_pelanggan VARCHAR(10) PRIMARY KEY,
    nama_pelanggan VARCHAR(50),
    kota_pelanggan VARCHAR(50)
);

INSERT INTO nf3_pelanggan VALUES 
('CUST-01', 'Budi Santoso', 'Dalung'),
('CUST-02', 'Ayu Lestari', 'Denpasar');

-- 2. Master Barang (Sama seperti 2NF)
CREATE TABLE nf3_barang (
    kode_barang VARCHAR(10) PRIMARY KEY,
    nama_barang VARCHAR(50),
    harga INT
);

INSERT INTO nf3_barang VALUES 
('BRG-1', 'Mouse', 150000),
('BRG-2', 'Keyboard', 300000);

-- 3. Tabel Invoice (Sekarang sangat bersih, hanya mencatat kapan & siapa)
CREATE TABLE nf3_invoice (
    no_invoice VARCHAR(10) PRIMARY KEY,
    tanggal DATE,
    id_pelanggan VARCHAR(10),
    FOREIGN KEY (id_pelanggan) REFERENCES nf3_pelanggan(id_pelanggan)
);

INSERT INTO nf3_invoice VALUES 
('INV-101', '2026-04-01', 'CUST-01'),
('INV-102', '2026-04-02', 'CUST-02');

-- 4. Tabel Detail Invoice (Sama seperti 2NF)
CREATE TABLE nf3_detail_invoice (
    no_invoice VARCHAR(10),
    kode_barang VARCHAR(10),
    qty INT,
    FOREIGN KEY (no_invoice) REFERENCES nf3_invoice(no_invoice),
    FOREIGN KEY (kode_barang) REFERENCES nf3_barang(kode_barang)
);

INSERT INTO nf3_detail_invoice VALUES 
('INV-101', 'BRG-1', 2),
('INV-101', 'BRG-2', 1),
('INV-102', 'BRG-1', 1);

SELECT * FROM nf3_pelanggan;
SELECT * FROM nf3_barang;
SELECT * FROM nf3_invoice;
SELECT * FROM nf3_detail_invoice;

-- ASSIGNMENT

-- ==========================================
-- SETUP DATABASE
-- ==========================================
CREATE DATABASE perpustakaan_db;
USE perpustakaan_db;


-- ==========================================
-- 0NF (UNF) / DATA MENTAH
-- Kondisi: Terdapat data yang digabung dalam satu kolom (Daftar Buku).
-- ==========================================

CREATE TABLE nf0_peminjaman_mentah (
    no_pinjam VARCHAR(10),
    tgl_pinjam DATE,
    id_anggota VARCHAR(10),
    nama_anggota VARCHAR(50),
    kelas_siswa VARCHAR(20),
    daftar_buku_dipinjam VARCHAR(100), -- KESALAHAN: Multivalue
    pustakawan VARCHAR(50)
);

INSERT INTO nf0_peminjaman_mentah VALUES 
('PJ-001', '2026-05-01', 'A001', 'Rina Melati', '10 IPA 1', 'BK-01 (Laskar Pelangi), BK-02 (Bumi Manusia)', 'Pak Anton'),
('PJ-002', '2026-05-02', 'A002', 'Budi Santoso', '11 IPS 2', 'BK-01 (Laskar Pelangi)', 'Bu Siska'),
('PJ-003', '2026-05-03', 'A001', 'Rina Melati', '10 IPA 1', 'BK-03 (Filosofi Teras)', 'Pak Anton');

-- Cek Data 0NF
SELECT * FROM nf0_peminjaman_mentah;


-- ==========================================
-- 1NF (FIRST NORMAL FORM)
-- Aturan: Tidak boleh ada multivalue. Pecah daftar buku menjadi baris-baris baru.
-- ==========================================

CREATE TABLE nf1_peminjaman (
    no_pinjam VARCHAR(10),
    tgl_pinjam DATE,
    id_anggota VARCHAR(10),
    nama_anggota VARCHAR(50),
    kelas_siswa VARCHAR(20),
    kode_buku VARCHAR(10),
    judul_buku VARCHAR(50),
    nama_pustakawan VARCHAR(50)
);

-- Perhatikan: PJ-001 dipecah menjadi dua baris agar setiap sel hanya berisi satu nilai (Atomic)
INSERT INTO nf1_peminjaman VALUES 
('PJ-001', '2026-05-01', 'A001', 'Rina Melati', '10 IPA 1', 'BK-01', 'Laskar Pelangi', 'Pak Anton'),
('PJ-001', '2026-05-01', 'A001', 'Rina Melati', '10 IPA 1', 'BK-02', 'Bumi Manusia', 'Pak Anton'),
('PJ-002', '2026-05-02', 'A002', 'Budi Santoso', '11 IPS 2', 'BK-01', 'Laskar Pelangi', 'Bu Siska'),
('PJ-003', '2026-05-03', 'A001', 'Rina Melati', '10 IPA 1', 'BK-03', 'Filosofi Teras', 'Pak Anton');

-- Cek Data 1NF
SELECT * FROM nf1_peminjaman;


-- ==========================================
-- 2NF (SECOND NORMAL FORM)
-- Aturan: Hilangkan Ketergantungan Parsial. 
-- Pisahkan data Buku dan data Transaksi ke tabel yang berbeda.
-- ==========================================

-- 1. Tabel Buku
CREATE TABLE nf2_buku (
    kode_buku VARCHAR(10) PRIMARY KEY,
    judul_buku VARCHAR(50)
);

INSERT INTO nf2_buku VALUES 
('BK-01', 'Laskar Pelangi'),
('BK-02', 'Bumi Manusia'),
('BK-03', 'Filosofi Teras');

-- 2. Tabel Peminjaman Induk
CREATE TABLE nf2_peminjaman (
    no_pinjam VARCHAR(10) PRIMARY KEY,
    tgl_pinjam DATE,
    id_anggota VARCHAR(10),
    nama_anggota VARCHAR(50),
    kelas_siswa VARCHAR(20),
    nama_pustakawan VARCHAR(50)
);

INSERT INTO nf2_peminjaman VALUES 
('PJ-001', '2026-05-01', 'A001', 'Rina Melati', '10 IPA 1', 'Pak Anton'),
('PJ-002', '2026-05-02', 'A002', 'Budi Santoso', '11 IPS 2', 'Bu Siska'),
('PJ-003', '2026-05-03', 'A001', 'Rina Melati', '10 IPA 1', 'Pak Anton');

-- 3. Tabel Detail Peminjaman (Junction)
CREATE TABLE nf2_detail_pinjam (
    no_pinjam VARCHAR(10),
    kode_buku VARCHAR(10),
    FOREIGN KEY (no_pinjam) REFERENCES nf2_peminjaman(no_pinjam),
    FOREIGN KEY (kode_buku) REFERENCES nf2_buku(kode_buku)
);

INSERT INTO nf2_detail_pinjam VALUES 
('PJ-001', 'BK-01'),
('PJ-001', 'BK-02'),
('PJ-002', 'BK-01'),
('PJ-003', 'BK-03');


-- ==========================================
-- 3NF (THIRD NORMAL FORM) - HASIL AKHIR
-- Aturan: Hilangkan Ketergantungan Transitif.
-- Data Anggota dan Pustakawan harus dikeluarkan dari tabel Peminjaman.
-- ==========================================

-- 1. Master Anggota
CREATE TABLE nf3_anggota (
    id_anggota VARCHAR(10) PRIMARY KEY,
    nama_anggota VARCHAR(50),
    kelas_siswa VARCHAR(20)
);

INSERT INTO nf3_anggota VALUES 
('A001', 'Rina Melati', '10 IPA 1'),
('A002', 'Budi Santoso', '11 IPS 2');

-- 2. Master Pustakawan (Inisiatif membuat ID Pustakawan)
CREATE TABLE nf3_pustakawan (
    id_pustakawan VARCHAR(10) PRIMARY KEY,
    nama_pustakawan VARCHAR(50)
);

INSERT INTO nf3_pustakawan VALUES 
('P-01', 'Pak Anton'),
('P-02', 'Bu Siska');

-- 3. Master Buku (Sama dengan 2NF)
CREATE TABLE nf3_buku (
    kode_buku VARCHAR(10) PRIMARY KEY,
    judul_buku VARCHAR(50)
);

INSERT INTO nf3_buku VALUES 
('BK-01', 'Laskar Pelangi'),
('BK-02', 'Bumi Manusia'),
('BK-03', 'Filosofi Teras');

-- 4. Tabel Transaksi Peminjaman (Sangat Bersih)
CREATE TABLE nf3_peminjaman (
    no_pinjam VARCHAR(10) PRIMARY KEY,
    tgl_pinjam DATE,
    id_anggota VARCHAR(10),
    id_pustakawan VARCHAR(10),
    FOREIGN KEY (id_anggota) REFERENCES nf3_anggota(id_anggota),
    FOREIGN KEY (id_pustakawan) REFERENCES nf3_pustakawan(id_pustakawan)
);

INSERT INTO nf3_peminjaman VALUES 
('PJ-001', '2026-05-01', 'A001', 'P-01'),
('PJ-002', '2026-05-02', 'A002', 'P-02'),
('PJ-003', '2026-05-03', 'A001', 'P-01');

-- 5. Tabel Detail Peminjaman (Sama dengan 2NF, diarahkan ke tabel 3NF)
CREATE TABLE nf3_detail_pinjam (
    no_pinjam VARCHAR(10),
    kode_buku VARCHAR(10),
    FOREIGN KEY (no_pinjam) REFERENCES nf3_peminjaman(no_pinjam),
    FOREIGN KEY (kode_buku) REFERENCES nf3_buku(kode_buku)
);

INSERT INTO nf3_detail_pinjam VALUES 
('PJ-001', 'BK-01'),
('PJ-001', 'BK-02'),
('PJ-002', 'BK-01'),
('PJ-003', 'BK-03');


-- ==========================================
-- PEMBUKTIAN DENGAN MULTI-JOIN
-- Menampilkan kembali data seperti bentuk aslinya tanpa anomali
-- ==========================================

SELECT 
    p.no_pinjam,
    p.tgl_pinjam,
    a.id_anggota,
    a.nama_anggota,
    a.kelas_siswa,
    b.kode_buku,
    b.judul_buku,
    pt.nama_pustakawan
FROM nf3_peminjaman p
JOIN nf3_anggota a ON p.id_anggota = a.id_anggota
JOIN nf3_pustakawan pt ON p.id_pustakawan = pt.id_pustakawan
JOIN nf3_detail_pinjam dp ON p.no_pinjam = dp.no_pinjam
JOIN nf3_buku b ON dp.kode_buku = b.kode_buku
ORDER BY p.no_pinjam ASC;