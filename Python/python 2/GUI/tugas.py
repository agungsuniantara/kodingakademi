# judul : Data Diri
# Name : input
# Umur : input
# Alamat : input
# Gender : Radio button
# Hobi : Checkbox
# Major: listbox
# Button Submit

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Aplikasi Form")
root.geometry("400x700")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)

# judul
label_judul = Label(root, text="DATA DIRI", font=("Arial", 16, "bold"))
label_judul.grid(row=0, column=0, columnspan=2, pady=(15, 20)) 

# nama
label_name = Label(root, text="Name:")
label_name.grid(row=1, column=0, sticky=W, padx=15, pady=5)

entry_name = Entry(root, width=30)
entry_name.grid(row=1, column=1, sticky=NSEW, pady=5)

# umur
label_umur = Label(root, text="Umur:")
label_umur.grid(row=2, column=0, sticky=W, padx=15, pady=5)

entry_umur = Entry(root, width=30)
entry_umur.grid(row=2, column=1, sticky=NSEW, pady=5)

# alamat
label_alamat = Label(root, text="Alamat:")
label_alamat.grid(row=3, column=0, sticky=W, padx=15, pady=5)

teks_alamat = Text(root, height=4, width=30, font=("Arial", 10))
teks_alamat.grid(row=3, column=1, sticky=NSEW, pady=5)

# gender
label_gender = Label(root, text="Gender:")
label_gender.grid(row=4, column=0, sticky=W, padx=15, pady=5)

frame_gender = Frame(root)
frame_gender.grid(row=4, column=1, sticky=NSEW)

var_gender = StringVar()
var_gender.set("Male")

radio_male = Radiobutton(frame_gender, text="Male", variable=var_gender, value="Male")
radio_male.grid(row=0, column=0, sticky=NSEW)

radio_female = Radiobutton(frame_gender, text="Female", variable=var_gender, value="Female")
radio_female.grid(row=0, column=1, sticky=NSEW)

# hobi
label_hobi = Label(root, text="Hobi:")
label_hobi.grid(row=5, column=0, sticky=W, padx=15, pady=10)

var_hobi1 = IntVar()
var_hobi2 = IntVar()
var_hobi3 = IntVar()

frame_hobi = Frame(root)
frame_hobi.grid(row=5, column=1, sticky=NSEW)

check_hobi1 = Checkbutton(frame_hobi, text="Membaca", variable=var_hobi1)
check_hobi1.grid(row=0, column=0, sticky=NSEW)

check_hobi2 = Checkbutton(frame_hobi, text="Olahraga", variable=var_hobi2)
check_hobi2.grid(row=0, column=1, sticky=NSEW)

check_hobi3 = Checkbutton(frame_hobi, text="Koding / IT", variable=var_hobi3)
check_hobi3.grid(row=0, column=2, sticky=NSEW)

# major
label_major = Label(root, text="Major:")
label_major.grid(row=6, column=0, sticky=W, padx=15, pady=10)

listbox_major = Listbox(root, height=5, width=30, exportselection=False, font=("Arial", 10))
listbox_major.grid(row=6, column=1, sticky=NSEW, pady=10)

listbox_major.insert(END, "Teknik Informatika")
listbox_major.insert(END, "Sistem Informasi")
listbox_major.insert(END, "Ilmu Komputer")
listbox_major.insert(END, "Manajemen")
listbox_major.insert(END, "Desain")

# ==========================================
# 7. Button Submit
# ==========================================
btn_submit = Button(root, text="Submit")
btn_submit.grid(row=7, column=0, columnspan=2, pady=20, ipadx=20)

root.mainloop()