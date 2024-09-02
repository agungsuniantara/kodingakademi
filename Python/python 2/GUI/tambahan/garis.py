import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI dengan Garis dan Judul")

# Menentukan ukuran jendela
root.geometry("500x800")

# Membuat Canvas untuk menggambar garis dan judul
canvas = tk.Canvas(root, width=500, height=800)
canvas.pack()

# Menggambar garis-garis dan memberikan judul
canvas.create_line(10, 10, 490, 10, fill="blue", width=2)  # Garis atas
canvas.create_text(250, 15, text="Judul Atas", fill="blue", font=("Helvetica", 12))

canvas.create_line(10, 790, 490, 790, fill="blue", width=2)  # Garis bawah
canvas.create_text(250, 785, text="Judul Bawah", fill="blue", font=("Helvetica", 12))

canvas.create_line(10, 10, 10, 790, fill="blue", width=2)  # Garis kiri
canvas.create_text(15, 400, text="Judul Kiri", fill="blue", font=("Helvetica", 12), angle=90)

canvas.create_line(490, 10, 490, 790, fill="blue", width=2)  # Garis kanan
canvas.create_text(485, 400, text="Judul Kanan", fill="blue", font=("Helvetica", 12), angle=90)

# Menjalankan aplikasi GUI
root.mainloop()
