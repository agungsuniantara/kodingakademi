import tkinter as tk
from tkinter import messagebox
import session
import gui_login
import gui_admin
import gui_kasir
import gui_manager
import core_db

def router_logout():
    """
    Fungsi untuk menghapus sesi dan mengembalikan layar ke halaman login.
    Fungsi ini akan dikirim (di-passing) ke gui_admin dan gui_kasir.
    """
    konfirmasi = messagebox.askyesno("Logout", "Apakah Anda yakin ingin keluar?")
    if konfirmasi:
        # Hapus data sesi di memori
        session.current_user = None
        # Panggil ulang halaman login
        gui_login.tampilkan_halaman(window, router_setelah_login)

def router_setelah_login(role):
    """
    Fungsi Callback: Menentukan halaman mana yang dibuka 
    berdasarkan level otorisasi (Role) setelah login sukses.
    """
    if role == "Admin":
        gui_admin.tampilkan_halaman(window, router_logout)
    elif role == "Kasir":
        gui_kasir.tampilkan_halaman(window, router_logout)
    elif role == "Manager":
        gui_manager.tampilkan_halaman(window, router_logout)
    else:
        messagebox.showerror("Akses Ditolak", "Role tidak dikenali!")
        router_logout()

# ==========================================
# ENTRY POINT APLIKASI
# ==========================================
if __name__ == "__main__":
    # 1. Pastikan file CSV terbuat saat aplikasi pertama dijalankan
    core_db.inisialisasi_file()
    
    # 2. Inisialisasi Window Utama
    window = tk.Tk()
    window.title("Sistem Point of Sale v2.0")
    window.geometry("850x600")
    
    # 3. Eksekusi halaman pertama (Login)
    # Kita mengirimkan 'window' sebagai kanvas, dan 'router_setelah_login' sebagai arah tujuan jika sukses
    gui_login.tampilkan_halaman(window, router_setelah_login)
    
    # 4. Tahan window agar terus berjalan
    window.mainloop()