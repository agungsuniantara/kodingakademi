import tkinter as tk
from tkinter import ttk, messagebox

book_list = [] 

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
        return
        
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login", "Login Berhasil!")
        window.destroy() 
        show_main_window()
    else:
        messagebox.showerror("Login Gagal", "Username atau password tidak tepat!")

def on_enter(event):
    login()

def buat_input(frame, text, row, col):
    label = tk.Label(frame, text=text, anchor="w", width=12)
    label.grid(row=row, column=col, padx=10, pady=8, sticky="w")
    entry = tk.Entry(frame, width=25)
    entry.grid(row=row, column=col+1, padx=10, pady=8)
    return entry

def tambah_data():
    no = len(book_list) + 1
    data = (
        no,
        no_isbn_entry.get(),
        judul_entry.get(),
        penulis_entry.get(),
        harga_jual_entry.get(),
        penerbit_entry.get(),
        harga_pokok_entry.get(),
        tahun_entry.get(),
        stok_entry.get()
    )
    if all(data[1:]):
        book_list.append(data)
        tampil_data()
        clear_entries()
        messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")
    else:
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")

def hapus_data():
    try:
        selected_item = tree.selection()[0]
        item_index = tree.index(selected_item)
        del book_list[item_index]
        tampil_data()
        messagebox.showinfo("Sukses", "Data berhasil dihapus!")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")

def tampil_data():
    for item in tree.get_children():
        tree.delete(item)
    for book in book_list:
        tree.insert("", "end", values=book)

def cari_data():
    query = cari_entry.get().lower()
    for item in tree.get_children():
        tree.delete(item)
    for book in book_list:
        if query in book[2].lower():
            tree.insert("", "end", values=book)

def clear_entries():
    no_isbn_entry.delete(0, tk.END)
    judul_entry.delete(0, tk.END)
    penulis_entry.delete(0, tk.END)
    harga_jual_entry.delete(0, tk.END)
    penerbit_entry.delete(0, tk.END)
    harga_pokok_entry.delete(0, tk.END)
    tahun_entry.delete(0, tk.END)
    stok_entry.delete(0, tk.END)

def show_main_window(): 
    main_window = tk.Tk()
    main_window.title("Form Input Data Buku")
    main_window.geometry("")
    main_window.resizable(False, False)
    
    # Frame Input Data
    frame_input = tk.LabelFrame(main_window, text="Input Data", font=("Arial", 10, "bold"), padx=15, pady=15)
    frame_input.pack(padx=20, pady=15, fill="x", ipadx=10, ipady=10)

    global no_isbn_entry, judul_entry, penulis_entry, harga_jual_entry, cari_entry, tree, penerbit_entry, harga_pokok_entry, tahun_entry, stok_entry
    no_isbn_entry = buat_input(frame_input, "No ISBN:", 1, 0)
    penerbit_entry = buat_input(frame_input, "Penerbit:", 2, 0)
    harga_pokok_entry = buat_input(frame_input, "Harga Pokok:", 3, 0)
    harga_jual_entry = buat_input(frame_input, "Harga Jual:", 4, 0)

    judul_entry = buat_input(frame_input, "Judul:", 1, 2)
    penulis_entry = buat_input(frame_input, "Penulis:", 2, 2)
    tahun_entry = buat_input(frame_input, "Tahun:", 3, 2)
    stok_entry = buat_input(frame_input, "Stok:", 4, 2)

    frame_utama = tk.Frame(main_window, padx=10, pady=10)
    frame_utama.pack(padx=20, pady=5, fill="x")

    frame_tombol = tk.LabelFrame(frame_utama, text="Tombol", font=("Arial", 10, "bold"), padx=10, pady=10)
    frame_tombol.pack(side="left", padx=5, pady=5)

    btn_tambah = tk.Button(frame_tombol, text="Tambah", command=tambah_data, width=15)
    btn_tambah.pack(side="left", padx=5)
    btn_hapus = tk.Button(frame_tombol, text="Hapus", command=hapus_data, width=15)
    btn_hapus.pack(side="left", padx=5)

    frame_keterangan = tk.LabelFrame(frame_utama, text="Keterangan", font=("Arial", 10, "bold"), padx=10, pady=10)
    frame_keterangan.pack(side="left", padx=5, pady=5, fill="x", expand=True)

    label_keterangan = tk.Label(frame_keterangan, text="Untuk ubah dan hapus, klik tabel terlebih dahulu")
    label_keterangan.pack(padx=5, pady=5)

    frame_pencarian = tk.LabelFrame(main_window, text="Pencarian", font=("Arial", 10, "bold"), padx=10, pady=10)
    frame_pencarian.pack(padx=20, pady=5, fill="x")

    label_cari = tk.Label(frame_pencarian, text="Cari Judul", anchor="w", width=12)
    label_cari.grid(row=0, column=0, padx=5, pady=2)
    cari_entry = tk.Entry(frame_pencarian, width=40)
    cari_entry.grid(row=0, column=1, padx=5, pady=2)
    btn_cari = tk.Button(frame_pencarian, text="Cari", command=cari_data, width=10)
    btn_cari.grid(row=0, column=2, padx=5, pady=2)

    frame_tabel = tk.LabelFrame(main_window, text="Tabel Data Buku", font=("Arial", 10, "bold"), padx=10, pady=10)
    frame_tabel.pack(padx=20, pady=5, fill="both", expand=True)

    tree = ttk.Treeview(frame_tabel, columns=("No", "No ISBN", "Judul", "Penulis", "Harga", "Penerbit", "Harga Pokok", "Tahun", "Stok"), show="headings")
    for col in ("No", "No ISBN", "Judul", "Penulis", "Harga", "Penerbit", "Harga Pokok", "Tahun", "Stok"):
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(fill="both", expand=True)

    main_window.mainloop()

# Login Window
window = tk.Tk()
window.title("Login")
window.geometry("300x250")

tk.Label(window, text="Silakan Login", font=("Arial", 14, "bold")).pack(pady=20)

tk.Label(window, text="Username *").pack()
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

tk.Label(window, text="Password *").pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

entry_password.bind('<Return>', on_enter)

button_frame = tk.Frame(window, pady=15)
button_frame.pack()

tk.Button(button_frame, text="Login", command=login, width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Keluar", command=window.destroy, width=10).pack(side=tk.LEFT, padx=5)

window.mainloop()
