import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

Username = "admin"
Password = "1234"

book_list = [] 

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "gadistya" and password == "2914":
        messagebox.showinfo("Login, Login Berhasil!")
        window.destroy() #destroy tu ilang atau menutup
        show_main_window() 
    else:
        messagebox.showerror("Login Gagal", "Username atau password tidak tepat!")

def tambah_buku():
    judul = judul_entry.get()
    penulis = penulis_entry.get()
    harga = harga_entry.get()
    if not judul or not penulis or not harga:
        messagebox.showerror("Gagal", "Data tidak lengkap, Gagal Menyimpan Data")
        return
    try:
        harga = float(harga)  
    except ValueError:
        messagebox.showerror("Gagal", "Harga harus berupa angka")
        return
    
    book_list.append((judul, penulis, f"Rp {harga:,.0f}"))
    messagebox.showinfo("Sukses", "Berhasil Menambah Data Baru")
    update_treeview()

    judul_entry.delete(0, tk.END)
    penulis_entry.delete(0, tk.END)
    harga_entry.delete(0, tk.END)

def update_treeview():
    for row in tree.get_children():
        tree.delete(row) 
    for i, book in enumerate(book_list, start=1):
        tree.insert("", "end", values=(i, *book))  

def show_main_window(): 
    global tree
    global judul_entry, penulis_entry, harga_entry, tree

    main_window = tk.Tk()
    main_window.title("Manajemen Buku Toko")
    main_window.geometry("600x400")
    main_window.configure(bg="#f0f0f0")

    input_frame = tk.LabelFrame(main_window, text="Tambah Buku Baru", padx=10, pady=10, font=("Arial", 12, "bold"))
    input_frame.pack(pady=10, padx=10, fill="x")

    tk.Label(input_frame, text="Judul Buku").grid(row=0, column=0, sticky="w")
    judul_entry = tk.Entry(input_frame, width=50)
    judul_entry.grid(row=0, column=1, pady=5)

    tk.Label(input_frame, text="Penulis").grid(row=1, column=0, sticky="w")
    penulis_entry = tk.Entry(input_frame, width=50)
    penulis_entry.grid(row=1, column=1, pady=5)

    tk.Label(input_frame, text="Harga").grid(row=2, column=0, sticky="w")
    harga_entry = tk.Entry(input_frame, width=50)
    harga_entry.grid(row=2, column=1, pady=5)

    tk.Button(input_frame, text="Tambah Buku", command=tambah_buku, bg="#4CAF50", fg="white", width=20).grid(row=3, columnspan=2, pady=10)

    tree_frame = tk.Frame(main_window)
    tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

    tree_scroll = tk.Scrollbar(tree_frame)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, columns=("No", "Judul", "Penulis", "Harga"), show="headings")
    tree.pack(fill="both", expand=True)
    tree_scroll.config(command=tree.yview)

    tree.heading("No", text="No")
    tree.heading("Judul", text="Judul Buku")
    tree.heading("Penulis", text="Penulis")
    tree.heading("Harga", text="Harga")

    tree.column("No", width=50, anchor="center")
    tree.column("Judul", anchor="w")
    tree.column("Penulis", anchor="w")
    tree.column("Harga", anchor="center")

    main_window.mainloop()

window = tk.Tk()
window.title("Login")
window.geometry("300x250")
window.configure(bg="#e0e0e0")

tk.Label(window, text="Silakan Login", font=("Arial", 14, "bold"), bg="#e0e0e0").pack(pady=10) #jendela prtm yg muncul pas program jalan

tk.Label(window, text="Username *", bg="#e0e0e0").pack()
entry_username = tk.Entry(window)
entry_username.pack()

tk.Label(window, text="Password *", bg="#e0e0e0").pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

tk.Button(window, text="Login", command=login, bg="#2196F3", fg="white", width=15).pack(pady=15)

window.mainloop()