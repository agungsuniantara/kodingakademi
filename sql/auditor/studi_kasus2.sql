-- TASK 1 — Siapa yang klaim paling besar?
SELECT 
    e.nama, 
    e.departemen, 
    c.tanggal,
    c.kategori, 
    c.jumlah AS nominal_klaim
FROM expense_claims c
INNER JOIN employees e 
    ON c.employee_id = e.employee_id
ORDER BY c.jumlah DESC
LIMIT 20;

-- TASK 2 — Ada yang perjalanan ke 2 kota di hari yang sama?
WITH DeteksiTripGanda AS (
    SELECT 
        e.nama,
        t.tgl_mulai,
        t.kota_tujuan,
        COUNT(*) OVER (PARTITION BY t.employee_id, t.tgl_mulai) AS frekuensi_dihari_sama
    FROM trips t
    INNER JOIN employees e 
        ON t.employee_id = e.employee_id
)
SELECT * FROM DeteksiTripGanda
WHERE frekuensi_dihari_sama > 1
ORDER BY nama, tgl_mulai;

-- TASK 3 — Siapa yang perjalanan dinas paling sering? (>5x per bulan)
WITH DeteksiSeringDinas AS (
    SELECT 
        e.nama,
        e.departemen,
        t.tgl_mulai,
        EXTRACT(MONTH FROM t.tgl_mulai) AS bulan_kejadian,
        COUNT(*) OVER (PARTITION BY t.employee_id, EXTRACT(MONTH FROM t.tgl_mulai)) AS jumlah_trip_perbulan
    FROM trips t
    INNER JOIN employees e 
        ON t.employee_id = e.employee_id
)
SELECT * FROM DeteksiSeringDinas
WHERE jumlah_trip_perbulan > 5
ORDER BY jumlah_trip_perbulan DESC;

-- TASK 4 — Bandingkan klaim vs rata-rata departemen
WITH AnalisisRataDept AS (
    SELECT 
        e.nama, 
        e.departemen, 
        c.jumlah AS klaim_aktual,
        AVG(c.jumlah) OVER (PARTITION BY e.departemen) AS rata_rata_dept
    FROM expense_claims c
    INNER JOIN employees e 
        ON c.employee_id = e.employee_id
)
SELECT 
    nama,
    departemen,
    klaim_aktual,
    rata_rata_dept,
    CASE 
        WHEN klaim_aktual > (rata_rata_dept * 3) THEN 'SANGAT MENCURIGAKAN'
        ELSE 'Normal'
    END AS status_kewajaran
FROM AnalisisRataDept
WHERE klaim_aktual > rata_rata_dept
ORDER BY klaim_aktual DESC;

-- TASK 5 — Risk Summary: Gabungkan semua temuan
WITH RekapTrip AS (
    SELECT 
        employee_id,
        COUNT(*) OVER (PARTITION BY employee_id) AS total_trip,
        ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY tgl_mulai DESC) AS urutan_trip
    FROM trips
),
RekapKlaim AS (
    SELECT 
        employee_id,
        MAX(jumlah) OVER (PARTITION BY employee_id) AS klaim_terbesar,
        SUM(jumlah) OVER (PARTITION BY employee_id) AS total_klaim,
        ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY jumlah DESC) AS urutan_klaim
    FROM expense_claims
)
SELECT 
    e.nama,
    e.departemen,
    t.total_trip,
    k.total_klaim,
    k.klaim_terbesar,
    CASE 
        WHEN k.klaim_terbesar > 3000000 OR t.total_trip > 10 THEN 'HIGH RISK'
        WHEN k.klaim_terbesar > 1000000 THEN 'MEDIUM RISK'
        ELSE 'LOW RISK'
    END AS risk_level
FROM employees e
LEFT JOIN RekapTrip t 
    ON e.employee_id = t.employee_id AND t.urutan_trip = 1
LEFT JOIN RekapKlaim k 
    ON e.employee_id = k.employee_id AND k.urutan_klaim = 1
ORDER BY 
    CASE risk_level 
        WHEN 'HIGH RISK' THEN 1 
        WHEN 'MEDIUM RISK' THEN 2 
        ELSE 3 
    END;








