import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Tkinter Data Types Example")

# Menentukan ukuran jendela
root.geometry("400x600")

# StringVar
string_var = tk.StringVar()
string_var.set("Default Text")

label_string = tk.Label(root, textvariable=string_var)
label_string.place(x=10, y=10)

entry_string = tk.Entry(root, textvariable=string_var)
entry_string.place(x=10, y=40)

# IntVar
int_var = tk.IntVar()
int_var.set(0)

label_int = tk.Label(root, textvariable=int_var)
label_int.place(x=10, y=70)

scale_int = tk.Scale(root, variable=int_var, from_=0, to=10, orient=tk.HORIZONTAL)
scale_int.place(x=10, y=90)

# DoubleVar
double_var = tk.DoubleVar()
double_var.set(0.0)

label_double = tk.Label(root, textvariable=double_var)
label_double.place(x=10, y=140)

spinbox_double = tk.Spinbox(
    root, textvariable=double_var, from_=0, to=10, increment=0.1
)
spinbox_double.place(x=10, y=170)

# BooleanVar
boolean_var = tk.BooleanVar()
boolean_var.set(False)

label_boolean = tk.Label(root, textvariable=boolean_var)
label_boolean.place(x=10, y=200)

checkbox_boolean = tk.Checkbutton(root, text="Check me", variable=boolean_var)
checkbox_boolean.place(x=10, y=230)

# Menjalankan aplikasi GUI
root.mainloop()
