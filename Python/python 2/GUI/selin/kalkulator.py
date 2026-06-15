from tkinter import *

root = Tk()
root.title("Python Calculator")
root.geometry("300x250")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

layar = Entry(root, font=("Arial", 14))
layar.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=5, sticky="nsew")

btn_7 = Button(root, text="7", font=("Arial", 12))
btn_7.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)

btn_8 = Button(root, text="8", font=("Arial", 12))
btn_8.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)

btn_9 = Button(root, text="9", font=("Arial", 12))
btn_9.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)

btn_tambah = Button(root, text="+", font=("Arial", 12))
btn_tambah.grid(row=1, column=3, sticky="nsew", padx=1, pady=1)

btn_4 = Button(root, text="4", font=("Arial", 12))
btn_4.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)

btn_5 = Button(root, text="5", font=("Arial", 12))
btn_5.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)

btn_6 = Button(root, text="6", font=("Arial", 12))
btn_6.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)

btn_kurang = Button(root, text="-", font=("Arial", 12))
btn_kurang.grid(row=2, column=3, sticky="nsew", padx=1, pady=1)

btn_1 = Button(root, text="1", font=("Arial", 12))
btn_1.grid(row=3, column=0, sticky="nsew", padx=1, pady=1)

btn_2 = Button(root, text="2", font=("Arial", 12))
btn_2.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)

btn_3 = Button(root, text="3", font=("Arial", 12))
btn_3.grid(row=3, column=2, sticky="nsew", padx=1, pady=1)

btn_kali = Button(root, text="*", font=("Arial", 12))
btn_kali.grid(row=3, column=3, sticky="nsew", padx=1, pady=1)

btn_c = Button(root, text="c", font=("Arial", 12))
btn_c.grid(row=4, column=0, sticky="nsew", padx=1, pady=1)

btn_0 = Button(root, text="0", font=("Arial", 12))
btn_0.grid(row=4, column=1, sticky="nsew", padx=1, pady=1)

btn_sama_dengan = Button(root, text="=", font=("Arial", 12))
btn_sama_dengan.grid(row=4, column=2, sticky="nsew", padx=1, pady=1)

btn_bagi = Button(root, text="/", font=("Arial", 12))
btn_bagi.grid(row=4, column=3, sticky="nsew", padx=1, pady=1)

root.mainloop()