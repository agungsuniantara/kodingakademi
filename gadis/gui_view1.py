import tkinter as tk
from tkinter import ttk, messagebox

win = tk.Tk()
win.geometry('1350x700+0+0')
win.title('Student Management System')
win.config(bg='white')

title_label = tk.Label(win, text= "Student Management System", 
font=('Arial', 25), border=12, relief=tk.GROOVE, bg='black', foreground='white')
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text = 'Enter Details', 
font=('Arial',20), bg='Black', fg='white', bd=12, relief=tk.GROOVE)
detail_frame.place(x=20, y=90, width=420, height=575)

npm = tk.Label(detail_frame, text='NPM', font=('arial', 17), bg='black', fg='white')
npm.grid(row=0, column=0, padx=2, pady=2)
npm_ent = tk.Entry(detail_frame, bd=7, font=('arial', 17))
npm_ent.grid(row=0, column=1, padx=2, pady=2)

nama= tk.Label(detail_frame, text='Nama', font=('arial',17), bg='black' , fg= 'white')
nama.grid(row=1, column=0,padx=2, pady=2)
nama_ent = tk.Entry (detail_frame, bd=7, font=('arial', 17))
nama_ent.grid(row=1, column=1, padx=2, pady=2)

program_studi = tk.Label(detail_frame, text='Prodi', font=('arial',17), bg='black', fg='white')
program_studi.grid(row=2, column=0,padx=2, pady=2)
program_studi_ent = ttk.Combobox(detail_frame, font=('arial', 17), state='readonly')
program_studi_ent['values']= ('Sistem Informasi', 'Informatika', 'Teknik industri')
program_studi_ent.grid(row=2, column=1, padx=2, pady=2)

fakultas = tk. Label(detail_frame, text='Fakultas', font=('arial',17), bg='black', fg='white' )
fakultas.grid(row=3, column=0, padx=2, pady=2)
fakultas_ent = tk.Entry(detail_frame, bd=7, font=('arial', 17))
fakultas_ent.grid(row=3, column=1,padx=2,pady=2)

angkatan = tk.Label(detail_frame, text= 'Angkatan', font=('arial',17), bg= 'black', fg= 'white')
angkatan.grid(row=4, column=0,padx=2,pady=2)
angkatan_ent = tk.Entry(detail_frame, bd=7, font=('arial', 17))
angkatan_ent.grid(row=4, column=1,padx=2,pady=2)

Alamat = tk.Label(detail_frame, text= 'Alamat', font=('arial',17), bg= 'black', fg= 'white')
Alamat.grid(row=5, column=0, padx=2, pady=2)
Alamat_ent = tk.Text(detail_frame, width=21, height=6, font=('arial', 17))
Alamat_ent.grid(row=5,column=1, padx=2, pady=2, columnspan=4)

button_frame = tk. Frame(detail_frame,bg='black', bd=10, relief=tk.GROOVE)
button_frame.place(x=27, y=390, width=339, height=112)

add_button = tk.Button (button_frame, bg='white', text='Add', bd=7, font=('Arial',12), width=15)
add_button.grid(row=0, column=0, padx=2, pady=2)

update_button = tk.Button(button_frame, bg='white', text='Update', bd=7, font=('Arial',12), width=15)
update_button.grid(row=0, column=1, padx=3, pady=2)

delete_button = tk.Button (button_frame, bg='white', text='Delete', bd=7, font=('Arial',12), width=15)
delete_button.grid(row=1, column=0, padx=2, pady=2)

clear_button = tk.Button (button_frame, bg='white', text='Clear', bd=7, font=('Arial',12), width=15)
clear_button.grid(row=1, column=1, padx=3, pady=2)

main_frame = tk.Frame(win, bg='white', bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

table_mahasiswa = ttk.Treeview(main_frame, columns=(
    'NPM',
    'Nama',
    'Prodi',
    'Fakultas',
    'Angkatan',
    'Alamat'
    ),

yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=table_mahasiswa.yview)
y_scroll.config(command=table_mahasiswa.yview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

table_mahasiswa.heading('NPM', text='NPM')
table_mahasiswa.heading('Nama', text='Nama')
table_mahasiswa.heading('Prodi', text='Prodi')
table_mahasiswa.heading('Fakultas', text='Fakultas')
table_mahasiswa.heading('Angkatan', text='Angkatan')
table_mahasiswa.heading('Alamat', text='Alamat')

table_mahasiswa['show'] = 'headings'

table_mahasiswa.column('NPM', width=100)
table_mahasiswa.column('Nama', width=100)
table_mahasiswa.column('Prodi', width=100)
table_mahasiswa.column('Fakultas', width=100)
table_mahasiswa.column('Angkatan', width=100)
table_mahasiswa.column('Alamat', width=100)

table_mahasiswa.pack(fill=tk.BOTH, expand=True)

def fill_fields(event):
    """Fills the fields with data from the selected row."""
    selected_item = table_mahasiswa.selection()
    if not selected_item:
        return
    
    values = table_mahasiswa.item(selected_item[0], "values")
    npm_ent.delete(0, tk.END)
    npm_ent.insert(0, values[0])

    nama_ent.delete(0, tk.END)
    nama_ent.insert(0, values[1])

    program_studi_ent.set(values[2])

    fakultas_ent.delete(0, tk.END)
    fakultas_ent.insert(0, values[3])

    angkatan_ent.delete(0, tk.END)
    angkatan_ent.insert(0, values[4])

    Alamat_ent.delete("1.0", tk.END)
    Alamat_ent.insert("1.0", values[5])

table_mahasiswa.bind("<<TreeviewSelect>>", fill_fields)
win.mainloop()

all_data = []

def add_record():
    if not all([npm_ent.get(), nama_ent(), program_studi_ent.get(),
    fakultas_ent.get(), angkatan_ent.get(), Alamat_ent.get("1.0", "end".strip)]):
        messagebox.showwarning("Warning", "All fields must be filled")
        return

new_record = (
    npm_ent.get(),
    nama_ent.get(),
    program_studi_ent.get(),
    fakultas_ent.get(),
    angkatan_ent.get(),
    Alamat_ent.get("1.0", "end").strip()
)
all_data.append(new_record)

table_mahasiswa.insert("", "end", values=new_record)

def clear_fields():
    npm_ent.delete(0, tk.END)
    nama_ent.delete(0, tk.END)
    program_studi_ent.set("")
    fakultas_ent.delete(0, tk.END)
    Alamat_ent.delete("1.0", tk.END)

clear_fields()
messagebox.showinfo("Success", "Record added successfully")

add_button.config(command=add_record)

def add_mahasiswa(self):
    nama = self.nama_entry.get()
    no_hp = self.no_hp_entry.get()
    angkatan = self.angkatan_entry.get()
    mata_kuliah = self.mata_kuliah_entry.get()
    dosen = self.dosen_entry.get()
    nilai = self.nilai_entry.get()

    if not nama or not angkatan or not mata_kuliah or not nilai:
        messagebox.showerror("Error", "Mohon lengkapi semua kolom yang diperlukan.")
        return

    perkuliahan = {
        "Nama": nama,
        "NPM": no_hp,
        "Angkatan": angkatan,
        "Mata Kuliah": mata_kuliah,
        "Dosen": dosen,
        "Nilai": nilai
    }
    self.kuliah.append(perkuliahan)

    perkuliahan_info = f"Nama: {nama} | Angkatan: {angkatan} | Mata Kuliah: {mata_kuliah}"
    self.perkuliahan_list.insert(tk.END, perkuliahan_info)

    self.clear_input_fields()

    self.add_button.config(command=self.add_mahasiswa)

def clear_input_fields(self):
    self.nama_entry.delete(0, tk.END)
    self.no_hp_entry.delete(0, tk.END)
    self.angkatan_entry.delete(0, tk.END)
    self.mata_kuliah_entry.delete(0, tk.END)
    self.dosen_entry.delete(0, tk.END)
    self.nilai_entry.delete(0, tk.END)