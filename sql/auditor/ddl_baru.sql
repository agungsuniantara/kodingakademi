-- ==========================================
-- 1. CREATE ( DDL )
-- ==========================================

CREATE DATABASE perpustakaan;

CREATE TABLE buku(
    id_buku SERIAL PRIMARY KEY,   -- SERIAL = Angka urut otomatis (Auto-Increment)
    judul VARCHAR(100),
    pengarang VARCHAR(50),
    tahun_terbit INT
);

-- ==========================================
-- 2. ALTER ( DDL )
-- ==========================================

-- ADD ( Menambah kolom baru )
ALTER TABLE buku
ADD COLUMN harga NUMERIC(10, 2),
ADD COLUMN kategori VARCHAR(30);

-- RENAME ( Mengganti nama kolom )
ALTER TABLE buku
RENAME COLUMN pengarang TO penulis;

-- ALTER COLUMN TYPE ( Mengubah tipe data )
-- Mengubah tahun_terbit dari tipe angka (INT) menjadi teks (VARCHAR)
ALTER TABLE buku
ALTER COLUMN tahun_terbit TYPE VARCHAR(4);

-- DROP COLUMN ( Menghapus kolom spesifik )
ALTER TABLE buku
DROP COLUMN harga;

-- ==========================================
-- 3. MENGELOLA ISI DATA ( DML )
-- ==========================================

-- INSERT ( Menambah baris data baru ke dalam tabel )
INSERT INTO buku (judul, penulis, tahun_terbit, kategori)
VALUES 
    ('Laskar Pelangi', 'Andrea Hirata', '2005', 'Fiksi'),
    ('Bumi Manusia', 'Pramoedya A. Toer', '1980', 'Sejarah'),
    ('Filosofi Teras', 'Henry Manampiring', '2018', 'Self-Improvement');

-- DELETE ( Menghapus baris data / row spesifik )
-- Perhatian: Selalu gunakan klausa WHERE agar tidak menghapus seluruh data!
DELETE FROM buku
WHERE judul = 'Bumi Manusia';

-- ==========================================
-- 4. TRUNCATE & DROP ( DDL )
-- ==========================================

-- TRUNCATE ( Menghapus / mengosongkan SEMUA baris data, tapi struktur tabelnya tetap utuh )
TRUNCATE TABLE buku;

-- DROP TABLE ( Menghancurkan tabel secara permanen beserta strukturnya )
DROP TABLE buku;

-- DROP DATABASE ( Menghapus database secara permanen )
-- Catatan: Di PostgreSQL, Anda tidak bisa melakukan DROP DATABASE 
-- jika sedang terhubung ke dalamnya. Pindah ke database lain dulu (misal: postgres).
DROP DATABASE perpustakaan;