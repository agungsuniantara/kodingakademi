import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os
import core_db
import session

# ==========================================
# STATE MANAGEMENT (Lokal untuk Halaman Kasir)
# ==========================================
keranjang_belanja = []  
total_belanja = 0
dict_barang = {}

def bersihkan_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def muat_data_combobox(combobox):
    global dict_barang
    dict_barang.clear()
    
    daftar_barang = core_db.ambil_semua_barang()
    
    list_tampilan = []
    for b in daftar_barang:
        teks_tampil = f"{b['id_barang']} - {b['nama_barang']}"
        dict_barang[teks_tampil] = b
        list_tampilan.append(teks_tampil)
        
    combobox['values'] = list_tampilan

def tambah_ke_keranjang(combobox, entry_qty, tree, label_total):
    global total_belanja
    
    pilihan = combobox.get()
    qty_teks = entry_qty.get().strip()
    
    if not pilihan or not qty_teks:
        messagebox.showwarning("Peringatan", "Pilih barang dan masukkan jumlahnya!")
        return
        
    if not qty_teks.isdigit():
        messagebox.showerror("Error", "Jumlah beli harus berupa angka!")
        return
        
    qty = int(qty_teks)
    if qty <= 0:
        messagebox.showerror("Error", "Jumlah beli minimal 1!")
        return
        
    barang = dict_barang[pilihan]
    
    if qty > barang['stok']:
        messagebox.showerror("Stok Kurang", f"Sisa stok {barang['nama_barang']} hanya {barang['stok']}!")
        return
        
    subtotal = qty * barang['harga']
    
    keranjang_belanja.append([barang['id_barang'], barang['nama_barang'], qty, barang['harga'], subtotal])
    
    tree.insert("", tk.END, values=(
        barang['nama_barang'],
        qty,
        f"Rp {barang['harga']}",
        f"Rp {subtotal}"
    ))
    
    total_belanja += subtotal
    label_total.config(text=f"Total: Rp {total_belanja}")
    
    entry_qty.delete(0, tk.END)

def proses_pembayaran(entry_bayar, tree, label_total, combobox):
    global total_belanja, keranjang_belanja
    
    if total_belanja == 0 or len(keranjang_belanja) == 0:
        messagebox.showwarning("Peringatan", "Keranjang belanja masih kosong!")
        return
        
    uang_teks = entry_bayar.get().strip()
    if not uang_teks.isdigit():
        messagebox.showerror("Error", "Masukkan jumlah uang dengan format angka!")
        return
        
    uang_bayar = int(uang_teks)
    if uang_bayar < total_belanja:
        messagebox.showerror("Error", "Uang bayar tidak mencukupi!")
        return
        
    kembalian = uang_bayar - total_belanja
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_transaksi = "TRX" + datetime.now().strftime("%Y%m%d%H%M%S")
    id_karyawan = session.current_user['id']
    nama_kasir = session.current_user['nama']
    
    detail_untuk_db = []
    for item in keranjang_belanja:
        detail_untuk_db.append([item[0], item[2], item[4]])
        
    core_db.simpan_transaksi_lengkap(id_transaksi, waktu_sekarang, id_karyawan, total_belanja, uang_bayar, detail_untuk_db)
    
    lebar_struk = 40
    nama_file_struk = f"struk_{id_transaksi}.txt"
    
    with open(nama_file_struk, "w") as struk:
        struk.write("KOPERASI SEKOLAH UMA".center(lebar_struk) + "\n")
        struk.write("=" * lebar_struk + "\n")
        struk.write(f"No  : {id_transaksi}\n")
        struk.write(f"Tgl : {waktu_sekarang}\n")
        struk.write(f"Opr : {nama_kasir}\n")
        struk.write("-" * lebar_struk + "\n")
        
        for item in keranjang_belanja:
            nama, qty, harga, sub = item[1], item[2], item[3], item[4]
            struk.write(f"{nama}\n")
            detail = f"  {qty} x {harga}"
            sub_str = f"Rp {sub}"
            spasi = lebar_struk - len(detail) - len(sub_str)
            struk.write(detail + (" " * spasi) + sub_str + "\n")
            
        struk.write("-" * lebar_struk + "\n")
        struk.write("TOTAL".ljust(15) + f": Rp {total_belanja}".rjust(25) + "\n")
        struk.write("BAYAR".ljust(15) + f": Rp {uang_bayar}".rjust(25) + "\n")
        struk.write("KEMBALI".ljust(15) + f": Rp {kembalian}".rjust(25) + "\n")
        struk.write("=" * lebar_struk + "\n")
        struk.write("Terima Kasih".center(lebar_struk) + "\n")

    messagebox.showinfo("Sukses", f"Transaksi Berhasil!\nKembalian: Rp {kembalian}\nStruk disimpan: {nama_file_struk}")
    
    keranjang_belanja.clear()
    total_belanja = 0
    
    for item in tree.get_children():
        tree.delete(item)
        
    label_total.config(text="Total: Rp 0")
    entry_bayar.delete(0, tk.END)
    
    muat_data_combobox(combobox)

def tampilkan_halaman(window, fungsi_logout):
    bersihkan_window(window)
    
    nama_kasir = session.current_user["nama"] if session.current_user else "Kasir"
    
    header_frame = tk.Frame(window, pady=15)
    header_frame.pack(fill="x")
    tk.Label(header_frame, text="SISTEM KASIR (POINT OF SALE)", font=("Arial", 18, "bold")).pack()
    tk.Label(header_frame, text=f"Kasir Bertugas: {nama_kasir}", font=("Arial", 12)).pack()
    
    main_frame = tk.Frame(window, padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)
    
    left_frame = tk.Frame(main_frame, width=300)
    left_frame.pack(side="left", fill="y", padx=(0, 20))
    
    tk.Label(left_frame, text="Input Barang", font=("Arial", 14, "bold")).pack(anchor="w", pady=(0, 15))
    
    tk.Label(left_frame, text="Pilih Barang (ID - Nama)").pack(anchor="w")
    combo_barang = ttk.Combobox(left_frame, font=("Arial", 12), width=28, state="readonly")
    combo_barang.pack(pady=(0, 10))
    
    tk.Label(left_frame, text="Jumlah").pack(anchor="w")
    entry_qty = tk.Entry(left_frame, font=("Arial", 12), width=30)
    entry_qty.pack(pady=(0, 20))
    
    btn_tambah = tk.Button(left_frame, text="TAMBAH KE KERANJANG", font=("Arial", 11, "bold"),
                           command=lambda: tambah_ke_keranjang(combo_barang, entry_qty, tree_keranjang, label_total))
    btn_tambah.pack(fill="x", pady=(0, 30))
    
    tk.Label(left_frame, text="Pembayaran", font=("Arial", 14, "bold")).pack(anchor="w", pady=(0, 10))
    
    tk.Label(left_frame, text="Uang Bayar (Rp)").pack(anchor="w")
    entry_bayar = tk.Entry(left_frame, font=("Arial", 14), width=25)
    entry_bayar.pack(pady=(0, 20))
    
    btn_bayar = tk.Button(left_frame, text="PROSES BAYAR & CETAK STRUK", font=("Arial", 12, "bold"),
                          command=lambda: proses_pembayaran(entry_bayar, tree_keranjang, label_total, combo_barang))
    btn_bayar.pack(fill="x", pady=5)
    
    btn_logout = tk.Button(left_frame, text="LOGOUT", font=("Arial", 12, "bold"),
                           command=fungsi_logout)
    btn_logout.pack(side="bottom", fill="x", pady=20)
    
    right_frame = tk.Frame(main_frame)
    right_frame.pack(side="right", fill="both", expand=True)
    
    tk.Label(right_frame, text="Keranjang Belanja", font=("Arial", 14, "bold")).pack(anchor="w", pady=(0, 10))
    
    kolom = ("Nama", "Qty", "Harga", "Subtotal")
    tree_keranjang = ttk.Treeview(right_frame, columns=kolom, show="headings", height=12)
    
    tree_keranjang.heading("Nama", text="Nama Barang")
    tree_keranjang.column("Nama", width=200, anchor="w")
    tree_keranjang.heading("Qty", text="Qty")
    tree_keranjang.column("Qty", width=50, anchor="center")
    tree_keranjang.heading("Harga", text="Harga Satuan")
    tree_keranjang.column("Harga", width=100, anchor="e")
    tree_keranjang.heading("Subtotal", text="Subtotal")
    tree_keranjang.column("Subtotal", width=120, anchor="e")
    
    tree_keranjang.pack(fill="both", expand=True)
    
    label_total = tk.Label(right_frame, text="Total: Rp 0", font=("Arial", 20, "bold"))
    label_total.pack(anchor="e", pady=15)
    
    muat_data_combobox(combo_barang)
