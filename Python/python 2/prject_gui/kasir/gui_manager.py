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
    daftar = core_db.ambil_semua_karyawan()
    for k in daftar:
        tree.insert("", tk.END, values=(k["id_karyawan"], k["username"], k["nama"], k["role"]))

def proses_tambah(entries, tree):
    id_k = entries['id'].get().strip()
    username = entries['username'].get().strip()
    password = entries['password'].get().strip()
    nama = entries['nama'].get().strip()
    role = entries['role'].get().strip()

    if not id_k or not username or not password or not nama or not role:
        messagebox.showerror("Error", "Semua kolom harus diisi!")
        return

    if role not in ("Admin", "Kasir", "Manager"):
        messagebox.showerror("Error", "Role harus salah satu dari: Admin, Kasir, Manager")
        return

    try:
        core_db.tambah_karyawan_baru(id_k, username, password, nama, role)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menambah karyawan: {e}")
        return

    messagebox.showinfo("Sukses", "Karyawan berhasil ditambahkan!")
    for e in entries.values():
        e.delete(0, tk.END)
    muat_data_tabel(tree)

def proses_edit(entries, tree):
    id_k = entries['id'].get().strip()
    username = entries['username'].get().strip()
    password = entries['password'].get().strip()
    nama = entries['nama'].get().strip()
    role = entries['role'].get().strip()

    if not id_k or not username or not password or not nama or not role:
        messagebox.showerror("Error", "Semua kolom harus diisi!")
        return

    if role not in ("Admin", "Kasir", "Manager"):
        messagebox.showerror("Error", "Role harus salah satu dari: Admin, Kasir, Manager")
        return

    try:
        core_db.edit_karyawan(id_k, username, password, nama, role)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal mengupdate karyawan: {e}")
        return

    messagebox.showinfo("Sukses", "Data karyawan berhasil diupdate!")
    for e in entries.values():
        e.delete(0, tk.END)
    muat_data_tabel(tree)

def proses_hapus(entries, tree):
    id_k = entries['id'].get().strip()
    if not id_k:
        messagebox.showerror("Error", "Masukkan ID Karyawan yang akan dihapus!")
        return

    if id_k == session.current_user["id"]:
        messagebox.showerror("Error", "Tidak bisa menghapus akun sendiri!")
        return

    konfirmasi = messagebox.askyesno("Konfirmasi", f"Hapus karyawan dengan ID {id_k}?")
    if not konfirmasi:
        return

    try:
        core_db.hapus_karyawan(id_k)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menghapus karyawan: {e}")
        return

    messagebox.showinfo("Sukses", "Karyawan berhasil dihapus!")
    for e in entries.values():
        e.delete(0, tk.END)
    muat_data_tabel(tree)

def on_pilih_tabel(tree, entries):
    selected = tree.selection()
    if not selected:
        return
    values = tree.item(selected[0])["values"]
    entries['id'].delete(0, tk.END)
    entries['id'].insert(0, values[0])
    entries['username'].delete(0, tk.END)
    entries['username'].insert(0, values[1])
    entries['nama'].delete(0, tk.END)
    entries['nama'].insert(0, values[2])
    entries['role'].set(values[3])
    entries['password'].delete(0, tk.END)

def tampilkan_halaman(window, fungsi_logout):
    bersihkan_window(window)

    nama_mgr = session.current_user["nama"] if session.current_user else "Manager"

    header_frame = tk.Frame(window, pady=15)
    header_frame.pack(fill="x")
    tk.Label(header_frame, text="DASHBOARD MANAGER - KELOLA KARYAWAN", font=("Arial", 18, "bold")).pack()
    tk.Label(header_frame, text=f"Selamat Bekerja, {nama_mgr}", font=("Arial", 12)).pack()

    main_frame = tk.Frame(window, padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)

    form_frame = tk.Frame(main_frame, width=300)
    form_frame.pack(side="left", fill="y", padx=(0, 20))

    tk.Label(form_frame, text="Form Karyawan", font=("Arial", 14, "bold")).pack(anchor="w", pady=(0, 15))

    tk.Label(form_frame, text="ID Karyawan").pack(anchor="w")
    entry_id = tk.Entry(form_frame, font=("Arial", 12), width=25)
    entry_id.pack(pady=(0, 10))

    tk.Label(form_frame, text="Username").pack(anchor="w")
    entry_username = tk.Entry(form_frame, font=("Arial", 12), width=25)
    entry_username.pack(pady=(0, 10))

    tk.Label(form_frame, text="Password").pack(anchor="w")
    entry_password = tk.Entry(form_frame, font=("Arial", 12), width=25)
    entry_password.pack(pady=(0, 10))

    tk.Label(form_frame, text="Nama Lengkap").pack(anchor="w")
    entry_nama = tk.Entry(form_frame, font=("Arial", 12), width=25)
    entry_nama.pack(pady=(0, 10))

    tk.Label(form_frame, text="Role").pack(anchor="w")
    combo_role = ttk.Combobox(form_frame, font=("Arial", 12), width=22, state="readonly", values=["Admin", "Kasir", "Manager"])
    combo_role.pack(pady=(0, 20))

    entries = {
        'id': entry_id, 'username': entry_username, 'password': entry_password,
        'nama': entry_nama, 'role': combo_role
    }

    btn_frame = tk.Frame(form_frame)
    btn_frame.pack(fill="x", pady=(0, 10))

    tk.Button(btn_frame, text="TAMBAH", font=("Arial", 10, "bold"),
              command=lambda: proses_tambah(entries, tree_karyawan)).pack(side="left", fill="x", expand=True, padx=(0, 3))
    tk.Button(btn_frame, text="EDIT", font=("Arial", 10, "bold"),
              command=lambda: proses_edit(entries, tree_karyawan)).pack(side="left", fill="x", expand=True, padx=3)
    tk.Button(btn_frame, text="HAPUS", font=("Arial", 10, "bold"),
              command=lambda: proses_hapus(entries, tree_karyawan)).pack(side="left", fill="x", expand=True, padx=(3, 0))

    tk.Button(form_frame, text="LOGOUT", font=("Arial", 12, "bold"),
              command=fungsi_logout).pack(side="bottom", fill="x", pady=20)

    table_frame = tk.Frame(main_frame)
    table_frame.pack(side="right", fill="both", expand=True)

    tk.Label(table_frame, text="Daftar Karyawan", font=("Arial", 14, "bold")).pack(anchor="w", pady=(0, 10))

    kolom = ("ID", "Username", "Nama", "Role")
    tree_karyawan = ttk.Treeview(table_frame, columns=kolom, show="headings", height=15)

    tree_karyawan.heading("ID", text="ID Karyawan")
    tree_karyawan.column("ID", width=100, anchor="center")
    tree_karyawan.heading("Username", text="Username")
    tree_karyawan.column("Username", width=120, anchor="w")
    tree_karyawan.heading("Nama", text="Nama Lengkap")
    tree_karyawan.column("Nama", width=200, anchor="w")
    tree_karyawan.heading("Role", text="Role")
    tree_karyawan.column("Role", width=100, anchor="center")

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree_karyawan.yview)
    tree_karyawan.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    tree_karyawan.pack(side="left", fill="both", expand=True)

    tree_karyawan.bind("<<TreeviewSelect>>", lambda e: on_pilih_tabel(tree_karyawan, entries))

    muat_data_tabel(tree_karyawan)
