import tkinter as tk


# Fungsi yang akan dipanggil saat tombol ditekan
def on_button_click():
    label.config(text="Hello, " + entry.get())


# Fungsi yang akan dipanggil saat kotak daftar dipilih
def on_listbox_select(event):
    selected_item = listbox.get(tk.ACTIVE)
    label.config(text="Anda memilih: " + selected_item)


# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI di Google Colab")

# Menentukan ukuran jendela
root.geometry("400x400")

# Membuat LabelFrame di sekitar elemen-elemen berikut
label_frame = tk.LabelFrame(root, text="Label Frame")
label_frame.place(x=10, y=10, width=380, height=500)

# Membuat label dan mengatur posisnya di dalam LabelFrame
label = tk.Label(label_frame, text="Masukkan nama:")
label.place(x=10, y=10)

# Membuat kotak input teks dan mengatur posisnya di dalam LabelFrame
entry = tk.Entry(label_frame)
entry.place(x=150, y=10)

# Membuat tombol dan mengatur posisnya di dalam LabelFrame
button = tk.Button(label_frame, text="Klik Saya", command=on_button_click)
button.place(x=10, y=50)

# Membuat kotak teks (Text) dan mengatur posisnya di dalam LabelFrame
text_widget = tk.Text(label_frame, width=30, height=7)
text_widget.place(x=10, y=90)

# Membuat kotak daftar (Listbox) dan mengatur posisnya di dalam LabelFrame
listbox = tk.Listbox(label_frame, width=20, height=3)
listbox.place(x=200, y=200)
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")
listbox.bind(
    "<<ListboxSelect>>", on_listbox_select
)  # Mengikat fungsi on_listbox_select saat ada item yang dipilih

# Menjalankan aplikasi GUI
root.mainloop()
