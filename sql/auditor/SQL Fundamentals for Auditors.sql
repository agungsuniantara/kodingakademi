CREATE TABLE tabel_karyawan_1000 (
    employee_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    role VARCHAR(20),
    approval_limit NUMERIC
);

CREATE TABLE tabel_transaksi_1000 (
    transaction_id VARCHAR(10) PRIMARY KEY,
    vendor_id VARCHAR(10),
    amount NUMERIC,
    transaction_date TIMESTAMP,
    created_by VARCHAR(10),
    status VARCHAR(20)
);

CREATE TABLE tabel_persetujuan_1000 (
    log_id VARCHAR(10) PRIMARY KEY,
    transaction_id VARCHAR(10),
    approved_by VARCHAR(10),
    approval_date TIMESTAMP
);

SELECT 
    transaction_id AS nomor_transaksi,
    transaction_date AS waktu_kejadian,
    amount AS nilai_transaksi
FROM tabel_transaksi_1000;

SELECT 
    transaction_id,
    vendor_id,
    amount
FROM tabel_transaksi_1000
WHERE amount >= 50000000;

SELECT 
    transaction_id,
    vendor_id,
    amount,
    created_by
FROM tabel_transaksi_1000
WHERE amount > 10000000 
  AND vendor_id IN ('VND80', 'VND50');

SELECT 
    employee_id,
    name,
    department
FROM tabel_karyawan_1000
WHERE employee_id LIKE 'EMP%'
  AND role = 'Manager';

SELECT 
    transaction_id,
    vendor_id,
    amount,
    transaction_date
FROM tabel_transaksi_1000
ORDER BY amount DESC
LIMIT 5;

SELECT 
    COUNT(*) AS total_jumlah_transaksi,
    SUM(amount) AS total_uang_keluar,
    AVG(amount) AS rata_rata_nilai_transaksi,
    MAX(amount) AS transaksi_terbesar,
    MIN(amount) AS transaksi_terkecil
FROM tabel_transaksi_1000;

SELECT 
    COUNT(*) AS jumlah_transaksi_berisiko,
    SUM(amount) AS total_nilai_berisiko
FROM tabel_transaksi_1000
WHERE amount > 50000000;

SELECT 
    COUNT(*) AS frekuensi_transaksi_vendor,
    SUM(amount) AS total_pembayaran_vendor
FROM tabel_transaksi_1000
WHERE vendor_id = 'VND80'
  AND transaction_date >= '2023-01-01' 
  AND transaction_date <= '2023-12-31';

SELECT 
    -- Menghitung total baris semua data
    COUNT(*) AS total_seluruh_log,
    -- Hanya menghitung baris yang nilai 'approved_by' tidak kosong
    COUNT(approved_by) AS total_log_dengan_penyetuju
FROM tabel_persetujuan_1000;

SELECT 
    t.transaction_id,
    t.amount,
    t.created_by AS id_pembuat,
    k.name AS nama_pembuat,
    k.department AS departemen_pembuat
FROM tabel_transaksi_1000 t
INNER JOIN tabel_karyawan_1000 k 
    ON t.created_by = k.employee_id;

SELECT 
    t.transaction_id,
    t.amount,
    t.status,
    p.log_id,
    p.approval_date
FROM tabel_transaksi_1000 t
LEFT JOIN tabel_persetujuan_1000 p 
    ON t.transaction_id = p.transaction_id
WHERE t.status = 'Approved' 
  AND p.log_id IS NULL;

SELECT 
    t.transaction_id,
    t.amount AS nominal_pengeluaran,
    p.approval_date,
    k.name AS nama_penyetuju,
    k.role AS jabatan_penyetuju,
    k.approval_limit AS batas_wewenang_maksimal
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p 
    ON t.transaction_id = p.transaction_id
INNER JOIN tabel_karyawan_1000 k 
    ON p.approved_by = k.employee_id
WHERE t.amount > k.approval_limit;

-- MINI CAPSTONE ( MATERI ) 
SELECT 
    t.transaction_id, 
    t.transaction_date, 
    t.amount, 
    k.name AS nama_penyetuju
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p 
    ON t.transaction_id = p.transaction_id
INNER JOIN tabel_karyawan_1000 k 
    ON p.approved_by = k.employee_id
WHERE t.amount > 30000000 
  AND k.role = 'Manager'
ORDER BY t.transaction_date DESC;
