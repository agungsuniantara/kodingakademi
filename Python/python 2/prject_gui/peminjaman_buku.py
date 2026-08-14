from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

file_name = "data.txt"
data_buku = "buku.txt"

def bersihkan_form():
    kode_box.delete(0, END)
    judul_box.delete(0, END)
    pengarang_box.delete(0, END)

def proses_tambah_buku():
    kode = kode_box.get().strip()
    judul = judul_box.get().strip()
    pengarang = pengarang_box.get().strip()
    
    kategori = kategori_listbox.curselection()
    if kategori:
        chosen_kategori = kategori[0]
        data_kategori = kategori_listbox.get(chosen_kategori)
    else:
        data_kategori = "Umum"
        
    status = "Tersedia"
    
    if not kode or not judul:
        messagebox.showerror("Error", "Kode Buku dan Judul tidak boleh kosong!")
        return

    with open(data_buku, "a") as file:
        file.write(f"{kode} | {judul} | {data_kategori} | {pengarang} | {status}\n")
    
    messagebox.showinfo("Sukses", "Buku berhasil ditambahkan!")
    bersihkan_form()

def pinjam_buku():
    kode = kode_box.get().strip()
    if not kode:
        messagebox.showerror("Error", "Masukkan Kode Buku yang ingin dipinjam!")
        return
        
    with open(data_buku, "r") as file:
        lines = file.readlines()

    found = False
    updated_lines = []
    
    for baris in lines:
        data_split = baris.split("|")
        if len(data_split) >= 5:
            data_kode = data_split[0].strip()
            if kode == data_kode:
                found = True
                status_sekarang = data_split[4].strip()
                
                if status_sekarang == "Dipinjam":
                    messagebox.showwarning("Gagal", "Buku ini sedang dipinjam!")
                    return
                else:
                    baris_baru = f"{data_split[0].strip()} | {data_split[1].strip()} | {data_split[2].strip()} | {data_split[3].strip()} | Dipinjam\n"
                    updated_lines.append(baris_baru)
            else:
                updated_lines.append(baris)
        else:
            updated_lines.append(baris)

    if found:
        with open(data_buku, "w") as file:
            file.writelines(updated_lines)
        messagebox.showinfo("Sukses", "Buku berhasil dipinjam!")
        bersihkan_form()
    else:
        messagebox.showerror("Error", "Kode Buku tidak ditemukan!")

def kembalikan_buku():
    kode = kode_box.get().strip()
    if not kode:
        messagebox.showerror("Error", "Masukkan Kode Buku yang ingin dikembalikan!")
        return
        
    with open(data_buku, "r") as file:
        lines = file.readlines()

    found = False
    updated_lines = []
    
    for baris in lines:
        data_split = baris.split("|")
        if len(data_split) >= 5:
            data_kode = data_split[0].strip()
            if kode == data_kode:
                found = True
                status_sekarang = data_split[4].strip()
                
                if status_sekarang == "Tersedia":
                    messagebox.showwarning("Gagal", "Buku ini sudah berada di perpustakaan!")
                    return
                else:
                    baris_baru = f"{data_split[0].strip()} | {data_split[1].strip()} | {data_split[2].strip()} | {data_split[3].strip()} | Tersedia\n"
                    updated_lines.append(baris_baru)
            else:
                updated_lines.append(baris)
        else:
            updated_lines.append(baris)

    if found:
        with open(data_buku, "w") as file:
            file.writelines(updated_lines)
        messagebox.showinfo("Sukses", "Buku berhasil dikembalikan!")
        bersihkan_form()
    else:
        messagebox.showerror("Error", "Kode Buku tidak ditemukan!")

# 4. FUNGSI HAPUS BUKU
def hapus_buku():
    kode = kode_box.get().strip()
    if not kode:
        messagebox.showerror("Error", "Masukkan Kode Buku yang ingin dihapus!")
        return
        
    with open(data_buku, "r") as file:
        lines = file.readlines()

    found = False
    updated_lines = []
    
    for baris in lines:
        data_split = baris.split("|")
        if len(data_split) >= 5:
            data_kode = data_split[0].strip()
            if kode == data_kode:
                found = True 
            else:
                updated_lines.append(baris)
        else:
            updated_lines.append(baris)

    if found:
        with open(data_buku, "w") as file:
            file.writelines(updated_lines)
        messagebox.showinfo("Hapus", "Buku berhasil dihapus!")
        bersihkan_form()
    else:
        messagebox.showerror("Error", "Kode Buku tidak ditemukan!")

def login():
    username = username_box.get().strip()
    password = password_box.get().strip()
    
    if not username or not password:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong")
        return

    found = False
    
    with open(file_name, "r") as file:
        for baris in file:
            data_split = baris.split("-")
            if len(data_split) == 2:
                file_user = data_split[0].strip()
                file_pass = data_split[1].strip()
                if username == file_user and password == file_pass:
                    found = True
                    break

    if found:
        messagebox.showinfo("Login", "Login Berhasil!")
        root.withdraw()              
        buka_halaman_perpustakaan()  
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah")

def buka_halaman_perpustakaan():
    global kode_box, judul_box, kategori_listbox, pengarang_box
    
    data = Tk()
    data.title("Sistem Peminjaman Buku Perpustakaan")
    data.geometry("550x550")
    
    judul_halaman = Label(data, text="Sistem Perpustakaan", font=("Times New Roman", 18))
    judul_halaman.grid(row=1, column=3, columnspan=2, pady=15)
    
    kode_label = Label(data, text="Kode Buku :", font=("Times New Roman", 16))
    kode_label.grid(row=3, column=1, sticky=W, padx=10)
    kode_box = Entry(data, font=("Times New Roman", 16))
    kode_box.grid(row=3, column=3, columnspan=2, pady=5)
    
    judul_label = Label(data, text="Judul Buku :", font=("Times New Roman", 16))
    judul_label.grid(row=4, column=1, sticky=W, padx=10)
    judul_box = Entry(data, font=("Times New Roman", 16))
    judul_box.grid(row=4, column=3, columnspan=2, pady=5)
    
    kategori_label = Label(data, text="Kategori :", font=("Times New Roman", 16))
    kategori_label.grid(row=5, column=1, sticky=NW, padx=10)
    kategori_listbox = Listbox(data, font=("Times New Roman", 14), height=5)
    kategori_listbox.grid(row=5, column=3, pady=5)
    kategori_listbox.insert(END, "Fiksi / Novel")
    kategori_listbox.insert(END, "Sains & Teknologi")
    kategori_listbox.insert(END, "Sejarah & Budaya")
    kategori_listbox.insert(END, "Komik / Manga")
    kategori_listbox.insert(END, "Biografi")
    
    pengarang_label = Label(data, text="Pengarang :", font=("Times New Roman", 16))
    pengarang_label.grid(row=11, column=1, sticky=W, padx=10)
    pengarang_box = Entry(data, font=("Times New Roman", 16))
    pengarang_box.grid(row=11, column=3, columnspan=2, pady=5)
    
    tambah_btn = Button(data, text="Tambah Buku", command=proses_tambah_buku)
    tambah_btn.grid(row=14, column=1, padx=5, pady=20)
    
    pinjam_btn = Button(data, text="Pinjam", command=pinjam_buku)
    pinjam_btn.grid(row=14, column=3, padx=5, pady=20)
    
    kembali_btn = Button(data, text="Kembalikan", command=kembalikan_buku)
    kembali_btn.grid(row=14, column=4, padx=5, pady=20)
    
    hapus_btn = Button(data, text="Hapus Buku", command=hapus_buku)
    hapus_btn.grid(row=14, column=5, padx=5, pady=20)
    
    keluar_btn = Button(data, text="Keluar Aplikasi", command=root.destroy)
    keluar_btn.grid(row=15, column=3, pady=10)
    
    data.mainloop()

root = Tk()
root.title("Login Petugas Perpustakaan")
root.geometry("400x400")

login_text = Label(root, text="Silahkan Login", font=("Times New Roman", 18))
login_text.grid(row=2, column=5, pady=20)

username_text = Label(root, text="Username*", font=("Times New Roman", 16))
username_text.grid(row=5, column=5, columnspan=2, sticky=W, padx=50)
username_box = Entry(root, font=("Times New Roman", 16))
username_box.grid(row=6, column=5, columnspan=2, pady=5)

password_text = Label(root, text="Password*", font=("Times New Roman", 16))
password_text.grid(row=8, column=5, columnspan=2, sticky=W, padx=50)
password_box = Entry(root, font=("Times New Roman", 16), show="*")
password_box.grid(row=9, column=5, columnspan=2, pady=5)

login_button = Button(root, text="Login", command=login)
login_button.grid(row=10, column=5, pady=20)

keluar_button = Button(root, text="Keluar", command=root.destroy)
keluar_button.grid(row=10, column=6, pady=20)

root.mainloop()