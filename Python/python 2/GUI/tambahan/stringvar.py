import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh StringVar")

# Membuat StringVar
string_var = tk.StringVar()

# Membuat elemen GUI yang terhubung dengan StringVar
label = tk.Label(root, textvariable=string_var)
label.pack()

entry = tk.Entry(root, textvariable=string_var)
entry.pack()

# Fungsi yang akan dipanggil saat tombol ditekan
def change_text():
    string_var.set("Teks telah berubah!")

button = tk.Button(root, text="Ubah Teks", command=change_text)
button.pack()

# Menjalankan aplikasi GUI
root.mainloop()
