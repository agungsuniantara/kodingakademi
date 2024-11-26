import tkinter as tk
from tkinter import messagebox
import os

# Direktori untuk menyimpan file
folder = r"D:\Python\Eka GUI Design\Teks"

# Membuat jendela utama
root = tk.Tk()
root.title("Portal Pendaftaran Mahasiswa KKN")
root.geometry("800x600")

# Data Kecamatan
data_kecamatan = {
    "Kab. Badung": ["Kuta", "Kuta Utara", "Kuta Selatan", "Mengwi", "Abiansemal", "Petang"],
    "Kota Denpasar": ["Denpasar Utara", "Denpasar Timur", "Denpasar Barat", "Denpasar Selatan"],
    "Kab. Gianyar": ["Blahbatuh", "Gianyar", "Payangan", "Sukawati", "Tampaksiring", "Tegallalang", "Ubud"],
    "Kab. Bangli": ["Susut", "Bangli", "Tembuku", "Kintamani"],
    "Kab. Buleleng": ["Gerokgak", "Seririt", "Busungbiu", "Banjar", "Sukasada", "Buleleng", "Sawan", "Kubutambahan", "Tejakula"],
    "Kab. Jembrana": ["Negara", "Mendoyo", "Pekutatan", "Melaya", "Jembrana"],
    "Kab. Karangasem": ["Rendang", "Sidemen", "Manggis", "Karangasem", "Abang", "Bebandem", "Selat", "Kubu"],
    "Kab. Klungkung": ["Nusa Penida", "Banjarangkan", "Klungkung", "Dawan"],
    "Kab. Tabanan": ["Selemadeg", "Selemadeg Timur", "Selemadeg Barat", "Kerambitan", "Tabanan", "Kediri", "Marga", "Penebel", "Baturiti", "Pupuan"],
}

# Fungsi untuk memperbarui dropdown kecamatan
def update_kecamatan(*args):
    selected_kabupaten = var_options.get()
    kecamatan_options = data_kecamatan.get(selected_kabupaten, ["Pilih Lokasi Kecamatan"])

    menu = option_menu_kecamatan["menu"]
    menu.delete(0, "end")
    for kecamatan in kecamatan_options:
        menu.add_command(label=kecamatan, command=lambda value=kecamatan: var_data_kecamatan.set(value))
    var_data_kecamatan.set("Pilih Lokasi Kecamatan")

# Fungsi untuk membaca input dari file dan menampilkan di kolom tampil
def read_text():
    nama_kelompok = teks_nama_kelompok.get()
    if not nama_kelompok:
        messagebox.showerror("Error", "Nama Kelompok tidak boleh kosong.")
        return

    file_path = os.path.join(folder, f"{nama_kelompok}.txt")
    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"File '{nama_kelompok}.txt' tidak ditemukan.")
        return

    with open(file_path, "r") as file:
        data = file.read()

    kolom_tampil.delete("1.0", tk.END)
    kolom_tampil.insert(tk.END, data)

# Fungsi untuk membaca input dari GUI dan menampilkan di kolom tampil
def create_text():
    nama_kelompok = teks_nama_kelompok.get()
    ketua = teks_ketua_kelompok.get()
    anggota1 = teks_anggota1_kelompok.get()
    anggota2 = teks_anggota2_kelompok.get()
    anggota3 = teks_anggota3_kelompok.get()
    lokasi_kab = var_options.get()
    kecamatan = var_data_kecamatan.get()
    
    # Cek tema edukasi
    tema = []
    if tema_var1.get():
        tema.append("Waspada Investasi Bodong")
    if tema_var2.get():
        tema.append("Pengelolaan Keuangan")
    if tema_var3.get():
        tema.append("Financial Technology")
    
    # Tampilkan hasil di kolom tampil
    hasil = (
        f"Nama Kelompok: {nama_kelompok}\n"
        f"Ketua: {ketua}\n"
        f"Anggota 1: {anggota1}\n"
        f"Anggota 2: {anggota2}\n"
        f"Anggota 3: {anggota3}\n"
        f"Tema Edukasi: {', '.join(tema)}\n"
        f"Lokasi KKN: {lokasi_kab}\n"
        f"Kecamatan: {kecamatan}\n"
    )
    kolom_tampil.delete("1.0", tk.END)
    kolom_tampil.insert(tk.END, hasil)

    # Simpan ke file
    file_path = os.path.join(folder, f"{nama_kelompok}.txt")
    with open(file_path, "w") as file:
        file.write(hasil)

# Fungsi untuk mengganti teks dan tersimpan
def update_txt():
    try:
        # Ambil input teks yang akan diganti dan teks baru
        search = teks_search.get()
        new = teks_update.get()
        nama_kelompok = teks_nama_kelompok.get()

        if not nama_kelompok:
            messagebox.showerror("Error", "Nama Kelompok tidak boleh kosong.")
            return

        # Path file yang akan diperbarui
        file_path = os.path.join(folder, f"{nama_kelompok}.txt")
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"File '{nama_kelompok}.txt' tidak ditemukan.")
            return

        # Baca teks dari file
        with open(file_path, "r") as file:
            current_text = file.read()

        # Ganti teks lama dengan teks baru
        updated_text = current_text.replace(search, new)

        # Perbarui kolom tampil
        kolom_tampil.delete("1.0", tk.END)
        kolom_tampil.insert(tk.END, updated_text)

        # Simpan teks yang diperbarui ke file
        with open(file_path, "w") as file:
            file.write(updated_text)

        # Pesan konfirmasi
        messagebox.showinfo("Success", f"File '{nama_kelompok}.txt' berhasil diperbarui.")
        
        # Kosongkan kolom search dan update
        teks_search.delete(0, tk.END)
        teks_update.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


# Variabel untuk dropdown kabupaten/kota
var_options = tk.StringVar(root)
var_options.set("Pilih Lokasi Kab/Kota")
var_options.trace("w", update_kecamatan)

# Variabel untuk dropdown kecamatan
var_data_kecamatan = tk.StringVar(root)
var_data_kecamatan.set("Pilih Lokasi Kecamatan")

# Variabel untuk checkbox tema edukasi
tema_var1 = tk.BooleanVar()
tema_var2 = tk.BooleanVar()
tema_var3 = tk.BooleanVar()

# Desain GUI
# Nama Kelompok

tk.Label(root, text="Nama Kelompok:").place(x=10, y=10)
teks_nama_kelompok = tk.Entry(root, width=100)
teks_nama_kelompok.place(x=150, y=10)

anggota_kelompok = tk.Label(
    root,
    text="Daftar Anggota Kelompok : ",
)
anggota_kelompok.place(x=10, y=40)

# Ketua Kelompok
tk.Label(root, text="Ketua Kelompok:").place(x=10, y=60)
teks_ketua_kelompok = tk.Entry(root, width=40)
teks_ketua_kelompok.place(x=10, y=80)

# Anggota Kelompok
tk.Label(root, text="Anggota 1:").place(x=10, y=100)
teks_anggota1_kelompok = tk.Entry(root, width=40)
teks_anggota1_kelompok.place(x=10, y=120)

tk.Label(root, text="Anggota 2:").place(x=10, y=140)
teks_anggota2_kelompok = tk.Entry(root, width=40)
teks_anggota2_kelompok.place(x=10, y=160)

tk.Label(root, text="Anggota 3:").place(x=10, y=180)
teks_anggota3_kelompok = tk.Entry(root, width=40)
teks_anggota3_kelompok.place(x=10, y=200)

# Tema Edukasi
tk.Label(root, text="Tema Edukasi ke Masyarakat:").place(x=10, y=240)
tk.Checkbutton(root, text="Waspada Investasi Bodong", variable=tema_var1).place(x=10, y=260)
tk.Checkbutton(root, text="Pengelolaan Keuangan", variable=tema_var2).place(x=10, y=280)
tk.Checkbutton(root, text="Financial Technology", variable=tema_var3).place(x=10, y=300)

# Dropdown Lokasi
tk.Label(root, text="Informasi Lokasi Dati II KKN:").place(x=300, y=60)
option_menu = tk.OptionMenu(root, var_options, *data_kecamatan.keys())
option_menu.place(x=300, y=80)

tk.Label(root, text="Kecamatan KKN:").place(x=300, y=120)
option_menu_kecamatan = tk.OptionMenu(root, var_data_kecamatan, "Pilih Lokasi Kecamatan")
option_menu_kecamatan.place(x=300, y=140)

# Kolom Tampil
tk.Label(root, text="Tampil:").place(x=300, y=190)
kolom_tampil = tk.Text(root, width=60, height=15)
kolom_tampil.place(x=300, y=210)

# Search and Update
tk.Label(root, text="Search text:").place(x=300, y=470)
teks_search = tk.Entry(root, width=30)
teks_search.place(x=300, y=490)

tk.Label(root, text="Update text:").place(x=500, y=470)
teks_update = tk.Entry(root, width=30)
teks_update.place(x=500, y=490)

# Tombol
tk.Button(root, text="Create", command=create_text).place(x=670, y=40)
tk.Button(root, text="Read", command=read_text).place(x=620, y=40)
tk.Button(root, text="Update", command=update_txt).place(x=700, y=490)

# Jalankan aplikasi
root.mainloop()