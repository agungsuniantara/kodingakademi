-- JOIN adalah perintah dalam SQL untuk menggabungkan baris dari dua atau lebih tabel berdasarkan kondisi tertentu. 
-- JOIN sering digunakan untuk mendapatkan data yang tersebar di beberapa tabel yang saling berelasi.

-- Mengapa Perlu JOIN ?
-- Relasi antar tabel adalah dasar dalam desain database relasional. JOIN memungkinkan kita:
-- Menghubungkan data dari tabel berbeda (misal: siswa dan kelas).
-- Mengambil informasi secara komprehensif yang tidak dapat diperoleh hanya dari satu tabel.

-- Tipe-tipe JOIN
-- 1. INNER JOIN: Mengambil data yang match di kedua tabel.
-- 2. LEFT JOIN (atau LEFT OUTER JOIN): Mengambil semua data dari tabel kiri, dan data yang match dari tabel kanan.
-- 3. RIGHT JOIN (atau RIGHT OUTER JOIN): Mengambil semua data dari tabel kanan, dan data yang match dari tabel kiri.
-- 4. FULL JOIN (atau FULL OUTER JOIN): Mengambil semua data dari kedua tabel, 
--    match atau tidak (tidak semua database mendukung FULL JOIN, MySQL butuh UNION).
-- 5. SELF JOIN: JOIN tabel dengan dirinya sendiri, untuk kasus relasi data dalam satu tabel

-- Create database

CREATE DATABASE sekolah_db;
USE sekolah_db;

CREATE TABLE wali_kelas (
    id_wali INT PRIMARY KEY AUTO_INCREMENT,
    nama_wali VARCHAR(50)
);

CREATE TABLE kelas (
    id_kelas INT PRIMARY KEY AUTO_INCREMENT,
    nama_kelas VARCHAR(50),
    id_wali INT,
    FOREIGN KEY (id_wali) REFERENCES wali_kelas(id_wali)
);

CREATE TABLE siswa (
    id_siswa INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(50),
    id_kelas INT,
    FOREIGN KEY (id_kelas) REFERENCES kelas(id_kelas)
);

CREATE TABLE karyawan (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(50),
    id_atasan INT,
    FOREIGN KEY (id_atasan) REFERENCES karyawan(id)
);

-- Insert data wali_kelas
INSERT INTO wali_kelas (nama_wali) VALUES 
('Pak Agus'),   
('Bu Dewi'),  
('Pak Slamet');   

-- Insert data kelas
INSERT INTO kelas (nama_kelas, id_wali) VALUES 
('IPA 1', 1),    
('IPA 2', 2);  

-- Insert data siswa
INSERT INTO siswa (nama, id_kelas) VALUES
('Ani', 1),
('Budi', 1),
('Cici', 2),
(NULL, NULL),  
('Eka', 1);

-- Insert data karyawan
INSERT INTO karyawan (nama, id_atasan) VALUES
('Pak Andi', NULL),      
('Bu Sari', 1),        
('Pak Joko', 1),       
('Bu Rita', 2),         
('Pak Tono', 3);      

-- ========== JOIN ==========

-- INNER JOIN
-- Mengembalikan baris jika ada kecocokan di kedua tabel.

SELECT siswa.nama, kelas.nama_kelas
FROM siswa 
INNER JOIN kelas ON siswa.id_kelas = kelas.id_kelas; 

-- Penjelasan:
-- Hanya menampilkan siswa yang punya data kelas yang match.

-- LEFT JOIN
-- Mengembalikan semua data dari tabel kiri dan data yang match dari tabel kanan. 
-- Jika tidak match, akan bernilai NULL.

SELECT siswa.nama, kelas.nama_kelas
FROM siswa 
LEFT JOIN kelas ON siswa.id_kelas = kelas.id_kelas;

-- Penjelasan:
-- Semua siswa akan ditampilkan, meski tidak ada kelas (nama_kelas = NULL jika tidak ditemukan).

-- RIGHT JOIN
-- Mengembalikan semua data dari tabel kanan, dan data yang match dari tabel kiri. Jika tidak match, akan bernilai NULL.

SELECT siswa.nama, kelas.nama_kelas
FROM siswa
RIGHT JOIN kelas ON siswa.id_kelas = kelas.id_kelas;

-- Penjelasan:
-- Semua kelas akan tampil, meskipun tidak ada siswa yang terdaftar di kelas itu (nama = NULL jika tidak ditemukan).

-- FULL JOIN (FULL OUTER JOIN)
-- Mengembalikan semua data dari kedua tabel, baik match maupun tidak.
-- MySQL secara default tidak punya FULL OUTER JOIN, tapi bisa disimulasikan dengan UNION.

SELECT siswa.nama, kelas.nama_kelas
FROM siswa
LEFT JOIN kelas ON siswa.id_kelas = kelas.id_kelas
UNION
SELECT siswa.nama, kelas.nama_kelas
FROM siswa
RIGHT JOIN kelas ON siswa.id_kelas = kelas.id_kelas;

-- Penjelasan:
-- Semua siswa dan semua kelas muncul, walaupun tidak saling terhubung.

-- SELF JOIN
-- JOIN tabel dengan dirinya sendiri, biasanya digunakan untuk struktur data hierarki (misal: atasan-bawahan di tabel karyawan).

SELECT a.nama AS nama_karyawan, b.nama AS nama_atasan
FROM karyawan a
LEFT JOIN karyawan b ON a.id_atasan = b.id;

-- Penjelasan:
-- Menampilkan nama karyawan beserta nama atasannya (jika ada).



-- ========== MULTI-JOIN DAN KOMBINASI JOIN ==========

-- 1. Multi-Join dengan INNER JOIN dan LEFT JOIN sekaligus
-- Tampilkan semua siswa yang sudah punya kelas (INNER JOIN), beserta wali kelas (LEFT JOIN; wali kelas bisa kosong jika belum ada)

SELECT 
    siswa.nama AS nama_siswa,
    kelas.nama_kelas,
    wali_kelas.nama_wali
FROM siswa
INNER JOIN kelas ON siswa.id_kelas = kelas.id_kelas
LEFT JOIN wali_kelas ON kelas.id_wali = wali_kelas.id_wali;

-- Penjelasan:
-- Hanya siswa yang punya kelas yang tampil.
-- Jika kelas sudah punya wali, nama wali akan muncul. Jika tidak, tetap tampil tapi nama wali NULL.

-- 2. Multi-Join dengan LEFT JOIN bertingkat
-- Tampilkan semua siswa (meskipun belum punya kelas), serta nama kelas dan nama wali kelas jika ada.

SELECT 
    siswa.nama AS nama_siswa,
    kelas.nama_kelas,
    wali_kelas.nama_wali
FROM siswa
LEFT JOIN kelas ON siswa.id_kelas = kelas.id_kelas
LEFT JOIN wali_kelas ON kelas.id_wali = wali_kelas.id_wali;

-- Penjelasan:
-- Semua siswa tetap muncul. Jika tidak ada kelas/wali kelas, kolomnya bernilai NULL.

-- 3. Multi-Join dengan LEFT dan RIGHT JOIN (hati-hati, hasilnya bisa besar/NULL)
-- Tampilkan semua kelas dan wali kelas (meskipun tidak ada siswa), serta nama siswa jika ada.

SELECT 
    siswa.nama AS nama_siswa,
    kelas.nama_kelas,
    wali_kelas.nama_wali
FROM kelas
LEFT JOIN siswa ON siswa.id_kelas = kelas.id_kelas
RIGHT JOIN wali_kelas ON kelas.id_wali = wali_kelas.id_wali;

-- Penjelasan:
-- Semua wali kelas pasti tampil. Jika tidak ada kelas, nama_kelas NULL; jika tidak ada siswa, nama_siswa NULL.

-- Catatan:
-- Kombinasi INNER JOIN, LEFT JOIN, dan RIGHT JOIN sangat umum dipakai pada query real-project,
-- sesuaikan dengan kebutuhan dan relasi antar tabel.

