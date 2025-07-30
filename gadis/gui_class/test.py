import tkinter as tk
from tkinter import messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI dengan Tkinter")
        self.root.geometry("400x300")
        
        self.label = tk.Label(self.root, text="Selamat datang di GUI Python!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.button = tk.Button(self.root, text="Klik Saya", command=self.on_button_click)
        self.button.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 12))
        self.entry.pack(pady=10)

    def on_button_click(self):
        user_input = self.entry.get()
        if user_input:
            messagebox.showinfo("Pesan", f"Selamat datang, {user_input}!")
        else:
            messagebox.showwarning("Pesan", "Harap masukkan nama terlebih dahulu.")

if __name__ == "__main__":
    root = tk.Tk() 
    app = MyApp(root) 
    root.mainloop()
