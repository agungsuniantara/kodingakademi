import tkinter as tk


def on_button_click():
    label_result.config(text=f"Hello, {entry_name.get()}!")


def on_listbox_select(event):
    selected_item = listbox.get(listbox.curselection())
    label_listbox_result.config(text=f"Selected Item: {selected_item}")


def on_checkbox_change():
    label_checkbox_result.config(text=f"Checkbox State: {checkbox_var.get()}")


def on_radiobutton_change():
    label_radiobutton_result.config(text=f"Selected Gender: {radio_var.get()}")


def on_optionmenu_change(*args):
    label_optionmenu_result.config(text=f"Selected Option: {var_optionmenu.get()}")


def on_scale_change(value):
    label_scale_result.config(text=f"Scale Value: {int(value)}")


def on_spinbox_change():
    label_spinbox_result.config(text=f"Spinbox Value: {spinbox_var.get()}")


# Membuat jendela utama
root = tk.Tk()
root.title("Tkinter Data Types Example")

# Label
label_text = tk.StringVar()
label_text.set("Hello, Tkinter!")
label = tk.Label(root, textvariable=label_text)
label.pack()

# Entry
entry_name = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_name)
entry.pack()

# Button
button = tk.Button(root, text="Say Hello", command=on_button_click)
button.pack()

# Text
text_widget = tk.Text(root, width=30, height=5)
text_widget.insert(tk.END, "This is a Text Widget.")
text_widget.pack()

# Listbox
listbox = tk.Listbox(root, height=3)
listbox.pack()
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")
listbox.bind("<<ListboxSelect>>", on_listbox_select)

# Checkbutton
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(
    root, text="Agree to Terms", variable=checkbox_var, command=on_checkbox_change
)
checkbox.pack()

# Radiobutton
radio_var = tk.StringVar()
radio_var.set("Male")
radio_male = tk.Radiobutton(
    root, text="Male", variable=radio_var, value="Male", command=on_radiobutton_change
)
radio_male.pack()
radio_female = tk.Radiobutton(
    root,
    text="Female",
    variable=radio_var,
    value="Female",
    command=on_radiobutton_change,
)
radio_female.pack()

# OptionMenu
options = ["Option 1", "Option 2", "Option 3"]
var_optionmenu = tk.StringVar(root)
var_optionmenu.set(options[0])
option_menu = tk.OptionMenu(root, var_optionmenu, *options)
option_menu.pack()
var_optionmenu.trace("w", on_optionmenu_change)

# Scale
scale_var = tk.DoubleVar()
scale = tk.Scale(
    root,
    variable=scale_var,
    from_=0,
    to=10,
    orient=tk.HORIZONTAL,
    command=on_scale_change,
)
scale.pack()

# Spinbox
spinbox_var = tk.IntVar()
spinbox = tk.Spinbox(
    root, from_=0, to=10, textvariable=spinbox_var, command=on_spinbox_change
)
spinbox.pack()

# Labels for displaying results
label_result = tk.Label(root, text="")
label_result.pack()

label_listbox_result = tk.Label(root, text="")
label_listbox_result.pack()

label_checkbox_result = tk.Label(root, text="")
label_checkbox_result.pack()

label_radiobutton_result = tk.Label(root, text="")
label_radiobutton_result.pack()

label_optionmenu_result = tk.Label(root, text="")
label_optionmenu_result.pack()

label_scale_result = tk.Label(root, text="")
label_scale_result.pack()

label_spinbox_result = tk.Label(root, text="")
label_spinbox_result.pack()

# Menjalankan aplikasi GUI
root.mainloop()
