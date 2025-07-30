import tkinter as tk 

# membuat jendela utama
root = tk.Tk()
root.title("GUI PYTHON")

# menentukan ukuran jendela
root.geometry("400x600") # ("width x height")

# membuat label
label = tk.Label(root, text = "ini label")
label.place(x = 10, y = 10)

# membuat kotak input teks
entry = tk.Entry(root)
entry.place(x = 10, y = 40)

# membuat button
button = tk.Button(root, text="Klik Saya")
button.place(x=10, y=70)

# membuat kotak teks (Text)
text_widget = tk.Text(root, width=30, height=7)
text_widget.place(x = 10, y = 110)

# membuat kotak daftar (listbox)
listbox = tk.Listbox(root, width=20, height=3)
listbox.place(x=10, y=240)
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")
listbox.bind()

# membuat kotak centang
checkbox = tk.Checkbutton(root, text="Tampilkan nama")
checkbox.place(x=10, y=300)

# membuat tombol radio
var_radio = tk.StringVar(root)
var_radio.set("Perempuan")
male_radio = tk.Radiobutton(root, text="Laki-laki", variable=var_radio, value="Laki-laki")
female_radio = tk.Radiobutton(root, text="Perempuan", variable=var_radio, value="Perempuan")
male_radio.place(x=10, y=330)
female_radio.place(x=100, y=330)

# Membuat OptionMenu (menu pilihan)
option = ["Option 1", "Option 2", "Option 3"]
var_option = tk.StringVar(root)
var_option.set("selected inside")
option_menu = tk.OptionMenu(root, var_option, *option)
option_menu.place(x = 10, y = 360)

# Membuat scale
scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
scale.place(x=10, y=400)

# Membuat spinbox
spinbox = tk.Spinbox(root, from_=0, to=10, increment=0.1)
spinbox.place(x=10, y=460)

root.mainloop()