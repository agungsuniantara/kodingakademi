import tkinter as tk

# Fungsi yang akan dipanggil saat tombol ditekan
def on_button_click():
    label.config(text="Hello, " + entry.get())

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI di Google Colab")
root.geometry("400x400")

# Menentukan bahwa jendela tidak dapat diubah ukurannya
root.resizable(False, False)

# Membuat label dan mengatur posisinya
label = tk.Label(root, text="Masukkan nama:")
label.pack(side="left", padx=10, pady=10)  # Menempatkan label di sebelah kiri dengan padding

# Membuat kotak input teks dan mengatur posisinya di sebelah kanan
entry = tk.Entry(root)
entry.pack(side="right", padx=10, pady=10)  # Menempatkan input teks di sebelah kanan dengan padding

# Membuat tombol dan mengatur posisinya
button = tk.Button(root, text="Klik Saya", command=on_button_click)
button.pack(side="top", padx=10, pady=10)  # Menempatkan tombol di bagian atas dengan padding

# Menjalankan aplikasi GUI
root.mainloop()
