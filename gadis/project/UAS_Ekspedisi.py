import tkinter as tk
from tkinter import ttk, messagebox

class EkspedisiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Ekspedisi")
        self.root.geometry("300x200")
        self.root.configure(bg="#68BBD6")

        # --- Login Form ---
        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "12345":
            messagebox.showinfo("Login Berhasil", "Selamat datang di Aplikasi Ekspedisi/Pengiriman!")
            self.root.destroy()
            self.main_menu()
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")

    def main_menu(self):
        # Membuat window baru setelah login
        self.menu_win = tk.Tk()
        self.menu_win.geometry('1350x700+0+0')
        self.menu_win.title('Ekspedisi/Pengiriman')
        self.menu_win.config(bg='white')

        # Title
        title_label = tk.Label(self.menu_win, text="Ekspedisi/Pengiriman",
                               font=('Arial', 25), border=12, relief=tk.GROOVE, bg='#19376D', foreground='white')
        title_label.pack(side=tk.TOP, fill=tk.X)

        # Frames
        detail_frame = tk.LabelFrame(self.menu_win, text='Enter Details',
                                     font=('arial', 20), bg='#19376D', fg='white', bd=12, relief=tk.GROOVE)
        detail_frame.place(x=20, y=90, width=420, height=575)

        data_frame = tk.Frame(self.menu_win, bd=12, bg='#576CBC', relief=tk.GROOVE)
        data_frame.place(x=450, y=90, width=810, height=575)

        # Form Entries
        self.nama_awal_ent = self._make_label_entry(detail_frame, 'Nama Penerima', 0)
        self.alamat_penerima_ent = self._make_label_entry(detail_frame, 'Alamat Penerima', 2)
        self.provinsi_ent = self._make_label_entry(detail_frame, 'Provinsi', 3)
        self.kabupaten_ent = self._make_label_entry(detail_frame, 'Kabupaten', 4)
        self.kode_pos_ent = self._make_label_entry(detail_frame, 'Kode POS', 5)
        self.tlpn_ent = self._make_label_entry(detail_frame, 'Telepon', 6)

        # Buttons
        button_frame = tk.Frame(detail_frame, bg='#576CBC', bd=10, relief=tk.GROOVE)
        button_frame.place(x=27, y=390, width=339, height=112)

        add_button = tk.Button(button_frame, bg='white', text='Add', bd=7, font=('Arial', 12), width=15, command=self.add_record)
        add_button.grid(row=0, column=0, padx=2, pady=2)

        update_button = tk.Button(button_frame, bg='white', text='Update', bd=7, font=('Arial', 12), width=15, command=self.update_record)
        update_button.grid(row=0, column=1, padx=3, pady=2)

        delete_button = tk.Button(button_frame, bg='white', text='Delete', bd=7, font=('Arial', 12), width=15, command=self.delete_record)
        delete_button.grid(row=1, column=0, padx=2, pady=2)

        clear_button = tk.Button(button_frame, bg='white', text='Clear', bd=7, font=('Arial', 12), width=15, command=self.clear_fields)
        clear_button.grid(row=1, column=1, padx=3, pady=2)

        # Table
        main_frame = tk.Frame(data_frame, bg='white', bd=11, relief=tk.GROOVE)
        main_frame.pack(fill=tk.BOTH, expand=True)

        y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
        x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

        self.table_Ekspedisi = ttk.Treeview(main_frame, columns=(
            'Nama Penerima', 'Alamat Penerima', 'Provinsi', 'Kabupaten', 'Kode POS', 'Telepon'),
            yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        y_scroll.config(command=self.table_Ekspedisi.yview)
        x_scroll.config(command=self.table_Ekspedisi.xview)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        for col in ('Nama Penerima', 'Alamat Penerima', 'Provinsi', 'Kabupaten', 'Kode POS', 'Telepon'):
            self.table_Ekspedisi.heading(col, text=col)
            self.table_Ekspedisi.column(col, width=120)
        self.table_Ekspedisi['show'] = 'headings'
        self.table_Ekspedisi.pack(fill=tk.BOTH, expand=True)

        self.table_Ekspedisi.bind("<<TreeviewSelect>>", self.fill_fields)

    def _make_label_entry(self, parent, label, row):
        lbl = tk.Label(parent, text=label, font=('arial', 17), bg='#576CBC', fg='white')
        lbl.grid(row=row, column=0, padx=2, pady=2)
        ent = tk.Entry(parent, bd=7, font=('arial', 17))
        ent.grid(row=row, column=1, padx=2, pady=2)
        return ent

    def fill_fields(self, event):
        selected_item = self.table_Ekspedisi.selection()
        if not selected_item:
            return
        values = self.table_Ekspedisi.item(selected_item[0], "values")
        self.nama_awal_ent.delete(0, tk.END)
        self.nama_awal_ent.insert(0, values[0])
        self.alamat_penerima_ent.delete(0, tk.END)
        self.alamat_penerima_ent.insert(0, values[1])
        self.provinsi_ent.delete(0, tk.END)
        self.provinsi_ent.insert(0, values[2])
        self.kabupaten_ent.delete(0, tk.END)
        self.kabupaten_ent.insert(0, values[3])
        self.kode_pos_ent.delete(0, tk.END)
        self.kode_pos_ent.insert(0, values[4])
        self.tlpn_ent.delete(0, tk.END)
        self.tlpn_ent.insert(0, values[5])

    def add_record(self):
        fields = [self.nama_awal_ent, self.alamat_penerima_ent, self.provinsi_ent, self.kabupaten_ent, self.kode_pos_ent, self.tlpn_ent]
        values = [field.get().strip() for field in fields]
        if not all(values):
            messagebox.showwarning("Warning", "All fields must be filled")
            return
        self.table_Ekspedisi.insert("", "end", values=values)
        self.clear_fields()
        messagebox.showinfo("Success", "Record added successfully")

    def update_record(self):
        selected_item = self.table_Ekspedisi.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a record to update")
            return
        values = (
            self.nama_awal_ent.get(),
            self.alamat_penerima_ent.get(),
            self.provinsi_ent.get(),
            self.kabupaten_ent.get(),
            self.kode_pos_ent.get(),
            self.tlpn_ent.get(),
        )
        self.table_Ekspedisi.item(selected_item, values=values)
        self.clear_fields()
        messagebox.showinfo("Success", "Record updated successfully")

    def delete_record(self):
        selected_item = self.table_Ekspedisi.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a record to delete")
            return
        self.table_Ekspedisi.delete(selected_item)
        self.clear_fields()
        messagebox.showinfo("Success", "Record deleted successfully")

    def clear_fields(self):
        for field in [self.nama_awal_ent, self.alamat_penerima_ent, self.provinsi_ent, self.kabupaten_ent, self.kode_pos_ent, self.tlpn_ent]:
            field.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EkspedisiApp(root)
    root.mainloop()
