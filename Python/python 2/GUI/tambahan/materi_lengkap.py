import tkinter as tk
from tkinter import StringVar


# Fungsi yang akan dipanggil saat tombol "Klik Saya" ditekan
def on_button_click():
    name = entry.get()
    gender = gender_var.get()
    selected_option = selected_option_var.get()

    greeting = "Hello, "
    if name:
        greeting += name
    else:
        greeting += "World"

    if gender:
        greeting += ", " + gender

    if selected_option != "Select":
        greeting += ". Anda memilih: " + selected_option

    result_text.config(text=greeting)


# Fungsi yang akan dipanggil saat tombol "Reset" ditekan
def on_reset_button_click():
    entry.delete(0, tk.END)
    result_text.config(text="")


# Fungsi yang akan dipanggil saat kotak daftar dipilih
def on_listbox_select(event):
    selected_item = listbox.get(tk.ACTIVE)
    label1.config(text="Anda memilih: " + selected_item)


# Fungsi yang akan dipanggil saat kotak centang diubah
def on_checkbox_change():
    show_name = show_name_var.get()
    entry.config(state=tk.NORMAL if show_name else tk.DISABLED)


# Fungsi yang akan dipanggil saat tombol radio diubah
def on_radio_change():
    gender = gender_var.get()
    if gender == "Laki-laki":
        text_widget.delete(1.0, tk.END)  # Menghapus teks sebelumnya
        text_widget.insert(tk.END, "Anda memilih jenis kelamin: Laki-laki")
    elif gender == "Perempuan":
        text_widget.delete(1.0, tk.END)  # Menghapus teks sebelumnya
        text_widget.insert(tk.END, "Anda memilih jenis kelamin: Perempuan")


# Fungsi yang akan dipanggil saat opsi dipilih dari OptionMenu
def on_option_select(*args):
    selected_option = selected_option_var.get()
    if selected_option != "Select":
        result_text.config(
            text=result_text.cget("text") + ". Anda memilih: " + selected_option
        )


# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI di Google Colab")

# Menentukan ukuran jendela
root.geometry("500x800")

# Membuat label "Masukkan nama:"
label1 = tk.Label(root, text="Masukkan nama:")
label1.place(x=10, y=20)

# Membuat kotak input teks
entry = tk.Entry(root)
entry.place(x=10, y=50)

# Membuat tombol "Klik Saya"
button = tk.Button(root, text="Klik Saya", command=on_button_click)
button.place(x=10, y=80)

# Membuat label hasil
result_text = tk.Label(root, text="", font=("Helvetica", 16))
result_text.place(x=10, y=110)

# Membuat tombol "Reset"
reset_button = tk.Button(root, text="Reset", command=on_reset_button_click)
reset_button.place(x=10, y=140)

# Membuat kotak daftar (Listbox) dan mengatur posisinya
listbox = tk.Listbox(root, width=20, height=3)
listbox.place(x=10, y=180)
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")
listbox.bind(
    "<<ListboxSelect>>", on_listbox_select
)  # Mengikat fungsi on_listbox_select saat ada item yang dipilih

# Membuat kotak centang
show_name_var = tk.BooleanVar()
checkbox = tk.Checkbutton(
    root, text="Tampilkan nama", variable=show_name_var, command=on_checkbox_change
)
checkbox.place(x=10, y=240)

# Membuat tombol radio
gender_var = tk.StringVar()
gender_var.set("Laki-laki")  # Pilihan default
male_radio = tk.Radiobutton(
    root,
    text="Laki-laki",
    variable=gender_var,
    value="Laki-laki",
    command=on_radio_change,
)
female_radio = tk.Radiobutton(
    root,
    text="Perempuan",
    variable=gender_var,
    value="Perempuan",
    command=on_radio_change,
)
male_radio.place(x=10, y=270)
female_radio.place(x=10, y=290)

# Membuat kotak teks (Text)
text_widget = tk.Text(root, width=50, height=10)
text_widget.place(x=10, y=330)

# Membuat OptionMenu (Menu Pilihan)
options = ["Select", "Option 1", "Option 2", "Option 3"]
selected_option_var = StringVar(root)
selected_option_var.set(options[0])  # Pilihan awal
option_menu = tk.OptionMenu(
    root, selected_option_var, *options, command=on_option_select
)
option_menu.place(x=10, y=500)

# Menjalankan aplikasi GUI
root.mainloop()
