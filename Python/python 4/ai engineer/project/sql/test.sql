CREATE DATABASE wedding_db;
USE wedding_db;

CREATE TABLE pelanggan (
    id_pelanggan INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    no_hp VARCHAR(15) UNIQUE,
    email VARCHAR(100),
    kota VARCHAR(50) DEFAULT 'Denpasar',
    tanggal_daftar DATE
);

CREATE TABLE vendor (
    id_vendor INT AUTO_INCREMENT PRIMARY KEY,
    nama_vendor VARCHAR(100) NOT NULL,
    jenis_vendor ENUM('venue', 'katering', 'foto', 'dekorasi', 'hiburan') NOT NULL,
    kota VARCHAR(50) DEFAULT 'Denpasar',
    kontak VARCHAR(15)
);

CREATE TABLE paket (
    id_paket INT AUTO_INCREMENT PRIMARY KEY,
    id_vendor INT NOT NULL,
    nama_paket VARCHAR(100) NOT NULL,
    harga DECIMAL(12,2) NOT NULL,
    deskripsi TEXT,
    FOREIGN KEY (id_vendor) REFERENCES vendor(id_vendor)
);

