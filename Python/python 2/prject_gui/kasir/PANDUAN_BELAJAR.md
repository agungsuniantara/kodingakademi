# 📚 Panduan Belajar — Project Sistem Kasir (POS) dengan Python & Tkinter

> **Tujuan**: Memahami alur kerja aplikasi desktop berbasis GUI dengan Tkinter, pemisahan concern (GUI, Logic, Data), dan operasi CSV sebagai database sederhana.

---

## 🗺️ Peta Arsitektur Project

```
kasir/
├── main.py            ← Entry point & Router
├── session.py         ← Menyimpan sesi pengguna aktif
├── core_db.py         ← Semua logika data (CRUD, transaksi, laporan)
├── gui_login.py       ← Halaman Login
├── gui_admin.py       ← Dashboard Admin (CRUD Barang)
├── gui_kasir.py       ← Halaman Kasir (Keranjang, Bayar, Struk)
├── gui_manager.py     ← Dashboard Manager (CRUD Karyawan)
├── karyawan.csv       ← Database pengguna
├── barang.csv         ← Database inventaris
├── transaksi.csv      ← Database header transaksi
└── detail_transaksi.csv ← Database detail item transaksi
```

---

## 👤 Akun Default (untuk Login)

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |
| Kasir | `kasir` | `kasir123` |
| Manager | `manager` | `manager123` |

---

## 🚀 Menjalankan Aplikasi

Buka terminal di folder project ini, lalu jalankan:

```bash
python main.py
```

---

## 🔍 Panduan Eksplorasi Kode

Baca setiap file berikut secara berurutan untuk memahami arsitektur:

### `session.py`
File ini hanya ada 2 baris. Variabel `current_user` berfungsi untuk menyimpan data user yang sedang login (dict dengan key: `id`, `nama`, `role`). Diakses oleh semua modul GUI untuk menampilkan nama user dan menentukan hak akses.

### `core_db.py`
File ini adalah **otak** aplikasi. Semua logika bisnis dan operasi data ada di sini.

- **`buat_id_transaksi()`** — Membuat ID transaksi unik berbasis counter dengan format `TRX000001`. Membaca angka dari `.counter.txt`, menambah 1, lalu menulis kembali.
- **`inisialisasi_file()`** — Membuat file CSV kosong beserta header jika file belum ada. Dipanggil di awal aplikasi dan sebelum setiap operasi baca.
- **`simpan_transaksi_lengkap()`** — Menyimpan transaksi secara atomik: simpan header transaksi → simpan detail item → kurangi stok per item.
- **Rollback transaksi** — Jika terjadi error di tengah proses, fungsi menghapus baris transaksi terakhir yang baru ditulis dan mengembalikan stok.

### `main.py`
File ini mengimplementasikan **Routing**. Alur aplikasi:
1. Membuat window Tkinter
2. Memanggil `gui_login.tampilkan_halaman()` sebagai halaman pertama
3. Setelah login berhasil, memanggil `router_setelah_login(role)`
4. Router menentukan GUI yang sesuai berdasarkan role (Admin/Kasir/Manager)

Fungsi `router_setelah_login` menerima parameter `role` dan menentukan halaman mana yang dibuka. Jika ingin menambahkan role baru, tambahkan kondisi baru di fungsi ini.

### `gui_login.py`
Validasi login dilakukan dengan membaca input username & password, kemudian memanggil `core_db.validasi_login()` untuk mencocokkan data di `karyawan.csv`. Jika cocok, data user disimpan ke `session.current_user` dan callback navigasi dipanggil.

### `gui_admin.py`
Admin bisa melakukan CRUD Barang:
- Data di tabel dapat diklik dan masuk ke form melalui binding `<<TreeviewSelect>>` yang memanggil fungsi `on_pilih_tabel()`
- Perbedaan `tambah_barang_baru()` dan `edit_barang()` di `core_db.py`: `tambah_barang_baru()` menggunakan mode append (`"a"`) ke file, sedangkan `edit_barang()` membaca seluruh file, mengubah baris yang cocok, lalu menulis ulang seluruh file (overwrite)

### `gui_kasir.py`
Bagian ini menangani transaksi kasir:
- Variabel global `keranjang_belanja` menyimpan list item yang dipilih `[id_barang, nama, qty, harga, subtotal]`
- Variabel `total_belanja` menjumlahkan semua subtotal
- Fungsi `proses_pembayaran()` memvalidasi keranjang dan uang bayar, membuat ID transaksi, menyimpan transaksi, dan mencetak struk

Struk transaksi ditulis dengan `open(nama_file_struk, "w")`, menggunakan `.center()` dan `.ljust()`/`.rjust()` untuk format kolom rata tengah/kiri/kanan.

### `gui_manager.py`
Manager mengelola data karyawan:
- Melakukan CRUD pada `karyawan.csv`
- Memiliki validasi role (hanya Admin/Kasir/Manager yang diterima)
- Tidak bisa menghapus akun sendiri (validasi di `proses_hapus()`)

---

## 📋 Panduan Pengerjaan Project

Berikut adalah panduan langkah demi langkah untuk memahami dan mengembangkan project ini:

### Tahap 1: Memahami Struktur Dasar
1. Baca `main.py` untuk memahami alur startup aplikasi
2. Pelajari `session.py` untuk memahami cara kerja sesi pengguna
3. Baca `core_db.py` untuk memahami operasi data (file CSV)
4. Pelajari `gui_login.py` untuk memahami validasi login

### Tahap 2: Memahami GUI Admin
1. Baca `gui_admin.py` untuk memahami layout dan komponen form
2. Pelajari fungsi CRUD di `core_db.py` yang digunakan Admin
3. Coba jalankan aplikasi, login sebagai Admin, dan uji setiap tombol (Tambah/Edit/Hapus)
4. Perhatikan data apa yang berubah di `barang.csv` setelah setiap operasi

### Tahap 3: Memahami Transaksi Kasir
1. Baca `gui_kasir.py` dan pahami alur: pilih barang → tambah ke keranjang → bayar → cetak struk
2. Pelajari fungsi `simpan_transaksi_lengkap()` di `core_db.py`
3. Login sebagai Kasir, lakukan transaksi, dan cek:
   - Data yang ditambahkan ke `transaksi.csv`
   - Data yang ditambahkan ke `detail_transaksi.csv`
   - Perubahan stok di `barang.csv`
   - File struk `.txt` yang dihasilkan

### Tahap 4: Memahami Manajemen Karyawan
1. Baca `gui_manager.py` untuk memahami CRUD karyawan
2. Login sebagai Manager dan uji tambah/edit/hapus karyawan
3. Cek perubahan di `karyawan.csv`

### Tahap 5: Analisis Data CSV
1. Buka `transaksi.csv` dan `detail_transaksi.csv`
2. Identifikasi transaksi dengan total belanja terbesar
3. Hitung berapa kali setiap karyawan melakukan transaksi
4. Tentukan barang apa yang paling sering dibeli

---

## 🛠️ Tantangan untuk Dikerjakan

Berikut tantangan untuk memperluas project ini:

### 1. Pencarian Barang di Admin
Tambahkan kolom **Search/Filter** di dashboard Admin agar admin bisa mencari barang berdasarkan nama atau ID.

### 2. Edit Password dengan Konfirmasi
Saat Manager mengedit data karyawan, tambahkan validasi bahwa **Password Baru dan Konfirmasi Password harus sama**.

### 3. Laporan Penjualan Harian
Tambahkan fitur filter laporan penjualan berdasarkan **tanggal** (misal: transaksi hari ini).

### 4. Format Rupiah Otomatis
Saat Admin menginput harga barang, ubah entry harga agar otomatis menampilkan format `Rp 5.000` (dengan titik sebagai pemisah ribuan).

### 5. Validasi ID Otomatis
Saat Admin menambah barang, buatlah ID otomatis (misal: `BRG009`) jika kolom ID dikosongkan.

### 6. Struk dengan Qty Bintang
Ubah format struk agar barang dengan qty > 1 ditandai dengan bintang `(*)`.

### 7. Logout dari Semua Halaman
Tambahkan tombol logout juga di `gui_manager.py`.

### 8. Hapus Transaksi Terakhir
Tambahkan fitur **Batalkan Transaksi Terakhir** di dashboard Kasir, yang akan menghapus transaksi terakhir, mengembalikan stok, dan menghapus struk .txt yang sesuai.

---

## 📋 Checklist Pemahaman

Gunakan checklist ini untuk mengecek seberapa jauh pemahaman:

- [ ] Bisa menjelaskan arsitektur MVC/MV sederhana pada project ini
- [ ] Bisa menjelaskan perbedaan append vs overwrite pada file CSV
- [ ] Bisa menjelaskan alur transaksi dari input sampai cetak struk
- [ ] Bisa menjelaskan mekanisme rollback transaksi
- [ ] Bisa menambahkan fitur baru ke salah satu GUI
- [ ] Bisa memperbaiki bug sederhana (misal: validasi input)
- [ ] Bisa menjelaskan peran setiap role (Admin, Kasir, Manager)

---

## 📖 Referensi Tambahan

- **Tkinter**: https://docs.python.org/3/library/tkinter.html
- **CSV Module**: https://docs.python.org/3/library/csv.html
- **String Formatting**: https://docs.python.org/3/library/string.html#formatstrings

---

> Dibuat untuk pembelajaran Sistem Kasir berbasis GUI dengan Python & Tkinter.
> Project ini menggunakan CSV sebagai database sederhana untuk memudahkan pemahaman struktur data.
