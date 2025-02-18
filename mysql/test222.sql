USE megastore;

SELECT 
    Pegawai.employee_name,
    Transaksi.product_id
FROM 
    Transaksi
JOIN Pegawai ON Transaksi.employee_id = Pegawai.employee_id;
