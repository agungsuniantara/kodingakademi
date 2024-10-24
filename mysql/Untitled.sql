-- Membuat database / basis data baru
CREATE DATABASE perpustakaan; 

-- Menggunakan database yang sudah dibuat
USE perpustakaan; 

-- Membuat tabel buku
CREATE TABLE buku (
	id INT PRIMARY KEY AUTO_INCREMENT,
    judul VARCHAR(100),
    penulis VARCHAR(100),
    tahun_terbit DATE
); 

-- Menambahkan kolom baru pada tabel
ALTER TABLE buku ADD penerbit VARCHAR(100);

-- Mengubah tipe data kolom
ALTER TABLE buku MODIFY COLUMN tahun_terbit INT;

-- Membuat tabel anggota
CREATE TABLE anggota (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(100),
    penulis VARCHAR(100),
    umur INT,
    buku_id INT
);

-- Menambahkan foreign key pada tabel anggota kolom buku_id
ALTER TABLE anggota ADD CONSTRAINT fk_buku_id FOREIGN KEY (buku_id) REFERENCES buku(id);

-- Menampilkan isi kolom
DESCRIBE anggota;

-- Menghapus database
DROP DATABASE perpustakaan;

-- Menghapus tabel
DROP TABLE anggota