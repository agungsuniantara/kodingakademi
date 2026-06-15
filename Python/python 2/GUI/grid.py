import tkinter as tk

root = tk.Tk()
root.title("Grid GUI")
root.geometry("600x600")

# 1. Membuat Frame utama sebagai wadah (container) untuk grid
main_frame = tk.Frame(root)
# Menempatkan frame tepat di tengah window (relx 0.5 = 50% X, rely 0.5 = 50% Y)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Mengatur padx=0 untuk menghilangkan margin horizontal
label = tk.Label(main_frame, text="masukan nama : ")
label.grid(row=0, column=0, padx=0, pady=10, ipadx=10, ipady=5)

entry = tk.Entry(main_frame)
entry.grid(row=0, column=1, padx=0, pady=10)

button = tk.Button(main_frame, text="Klik")
button.grid(row=0, column=2, padx=0, pady=10)

test_text = tk.Label(main_frame, text="test_text", font=("Helvetica", 16))
test_text.grid(row=1, column=0, columnspan=3, padx=0, pady=10)

reset_button = tk.Button(main_frame, text="Reset")
reset_button.grid(row=2, column=1, padx=0, pady=10)

root.mainloop()