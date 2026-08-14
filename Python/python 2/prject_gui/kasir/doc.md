# Sistem Point of Sale (POS) Koperasi Sekolah

## Deskripsi
Aplikasi desktop Python dengan antarmuka grafis (tkinter) untuk mengelola transaksi penjualan di koperasi sekolah. Data disimpan dalam file CSV.

## Fitur Utama
1. **Autentikasi**: Login dengan role Admin, Kasir, dan Manager
2. **Manajemen Inventaris (Admin)**: Melihat daftar barang, menambah barang baru
3. **Transaksi Kasir**: Memilih barang, memasukkan jumlah, menghitung total, memproses pembayaran, dan mencetak struk
4. **Manajemen Karyawan (Manager)**: Melihat, menambah, mengedit, dan menghapus data karyawan
5. **Penyimpanan Data**: Menggunakan file CSV untuk menyimpan data karyawan, barang, transaksi, dan detail transaksi

## Struktur File
- `main.py`: Entry point dan router navigasi antar halaman
- `core_db.py`: Fungsi akses dan manipulasi data CSV
- `session.py`: Menyimpan status login pengguna aktif
- `gui_login.py`: Antarmuka halaman login
- `gui_kasir.py`: Antarmuka halaman kasir (transaksi penjualan)
- `gui_admin.py`: Antarmuka halaman admin (manajemen inventaris)
- `gui_manager.py`: Antarmuka halaman manager (manajemen karyawan)
- File CSV: `karyawan.csv`, `barang.csv`, `transaksi.csv`, `detail_transaksi.csv`

## Cara Menjalankan
```bash
python main.py
```

## Akun Default
- **Admin**: username `admin`, password `admin123`
- **Kasir**: username `kasir`, password `kasir123`
- **Manager**: username `manager`, password `manager123`