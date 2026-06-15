CREATE TABLE tabel_kinerja_penjualan (
    id_karyawan VARCHAR(10) PRIMARY KEY,
    nama_karyawan VARCHAR(50),
    id_manajer VARCHAR(10),
    departemen VARCHAR(50),
    total_penjualan NUMERIC
);

INSERT INTO tabel_kinerja_penjualan (id_karyawan, nama_karyawan, id_manajer, departemen, total_penjualan) VALUES
('EMP01', 'Direktur Utama', NULL, 'Eksekutif', 0),
('EMP02', 'Manajer Utara', 'EMP01', 'Penjualan', 25000000),
('EMP03', 'Manajer Selatan', 'EMP01', 'Penjualan', 15000000),
('EMP04', 'Staf A', 'EMP02', 'Penjualan', 45000000),
('EMP05', 'Staf B', 'EMP02', 'Penjualan', 30000000),
('EMP06', 'Staf C', 'EMP03', 'Penjualan', 10000000);

SELECT * FROM tabel_kinerja_penjualan;

-- Bagian 2: Struktur dan Sintaks Dasar CTE
WITH RataRataPerusahaan AS (
    SELECT AVG(total_penjualan) AS nilai_rata_rata
    FROM tabel_kinerja_penjualan
)
SELECT 
    t.nama_karyawan,
    t.total_penjualan,
    r.nilai_rata_rata
FROM tabel_kinerja_penjualan t
CROSS JOIN RataRataPerusahaan r
WHERE t.total_penjualan > r.nilai_rata_rata;

-- Bagian 3: Rantai CTE (Multiple CTEs)
WITH TotalPerManajer AS (
    SELECT 
        id_manajer, 
        SUM(total_penjualan) AS akumulasi_tim
    FROM tabel_kinerja_penjualan
    WHERE id_manajer IS NOT NULL
    GROUP BY id_manajer
),
KalkulasiKontribusi AS (
    SELECT 
        k.nama_karyawan,
        k.id_manajer,
        k.total_penjualan,
        m.akumulasi_tim,
        (k.total_penjualan / NULLIF(m.akumulasi_tim, 0)) * 100 AS persentase_kontribusi
    FROM tabel_kinerja_penjualan k
    INNER JOIN TotalPerManajer m 
        ON k.id_manajer = m.id_manajer
)

SELECT * FROM KalkulasiKontribusi
WHERE nama_karyawan LIKE 'Staf%';

-- Bagian 4: Kombinasi CTE dengan Window Functions

WITH PeringkatPenjualan AS (
    SELECT 
        nama_karyawan,
        departemen,
        total_penjualan,
        DENSE_RANK() OVER (ORDER BY total_penjualan DESC) AS ranking
    FROM tabel_kinerja_penjualan
)

SELECT * FROM PeringkatPenjualan
WHERE ranking <= 2;

-- Bagian 5: CTE Rekursif (Recursive CTE)

WITH RECURSIVE HierarkiOrganisasi AS (
    SELECT 
        id_karyawan,
        nama_karyawan,
        id_manajer,
        1 AS level_kedalaman,
        CAST(nama_karyawan AS VARCHAR(255)) AS rantai_komando
    FROM tabel_kinerja_penjualan
    WHERE id_manajer IS NULL

    UNION ALL

    SELECT 
        t.id_karyawan,
        t.nama_karyawan,
        t.id_manajer,
        h.level_kedalaman + 1,
        CAST(h.rantai_komando || ' -> ' || t.nama_karyawan AS VARCHAR(255))
    FROM tabel_kinerja_penjualan t
    INNER JOIN HierarkiOrganisasi h 
        ON t.id_manajer = h.id_karyawan
)

SELECT 
    id_karyawan,
    nama_karyawan,
    level_kedalaman,
    rantai_komando
FROM HierarkiOrganisasi
ORDER BY level_kedalaman, id_karyawan;