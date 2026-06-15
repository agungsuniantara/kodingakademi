SELECT 
    transaction_id,
    amount,
    transaction_date,
    EXTRACT(ISODOW FROM transaction_date) AS hari_kejadian,
    EXTRACT(HOUR FROM transaction_date) AS jam_kejadian
FROM tabel_transaksi_1000
WHERE EXTRACT(ISODOW FROM transaction_date) IN (6, 7)
   OR EXTRACT(HOUR FROM transaction_date) < 8
   OR EXTRACT(HOUR FROM transaction_date) >= 17
ORDER BY transaction_date DESC;

SELECT 
    t.transaction_id,
    t.transaction_date AS waktu_pembuatan,
    p.approval_date AS waktu_persetujuan,
    EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) AS selisih_waktu_detik
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p
    ON t.transaction_id = p.transaction_id
WHERE EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) <= 60
  AND EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) > 0
ORDER BY selisih_waktu_detik ASC;

SELECT 
    t.transaction_id,
    t.transaction_date AS waktu_pembuatan,
    p.approval_date AS waktu_persetujuan,
    ROUND(EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date) / (3600 * 24))) AS selisih_hari
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p
    ON t.transaction_id = p.transaction_id
WHERE ROUND(EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date) / (3600 * 24))) > 2;

WITH AnalisisWaktuOperasional AS (
    SELECT 
        t.transaction_id,
        t.amount,
        t.transaction_date,
        p.approval_date,
        EXTRACT(ISODOW FROM t.transaction_date) AS hari_transaksi,
        EXTRACT(HOUR FROM t.transaction_date) AS jam_transaksi,
        EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) AS durasi_persetujuan_detik
    FROM tabel_transaksi_1000 t
    INNER JOIN tabel_persetujuan_1000 p
        ON t.transaction_id = p.transaction_id
)

SELECT 
    transaction_id,
    amount,
    hari_transaksi,
    jam_transaksi,
    durasi_persetujuan_detik
FROM AnalisisWaktuOperasional
WHERE hari_transaksi IN (6, 7)
   OR jam_transaksi < 8
   OR jam_transaksi >= 17
   OR durasi_persetujuan_detik <= 60
ORDER BY amount DESC;

SELECT 
    transaction_id,
    vendor_id,
    amount,
    SUM(amount) OVER (PARTITION BY vendor_id) AS total_pengeluaran_vendor
FROM tabel_transaksi_1000;

SELECT 
    vendor_id, 
    SUM(amount) AS total_pengeluaran_vendor,
	COUNT(transaction_id) AS jumlah_data
FROM tabel_transaksi_1000
WHERE vendor_id IN ('VND12','VND103', 'VND118')
GROUP BY vendor_id
HAVING SUM(amount) > 10000000
ORDER BY total_pengeluaran_vendor DESC;

SELECT 
    t.transaction_id,
    p.approved_by,
    t.amount,
    ROW_NUMBER() OVER (
        PARTITION BY p.approved_by 
        ORDER BY t.amount DESC
    ) AS urutan_transaksi_terbesar
FROM tabel_persetujuan_1000 p
INNER JOIN tabel_transaksi_1000 t 
    ON p.transaction_id = t.transaction_id;

SELECT 
    t.transaction_id, 
    t.amount, 
    t.transaction_date,
    t.created_by AS identitas_pembuat, 
    p.approved_by AS identitas_penyetuju
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p 
    ON t.transaction_id = p.transaction_id
WHERE t.created_by = p.approved_by
ORDER BY t.amount DESC;

SELECT 
    t.transaction_id, 
    t.amount AS nominal_pengeluaran_aktual, 
    p.approved_by AS id_penyetuju, 
    k.role AS tingkat_jabatan, 
    k.approval_limit AS batas_wewenang_resmi
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p 
    ON t.transaction_id = p.transaction_id
INNER JOIN tabel_karyawan_1000 k 
    ON p.approved_by = k.employee_id
WHERE t.amount > k.approval_limit
ORDER BY t.transaction_date DESC;

-- Compliant / Safe Transactions
WITH PemeriksaanKepatuhan AS (
    -- Tahap 1: Mengumpulkan seluruh informasi dan ekstraksi waktu
    SELECT 
        t.transaction_id,
        t.amount,
        t.transaction_date,
        t.created_by,
        p.approved_by,
        p.approval_date,
        k.approval_limit,
        EXTRACT(EPOCH FROM (CAST(p.approval_date AS TIMESTAMP) - CAST(t.transaction_date AS TIMESTAMP))) AS selisih_waktu_detik,
        EXTRACT(ISODOW FROM CAST(t.transaction_date AS TIMESTAMP)) AS indeks_hari,
        EXTRACT(HOUR FROM CAST(t.transaction_date AS TIMESTAMP)) AS jam_kejadian
    FROM tabel_transaksi_1000 t
    INNER JOIN tabel_persetujuan_1000 p 
        ON t.transaction_id = p.transaction_id
    INNER JOIN tabel_karyawan_1000 k 
        ON p.approved_by = k.employee_id
)

-- Tahap 2: Menyingkirkan seluruh anomali dan menampilkan data bersih
SELECT 
    transaction_id,
    amount,
    transaction_date,
    approval_date,
    'Sesuai Prosedur' AS status_kepatuhan
FROM PemeriksaanKepatuhan
WHERE created_by <> approved_by                     -- Lolos Uji Pemisahan Tugas
  AND amount <= approval_limit                      -- Lolos Uji Batas Wewenang
  AND selisih_waktu_detik > 60                      -- Lolos Uji Kewajaran Evaluasi
  AND indeks_hari IN (1, 2, 3, 4, 5)                -- Lolos Uji Hari Kerja
  AND jam_kejadian >= 8 AND jam_kejadian < 17       -- Lolos Uji Jam Operasional
ORDER BY transaction_date DESC;

SELECT
    t.transaction_id,
    t.transaction_date AS waktu_pembuatan,
    p.approval_date AS waktu_persetujuan,
    EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) AS selisih_waktu_detik
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p
    ON t.transaction_id = p.transaction_id
WHERE EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) <= 45
  AND EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) > 0;

-- assignment

-- no 1
SELECT
    transaction_id,
    amount,
    transaction_date,
    EXTRACT(ISODOW FROM transaction_date) AS indeks_hari
FROM tabel_transaksi_1000
WHERE EXTRACT(ISODOW FROM transaction_date) IN (6, 7);

-- no 2
SELECT
    transaction_id,
    amount,
    transaction_date,
    EXTRACT(HOUR FROM transaction_date) AS jam_kejadian
FROM tabel_transaksi_1000
WHERE EXTRACT(HOUR FROM transaction_date) < 6;

-- no 3
SELECT
    t.transaction_id,
    t.amount,
    t.created_by AS identitas_pembuat,
    p.approved_by AS identitas_penyetuju
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p
    ON t.transaction_id = p.transaction_id
WHERE t.created_by = p.approved_by;

-- no 4
SELECT
    t.transaction_id,
    t.transaction_date AS waktu_pembuatan,
    p.approval_date AS waktu_persetujuan,
    EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) AS selisih_waktu_detik
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p
    ON t.transaction_id = p.transaction_id
WHERE EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) <= 45
  AND EXTRACT(EPOCH FROM (p.approval_date - t.transaction_date)) > 0;

-- no 5
SELECT
    t.transaction_id,
    t.amount,
    t.status AS status_dokumen,
    p.log_id AS id_rekam_jejak
FROM tabel_transaksi_1000 t
LEFT JOIN tabel_persetujuan_1000 p
    ON t.transaction_id = p.transaction_id
WHERE t.status = 'Approved'
  AND p.log_id IS NULL;

-- no 6
SELECT
    transaction_id,
    vendor_id,
    amount,
    SUM(amount) OVER (PARTITION BY vendor_id) AS total_pengeluaran_vendor
FROM tabel_transaksi_1000;

-- no 7
WITH PeringkatTransaksi AS (
    SELECT
        t.transaction_id,
        p.approved_by,
        t.amount,
        ROW_NUMBER() OVER (
            PARTITION BY p.approved_by 
            ORDER BY t.amount DESC
        ) AS urutan_transaksi_terbesar
    FROM tabel_transaksi_1000 t
    INNER JOIN tabel_persetujuan_1000 p
        ON t.transaction_id = p.transaction_id
)
SELECT
    transaction_id,
    approved_by,
    amount,
    urutan_transaksi_terbesar
FROM PeringkatTransaksi
WHERE urutan_transaksi_terbesar <= 3;

-- no 8
WITH DeteksiDuplikat AS (
    SELECT
        transaction_id,
        vendor_id,
        amount,
        transaction_date,
        COUNT(*) OVER (PARTITION BY vendor_id, amount) AS jumlah_kemunculan
    FROM tabel_transaksi_1000
)
SELECT
    transaction_id,
    vendor_id,
    amount,
    transaction_date,
    jumlah_kemunculan
FROM DeteksiDuplikat
WHERE jumlah_kemunculan > 1
ORDER BY vendor_id, amount, transaction_date;

-- no 9
SELECT
    t.transaction_id,
    t.amount AS nominal_pengeluaran_aktual,
    p.approved_by AS id_penyetuju,
    k.role AS tingkat_jabatan,
    k.approval_limit AS batas_wewenang_resmi
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p
    ON t.transaction_id = p.transaction_id
INNER JOIN tabel_karyawan_1000 k
    ON p.approved_by = k.employee_id
WHERE t.amount > k.approval_limit;

-- no 10
WITH AkumulasiHarian AS (
    SELECT
        transaction_id,
        created_by,
        vendor_id,
        amount,
        transaction_date,
        SUM(amount) OVER (
            PARTITION BY vendor_id, created_by, CAST(transaction_date AS DATE)
            ORDER BY transaction_date
        ) AS total_harian_ke_vendor
    FROM tabel_transaksi_1000
)
SELECT
    transaction_id,
    created_by,
    vendor_id,
    amount,
    transaction_date,
    total_harian_ke_vendor
FROM AkumulasiHarian
WHERE total_harian_ke_vendor > 50000000;

WITH DeteksiDuplikat AS (
    SELECT 
        transaction_id, 
        vendor_id, 
        amount, 
        transaction_date,
        COUNT(*) OVER (PARTITION BY vendor_id, amount) AS jumlah_kemunculan
    FROM tabel_transaksi_1000
)

SELECT 
    transaction_id, 
    vendor_id, 
    amount, 
    transaction_date,
    jumlah_kemunculan
FROM DeteksiDuplikat
WHERE jumlah_kemunculan > 1
ORDER BY vendor_id, amount, transaction_date;

















