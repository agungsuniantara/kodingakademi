import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import os

def create_note():
    nim = nim_input.get().strip()
    if nim == "":
        messagebox.showwarning("Peringatan", "NIM tidak boleh kosong!")
        return

    nama_file = f"{nim}.txt"
    teks = kolom_teks.get("1.0", tk.END)

    if os.path.exists(nama_file):
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"File {nama_file} sudah ada. Timpa isi file?"
        )
        if not konfirmasi:
            return

    with open(nama_file, "w") as file:
        file.write(teks)
    kolom_teks.delete("1.0", tk.END)
    messagebox.showinfo("Sukses", f"Catatan {nama_file} berhasil disimpan.")

def read_note():
    nim = nim_input.get().strip()
    if nim == "":
        messagebox.showwarning("Peringatan", "NIM tidak boleh kosong!")
        return

    nama_file = f"{nim}.txt"
    try:
        with open(nama_file, "r") as file:
            data = file.read()
        kolom_tampil.delete("1.0", tk.END)
        kolom_tampil.insert(tk.END, data)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {nama_file} tidak ditemukan!")

def append_note():
    nim = nim_input.get().strip()
    if nim == "":
        messagebox.showwarning("Peringatan", "NIM tidak boleh kosong!")
        return

    nama_file = f"{nim}.txt"
    teks = kolom_teks.get("1.0", tk.END).strip()
    if teks == "":
        messagebox.showwarning("Peringatan", "Catatan tidak boleh kosong!")
        return

    tanggal = datetime.now().strftime("%Y-%m-%d")
    try:
        with open(nama_file, "a") as file:
            file.write(f"[{tanggal}] {teks}\n")
        kolom_teks.delete("1.0", tk.END)
        messagebox.showinfo("Sukses", f"Catatan ditambahkan ke {nama_file}.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {nama_file} tidak ditemukan!")

def update_note():
    nim = nim_input.get().strip()
    if nim == "":
        messagebox.showwarning("Peringatan", "NIM tidak boleh kosong!")
        return

    nama_file = f"{nim}.txt"
    kata_lama = kata_lama_input.get()
    kata_baru = kata_baru_input.get()

    if kata_lama == "":
        messagebox.showwarning("Peringatan", "Kata lama tidak boleh kosong!")
        return

    try:
        with open(nama_file, "r") as file:
            data = file.read()
        data = data.replace(kata_lama, kata_baru)
        with open(nama_file, "w") as file:
            file.write(data)
        kata_lama_input.delete(0, tk.END)
        kata_baru_input.delete(0, tk.END)
        messagebox.showinfo("Sukses", "Kata berhasil diganti.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {nama_file} tidak ditemukan!")

def delete_note():
    nim = nim_hapus_input.get().strip()
    if nim == "":
        messagebox.showwarning("Peringatan", "NIM tidak boleh kosong!")
        return

    nama_file = f"{nim}.txt"
    if not os.path.exists(nama_file):
        messagebox.showerror("Error", f"File {nama_file} tidak ditemukan!")
        return

    konfirmasi = messagebox.askyesno(
        "Konfirmasi",
        f"Yakin ingin menghapus file {nama_file}?"
    )
    if konfirmasi:
        os.remove(nama_file)
        nim_hapus_input.delete(0, tk.END)
        kolom_tampil.delete("1.0", tk.END)
        label_baris.config(text="Jumlah baris: -")
        messagebox.showinfo("Sukses", f"File {nama_file} berhasil dihapus.")

def count_lines():
    nim = nim_input.get().strip()
    if nim == "":
        messagebox.showwarning("Peringatan", "NIM tidak boleh kosong!")
        return

    nama_file = f"{nim}.txt"
    try:
        with open(nama_file, "r") as file:
            jumlah = sum(1 for baris in file if baris.strip() != "")
        label_baris.config(text=f"Jumlah baris: {jumlah}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {nama_file} tidak ditemukan!")

def list_files():
    kolom_tampil.delete("1.0", tk.END)
    daftar = [f for f in os.listdir() if f.endswith(".txt")]
    if daftar:
        kolom_tampil.insert(tk.END, "\n".join(sorted(daftar)))
    else:
        kolom_tampil.insert(tk.END, "Tidak ada file .txt di folder ini.")

# Membuat jendela utama
root = tk.Tk()
root.title("Manajer Catatan Mahasiswa")
root.resizable(False, False)

# === KOLOM 1: Catatan ===
frame_kiri = ttk.LabelFrame(root, text=" Catatan ")
frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

label_nim = tk.Label(frame_kiri, text="NIM :")
label_nim.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))

nim_input = tk.Entry(frame_kiri, width=22)
nim_input.grid(row=1, column=0, columnspan=2, sticky="we", padx=10)

label_teks = tk.Label(frame_kiri, text="Catatan :")
label_teks.grid(row=2, column=0, sticky="w", padx=10, pady=(8, 2))

kolom_teks = tk.Text(frame_kiri, width=28, height=9)
kolom_teks.grid(row=3, column=0, columnspan=2, padx=10)

button_create = tk.Button(frame_kiri, text="Simpan Baru", width=13, command=create_note)
button_create.grid(row=4, column=0, padx=(10, 2), pady=10, sticky="we")

button_append = tk.Button(frame_kiri, text="Tambah Catatan", width=13, command=append_note)
button_append.grid(row=4, column=1, padx=(2, 10), pady=10, sticky="we")

button_count = tk.Button(frame_kiri, text="Hitung Baris", width=13, command=count_lines)
button_count.grid(row=5, column=0, padx=(10, 2), sticky="we")

label_baris = tk.Label(frame_kiri, text="Jumlah baris: -")
label_baris.grid(row=5, column=1, padx=(2, 10), sticky="w")

# === KOLOM 2: Update & Hapus ===
frame_tengah = ttk.LabelFrame(root, text=" Edit & Hapus ")
frame_tengah.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

label_kata_lama = tk.Label(frame_tengah, text="Kata lama :")
label_kata_lama.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))

kata_lama_input = tk.Entry(frame_tengah, width=22)
kata_lama_input.grid(row=1, column=0, sticky="we", padx=10)

label_kata_baru = tk.Label(frame_tengah, text="Kata baru :")
label_kata_baru.grid(row=2, column=0, sticky="w", padx=10, pady=(8, 2))

kata_baru_input = tk.Entry(frame_tengah, width=22)
kata_baru_input.grid(row=3, column=0, sticky="we", padx=10)

button_update = tk.Button(frame_tengah, text="Ganti Kata", width=20, command=update_note)
button_update.grid(row=4, column=0, padx=10, pady=10, sticky="we")

separator = ttk.Separator(frame_tengah, orient="horizontal")
separator.grid(row=5, column=0, sticky="we", padx=10, pady=5)

label_nim_hapus = tk.Label(frame_tengah, text="NIM (hapus) :")
label_nim_hapus.grid(row=6, column=0, sticky="w", padx=10, pady=(2, 2))

nim_hapus_input = tk.Entry(frame_tengah, width=22)
nim_hapus_input.grid(row=7, column=0, sticky="we", padx=10)

button_delete = tk.Button(frame_tengah, text="Hapus File", width=20, command=delete_note)
button_delete.grid(row=8, column=0, padx=10, pady=10, sticky="we")

button_list = tk.Button(frame_tengah, text="Daftar Catatan", width=20, command=list_files)
button_list.grid(row=9, column=0, padx=10, pady=(0, 10), sticky="we")

# === KOLOM 3: Tampil ===
frame_kanan = ttk.LabelFrame(root, text=" Tampil ")
frame_kanan.grid(row=0, column=2, padx=10, pady=10, sticky="ns")

kolom_tampil = tk.Text(frame_kanan, width=36, height=17)
kolom_tampil.grid(row=0, column=0, padx=10, pady=10)

button_read = tk.Button(frame_kanan, text="Tampilkan", width=14, command=read_note)
button_read.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="we")

# Menyamakan tinggi ketiga kolom
root.update_idletasks()
tinggi_max = max(frame_kiri.winfo_reqheight(),
                 frame_tengah.winfo_reqheight(),
                 frame_kanan.winfo_reqheight())
frame_kiri.config(height=tinggi_max)
frame_tengah.config(height=tinggi_max)
frame_kanan.config(height=tinggi_max)

root.mainloop()