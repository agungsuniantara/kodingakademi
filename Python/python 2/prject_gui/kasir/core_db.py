import csv
import os

# ==========================================
# KONFIGURASI NAMA FILE
# ==========================================
FILE_KARYAWAN = "karyawan.csv"
FILE_BARANG = "barang.csv"
FILE_TRANSAKSI = "transaksi.csv"
FILE_DETAIL = "detail_transaksi.csv"
_FILE_COUNTER_PATH = ".counter.txt"


def _baca_counter():
    try:
        with open(_FILE_COUNTER_PATH, "r") as f:
            return int(f.read().strip() or "0")
    except Exception:
        return 0


def _tulis_counter(nilai):
    with open(_FILE_COUNTER_PATH, "w") as f:
        f.write(str(nilai))


def buat_id_transaksi():
    """Membuat ID transaksi unik berbasis counter untuk mencegah bentrok."""
    nomor = _baca_counter() + 1
    _tulis_counter(nomor)
    return f"TRX{nomor:06d}"

# ==========================================
# 1. INISIALISASI DATABASE (FILE CSV)
# ==========================================
def inisialisasi_file():
    """
    Fungsi ini dipanggil saat aplikasi pertama kali dijalankan.
    Jika file CSV belum ada, fungsi ini akan membuatnya beserta baris header.
    """
    # Buat file karyawan.csv jika belum ada (sekaligus beri 1 akun default)
    if not os.path.exists(FILE_KARYAWAN):
        with open(FILE_KARYAWAN, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id_karyawan", "username", "password", "nama", "role"])
            writer.writerow(["KRY001", "admin", "admin123", "Administrator", "Admin"])
            writer.writerow(["KRY002", "kasir", "kasir123", "Petugas Kasir", "Kasir"])
            writer.writerow(["KRY005", "manager", "manager123", "Manager Utama", "Manager"])
            
    # Buat file barang.csv
    if not os.path.exists(FILE_BARANG):
        with open(FILE_BARANG, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id_barang", "nama_barang", "harga", "stok"])
            
    # Buat file transaksi.csv
    if not os.path.exists(FILE_TRANSAKSI):
        with open(FILE_TRANSAKSI, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id_transaksi", "waktu", "id_karyawan", "total_belanja", "uang_bayar"])
            
    # Buat file detail_transaksi.csv
    if not os.path.exists(FILE_DETAIL):
        with open(FILE_DETAIL, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id_transaksi", "id_barang", "qty", "subtotal"])


# ==========================================
# 2. FUNGSI OTENTIKASI (KARYAWAN)
# ==========================================
def validasi_login(username, password):
    """
    Mengecek apakah username dan password cocok dengan data di karyawan.csv.
    Mengembalikan Dictionary data user jika sukses, atau None jika gagal.
    """
    inisialisasi_file() # Pastikan file ada sebelum dibaca
    
    with open(FILE_KARYAWAN, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                return {
                    "id": row["id_karyawan"],
                    "nama": row["nama"],
                    "role": row["role"]
                }
    return None # Jika tidak ada yang cocok


# ==========================================
# 3. FUNGSI MANAJEMEN BARANG (CRUD DASAR)
# ==========================================
def ambil_semua_barang():
    """Membaca seluruh data barang dan mengembalikannya dalam bentuk List of Dictionaries."""
    inisialisasi_file()
    daftar_barang = []
    
    with open(FILE_BARANG, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Konversi harga dan stok menjadi integer agar bisa dihitung nantinya
            row["harga"] = int(row["harga"])
            row["stok"] = int(row["stok"])
            daftar_barang.append(row)
            
    return daftar_barang

def tambah_barang_baru(id_barang, nama, harga, stok):
    """Menambahkan satu baris data barang baru ke CSV."""
    if not id_barang or not nama:
        raise ValueError("ID Barang dan Nama Barang harus diisi!")
    if not isinstance(harga, int) or harga < 0:
        raise ValueError("Harga harus berupa bilangan bulat non-negatif!")
    if not isinstance(stok, int) or stok < 0:
        raise ValueError("Stok harus berupa bilangan bulat non-negatif!")

    semua = ambil_semua_barang()
    for b in semua:
        if b["id_barang"] == id_barang:
            raise ValueError(f"ID Barang '{id_barang}' sudah ada!")

    with open(FILE_BARANG, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id_barang, nama, str(harga), str(stok)])
        
def edit_barang(id_barang, nama_baru, harga_baru, stok_baru):
    """
    Mengubah data barang berdasarkan id_barang.
    Logika overwrite: baca semua isi file, ubah baris yang cocok, tulis ulang.
    """
    semua_barang = []
    found = False

    with open(FILE_BARANG, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        semua_barang.append(header)

        for row in reader:
            if row[0] == id_barang:
                row[1] = nama_baru
                row[2] = str(harga_baru)
                row[3] = str(stok_baru)
                found = True
            semua_barang.append(row)

    if not found:
        raise ValueError(f"Barang dengan ID '{id_barang}' tidak ditemukan!")

    with open(FILE_BARANG, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(semua_barang)


def hapus_barang(id_barang):
    """
    Menghapus satu baris barang berdasarkan id_barang.
    Logika overwrite: baca semua isi file, buang baris yang cocok, tulis ulang.
    """
    semua_barang = []
    found = False

    with open(FILE_BARANG, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        semua_barang.append(header)

        for row in reader:
            if row[0] != id_barang:
                semua_barang.append(row)
            else:
                found = True

    if not found:
        raise ValueError(f"Barang dengan ID '{id_barang}' tidak ditemukan!")

    with open(FILE_BARANG, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(semua_barang)


# ==========================================
# 4. FUNGSI TRANSAKSI & INVENTORY LOGIC
# ==========================================
def kurangi_stok_barang(id_barang, jumlah_beli):
    """
    Logika overwrite:
    1. Baca semua isi file barang.csv ke dalam List.
    2. Cari id_barang yang sesuai, validasi stok cukup, kurangi stoknya.
    3. Tulis ulang seluruh isi List kembali ke barang.csv.
    """
    semua_barang = []

    with open(FILE_BARANG, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        semua_barang.append(header)

        for row in reader:
            row_id = row[0]
            stok_lama = int(row[3])

            if row_id == id_barang:
                if stok_lama < jumlah_beli:
                    raise ValueError(
                        f"Stok tidak cukup untuk barang ID {id_barang}. "
                        f"Sisa: {stok_lama}, diminta: {jumlah_beli}"
                    )
                stok_baru = stok_lama - jumlah_beli
                row[3] = str(stok_baru)

            semua_barang.append(row)

    with open(FILE_BARANG, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(semua_barang)


def hapus_transaksi_terakhir(id_transaksi):
    """
    Menghapus transaksi terakhir yang ditambahkan (rollback sederhana).
    Hapus baris terakhir di FILE_TRANSAKSI dengan id_transaksi yang sesuai.
    """
    semua_transaksi = []
    with open(FILE_TRANSAKSI, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        semua_transaksi.append(header)
        for row in reader:
            if row[0] != id_transaksi:
                semua_transaksi.append(row)
    with open(FILE_TRANSAKSI, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(semua_transaksi)


def simpan_transaksi_lengkap(id_transaksi, waktu, id_karyawan, total_belanja, uang_bayar, keranjang):
    """
    Fungsi ini sangat penting (bersifat Atomik).
    Mengeksekusi penulisan nota, penulisan detail item, dan pengurangan stok secara berurutan.
    Parameter 'keranjang' diasumsikan sebagai List yang berisi data: [id_barang, qty, subtotal]

    Jika terjadi error di tengah proses, fungsi akan melakukan rollback sederhana
    dengan menghapus header transaksi yang sudah tertulis dan mengembalikan stok.
    """
    try:
        with open(FILE_TRANSAKSI, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id_transaksi, waktu, id_karyawan, total_belanja, uang_bayar])

        with open(FILE_DETAIL, "a", newline="") as f:
            writer = csv.writer(f)

            for item in keranjang:
                id_barang = item[0]
                qty = item[1]
                subtotal = item[2]

                writer.writerow([id_transaksi, id_barang, qty, subtotal])
                kurangi_stok_barang(id_barang, qty)

    except Exception as e:
        try:
            hapus_transaksi_terakhir(id_transaksi)
        except Exception:
            pass
        raise RuntimeError(
            f"Transaksi gagal dan telah di-rollback. Error: {e}"
        ) from e


# ==========================================
# 5. FUNGSI MANAJEMEN KARYAWAN (CRUD)
# ==========================================
def ambil_semua_karyawan():
    inisialisasi_file()
    daftar_karyawan = []
    with open(FILE_KARYAWAN, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            daftar_karyawan.append(row)
    return daftar_karyawan

def tambah_karyawan_baru(id_karyawan, username, password, nama, role):
    with open(FILE_KARYAWAN, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id_karyawan, username, password, nama, role])

def edit_karyawan(id_karyawan, username_baru, password_baru, nama_baru, role_baru):
    semua_karyawan = []
    with open(FILE_KARYAWAN, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        semua_karyawan.append(header)
        for row in reader:
            if row[0] == id_karyawan:
                row[1] = username_baru
                row[2] = password_baru
                row[3] = nama_baru
                row[4] = role_baru
            semua_karyawan.append(row)
    with open(FILE_KARYAWAN, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(semua_karyawan)

def hapus_karyawan(id_karyawan):
    semua_karyawan = []
    with open(FILE_KARYAWAN, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        semua_karyawan.append(header)
        for row in reader:
            if row[0] != id_karyawan:
                semua_karyawan.append(row)
    with open(FILE_KARYAWAN, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(semua_karyawan)

# ==========================================
# 6. FUNGSI LAPORAN PENJUALAN (MANAGER)
# ==========================================
def ambil_semua_transaksi():
    """
    Membaca seluruh transaksi dari transaksi.csv dan menggabungkan
    nama kasir dari karyawan.csv. Diurutkan dari transaksi terbaru.
    """
    inisialisasi_file()
    
    # Peta id_karyawan -> nama (untuk join)
    peta_karyawan = {}
    with open(FILE_KARYAWAN, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            peta_karyawan[row["id_karyawan"]] = row["nama"]
    
    daftar_transaksi = []
    with open(FILE_TRANSAKSI, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["total_belanja"] = int(row["total_belanja"])
            row["uang_bayar"] = int(row["uang_bayar"])
            row["nama_kasir"] = peta_karyawan.get(row["id_karyawan"], "Tidak diketahui")
            daftar_transaksi.append(row)
    
    # Format waktu "YYYY-MM-DD HH:MM:SS" bisa diurutkan sebagai string
    daftar_transaksi.sort(key=lambda t: t["waktu"], reverse=True)
    return daftar_transaksi


def ambil_produk_terlaris():
    """
    Menggabungkan seluruh detail_transaksi.csv per id_barang,
    menghitung total qty dan subtotal, lalu mengurutkan dari yang terlaris.
    """
    inisialisasi_file()
    
    # Peta id_barang -> nama (untuk join)
    peta_barang = {}
    with open(FILE_BARANG, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            peta_barang[row["id_barang"]] = row["nama_barang"]
    
    agregat = {}  # id_barang -> [total_qty, total_subtotal]
    with open(FILE_DETAIL, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            id_barang = row["id_barang"]
            qty = int(row["qty"])
            subtotal = int(row["subtotal"])
            
            if id_barang not in agregat:
                agregat[id_barang] = [0, 0]
            agregat[id_barang][0] += qty
            agregat[id_barang][1] += subtotal
    
    hasil = []
    for id_barang, (qty, subtotal) in agregat.items():
        hasil.append({
            "id_barang": id_barang,
            "nama_barang": peta_barang.get(id_barang, "Barang dihapus"),
            "qty": qty,
            "subtotal": subtotal
        })
    
    hasil.sort(key=lambda p: p["qty"], reverse=True)
    return hasil


def ambil_ringkasan_penjualan():
    """Menghitung total transaksi, total penjualan, dan rata-rata per transaksi."""
    daftar = ambil_semua_transaksi()
    
    total_transaksi = len(daftar)
    total_penjualan = sum(t["total_belanja"] for t in daftar)
    rata_rata = total_penjualan // total_transaksi if total_transaksi > 0 else 0
    
    return {
        "total_transaksi": total_transaksi,
        "total_penjualan": total_penjualan,
        "rata_rata": rata_rata
    }