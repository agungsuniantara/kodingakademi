import tkinter as tk
from tkinter import ttk, messagebox

nama_file = "data.txt"
data_karyawan = "karyawan.txt"

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
        return
    
    found = False
    
    with open(nama_file, "r") as file:
        for baris in file:
            if "-" in baris:
                data_split = baris.split("-")
                file_user = data_split[0].strip()
                file_pass = data_split[1].strip()
                
                if username == file_user and password == file_pass:
                    found = True
                    break
                
    if found:
        messagebox.showinfo("Login", "Login Berhasil!")
        karyawan()
    else:
        messagebox.showerror("Login Gagal", "Username atau password tidak tepat!")

def proses_register():
    username_baru = entry_reg_user.get()
    password_baru = entry_reg_pass.get()
    
    if not username_baru or not password_baru:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
        return
        
    with open(nama_file, "a") as file:
        file.write(f"{username_baru}-{password_baru}\n")
        
    messagebox.showinfo("Sukses", "Registrasi Berhasil! Silakan login kembali.")
    reg_window.destroy()
    window.deiconify()

def register():
    global reg_window, entry_reg_user, entry_reg_pass
    
    window.withdraw() 
    
    reg_window = tk.Toplevel(window)
    reg_window.title("Register")
    reg_window.geometry("300x250")
    
    tk.Label(reg_window, text="Silakan Register", font=("Arial", 14, "bold")).pack(pady=20)

    tk.Label(reg_window, text="Username Baru").pack()
    entry_reg_user = tk.Entry(reg_window)
    entry_reg_user.pack(pady=5)

    tk.Label(reg_window, text="Password Baru").pack()
    entry_reg_pass = tk.Entry(reg_window, show="*") 
    entry_reg_pass.pack(pady=5)

    tk.Button(reg_window, text="Submit", command=proses_register, width=10).pack(pady=15)

def proses_tambah_data():
    nik = entry_nik.get()
    nama = entry_nama.get()
    jabatan = combo_jabatan.get()
    alamat = entry_alamat.get()
    email = entry_email.get()
    telpon = entry_telpon.get()
    
    if not nik or not nama:
        messagebox.showerror("Error", "NIK dan Nama tidak boleh kosong!")
        return
        
    with open(data_karyawan, "a") as f:
        f.write(f"{nik}|{nama}|{jabatan}|{alamat}|{email}|{telpon}\n")
            
    messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")
    
    # Kosongkan form setelah berhasil disimpan
    entry_nik.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    combo_jabatan.set("IT Engineer")
    entry_alamat.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telpon.delete(0, tk.END)

def logout():
    kar_window.destroy()
    window.deiconify()

def karyawan():
    global kar_window, entry_nik, entry_nama, combo_jabatan, entry_alamat, entry_email, entry_telpon
    
    window.withdraw() 
    
    kar_window = tk.Tk()
    kar_window.title("Data Karyawan")
    kar_window.geometry("600x400")

    tk.Label(kar_window, text="DATA KARYAWAN", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=25)

    form_frame = tk.Frame(kar_window)
    form_frame.grid(row=1, column=0, padx=50, sticky="w")
    
    tk.Label(form_frame, text="NIK").grid(row=0, column=0, sticky="w", pady=7)
    entry_nik = tk.Entry(form_frame, width=25)
    entry_nik.grid(row=0, column=1, sticky="w", pady=7, padx=20)

    tk.Label(form_frame, text="Nama Karyawan").grid(row=1, column=0, sticky="w", pady=7)
    entry_nama = tk.Entry(form_frame, width=45)
    entry_nama.grid(row=1, column=1, sticky="w", pady=7, padx=20)

    tk.Label(form_frame, text="Jabatan").grid(row=2, column=0, sticky="w", pady=7)
    combo_jabatan = ttk.Combobox(form_frame, values=["IT Engineer", "Network Admin", "Programmer", "Manager"], width=20, state="readonly")
    combo_jabatan.set("IT Engineer")
    combo_jabatan.grid(row=2, column=1, sticky="w", pady=7, padx=20)

    tk.Label(form_frame, text="Alamat").grid(row=3, column=0, sticky="w", pady=7)
    entry_alamat = tk.Entry(form_frame, width=60)
    entry_alamat.grid(row=3, column=1, sticky="w", pady=7, padx=20)

    tk.Label(form_frame, text="Email").grid(row=4, column=0, sticky="w", pady=7)
    entry_email = tk.Entry(form_frame, width=45)
    entry_email.grid(row=4, column=1, sticky="w", pady=7, padx=20)

    tk.Label(form_frame, text="No. Telpon").grid(row=5, column=0, sticky="w", pady=7)
    entry_telpon = tk.Entry(form_frame, width=30)
    entry_telpon.grid(row=5, column=1, sticky="w", pady=7, padx=20)

    btn_frame = tk.Frame(kar_window)
    btn_frame.grid(row=2, column=0, pady=30, padx=25)
    
    tk.Button(btn_frame, text="Tambah Data", width=12, command=proses_tambah_data).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Logout", width=8, command=logout).grid(row=0, column=2, padx=5)


window = tk.Tk()
window.title("Login")
window.geometry("500x250")

tk.Label(window, text="Silakan Login", font=("Arial", 14, "bold")).pack(pady=20)

tk.Label(window, text="Username").pack()
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

tk.Label(window, text="Password").pack()
entry_password = tk.Entry(window, show="*") 
entry_password.pack(pady=5)

button_frame = tk.Frame(window, pady=15)
button_frame.pack()

tk.Button(button_frame, text="Login", command=login, width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Register", command=register, width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Keluar", command=window.destroy, width=10).pack(side=tk.LEFT, padx=5)

window.mainloop()