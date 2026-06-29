from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import datetime

# ==================== DATA ====================
file_akun = "data.txt"
file_transaksi = "riwayat_transaksi.txt"

# Daftar menu dan harga (Dictionary)
menu_kasir = {
    "Buku Tulis": 5000,
    "Pensil 2B": 3000,
    "Pulpen Hitam": 4000,
    "Penghapus": 2000,
    "Penggaris 30cm": 3500
}

# Variabel global untuk menyimpan total belanja
total_belanja = 0

# ==================== FUNGSI KASIR ====================
def tambah_ke_keranjang():
    global total_belanja
    
    barang_pilihan = barang_combobox.get()
    jumlah_teks = jumlah_box.get()
    
    # Validasi input
    if not barang_pilihan or not jumlah_teks:
        messagebox.showwarning("Peringatan", "Pilih barang dan masukkan jumlahnya!")
        return
        
    if not jumlah_teks.isdigit():
        messagebox.showerror("Error", "Jumlah harus berupa angka!")
        return
        
    jumlah = int(jumlah_teks)
    harga_satuan = menu_kasir[barang_pilihan]
    sub_total = harga_satuan * jumlah
    
    # Tambahkan ke total belanja global
    total_belanja += sub_total
    
    # Tampilkan di listbox keranjang
    teks_keranjang = f"{barang_pilihan} (x{jumlah}) - Rp {sub_total}"
    keranjang_listbox.insert(END, teks_keranjang)
    
    # Update label total
    label_total_harga.config(text=f"Total: Rp {total_belanja}")
    
    # Kosongkan box jumlah untuk input selanjutnya
    jumlah_box.delete(0, END)

def proses_pembayaran():
    global total_belanja
    
    if total_belanja == 0:
        messagebox.showwarning("Peringatan", "Keranjang masih kosong!")
        return
        
    uang_teks = uang_box.get()
    
    if not uang_teks.isdigit():
        messagebox.showerror("Error", "Masukkan jumlah uang dengan benar (angka)!")
        return
        
    uang_bayar = int(uang_teks)
    
    if uang_bayar < total_belanja:
        messagebox.showerror("Error", "Uang tidak cukup!")
        return
        
    kembalian = uang_bayar - total_belanja
    
    # Tampilkan kembalian
    messagebox.showinfo("Berhasil", f"Pembayaran Sukses!\nTotal: Rp {total_belanja}\nBayar: Rp {uang_bayar}\nKembalian: Rp {kembalian}")
    
    # Simpan ke file riwayat
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_transaksi, "a") as file:
        file.write(f"[{waktu_sekarang}] Total: Rp{total_belanja} | Bayar: Rp{uang_bayar} | Kembali: Rp{kembalian}\n")
        
    # Reset kasir setelah selesai bayar
    keranjang_listbox.delete(0, END)
    total_belanja = 0
    label_total_harga.config(text="Total: Rp 0")
    uang_box.delete(0, END)

def buka_halaman_kasir():
    # Menutup halaman login
    root.withdraw()
    
    global barang_combobox, jumlah_box, keranjang_listbox, label_total_harga, uang_box
    
    kasir = Toplevel()
    kasir.title("Aplikasi Kasir Sekolah")
    kasir.geometry("600x550")
    
    # Judul
    Label(kasir, text="Sistem Kasir Koperasi Siswa", font=("Times New Roman", 20, "bold")).grid(row=0, column=0, columnspan=3, pady=20)
    
    # --- AREA INPUT BARANG ---
    Label(kasir, text="Pilih Barang :", font=("Times New Roman", 14)).grid(row=1, column=0, padx=10, sticky="w")
    
    daftar_nama_barang = list(menu_kasir.keys())
    barang_combobox = Combobox(kasir, values=daftar_nama_barang, font=("Times New Roman", 14), state="readonly")
    barang_combobox.grid(row=1, column=1, padx=10, pady=5)
    barang_combobox.set("Pilih Barang")
    
    Label(kasir, text="Jumlah :", font=("Times New Roman", 14)).grid(row=2, column=0, padx=10, sticky="w")
    jumlah_box = Entry(kasir, font=("Times New Roman", 14), width=10)
    jumlah_box.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    
    Button(kasir, text="Tambah ke Keranjang", command=tambah_ke_keranjang).grid(row=3, column=1, pady=10, sticky="w")
    
    # --- AREA KERANJANG ---
    Label(kasir, text="Keranjang Belanja:", font=("Times New Roman", 14)).grid(row=4, column=0, padx=10, pady=10, sticky="nw")
    keranjang_listbox = Listbox(kasir, font=("Times New Roman", 12), width=40, height=8)
    keranjang_listbox.grid(row=4, column=1, columnspan=2, padx=10)
    
    # --- AREA PEMBAYARAN ---
    label_total_harga = Label(kasir, text="Total: Rp 0", font=("Times New Roman", 16, "bold"))
    label_total_harga.grid(row=5, column=1, pady=10, sticky="w")
    
    Label(kasir, text="Uang Bayar :", font=("Times New Roman", 14)).grid(row=6, column=0, padx=10, sticky="w")
    uang_box = Entry(kasir, font=("Times New Roman", 14))
    uang_box.grid(row=6, column=1, padx=10, pady=5, sticky="w")
    
    Button(kasir, text="BAYAR", command=proses_pembayaran, width=15).grid(row=7, column=1, pady=15, sticky="w")
    
    Button(kasir, text="Keluar", command=root.destroy).grid(row=7, column=2, pady=15)

# ==================== FUNGSI LOGIN ====================
def login():
    username = username_box.get()
    password = password_box.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong")
        return
        
    found = False
    try:
        with open(file_akun, "r") as file:
            for baris in file:
                # Hindari baris kosong
                if "-" in baris:
                    data_split = baris.split("-")
                    file_user = data_split[0].strip()
                    file_pass = data_split[1].strip()
                    if username == file_user and password == file_pass:
                        found = True
                        break
    except FileNotFoundError:
        messagebox.showerror("Error File", f"File '{file_akun}' tidak ditemukan. Buat file tersebut terlebih dahulu.")
        return
            
    if found:
        messagebox.showinfo("Login", "Login Berhasil")
        buka_halaman_kasir()
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah")

# ==================== HALAMAN LOGIN (ROOT) ====================
root = Tk()
root.title("Login Kasir")
root.geometry("400x300")

Label(root, text="Silahkan Login", font=("Times New Roman", 18, "bold")).pack(pady=20)

Label(root, text="Username:", font=("Times New Roman", 14)).pack()
username_box = Entry(root, font=("Times New Roman", 14))
username_box.pack(pady=5)

Label(root, text="Password:", font=("Times New Roman", 14)).pack()
password_box = Entry(root, font=("Times New Roman", 14), show="*") # Bintang untuk sembunyikan password
password_box.pack(pady=5)

Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()