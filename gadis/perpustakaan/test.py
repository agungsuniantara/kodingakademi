import tkinter as tk

# Membuat root window tanpa ukuran tetap
root = tk.Tk()
root.title("Form Input Data Buku")
root.geometry("")  # Window otomatis menyesuaikan isi
root.resizable(False, False)  # Mengunci ukuran window

# Frame Utama menggunakan LabelFrame
frame_utama = tk.LabelFrame(root, text="Input Data", font=("Arial", 10, "bold"),
                            padx=10, pady=10, bd=2, relief="groove", labelanchor="nw")
frame_utama.pack(padx=10, pady=10, fill="both", expand=True)

# Fungsi untuk membuat label dan entry
def buat_input(frame, text, row, col):
    label = tk.Label(frame, text=text, anchor="w", width=12)
    label.grid(row=row, column=col, padx=5, pady=5, sticky="w")
    entry = tk.Entry(frame, width=25)
    entry.grid(row=row, column=col+1, padx=5, pady=5)
    return entry

# Kolom kiri
no_isbn_entry = buat_input(frame_utama, "No ISBN:", 1, 0)
penerbit_entry = buat_input(frame_utama, "Penerbit:", 2, 0)
harga_pokok_entry = buat_input(frame_utama, "Harga Pokok:", 3, 0)
harga_jual_entry = buat_input(frame_utama, "Harga Jual:", 4, 0)

# Kolom kanan
judul_entry = buat_input(frame_utama, "Judul:", 1, 2)
penulis_entry = buat_input(frame_utama, "Penulis:", 2, 2)
tahun_entry = buat_input(frame_utama, "Tahun:", 3, 2)
stok_entry = buat_input(frame_utama, "Stok:", 4, 2)

# Tombol Simpan
btn_simpan = tk.Button(frame_utama, text="Simpan", width=10)
btn_simpan.grid(row=5, column=0, columnspan=4, pady=10)

# Menjalankan aplikasi
root.mainloop()
