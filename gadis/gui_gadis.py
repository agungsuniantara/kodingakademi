import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = tk.Tk()
win.configure(bg="white")
win.geometry('300x300')
win.title("Halaman Perkenalan")
NamaDepan = tk.StringVar()
NamaBelakang = tk.StringVar()

def Perkenalan(NamaDepan_var, NamaBelakang_var):
    frame = ttk.Frame(win)
    frame.pack(padx=10, pady=10, fill="x", expand=True)

    NamaDepan_label = ttk.Label(frame, text="Masukkan Nama Depan")
    NamaDepan_label.pack(padx=10, pady=10)
    NamaDepan_entry = ttk.Entry(frame, textvariable=NamaDepan_var)
    NamaDepan_entry.pack(fill="x", expand=True)

    NamaBelakang_label = ttk.Label(frame, text="Masukkan Nama Belakang")
    NamaBelakang_label.pack(padx=10, pady=10)
    NamaBelakang_entry = ttk.Entry(frame, textvariable=NamaBelakang_var)
    NamaBelakang_entry.pack(fill="x", expand=True)

    btn = ttk.Button(frame, text="Perkenalan", command=lambda:tombolSapa(NamaDepan_var, NamaBelakang_var))
    btn.pack(pady=10, fill="x", expand=True)

def tombolSapa(NamaDepan_var, NamaBelakang_var):
    if NamaDepan_var.get() == "" or NamaBelakang_var.get() == "":
        messagebox.showerror(title="Error", message="Nama Depan & Nama Belakang Wajib diisi",)
    else:
        messagebox.showinfo(title="Succes", messsage=f"Halo{NamaDepan_var.get()} {NamaBelakang_var.get()}, Salam Kenal")
        NamaDepan_var.set("")
        NamaBelakang_var.set("")

Perkenalan(NamaDepan, NamaBelakang)

win.mainloop()