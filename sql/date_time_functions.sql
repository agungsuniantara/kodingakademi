CREATE TABLE tabel_log_aktivitas (
    log_id INT PRIMARY KEY,
    nama_proses VARCHAR(50),
    waktu_mulai TIMESTAMP,
    waktu_selesai TIMESTAMP
);

INSERT INTO tabel_log_aktivitas (log_id, nama_proses, waktu_mulai, waktu_selesai) VALUES
(101, 'Proses Pencadangan', '2024-05-10 23:00:00', '2024-05-11 01:15:30'),
(102, 'Pembaruan Sistem', '2024-05-12 08:30:00', '2024-05-12 08:35:45'),
(103, 'Sinkronisasi Data', '2024-05-12 14:00:00', '2024-05-12 14:00:45'),
(104, 'Audit Mingguan', '2024-05-18 02:15:00', '2024-05-18 04:45:00');

SELECT * FROM tabel_log_aktivitas;

SELECT 
    log_id, 
    waktu_mulai, 
    CURRENT_DATE AS tanggal_hari_ini,
    NOW() AS waktu_server_sekarang
FROM tabel_log_aktivitas;

SELECT 
    log_id,
    nama_proses,
    waktu_mulai,
    EXTRACT(ISODOW FROM waktu_mulai) AS indeks_hari,
    EXTRACT(HOUR FROM waktu_mulai) AS jam_dieksekusi
FROM tabel_log_aktivitas
WHERE EXTRACT(ISODOW FROM waktu_mulai) IN (6, 7);

SELECT 
    log_id,
    waktu_mulai AS format_baku,
    TO_CHAR(waktu_mulai, 'Day, DD Month YYYY') AS format_tanggal_huruf,
    TO_CHAR(waktu_mulai, 'HH24:MI') AS format_jam_saja
FROM tabel_log_aktivitas;

SELECT 
    log_id,
    nama_proses,
    waktu_mulai,
    waktu_selesai,
    (waktu_selesai - waktu_mulai) AS durasi_interval,
    EXTRACT(EPOCH FROM (waktu_selesai - waktu_mulai)) AS durasi_total_detik
FROM tabel_log_aktivitas
WHERE EXTRACT(EPOCH FROM (waktu_selesai - waktu_mulai)) < 60;

SELECT 
    log_id,
    waktu_mulai AS waktu_asli,
    DATE_TRUNC('month', waktu_mulai) AS awal_bulan_kejadian,
    DATE_TRUNC('day', waktu_mulai) AS waktu_dibulatkan_ke_hari
FROM tabel_log_aktivitas
ORDER BY log_id;
