import tkinter as tk
from tkinter import ttk
import os

data_directory = r"pariwisata_bali\datanew"
list_file = r"pariwisata_bali\datanew\all.txt"

def load_destinations_to_listbox(listbox, category):
    listbox.delete(0, tk.END)  # Hapus item sebelumnya dari listbox
    file_path = os.path.join(data_directory, f"{category.lower()}.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = file.readlines()
            for i in data:
                listbox.insert(tk.END, i.strip())  # Tambahkan data ke listbox

def on_checkbox1_clicked():
    if checkbox1_var.get() == 1:
        load_destinations_to_listbox(listbox1, "all")
    else:
        listbox1.delete(
            0, tk.END
        )  # Hapus item pada listbox1 jika checkbox1 tidak dicentang
    update_combo_values()

def update_combo_values():
    if checkbox2_var.get() == 1:
        combo["values"] = [
            "danau",
            "desa",
            "family",
            "fauna",
            "kebun",
            "monumen",
            "museum",
            "pasar",
            "pura",
            "sawah",
            "sunrise",
            "sunset",
        ]
        combo_var.set("Pilih Kategori")  # Set nilai default pada combo
    else:
        combo["values"] = [
            "Pilih Kategori"
        ]  # Tulisan awal ketika checkbox2 tidak dicentang
        combo_var.set("Pilih Kategori")  # Set nilai default pada combo
        listbox2.delete(
            0, tk.END
        )  # Hapus data pada listbox2 jika checkbox2 tidak dicentang


def on_select_button_clicked():
    selected_category = combo_var.get()
    if selected_category != "Pilih Kategori":
        load_destinations_to_listbox(listbox2, selected_category)


# Membuat jendela utama
root = tk.Tk()
root.title("GUI PYTHON")

# Menentukan ukuran jendela
root.geometry("600x420")

# Membuat LabelFrame di sekitar elemen-elemen berikut
label_frame = tk.LabelFrame(root)
label_frame.place(x=10, y=10, width=580, height=400)

# Membuat label
label = tk.Label(
    root,
    text="Selamat datang! \n Ayo tentukan destinasi di pulau bali sesuai keinginanmu",
)
label.place(x=150, y=10)

# Membuat variabel IntVar untuk menyimpan nilai checkbox1
checkbox1_var = tk.IntVar()

# Membuat checkbox
checkbox1 = tk.Checkbutton(
    root,
    text="Daftar Seluruh Wisata",
    variable=checkbox1_var,
    command=on_checkbox1_clicked,
)
checkbox1.place(x=20, y=70)

# Membuat variabel IntVar untuk menyimpan nilai checkbox2
checkbox2_var = tk.IntVar()

# Membuat checkbox
checkbox2 = tk.Checkbutton(
    root,
    text="Pilih Wisata Berdasarkan Kategori",
    variable=checkbox2_var,
    command=on_checkbox1_clicked,  # Update combo values saat checkbox2 diklik
)
checkbox2.place(x=300, y=70)

# Membuat kotak teks (Text)
listbox1 = tk.Listbox(root, width=40, height=17)
listbox1.place(x=20, y=110)

# Membuat variabel StringVar untuk menyimpan nilai combo
combo_var = tk.StringVar()

combo = ttk.Combobox(
    root, state="readonly", values=["Pilih Kategori"], textvariable=combo_var
)
combo.place(x=280, y=110, width=200)
combo.set("Pilih Kategori")  # Set tulisan awal sebagai nilai default
button = ttk.Button(text="Select", command=on_select_button_clicked)
button.place(x=490, y=108)

listbox2 = tk.Listbox(root, width=45, height=10)
listbox2.place(x=280, y=150)

# Menjalankan aplikasi GUI
root.mainloop()
