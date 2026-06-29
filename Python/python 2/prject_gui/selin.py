from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

file_name = "username and password.txt"
data_karyawan = "karyawan.txt"

def proses_tambah_data():
    nik = nik_box.get()
    nama = nama_karyawanbox.get()
    jabatan = jabatan_listbox.curselection()
    if jabatan:
        chosen_jabatan = jabatan[0]
        data_jabatan = jabatan_listbox.get(chosen_jabatan)
    else:
        data_jabatan = "Tidak ada yang dipilih"
    alamat = alamat_box.get()
    email = email_box.get()
    phone = phone_box.get()
    
    with open(data_karyawan, "a") as file:
        file.write(f"{nik} | {nama} | {data_jabatan} | {alamat} | {email} | {phone}")
    messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")
    
    if not nik or not nama:
        messagebox.showinfo("Error", "NIK dan nama tidak boleh kosong!")
        return

def edit_data():
    nik = nik_box.get()
    nama = nama_karyawanbox.get()
    
    jabatan = jabatan_listbox.curselection()
    if jabatan:
        chosen_jabatan = jabatan[0]
        data_jabatan = jabatan_listbox.get(chosen_jabatan)
    else:
        data_jabatan = "Tidak ada yang dipilih"
        
    alamat = alamat_box.get()
    email = email_box.get()
    phone = phone_box.get()
    
    data_baru = f"{nik} | {nama} | {data_jabatan} | {alamat} | {email} | {phone}\n"
    
    with open(data_karyawan, "r") as file:
        lines = file.readlines()

    found = False
    with open(data_karyawan, "w") as file:
        for baris in lines:
            data_split = baris.split("|")
            data_nik = data_split[0].strip()
            
            if nik == data_nik:
                file.write(data_baru)
                found = True
            else:
                file.write(baris)
                
    if found:
        messagebox.showinfo("Edit", "Edit berhasil!")
    else:
        messagebox.showinfo("Error", "NIK tidak ditemukan")

def hapus_data():
    nik = nik_box.get()
    nama = nama_karyawanbox.get()
    jabatan = jabatan_listbox.get()
    alamat = alamat_box.get()
    email = email_box.get()
    phone = phone_box.get()
    with open(data_karyawan, "r") as file:
        for baris in file:
            data_split = baris.split("|")
            data_nik = data_split[0].strip()
    
def login():
    found = False
    username = username_box.get()
    password = password_box.get()
    with open(file_name, "r") as file:
        for baris in file:
            data_split = baris.split("-")
            file_user = data_split[0].strip()
            file_pass = data_split[1].strip()
            if username == file_user and password == file_pass:
                found = True
                break
            
    if found:
        messagebox.showinfo("Login", "Login Berhasil")
        root.withdraw()
    else:
        messagebox.showerror("Login Gagal", "Username atau password tidak tepat")
    
    if not username or not password:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong")
    
    global nik_box, nama_karyawanbox, jabatan_listbox, alamat_box, email_box, phone_box
    
    data = Tk()
    data.title("Halaman Data Karyawan")
    data.geometry("500x500")
    
    data_karyawantext = Label(data, text = "Data Karyawan", font = ("Times New Roman", 18))
    data_karyawantext.grid(row = 1, column = 3, columnspan = 2)
    
    nik = Label(data, text = "NIK :", font = ("Times New Roman", 16))
    nik.grid(row = 3, column = 1)
    
    nik_box = Entry(data, font = ("Times New Roman", 16))
    nik_box.grid(row = 3, column = 3, columnspan = 2)
    
    nama_karyawan = Label(data, text = "Nama Karyawan :", font = ("Times New Roman", 16))
    nama_karyawan.grid(row = 4, column = 1)
    
    nama_karyawanbox = Entry(data, font = ("Times New Roman", 16))
    nama_karyawanbox.grid(row = 4, column = 3, columnspan = 2)
    
    jabatan = Label(data, text= "Jabatan :", font = ("Times New Roman", 16))
    jabatan.grid(row = 5, column = 1)
    
    jabatan_listbox = Listbox(data, font = ("Times New Roman", 16))
    jabatan_listbox.grid(row = 5, column = 3)
    jabatan_listbox.insert(END, "IT Engineer")
    jabatan_listbox.insert(END, "Director")
    jabatan_listbox.insert(END, "Manager")
    jabatan_listbox.insert(END, "Data Analyst")
    jabatan_listbox.insert(END, "Others")
    
    alamat = Label(data, text = "Alamat :", font = ("Times New Roman", 16))
    alamat.grid(row = 11, column = 1)
    
    alamat_box = Entry(data, font = ("Times New Roman", 16))
    alamat_box.grid(row = 11, column = 3, columnspan = 2)
    
    email = Label(data, text = "Email :", font = ("Times New Roman", 16))
    email.grid(row = 12, column = 1)
    
    email_box = Entry(data, font = ("Times New Roman", 16))
    email_box.grid(row = 12, column = 3, columnspan = 2)
    
    phone = Label(data, text = "No. Telepon :", font = ("Times New Roman", 16))
    phone.grid(row = 13, column = 1)
    
    phone_box = Entry(data, font = ("Times New Roman", 16))
    phone_box.grid(row = 13, column = 3, columnspan = 2)
    
    tambah_data = Button(data, text = "Tambah Data", command = proses_tambah_data)
    tambah_data.grid(row = 14, column = 1)
    
    edit = Button(data, text = "Edit", command = edit_data)
    edit.grid(row = 14, column = 3)
    
    hapus = Button(data, text = "Hapus")
    hapus.grid(row = 14, column = 5)
    
    keluar = Button(data, text = "Keluar")
    keluar.grid(row = 14, column = 7)
    
root = Tk()
root.title("Login Page")
root.geometry("500x500")

login_text = Label(root, text = "Silahkan Login", font = ("Times New Roman", 18))
login_text.grid(row = 2, column = 5)

username_text = Label(root, text = "Username*", font = ("Times New Roman", 16))
username_text.grid(row = 5, column = 5, columnspan = 2)

username_box = Entry(root, font = ("Times New Roman", 16))
username_box.grid(row = 6, column = 5, columnspan = 2)

password_text = Label(root, text = "Password*", font = ("Times New Roman", 16))
password_text.grid(row = 8, column = 5, columnspan = 2)

password_box = Entry(root, font = ("Times New Roman", 16))
password_box.grid(row = 9, column = 5, columnspan = 2)

login_button = Button(root, text = "Login", command = login)
login_button.grid(row = 10, column = 5)

keluar_button = Button(root, text = "Keluar", command = root.destroy)
keluar_button.grid(row = 10, column = 6)

root.mainloop()