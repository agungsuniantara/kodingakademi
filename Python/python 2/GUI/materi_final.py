from tkinter import *
from tkinter.ttk import *

def ambil_data():
    data_entry = entry.get()
    print(f"Entry Teks     : {data_entry}")

    # Mengambil data dari Text (dari baris 1 karakter 0 sampai akhir)
    data_teks = teks.get("1.0", END).strip() 
    print(f"Text Area      : {data_teks}")

    status_check = "Dicentang" if var_check.get() == 1 else "Tidak Dicentang"
    print(f"Checkbutton    : {status_check}")

    data_gender = var.get()
    print(f"Radiobutton    : {data_gender}")

    data_opsi = var_option.get()
    print(f"OptionMenu     : {data_opsi}")

    data_scale = scale.get()
    data_spinbox = spinbox.get()
    print(f"Scale Value    : {data_scale}")
    print(f"Spinbox Value  : {data_spinbox}")
    
    pilihan_list = list_box.curselection()
    if pilihan_list:
        index_terpilih = pilihan_list[0]
        data_listbox = list_box.get(index_terpilih)
    else:
        data_listbox = "Tidak ada yang dipilih"
        
    print(f"Listbox        : {data_listbox}")


root = Tk()
root.title("My App")
root.geometry("400x700")

label1 = Label(root, text="ini label 1", font=("Arial", 16))
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = Label(root, text="ini label 2", font=("Arial", 16))
label2.grid(row=0, column=1, padx=10, pady=10)

entry = Entry(root, font=("Arial", 16))
entry.grid(row=1, column=0, pady=5)

teks = Text(root, font=("Arial", 16), height=5, width=30)
teks.grid(row=2, column=0, pady=5)

list_box = Listbox(root, font=("Arial", 16), height=5, exportselection=False)
list_box.grid(row=3, column=0, pady=5)
list_box.insert(END, "Item 1")
list_box.insert(END, "Item 2")
list_box.insert(END, "Item 3")

var_check = IntVar()
checkbox = Checkbutton(root, text="Check me", variable=var_check)
checkbox.grid(row=4, column=0, pady=5)

var = StringVar()
var.set("Male")
male_radio = Radiobutton(root, text="Male", variable=var, value="Male")
male_radio.grid(row=5, column=0)
female_radio = Radiobutton(root, text="Female", variable=var, value="Female")
female_radio.grid(row=5, column=1)

options = ["Option 1", "Option 2", "Option 3"]
var_option = StringVar(root)
option_menu = OptionMenu(root, var_option, "Option 1", *options)
option_menu.grid(row=7, column=0, pady=5)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
scale.grid(row=8, column=0, pady=5)

spinbox = Spinbox(root, from_=0, to=10, increment=1)
spinbox.grid(row=9, column=0, pady=5)

button = Button(root, text="Click Me", command=ambil_data)
button.grid(row=10, column=0, pady=20)

root.mainloop()