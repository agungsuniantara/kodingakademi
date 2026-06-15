from tkinter import *

# Inisialisasi jendela utama
root = Tk()
root.title("GUI CRUD")
root.geometry("650x350") # Menyesuaikan ukuran kira-kira seperti gambar

# ==========================================
# BARIS 0: Input Nama File
# ==========================================
label_nama = Label(root, text="Nama file :")
label_nama.grid(row=0, column=0, sticky=W, padx=10, pady=(15, 5))

entry_nama = Entry(root, width=20)
entry_nama.grid(row=0, column=1, sticky=W, pady=(15, 5))
entry_nama.insert(0, "baru") # Mengisi nilai awal sesuai gambar

# ==========================================
# BARIS 1: Label Area Teks
# ==========================================
label_teks = Label(root, text="Teks :")
label_teks.grid(row=1, column=0, sticky=W, padx=10)

label_tampil = Label(root, text="Tampil :")
label_tampil.grid(row=1, column=3, sticky=W, padx=10)

# ==========================================
# BARIS 2 & 3: Area Teks Input, Output, dan Tombol Tengah
# ==========================================
# Text Input (Kiri) - Menggabungkan 2 baris (rowspan=2) dan 2 kolom (columnspan=2)
text_input = Text(root, width=30, height=8)
text_input.grid(row=2, column=0, rowspan=2, columnspan=2, padx=10, pady=5)

# Tombol Create & Append (Tengah)
btn_create = Button(root, text="Create")
btn_create.grid(row=2, column=2, sticky=S, padx=5, pady=2) # sticky=S agar menempel ke bawah

btn_append = Button(root, text="Append")
btn_append.grid(row=3, column=2, sticky=N, padx=5, pady=2) # sticky=N agar menempel ke atas

# Text Output (Kanan) - Menggabungkan 2 baris (rowspan=2)
text_output = Text(root, width=30, height=8)
text_output.grid(row=2, column=3, rowspan=2, padx=10, pady=5)
# Mengisi nilai awal pada Tampil sesuai gambar
text_output.insert(END, "1. agung\n2. wahyu\n3. bayu") 

# Tombol Read (Paling Kanan)
btn_read = Button(root, text="Read")
btn_read.grid(row=2, column=4, sticky=N, padx=5, pady=5)

# ==========================================
# BARIS 4: Label Search dan Update
# ==========================================
label_search = Label(root, text="Search text :")
label_search.grid(row=4, column=0, sticky=W, padx=10, pady=(10, 0))

label_update = Label(root, text="Update text :")
label_update.grid(row=4, column=1, sticky=W, padx=10, pady=(10, 0))

# ==========================================
# BARIS 5: Input Search, Update, dan Tombol Update
# ==========================================
entry_search = Entry(root, width=15)
entry_search.grid(row=5, column=0, sticky=W, padx=10, pady=5)
entry_search.insert(0, "agung") # Mengisi kursor/teks sesuai gambar

entry_update = Entry(root, width=15)
entry_update.grid(row=5, column=1, sticky=W, padx=10, pady=5)

btn_update = Button(root, text="Update")
btn_update.grid(row=5, column=2, sticky=W, padx=5, pady=5)

# ==========================================
# BARIS 6 & 7: Area Hapus File
# ==========================================
label_file = Label(root, text="File:")
label_file.grid(row=6, column=0, sticky=W, padx=10, pady=(10, 0))

entry_file = Entry(root, width=15)
entry_file.grid(row=7, column=0, sticky=W, padx=10, pady=(0, 15))

btn_delete = Button(root, text="Delete")
btn_delete.grid(row=7, column=1, sticky=W, padx=10, pady=(0, 15))

# Jalankan loop aplikasi
root.mainloop()