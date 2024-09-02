import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("GUI PYTHON")

# Menentukan ukuran jendela
root.geometry("400x600")

# Membuat label
label = tk.Label(root, text="ini label")
label.place(x=10, y=10)

# Membuat kotak input teks
entry = tk.Entry(root)
entry.place(x=10, y=40)

# Membuat tombol
button = tk.Button(root, text="Klik Saya")
button.place(x=10, y=70)

# Membuat kotak teks (Text)
text_widget = tk.Text(root, width=30, height=7)
text_widget.place(x=10, y=110)

# Membuat kotak daftar (Listbox)
listbox = tk.Listbox(root, width=20, height=3)
listbox.place(x=10, y=240)
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")
listbox.bind()  # Mengikat fungsi on_listbox_select saat ada item yang dipilih

# Membuat kotak centang
checkbox = tk.Checkbutton(root, text="Tampilkan nama")
checkbox.place(x=10, y=300)

# Membuat tombol radio
var_radio = tk.StringVar(root)
var_radio.set("Laki-laki")
male_radio = tk.Radiobutton(
    root, text="Laki-laki", variable=var_radio, value="Laki-laki"
)
female_radio = tk.Radiobutton(
    root, text="Perempuan", variable=var_radio, value="Perempuan"
)
male_radio.place(x=10, y=330)
female_radio.place(x=100, y=330)

# Membuat OptionMenu (Menu Pilihan)
options = ["Option 1", "Option 2", "Option 3"]
var_options = tk.StringVar(root)
var_options.set("selected inside")
option_menu = tk.OptionMenu(root, var_options, *options)
option_menu.place(x=10, y=360)

# Mmebuat scale
scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
scale.place(x=10, y=400)

# Mmebuat spinbox
spinbox = tk.Spinbox(root, from_=0, to=10, increment=0.1)
spinbox.place(x=10, y=460)

# Menjalankan aplikasi GUI
root.mainloop()
