USE wedding_db;

SELECT COUNT(*) AS jumlah_pemesanan
FROM pemesanan;

SELECT COUNT(DISTINCT id_pelanggan) AS jumlah_pelanggan
FROM pemesanan;

SELECT AVG(jumlah_tamu) AS rata_rata_tamu
FROM pemesanan;

SELECT MIN(harga) AS harga_termurah, MAX(harga) AS harga_termahal
FROM paket;

SELECT AVG(rating) AS rata_rata_rating
FROM vendor;

SELECT status, COUNT(*) AS jumlah
FROM pemesanan
GROUP BY status;

SELECT kategori, AVG(rating) AS rata_rata_rating
FROM vendor
GROUP BY kategori;

SELECT kota, COUNT(*) AS jumlah_pelanggan
FROM pelanggan
GROUP BY kota;

SELECT nama_vendor, COUNT(*)
FROM vendor
GROUP BY kategori;

SELECT kategori, AVG(rating) AS rata_rata_rating
FROM vendor
GROUP BY kategori
HAVING AVG(rating) > 4.6;

SELECT kota, COUNT(*) AS jumlah_pelanggan
FROM pelanggan
GROUP BY kota
HAVING COUNT(*) > 1;

SELECT p.nama, ps.tanggal_acara, ps.status
FROM pemesanan AS ps
JOIN pelanggan AS p ON ps.id_pelanggan = p.id_pelanggan;

SELECT p.nama, ps.tanggal_acara, ps.status
FROM pemesanan ps
INNER JOIN pelanggan p ON ps.id_pelanggan = p.id_pelanggan;

SELECT p.nama, ps.tanggal_acara
FROM pelanggan p
LEFT JOIN pemesanan ps ON p.id_pelanggan = ps.id_pelanggan;

SELECT p.nama
FROM pelanggan p
LEFT JOIN pemesanan ps ON p.id_pelanggan = ps.id_pelanggan
WHERE ps.id_pemesanan IS NULL;

SELECT
    ps.id_pemesanan,
    pl.nama AS nama_pelanggan,
    v.nama_vendor,
    pk.nama_paket,
    ps.tanggal_acara,
    ps.status
FROM pemesanan ps
JOIN pelanggan pl ON ps.id_pelanggan = pl.id_pelanggan
JOIN vendor v ON ps.id_vendor = v.id_vendor
JOIN paket pk ON ps.id_paket = pk.id_paket
ORDER BY ps.tanggal_acara;

SELECT
    v.nama_vendor,
    COUNT(*) AS jumlah_pesanan,
    SUM(pk.harga) AS total_pendapatan
FROM pemesanan ps
JOIN vendor v ON ps.id_vendor = v.id_vendor
JOIN paket pk ON ps.id_paket = pk.id_paket
WHERE ps.status <> 'Batal'
GROUP BY v.id_vendor, v.nama_vendor
ORDER BY total_pendapatan DESC;

SELECT
    DATE_FORMAT(ps.tanggal_acara, '%Y-%m') AS bulan,
    SUM(pk.harga) AS pendapatan
FROM pemesanan ps
JOIN paket pk ON ps.id_paket = pk.id_paket
WHERE ps.status <> 'Batal'
GROUP BY bulan
ORDER BY bulan;

SELECT
    pk.nama_paket,
    COUNT(*) AS jumlah_pesanan
FROM pemesanan ps
JOIN paket pk ON ps.id_paket = pk.id_paket
GROUP BY pk.id_paket, pk.nama_paket
ORDER BY jumlah_pesanan DESC;

SELECT nama_paket, harga
FROM paket
WHERE harga > (SELECT AVG(harga) FROM paket);

SELECT nama
FROM pelanggan
WHERE id_pelanggan IN (
    SELECT id_pelanggan
    FROM pemesanan
    WHERE id_paket = (
        SELECT id_paket
        FROM paket
        ORDER BY harga DESC
        LIMIT 1
    )
);

SELECT AVG(rating_tinggi) AS rata_rata_rating_tinggi
FROM (
    SELECT rating AS rating_tinggi
    FROM vendor
    WHERE rating > 4.5
) AS sub;










