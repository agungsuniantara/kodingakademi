-- Database: kasir_db
CREATE DATABASE IF NOT EXISTS kasir_db;
USE kasir_db;

-- Tabel Barang
CREATE TABLE barang (
    id_barang INT AUTO_INCREMENT PRIMARY KEY,
    nama_barang VARCHAR(255) NOT NULL,
    harga_beli DECIMAL(15,2) NOT NULL,
    harga_jual DECIMAL(15,2) NOT NULL,
    stok INT DEFAULT 0,
    kategori VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabel Transaksi
CREATE TABLE transaksi (
    id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
    tanggal_transaksi DATE NOT NULL,
    total_harga DECIMAL(15,2) NOT NULL,
    diskon DECIMAL(15,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabel Detail Transaksi
CREATE TABLE detail_transaksi (
    id_detail INT AUTO_INCREMENT PRIMARY KEY,
    id_transaksi INT NOT NULL,
    id_barang INT NOT NULL,
    quantity INT NOT NULL,
    harga_satuan DECIMAL(15,2) NOT NULL,
    subtotal DECIMAL(15,2) NOT NULL,
    diskon_item DECIMAL(15,2) DEFAULT 0,
    FOREIGN KEY (id_transaksi) REFERENCES transaksi(id_transaksi) ON DELETE CASCADE,
    FOREIGN KEY (id_barang) REFERENCES barang(id_barang) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO barang (nama_barang, harga_beli, harga_jual, stok, kategori) VALUES
('Nasi Goreng', 8000, 12000, 50, 'Makanan'),
('Es Teh', 2000, 3000, 100, 'Minuman'),
('Ayam Bakar', 15000, 20000, 30, 'Makanan'),
('Jus Jeruk', 3000, 5000, 50, 'Minuman'),
('Gado-gado', 7000, 10000, 25, 'Makanan');