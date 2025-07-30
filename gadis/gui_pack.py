import tkinter as tk 

root = tk.Tk()
root.title("Contoh GUI")
root.geometry("400x400")
root.resizable(False, False)

label1 = tk.Label(root, text="masukan nama : ")
label1.pack(padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.pack(padx=10, pady=50)

button = tk.Button(root, text="Klik Saya")
button.pack(side="top", padx=10, pady=10) 

label = tk.Label(root, text="Masukkan nama:")
label.pack(side="left", padx=10, pady=10)

entry = tk.Entry(root)
entry.pack(side="right", padx=10, pady=10)

root.mainloop()