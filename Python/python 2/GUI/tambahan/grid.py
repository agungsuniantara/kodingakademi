import tkinter as tk

# Fungsi yang akan dipanggil saat tombol "Klik Saya" ditekan
def on_button_click():
    name = entry.get()
    if name:
        result_text.config(text="Hello, " + name)
    else:
        result_text.config(text="Hello, World")

# Fungsi yang akan dipanggil saat tombol "Reset" ditekan
def on_reset_button_click():
    entry.delete(0, tk.END)
    result_text.config(text="")

# Fungsi yang akan dipanggil saat kotak daftar dipilih
def on_listbox_select(event):
    selected_item = listbox.get(tk.ACTIVE)
    label.config(text="Anda memilih: " + selected_item)

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI di Google Colab")

# Menentukan ukuran jendela
root.geometry("500x500")

# Membuat label "Masukkan nama:"
label = tk.Label(root, text="Masukkan nama:")
label.grid(row=0, column=0, padx=0, pady=10)

# Membuat kotak input teks
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Membuat tombol "Klik Saya"
button = tk.Button(root, text="Klik Saya", command=on_button_click)
button.grid(row=0, column=2, padx=10, pady=10)

# Membuat label hasil
result_text = tk.Label(root, text="", font=("Helvetica", 16))
result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Membuat tombol "Reset"
reset_button = tk.Button(root, text="Reset", command=on_reset_button_click)
reset_button.grid(row=2, column=1, padx=10, pady=10)

# Membuat kotak teks (Text) dan mengatur posisinya
text_widget = tk.Text(root, width=30, height=10)
text_widget.grid(row=3, column=0, padx=10, pady=10)

# Membuat kotak daftar (Listbox) dan mengatur posisinya
listbox = tk.Listbox(root, width=20, height=5)
listbox.grid(row=4, column=0, padx=10, pady=10)
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")
listbox.bind(
    "<<ListboxSelect>>", on_listbox_select
)  # Mengikat fungsi on_listbox_select saat ada item yang dipilih

# Menjalankan aplikasi GUI
root.mainloop()
