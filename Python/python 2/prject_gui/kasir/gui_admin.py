import tkinter as tk
from tkinter import ttk, messagebox
import core_db
import session

def bersihkan_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def muat_data_tabel(tree):
    for item in tree.get_children():
        tree.delete(item)
        
    daftar_barang = core_db.ambil_semua_barang()
    
    for barang in daftar_barang:
        tree.insert("", tk.END, values=(
            barang["id_barang"], 
            barang["nama_barang"], 
            f"Rp {barang['harga']}",
            barang["stok"]
        ))

def bersihkan_form(entries):
    entries['id'].delete(0, tk.END)
    entries['nama'].delete(0, tk.END)
    entries['harga'].delete(0, tk.END)
    entries['stok'].delete(0, tk.END)

def proses_tambah_barang(entries, tree):
    id_barang = entries['id'].get().strip()
    nama = entries['nama'].get().strip()
    harga = entries['harga'].get().strip()
    stok = entries['stok'].get().strip()

    if not id_barang or not nama or not harga or not stok:
        messagebox.showerror("Error", "Semua kolom form harus diisi!")
        return

    if not harga.isdigit() or not stok.isdigit():
        messagebox.showerror("Error", "Harga dan Stok harus berupa angka yang valid!")
        return

    try:
        core_db.tambah_barang_baru(id_barang, nama, int(harga), int(stok))
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menambah barang: {e}")
        return

    messagebox.showinfo("Sukses", "Data barang berhasil ditambahkan ke sistem!")

    bersihkan_form(entries)
    muat_data_tabel(tree)

def proses_edit_barang(entries, tree):
    id_barang = entries['id'].get().strip()
    nama = entries['nama'].get().strip()
    harga = entries['harga'].get().strip()
    stok = entries['stok'].get().strip()

    if not id_barang or not nama or not harga or not stok:
        messagebox.showerror("Error", "Semua kolom form harus diisi!")
        return

    if not harga.isdigit() or not stok.isdigit():
        messagebox.showerror("Error", "Harga dan Stok harus berupa angka yang valid!")
        return

    try:
        core_db.edit_barang(id_barang, nama, int(harga), int(stok))
    except Exception as e:
        messagebox.showerror("Error", f"Gagal mengupdate barang: {e}")
        return

    messagebox.showinfo("Sukses", "Data barang berhasil diupdate!")

    bersihkan_form(entries)
    muat_data_tabel(tree)

def proses_hapus_barang(entries, tree):
    id_barang = entries['id'].get().strip()
    if not id_barang:
        messagebox.showerror("Error", "Masukkan ID Barang yang akan dihapus!")
        return

    konfirmasi = messagebox.askyesno("Konfirmasi", f"Hapus barang dengan ID {id_barang}?")
    if not konfirmasi:
        return

    try:
        core_db.hapus_barang(id_barang)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menghapus barang: {e}")
        return

    messagebox.showinfo("Sukses", "Barang berhasil dihapus!")
    bersihkan_form(entries)
    muat_data_tabel(tree)

def on_pilih_tabel(tree, entries):
    selected = tree.selection()
    if not selected:
        return
    values = tree.item(selected[0])["values"]
    
    # Harga di tabel tampil sebagai "Rp 5000", bersihkan agar bisa di-edit
    harga_str = str(values[2]).replace("Rp ", "").strip()
    
    bersihkan_form(entries)
    entries['id'].insert(0, values[0])
    entries['nama'].insert(0, values[1])
    entries['harga'].insert(0, harga_str)
    entries['stok'].insert(0, values[3])

def tampilkan_halaman(window, fungsi_logout):
    bersihkan_window(window)
    
    nama_admin = session.current_user["nama"] if session.current_user else "Administrator"
    
    header_frame = tk.Frame(window, pady=15)
    header_frame.pack(fill="x")
    tk.Label(header_frame, text="DASHBOARD ADMIN - INVENTORY", font=("Arial", 18, "bold")).pack()
    tk.Label(header_frame, text=f"Selamat Bekerja, {nama_admin}", font=("Arial", 12)).pack()
    
    main_frame = tk.Frame(window, padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)
    
    form_frame = tk.Frame(main_frame, width=300)
    form_frame.pack(side="left", fill="y", padx=(0, 20))
    
    tk.Label(form_frame, text="Form Barang", font=("Arial", 14, "bold")).pack(anchor="w", pady=(0, 15))
    
    tk.Label(form_frame, text="Kode / ID Barang").pack(anchor="w")
    entry_id = tk.Entry(form_frame, font=("Arial", 12), width=25)
    entry_id.pack(pady=(0, 10))
    
    tk.Label(form_frame, text="Nama Barang").pack(anchor="w")
    entry_nama = tk.Entry(form_frame, font=("Arial", 12), width=25)
    entry_nama.pack(pady=(0, 10))
    
    tk.Label(form_frame, text="Harga (Rp)").pack(anchor="w")
    entry_harga = tk.Entry(form_frame, font=("Arial", 12), width=25)
    entry_harga.pack(pady=(0, 10))
    
    tk.Label(form_frame, text="Stok").pack(anchor="w")
    entry_stok = tk.Entry(form_frame, font=("Arial", 12), width=25)
    entry_stok.pack(pady=(0, 20))
    
    entries = {'id': entry_id, 'nama': entry_nama, 'harga': entry_harga, 'stok': entry_stok}
    
    btn_frame = tk.Frame(form_frame)
    btn_frame.pack(fill="x", pady=(0, 10))
    
    tk.Button(btn_frame, text="TAMBAH", font=("Arial", 10, "bold"),
              command=lambda: proses_tambah_barang(entries, tree_barang)).pack(side="left", fill="x", expand=True, padx=(0, 3))
    tk.Button(btn_frame, text="EDIT", font=("Arial", 10, "bold"),
              command=lambda: proses_edit_barang(entries, tree_barang)).pack(side="left", fill="x", expand=True, padx=3)
    tk.Button(btn_frame, text="HAPUS", font=("Arial", 10, "bold"),
              command=lambda: proses_hapus_barang(entries, tree_barang)).pack(side="left", fill="x", expand=True, padx=(3, 0))
    
    btn_logout = tk.Button(form_frame, text="LOGOUT", font=("Arial", 12, "bold"),
                           command=fungsi_logout)
    btn_logout.pack(side="bottom", fill="x", pady=20)
    
    table_frame = tk.Frame(main_frame)
    table_frame.pack(side="right", fill="both", expand=True)
    
    tk.Label(table_frame, text="Master Data Inventaris", font=("Arial", 14, "bold")).pack(anchor="w", pady=(0, 10))
    
    kolom = ("ID", "Nama", "Harga", "Stok")
    tree_barang = ttk.Treeview(table_frame, columns=kolom, show="headings", height=15)
    
    tree_barang.heading("ID", text="ID Barang")
    tree_barang.column("ID", width=100, anchor="center")
    
    tree_barang.heading("Nama", text="Nama Barang")
    tree_barang.column("Nama", width=250, anchor="w")
    
    tree_barang.heading("Harga", text="Harga Satuan")
    tree_barang.column("Harga", width=120, anchor="e")
    
    tree_barang.heading("Stok", text="Stok")
    tree_barang.column("Stok", width=80, anchor="center")
    
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree_barang.yview)
    tree_barang.configure(yscrollcommand=scrollbar.set)
    
    scrollbar.pack(side="right", fill="y")
    tree_barang.pack(side="left", fill="both", expand=True)
    
    tree_barang.bind("<<TreeviewSelect>>", lambda e: on_pilih_tabel(tree_barang, entries))
    
    muat_data_tabel(tree_barang)