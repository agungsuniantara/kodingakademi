import tkinter as tk
from tkinter import ttk, messagebox

nama_file = "data.txt"

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    found = False
    with open(nama_file, "r") as file:
        for baris in file:
            data_split = baris.split("-")
            file_user = data_split[0].strip()
            file_pass = data_split[1].strip()
            
            if username == file_user and password == file_pass:
                found = True
                break
        
    if found:
        messagebox.showinfo("Login", "Login Berhasil!")
        window.destroy() 
    else:
        messagebox.showerror("Login Gagal", "Username atau password tidak tepat!")
    
    if not username or not password:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
        return


window = tk.Tk()
window.title("Login")
window.geometry("300x250")

tk.Label(window, text="Silakan Login", font=("Arial", 14, "bold")).pack(pady=20)

tk.Label(window, text="Username").pack()
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

tk.Label(window, text="Password").pack()
entry_password = tk.Entry(window)
entry_password.pack(pady=5)

button_frame = tk.Frame(window, pady=15)
button_frame.pack()

tk.Button(button_frame, text="Login", command=login, width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Keluar", command=window.destroy, width=10).pack(side=tk.LEFT, padx=5)

window.mainloop()
