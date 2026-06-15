-- 1. Tabel Direktori Karyawan
CREATE TABLE tabel_karyawan_1000 (
    employee_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    role VARCHAR(20),
    approval_limit NUMERIC
);

-- 2. Tabel Data Transaksi
CREATE TABLE tabel_transaksi_1000 (
    transaction_id VARCHAR(10) PRIMARY KEY,
    vendor_id VARCHAR(10),
    amount NUMERIC,
    transaction_date TIMESTAMP,
    created_by VARCHAR(10),
    status VARCHAR(20)
);

-- 3. Tabel Log Persetujuan
CREATE TABLE tabel_persetujuan_1000 (
    log_id VARCHAR(10) PRIMARY KEY,
    transaction_id VARCHAR(10),
    approved_by VARCHAR(10),
    approval_date TIMESTAMP
);