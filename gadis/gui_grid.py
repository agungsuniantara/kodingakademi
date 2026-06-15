import tkinter as tk

root = tk.Tk()
root.title("Grid GUI")
root.geometry("600x600")

label = tk.Label(root, text = "masukan nama : ")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=10)

button = tk.Button(root, text="Klik")
button.grid(row=0, column=2, padx=5, pady=10)

test_text = tk.Label(root, text="test_text", font=("Helvetica", 16))
test_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

reset_button = tk.Button(root, text="Reset")
reset_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()