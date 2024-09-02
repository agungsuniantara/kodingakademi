import tkinter as tk
from tkinter import StringVar, Menu

# Fungsi yang akan dipanggil saat opsi dipilih dari menu dropdown
def on_menu_select(option):
    result_text.config(text="Anda memilih: " + option)

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI dengan Menu Dropdown")

# Menentukan ukuran jendela
root.geometry("500x800")

# Membuat menu dropdown
menu_var = StringVar(root)
menu_var.set("Pilih opsi")  # Nilai awal

# Membuat Menubutton untuk menu dropdown
menu_button = tk.Menubutton(root, textvariable=menu_var, relief="raised")
menu_button.place(x=10, y=10)

# Membuat menu untuk Menubutton
menu = Menu(menu_button, tearoff=False)
menu.add_command(label="Opsi 1", command=lambda: on_menu_select("Opsi 1"))
menu.add_command(label="Opsi 2", command=lambda: on_menu_select("Opsi 2"))
menu.add_command(label="Opsi 3", command=lambda: on_menu_select("Opsi 3"))

# Menghubungkan menu dengan Menubutton
menu_button.configure(menu=menu)

# Membuat label hasil
result_text = tk.Label(root, text="", font=("Helvetica", 16))
result_text.place(x=10, y=50)

# Menjalankan aplikasi GUI
root.mainloop()
