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
	log_id VARCHAR(50) PRIMARY KEY,
    transaction_id VARCHAR(50),
    approved_by VARCHAR(50),
    approval_date TIMESTAMP,
    
    -- Membuat Foreign Key ke tabel transaksi
    CONSTRAINT fk_transaksi 
        FOREIGN KEY (transaction_id) 
        REFERENCES tabel_transaksi_1000(transaction_id),
        
    -- Membuat Foreign Key ke tabel karyawan
    CONSTRAINT fk_karyawan 
        FOREIGN KEY (approved_by) 
        REFERENCES tabel_karyawan_1000(employee_id)
);