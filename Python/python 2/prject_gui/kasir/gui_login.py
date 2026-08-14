import tkinter as tk
from tkinter import messagebox
import core_db
import session

def bersihkan_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def proses_login(entry_username, entry_password, window, fungsi_navigasi):
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    
    if not username or not password:
        messagebox.showerror("Error", "Username dan Password tidak boleh kosong!")
        return
        
    data_user = core_db.validasi_login(username, password)
    
    if data_user:
        session.current_user = data_user
        
        nama = data_user["nama"]
        role = data_user["role"]
        messagebox.showinfo("Login Berhasil", f"Selamat datang, {nama}!\nAnda login sebagai: {role}")
        
        fungsi_navigasi(role)
    else:
        messagebox.showerror("Login Gagal", "Username atau Password salah!")
        entry_password.delete(0, tk.END)

def tampilkan_halaman(window, fungsi_navigasi):
    bersihkan_window(window)
    
    tk.Label(window, text="Sistem Kasir Koperasi", font=("Arial", 24, "bold")).pack(pady=(40, 10))
    tk.Label(window, text="Silakan Login untuk Melanjutkan", font=("Arial", 12)).pack(pady=(0, 30))
    
    form_frame = tk.Frame(window)
    form_frame.pack()
    
    tk.Label(form_frame, text="Username", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=10, padx=10)
    entry_username = tk.Entry(form_frame, font=("Arial", 14), width=20)
    entry_username.grid(row=0, column=1, pady=10, padx=10)
    
    tk.Label(form_frame, text="Password", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=10, padx=10)
    entry_password = tk.Entry(form_frame, font=("Arial", 14), width=20, show="*")
    entry_password.grid(row=1, column=1, pady=10, padx=10)
    
    btn_login = tk.Button(window, text="LOGIN", font=("Arial", 12, "bold"), width=20,
                          command=lambda: proses_login(entry_username, entry_password, window, fungsi_navigasi))
    btn_login.pack(pady=30)
