import tkinter as tk
import os

folder = r"/Applications/MAMP/htdocs/local/kodingakademi/Python/python 2/GUI_crud/text"

def create_text():
    try:
        nama_file = f"{teks_nama.get()}.txt"
        if nama_file != "":
            teks = kolom_teks.get("1.0", tk.END)
            with open(os.path.join(folder, nama_file), "w") as file:
                file.write(teks)
            kolom_teks.delete("1.0", tk.END)
            read_text()
    except Exception as e:
        print("Error:", e)

def append_text():
    try:
        nama_file = f"{teks_nama.get()}.txt"
        if nama_file != "":
            teks = kolom_teks.get("1.0", tk.END)
            with open(os.path.join(folder, nama_file), "a") as file:
                file.write(teks)
            kolom_teks.delete("1.0", tk.END)
            read_text()
    except Exception as e:
        print("Error:", e)

def read_text():
    try:
        nama_file = f"{teks_nama.get()}.txt"
        if nama_file != "":
            with open(os.path.join(folder, nama_file), "r") as file:
                data = file.read()
                kolom_tampil.delete("1.0", tk.END)
                kolom_tampil.insert(tk.END, data)
        else:
            kolom_tampil.delete("1.0", tk.END)
    except Exception as e:
        print("Error:", e)

def update_txt():
    try:
        nama_file = f"{teks_nama.get()}.txt"
        if nama_file != "":
            search = searchText_input.get()
            new = updateteks_input.get()
            with open(os.path.join(folder, nama_file), "r") as file:
                data = file.read()
                data = data.replace(search, new)
            with open(os.path.join(folder, nama_file), "w") as file:
                file.write(data)
            searchText_input.delete(0, tk.END) 
            updateteks_input.delete(0, tk.END)  
            read_text()
    except Exception as e:
        print("Error:", e)

def delete_txt():
    try:
        nama_file = f"{deletefile_input.get()}.txt"
        if nama_file != "":
            os.remove(os.path.join(folder, nama_file))
            deletefile_input.delete(0, tk.END)
            kolom_tampil.delete("1.0", tk.END)
            teks_nama.delete(0, tk.END)
    except Exception as e:
        print("Error:", e)

# Membuat jendela utama
root = tk.Tk()
root.title("GUI CRUD")

# Menentukan ukuran jendela
root.geometry("700x350")

# nama file
label_nama = tk.Label(
    root,
    text="Nama file : ",
)
label_nama.place(x=30, y=10)

# teks nama file
teks_nama = tk.Entry(root)
teks_nama.place(x=100, y=13)

# teks submit
label_teks = tk.Label(
    root,
    text="Teks : ",
)
label_teks.place(x=30, y=40)

# kolom teks submit
kolom_teks = tk.Text(root, width=30, height=7)
kolom_teks.place(x=30, y=70)

button_create = tk.Button(root, text="Create", command=create_text)
button_create.place(x=290, y=70)

button_update = tk.Button(root, text="Append", command=append_text)
button_update.place(x=290, y=110)

# search text
search_teks = tk.Label(
    root,
    text="Search text : ",
)
search_teks.place(x=30, y=195)

# search text input
searchText_input = tk.Entry(root)
searchText_input.place(x=30, y=220)

# update text
update_teks = tk.Label(
    root,
    text="Update text : ",
)
update_teks.place(x=170, y=195)

# update text input
updateteks_input = tk.Entry(root)
updateteks_input.place(x=170, y=220)

button_update = tk.Button(root, text="Update", command=update_txt)
button_update.place(x=305, y=215)

# delete file
delete_teks = tk.Label(
    root,
    text="File: ",
)
delete_teks.place(x=30, y=250)

# delete text input
deletefile_input = tk.Entry(root)
deletefile_input.place(x=30, y=280)

button_delete = tk.Button(root, text="Delete", command=delete_txt)
button_delete.place(x=160, y=275)

# teks tampil
label_tampil = tk.Label(
    root,
    text="Tampil : ",
)
label_tampil.place(x=360, y=40)

# kolom teks tampil
kolom_tampil = tk.Text(root, width=30, height=7)  
kolom_tampil.place(x=360, y=70)  

button_read = tk.Button(root, text="Read", command=read_text)
button_read.place(x=620, y=70)

# Menjalankan aplikasi GUI
root.mainloop()
