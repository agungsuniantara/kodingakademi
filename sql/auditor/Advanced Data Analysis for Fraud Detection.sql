-- Session 1: Mastering Date and Time Functions

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

-- Session 2: Introduction to Window Functions

-- GROUPBY
SELECT 
    vendor_id, 
    SUM(amount) AS total_pengeluaran_vendor
FROM tabel_transaksi_1000
GROUP BY vendor_id;

SELECT 
    vendor_id, 
    SUM(amount) AS total_pengeluaran_vendor
FROM tabel_transaksi_1000
GROUP BY vendor_id
HAVING SUM(amount) > 50000000;

SELECT 
    vendor_id, 
    SUM(amount) AS total_pengeluaran_vendor
FROM tabel_transaksi_1000
WHERE vendor_id IN ('VND12','VND103', 'VND118')
GROUP BY vendor_id
HAVING SUM(amount) > 50000000;

SELECT 
    transaction_id,
    vendor_id,
    amount,
    SUM(amount) OVER (PARTITION BY vendor_id) AS total_pengeluaran_vendor
FROM tabel_transaksi_1000;

SELECT 
    transaction_id,
    created_by,
    vendor_id,
    amount,
    transaction_date,
    SUM(amount) OVER (
        PARTITION BY vendor_id, created_by, CAST(transaction_date AS DATE)
        ORDER BY transaction_date
    ) AS total_berjalan_harian
FROM tabel_transaksi_1000;

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
    transaction_id,
    vendor_id,
    transaction_date,
    amount AS nominal_saat_ini,
    LAG(amount, 1) OVER (
        PARTITION BY vendor_id 
        ORDER BY transaction_date
    ) AS nominal_transaksi_sebelumnya
FROM tabel_transaksi_1000
ORDER BY vendor_id, transaction_date;

-- Session 3: Common Table Expressions (CTEs)

-- Tahap 1: Membentuk tabel bayangan yang berisi perhitungan frekuensi transaksi
WITH KalkulasiDuplikat AS (
    SELECT 
        transaction_id, 
        vendor_id, 
        amount, 
        transaction_date,
        -- Menghitung jumlah kejadian untuk kombinasi vendor dan nominal yang sama
        COUNT(*) OVER (PARTITION BY vendor_id, amount) AS frekuensi_kemunculan
    FROM tabel_transaksi_1000
)

-- Tahap 2: Mengekstrak data dari tabel bayangan dengan filter anomali
SELECT 
    transaction_id, 
    vendor_id, 
    amount, 
    transaction_date,
    frekuensi_kemunculan
FROM KalkulasiDuplikat
WHERE frekuensi_kemunculan > 1 -- Menyaring baris yang terindikasi ganda
ORDER BY vendor_id, amount, transaction_date;

WITH KalkulasiDuplikat AS (
    SELECT 
        transaction_id, 
        vendor_id, 
        amount, 
        transaction_date,
        COUNT(*) OVER (PARTITION BY vendor_id, amount) AS frekuensi_kemunculan
    FROM tabel_transaksi_1000
)

SELECT 
    transaction_id, 
    vendor_id, 
    amount, 
    transaction_date,
    frekuensi_kemunculan
FROM KalkulasiDuplikat
WHERE frekuensi_kemunculan > 1 
ORDER BY vendor_id, amount, transaction_date;

-- CTE Tahap 1: Membuang elemen jam/menit agar tanggal bisa diakumulasi secara seragam
WITH EkstraksiTanggal AS (
    SELECT 
        transaction_id,
        created_by,
        vendor_id,
        amount,
        CAST(transaction_date AS DATE) AS tanggal_kejadian
    FROM tabel_transaksi_1000
),

-- CTE Tahap 2: Melakukan akumulasi berjalan pada tanggal yang sudah seragam
KalkulasiAkumulasiHarian AS (
    SELECT 
        transaction_id,
        created_by,
        vendor_id,
        amount,
        tanggal_kejadian,
        SUM(amount) OVER (
            PARTITION BY vendor_id, created_by, tanggal_kejadian
        ) AS total_harian_ke_vendor
    FROM EkstraksiTanggal
)

-- Kueri Utama: Mengungkap taktik pemecahan transaksi
SELECT 
    transaction_id,
    created_by,
    vendor_id,
    amount,
    total_harian_ke_vendor
FROM KalkulasiAkumulasiHarian
WHERE total_harian_ke_vendor > 50000000 -- Batas wewenang fiktif yang dicurigai
ORDER BY vendor_id, tanggal_kejadian;

-- FRAUD DETECTION

-- Self-Approval Fraud
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

-- Limit Breach Fraud
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

-- Phantom Records / Unapproved Executions
SELECT 
    t.transaction_id, 
    t.amount, 
    t.status AS status_dokumen, 
    p.log_id AS id_rekam_jejak,
    p.approval_date AS waktu_persetujuan
FROM tabel_transaksi_1000 t
LEFT JOIN tabel_persetujuan_1000 p 
    ON t.transaction_id = p.transaction_id
WHERE t.status = 'Approved' 
  AND p.log_id IS NULL;

-- Duplicate Transactions
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

-- Structuring / Split Transactions
WITH AkumulasiHarian AS (
    SELECT 
        transaction_id, 
        created_by, 
        vendor_id, 
        amount, 
        transaction_date,
        -- Mengakumulasi pengeluaran berdasarkan pembuat, vendor, dan tanggal (tanpa jam)
        SUM(amount) OVER (
            PARTITION BY vendor_id, created_by, CAST(transaction_date AS DATE)
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
WHERE total_harian_ke_vendor > 50000000
ORDER BY vendor_id, transaction_date;

-- Rubber Stamping & After-Hours
WITH InvestigasiWaktu AS (
    SELECT 
        t.transaction_id, 
        t.amount, 
        t.transaction_date, 
        p.approval_date,
        EXTRACT(EPOCH FROM (CAST(p.approval_date AS TIMESTAMP) - CAST(t.transaction_date AS TIMESTAMP))) AS selisih_waktu_detik,
        EXTRACT(ISODOW FROM CAST(t.transaction_date AS TIMESTAMP)) AS indeks_hari,
        EXTRACT(HOUR FROM CAST(t.transaction_date AS TIMESTAMP)) AS jam_kejadian
    FROM tabel_transaksi_1000 t
    INNER JOIN tabel_persetujuan_1000 p 
        ON t.transaction_id = p.transaction_id
)

SELECT 
    transaction_id, 
    amount, 
    transaction_date, 
    approval_date,
    selisih_waktu_detik,
    CASE 
        WHEN selisih_waktu_detik <= 60 THEN 'Persetujuan Instan (Indikasi Rubber Stamp)'
        WHEN indeks_hari IN (6, 7) THEN 'Pelanggaran Hari Libur (Akhir Pekan)'
        WHEN jam_kejadian < 8 OR jam_kejadian >= 17 THEN 'Pelanggaran Jam Operasional (After-Hours)'
    END AS temuan_pelanggaran
FROM InvestigasiWaktu
WHERE selisih_waktu_detik <= 60 
   OR indeks_hari IN (6, 7) 
   OR jam_kejadian < 8 
   OR jam_kejadian >= 17
ORDER BY selisih_waktu_detik ASC;

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


-- ASSIGNMENT

-- Kasus 1
SELECT 
    t.transaction_id,
    t.amount AS nominal_transaksi,
    k.name AS nama_penyetuju,
    k.role AS jabatan_penyetuju,
    t.transaction_date AS tanggal_transaksi,
    p.approval_date AS waktu_persetujuan
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p 
    ON t.transaction_id = p.transaction_id
INNER JOIN tabel_karyawan_1000 k 
    ON p.approved_by = k.employee_id
-- Menyaring transaksi bernilai tinggi
WHERE t.amount > 30000000
  -- Memfilter persetujuan yang terjadi pada waktu yang tidak wajar
  AND (
      EXTRACT(ISODOW FROM CAST(p.approval_date AS TIMESTAMP)) IN (6, 7) -- 6: Sabtu, 7: Minggu
      OR EXTRACT(HOUR FROM CAST(p.approval_date AS TIMESTAMP)) < 6      -- Dini hari sebelum 06:00
  )
ORDER BY p.approval_date DESC;

-- Kasus 2
SELECT 
    t.transaction_id,
    t.amount AS nominal_transaksi,
    t.created_by AS identitas_pembuat,
    p.approved_by AS identitas_penyetuju,
    k.approval_limit AS batas_wewenang_penyetuju,
    -- Membuat kolom kategorisasi anomali secara dinamis
    CASE 
        WHEN t.created_by = p.approved_by AND t.amount > k.approval_limit 
            THEN 'Pelanggaran Ganda (Persetujuan Mandiri & Lewat Batas)'
        WHEN t.created_by = p.approved_by 
            THEN 'Pelanggaran Segregasi (Persetujuan Mandiri)'
        WHEN t.amount > k.approval_limit 
            THEN 'Pelanggaran Otorisasi (Lewat Batas Wewenang)'
    END AS indikator_pelanggaran
FROM tabel_transaksi_1000 t
INNER JOIN tabel_persetujuan_1000 p 
    ON t.transaction_id = p.transaction_id
INNER JOIN tabel_karyawan_1000 k 
    ON p.approved_by = k.employee_id
-- Memunculkan data jika memenuhi salah satu dari dua kondisi ini
WHERE t.created_by = p.approved_by 
   OR t.amount > k.approval_limit
ORDER BY t.amount DESC;

-- Kasus 3
-- Tahap 1: Membangun tabel bayangan untuk mengkalkulasi akumulasi berjalan
WITH AkumulasiHarianVendor AS (
    SELECT 
        transaction_id,
        vendor_id,
        -- Membuang jam/menit agar dikelompokkan ke dalam hari yang sama
        CAST(transaction_date AS DATE) AS tanggal_transaksi,
        amount AS nominal_transaksi,
        -- Kalkulasi total berjalan tanpa merusak detail ID transaksi
        SUM(amount) OVER (
            PARTITION BY vendor_id, CAST(transaction_date AS DATE)
            ORDER BY transaction_date
        ) AS total_akumulasi_harian
    FROM tabel_transaksi_1000
)

-- Tahap 2: Mengekstrak hanya transaksi yang akumulasinya sudah menembus batas kewajaran
SELECT 
    transaction_id,
    vendor_id,
    tanggal_transaksi,
    nominal_transaksi,
    total_akumulasi_harian
FROM AkumulasiHarianVendor
-- Filter diletakkan di luar CTE karena Fungsi Jendela tidak diizinkan di dalam WHERE
WHERE total_akumulasi_harian > 75000000
ORDER BY vendor_id, tanggal_transaksi;

