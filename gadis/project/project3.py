import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

data_pengaduan = []  # Data tempat menyimpan pengaduan

# Fungsi untuk membuka jendela tambah data
def open_tambah_window(tree, tampil):
    tampil.destroy()
    tambah = Toplevel(tampil)  # Ganti Tk() dengan Toplevel
    tambah.geometry("300x200")
    tambah.configure(bg="#b1b1b1")
    tambah.title(text="Dusun Barbarscary")

    img = Image.open('gambar.jpeg')                
    img = img.resize((120, 120))                  
    img_tk = ImageTk.PhotoImage(img)   
    lbl = Label(tambah, image=img_tk)
    lbl.image = img_tk
    lbl.pack()

    Label(tambah, text="Input Page", font=("Times New Roman", 14), bg="#b1b1b1").pack(pady=10)
    Label(tambah, text="Kode ID", bg="#b1b1b1").pack()
    entry_kode = Entry(tambah)
    entry_kode.pack()

    Label(tambah, text="Nama Pengadu", bg="#b1b1b1").pack()
    entry_nama = Entry(tambah)
    entry_nama.pack()

    Label(tambah, text="Jenis", bg="#b1b1b1").pack()
    combo_jenis = ttk.Combobox(tambah, values=["Banjir", "Tawuran", "Kemalingan", "Mati Lampu"])
    combo_jenis.pack()

    Label(tambah, text="Status", bg="#b1b1b1").pack()
    status_var = StringVar(value="Proses")
    Radiobutton(tambah, text="Proses", variable=status_var, value="Proses", bg="#b1b1b1").pack()
    Radiobutton(tambah, text="Selesai", variable=status_var, value="Selesai", bg="#b1b1b1").pack()

    def simpan():
        kode = entry_kode.get()
        nama = entry_nama.get()
        jenis = combo_jenis.get()
        status = status_var.get()

        if not kode:
            messagebox.showerror("Error", "Kode ID harus diisi.")
            return
        if not nama:
            messagebox.showerror("Error", "Nama Pengadu harus diisi.")
            return
        if not jenis:
            messagebox.showerror("Error", "Jenis Harus dipilih.")
            return

        data_pengaduan.append({"Kode": kode, "Nama": nama, "Jenis": jenis, "Status": status})
        messagebox.showinfo("Sukses", "Data berhasil disimpan.")
        main_menu()  # Kembali ke halaman utama setelah simpan

    Button(tambah, text="Simpan", bg="#2E7D32", fg="white", command=simpan).pack(pady=5)
    Button(tambah, text="Kembali", bg="#C62828", fg="white", command=main_menu).pack(pady=5)

# Fungsi untuk membuka jendela ubah data
def open_ubah_window(tree, tampil):
    tampil.destroy()
    ubah = Toplevel(tampil)
    ubah.geometry("300x200")
    ubah.configure(bg="#b1b1b1")
    ubah.title("Ubah Data")

    Label(ubah, text="Masukkan Kode ID:", bg="#b1b1b1").pack(pady=10)
    entry_cari = Entry(ubah)
    entry_cari.pack()

    def cari_data():
        kode_cari = entry_cari.get()
        hasil = None
        for data in data_pengaduan:
            if data["Kode"] == kode_cari:
                hasil = data
                break
        if hasil is None:
            messagebox.showerror("Error", "Kode ID tidak ditemukan.")
        else:
            ubah.destroy()
            halaman_edit_data(hasil)

    Button(ubah, text="Ubah", bg="#2E7D32", fg="white", command=cari_data).pack(pady=5)
    Button(ubah, text="Kembali", bg="#C62828", fg="white", command=main_menu).pack(pady=5)

    def halaman_edit_data(data_awal):
        ubah2 = Toplevel(ubah)
        ubah2.geometry("300x600")
        ubah2.configure(bg="#b1b1b1")
        ubah2.title("Ubah Data")

        Label(ubah2, text="Ubah Data", font=("Times New Roman", 14), bg="#b1b1b1").pack(pady=10)

        Label(ubah2, text="Kode ID", bg="#b1b1b1").pack()
        entry_kode = Entry(ubah2)
        entry_kode.pack()
        entry_kode.insert(0, data_awal["Kode"])
        entry_kode.config(state='disabled')

        Label(ubah2, text="Nama Pengadu", bg="#b1b1b1").pack()
        entry_nama = Entry(ubah2)
        entry_nama.pack()
        entry_nama.insert(0, data_awal["Nama"])

        Label(ubah2, text="Jenis", bg="#b1b1b1").pack()
        combo_jenis = ttk.Combobox(ubah2, values=["Banjir", "Tawuran", "Kemalingan", "Mati Lampu"])
        combo_jenis.pack()
        combo_jenis.set(data_awal["Jenis"])

        Label(ubah2, text="Status", bg="#b1b1b1").pack()
        status_var = StringVar(value=data_awal["Status"])
        Radiobutton(ubah2, text="Proses", variable=status_var, value="Proses", bg="#b1b1b1").pack()
        Radiobutton(ubah2, text="Selesai", variable=status_var, value="Selesai", bg="#b1b1b1").pack()

        def simpan_perubahan():
            nama = entry_nama.get()
            jenis = combo_jenis.get()
            status = status_var.get()

            if not nama:
                messagebox.showerror("Error", "Nama Pengadu harus diisi.")
                return

            data_awal["Nama"] = nama
            data_awal["Jenis"] = jenis
            data_awal["Status"] = status
            messagebox.showinfo("Sukses", "Data berhasil diubah.")
            main_menu()

        Button(ubah2, text="Simpan", bg="#2E7D32", fg="white", command=simpan_perubahan).pack(pady=5)
        Button(ubah2, text="Kembali", bg="#C62828", fg="white", command=main_menu).pack(pady=5)

# Fungsi untuk membuka jendela hapus data
def open_hapus_window(tree, tampil):
    tampil.destroy()
    hapus = Toplevel(tampil)
    hapus.geometry("300x200")
    hapus.configure(bg="#b1b1b1")
    hapus.title("Hapus Data")

    Label(hapus, text="Masukkan Kode ID yang ingin dihapus:", bg="#b1b1b1").pack(pady=10)
    entry_hapus = Entry(hapus)
    entry_hapus.pack()

    def hapus_data():
        kode_hapus = entry_hapus.get()
        for data in data_pengaduan:
            if data["Kode"] == kode_hapus:
                data_pengaduan.remove(data)
                messagebox.showinfo("Sukses", f"Data dengan Kode ID '{kode_hapus}' berhasil dihapus.")
                main_menu()
                return
        messagebox.showerror("Error", "Kode ID tidak ditemukan.")

    Button(hapus, text="Hapus", bg="#2E7D32", fg="white", command=hapus_data).pack(pady=5)
    Button(hapus, text="Kembali", bg="#C62828", fg="white", command=main_menu).pack(pady=5)

# Fungsi utama untuk menampilkan menu utama
def main_menu():
    global tampil, tree
    try:
        tampil.destroy()
    except:
        pass

    tampil = Tk()
    tampil.geometry("300x400")
    tampil.configure(bg="#b1b1b1")
    tampil.title("Pusat Bantuan Dusun BarbarScary")

    Label(tampil, text="PUSAT BANTUAN DUSUN BARBARSCARY", font=("Times New Roman", 12), bg="#b1b1b1").pack(pady=10)
    tree = ttk.Treeview(tampil, columns=("Kode", "Nama", "Jenis", "Status"), show='headings')
    for col in ("Kode", "Nama", "Jenis", "Status"):
        tree.heading(col, text=col)
    tree.pack(pady=10)

    for data in data_pengaduan:
        tree.insert("", "end", values=(data["Kode"], data["Nama"], data["Jenis"], data["Status"]))

    Button(tampil, text="Tambah", command=lambda: open_tambah_window(tree, tampil)).pack(pady=5)
    Button(tampil, text="Ubah", command=lambda: open_ubah_window(tree, tampil)).pack(pady=5)
    Button(tampil, text="Hapus", command=lambda: open_hapus_window(tree, tampil)).pack(pady=5)

# Memulai aplikasi
main_menu()
