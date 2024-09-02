import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("GUI PYTHON")
root.geometry("400x600")

# Fungsi untuk menangani klik tombol
def on_button_click():
    label["text"] = f"Hello, {entry.get()}!"

# Fungsi untuk menangani perubahan pada Listbox
def on_listbox_select(event):
    selected_item = listbox.get(listbox.curselection())
    label["text"] = f"Item yang dipilih: {selected_item}"

# Fungsi untuk menangani perubahan pada Checkbutton
def on_checkbox_change():
    if checkbox_var.get() == 1:
        label["text"] = "Nama ditampilkan"
    else:
        label["text"] = "Nama tidak ditampilkan"

# Fungsi untuk menangani perubahan pada Radiobutton
def on_radio_change():
    label["text"] = f"Jenis kelamin: {var_radio.get()}"

# Fungsi untuk menangani perubahan pada OptionMenu
def on_option_menu_change(*args):
    label["text"] = f"Option terpilih: {var_options.get()}"

# Fungsi untuk menangani perubahan pada Scale
def on_scale_change(value):
    label["text"] = f"Nilai Scale: {value}"

# Fungsi untuk menangani perubahan pada Spinbox
def on_spinbox_change():
    label["text"] = f"Nilai Spinbox: {spinbox.get()}"

# Membuat label
label = tk.Label(root, text="ini label")
label.place(x=10, y=10)

# Membuat kotak input teks
entry = tk.Entry(root)
entry.place(x=10, y=40)

# Membuat tombol
button = tk.Button(root, text="Klik Saya", command=on_button_click)
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
listbox.bind("<<ListboxSelect>>", on_listbox_select)  # Mengikat fungsi on_listbox_select saat ada item yang dipilih

# Membuat kotak centang
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Tampilkan nama", variable=checkbox_var, command=on_checkbox_change)
checkbox.place(x=10, y=300)

# Membuat tombol radio
var_radio = tk.StringVar(root)
var_radio.set("Laki-laki")
male_radio = tk.Radiobutton(root, text="Laki-laki", variable=var_radio, value="Laki-laki", command=on_radio_change)
female_radio = tk.Radiobutton(root, text="Perempuan", variable=var_radio, value="Perempuan", command=on_radio_change)
male_radio.place(x=10, y=330)
female_radio.place(x=100, y=330)

# Membuat OptionMenu (Menu Pilihan)
options = ["Option 1", "Option 2", "Option 3"]
var_options = tk.StringVar(root)
var_options.set(options[0])
option_menu = tk.OptionMenu(root, var_options, *options)
option_menu.place(x=10, y=360)
var_options.trace_add("write", on_option_menu_change)  # Mengikat fungsi on_option_menu_change saat ada perubahan

# Membuat scale
scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, command=on_scale_change)
scale.place(x=10, y=400)

# Membuat spinbox
spinbox = tk.Spinbox(root, from_=0, to=10, increment=0.1, command=on_spinbox_change)
spinbox.place(x=10, y=460)

# Menjalankan aplikasi GUI
root.mainloop()
