-- Pembuatan Kerangka Tabel
CREATE TABLE tabel_transaksi_harian (
    id_transaksi INT PRIMARY KEY,
    id_karyawan VARCHAR(10),
    departemen VARCHAR(20),
    tanggal DATE,
    nominal NUMERIC
);

-- Memasukkan Data Simulasi
INSERT INTO tabel_transaksi_harian (id_transaksi, id_karyawan, departemen, tanggal, nominal) VALUES
(101, 'EMP01', 'Finance', '2024-05-01', 1000000),
(102, 'EMP02', 'Finance', '2024-05-02', 2500000),
(103, 'EMP01', 'Finance', '2024-05-03', 2500000), 
(104, 'EMP03', 'Sales',   '2024-05-01', 5000000),
(105, 'EMP04', 'Sales',   '2024-05-02', 3000000),
(106, 'EMP03', 'Sales',   '2024-05-04', 4000000);

SELECT * FROM tabel_transaksi_harian;

SELECT 
    id_transaksi,
    departemen,
    nominal,
    SUM(nominal) OVER (PARTITION BY departemen) AS total_pengeluaran_departemen
FROM tabel_transaksi_harian;

SELECT 
    id_transaksi,
    departemen,
    tanggal,
    nominal,
    SUM(nominal) OVER (
        PARTITION BY departemen 
        ORDER BY tanggal
    ) AS total_berjalan_departemen
FROM tabel_transaksi_harian;

SELECT 
    departemen,
    id_transaksi,
    nominal,
    ROW_NUMBER() OVER (PARTITION BY departemen ORDER BY nominal DESC) AS nomor_baris,
    RANK() OVER (PARTITION BY departemen ORDER BY nominal DESC) AS peringkat_rank,
    DENSE_RANK() OVER (PARTITION BY departemen ORDER BY nominal DESC) AS peringkat_padat
FROM tabel_transaksi_harian;

SELECT 
    id_karyawan,
    tanggal,
    nominal,
    LAG(nominal, 1) OVER (
        PARTITION BY id_karyawan 
        ORDER BY tanggal
    ) AS nominal_transaksi_sebelumnya,
    nominal - LAG(nominal, 1) OVER (
        PARTITION BY id_karyawan 
        ORDER BY tanggal
    ) AS selisih_dengan_sebelumnya
FROM tabel_transaksi_harian;

SELECT 
    departemen,
    id_transaksi,
    nominal,
    FIRST_VALUE(nominal) OVER (
        PARTITION BY departemen 
        ORDER BY nominal DESC
    ) AS nominal_tertinggi_di_departemen
FROM tabel_transaksi_harian;