SELECT 
	transaction_id AS nomor_transaksi,
	transaction_date AS waktu_transaksi,
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
WHERE amount > 1000000 AND amount < 10000000
ORDER BY amount DESC
LIMIT 5;

SELECT
	COUNT(*) AS total_jumlah_transaksi,
	SUM(amount) AS total_uang_keluar,
	ROUND(AVG(amount), 2) AS rata_rata_nilai_transaksi,
	MAX(amount) AS transaksi_terbesar,
	MIN(amount) AS transaksi_terkecil
FROM tabel_transaksi_1000;

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
	p.approved_by,
	p.log_id,
	p.approval_date
FROM tabel_transaksi_1000 t
LEFT JOIN tabel_persetujuan_1000 p
	ON t.transaction_id = p.transaction_id
WHERE t.status = 'Approved'
AND p.log_id IS NULL;

-- ASSIGNMENT

-- NO 1
SELECT 
    employee_id, 
    name, 
    department, 
    approval_limit
FROM tabel_karyawan_1000
WHERE role = 'Staff' AND department = 'Marketing';

-- NO 2
SELECT 
    transaction_id, 
    vendor_id, 
    amount
FROM tabel_transaksi_1000
WHERE amount < 2000000 OR vendor_id = 'VND12';

-- NO 3
SELECT 
    SUM(amount) AS total_pengeluaran,
    AVG(amount) AS rata_rata,
    MAX(amount) AS tertinggi
FROM tabel_transaksi_1000;

-- NO 4
SELECT 
    name, 
    department
FROM tabel_karyawan_1000
WHERE employee_id LIKE '%9' AND approval_limit > 10000000;

-- NO 5
SELECT 
    t.transaction_id, 
    t.amount,
	P.log_id
FROM tabel_transaksi_1000 t
LEFT JOIN tabel_persetujuan_1000 p 
  ON t.transaction_id = p.transaction_id
WHERE t.status = 'Approved' 
  AND p.log_id IS NULL;

-- NO 6
SELECT 
    t.transaction_id, 
    t.amount, 
    k.name
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p 
   ON t.transaction_id = p.transaction_id
INNER JOIN tabel_karyawan_1000 k 
   ON p.approved_by = k.employee_id
WHERE t.amount > 80000000 
  AND k.role = 'Manager'
ORDER BY t.amount DESC
LIMIT 5;











