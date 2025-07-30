import tkinter as tk
import os
import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import datetime

FILE_PENERIMA = "/Applications/MAMP/htdocs/local/kodingakademi/gadis/UAS/penerima.txt"
FILE_PENGIRIM = "/Applications/MAMP/htdocs/local/kodingakademi/gadis/UAS/pengirim.txt"
FILE_EKSPEDISI = "/Applications/MAMP/htdocs/local/kodingakademi/gadis/UAS/ekspedisi.txt"
FILE_PEMBAYARAN = "/Applications/MAMP/htdocs/local/kodingakademi/gadis/UAS/pembayaran.txt"

class EkspedisiApp:
    def __init__(self, win):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.win = win
        self.win.title("Login Ekspedisi")
        self.win.geometry("1000x600")

        #Background image
        self.bg_img = Image.open("/Applications/MAMP/htdocs/local/kodingakademi/gadis/UAS/gambar3.jpg").resize((1400, 700))
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(self.win, image=self.bg_photo, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.custom_font = ctk.CTkFont(family="Arial", size=30, weight="bold")
        form_frame = tk.Frame(self.win, bg="#B7E5F4", bd=0)
        form_frame.place(x=0, y=0, width=470, relheight=1.0)
        self.login_title = ctk.CTkLabel(
            form_frame,
            text="🚚 LAJU KIRIM 🚚",
            font=self.custom_font,
            text_color="#19376D"
        )
        self.login_title.place(relx=0.5, rely=0.15, anchor="center")

        inner_form = tk.Frame(form_frame, bg="#B7E5F4")
        inner_form.place(relx=0.5, rely=0.45, anchor="center")

        self.username_entry = ctk.CTkEntry(inner_form, width=220, height=35, corner_radius=15, placeholder_text="Username")
        self.username_entry.pack(pady=(10, 10))
        self.password_entry = ctk.CTkEntry(inner_form, show="*", width=220, height=35, corner_radius=15, placeholder_text="Password")
        self.password_entry.pack(pady=(0, 20))
        self.login_button = ctk.CTkButton(inner_form, text="Login", command=self.login, fg_color="#19376D", text_color="white", width=220, height=35, corner_radius=15)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "12345":
            messagebox.showinfo("Login Berhasil", "Selamat datang di Aplikasi Ekspedisi/Pengiriman!")
            self.win.withdraw()
            self.main_menu()
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")

    def logout(self):
        confirm = messagebox.askyesno("Logout", "Apakah Anda yakin ingin logout?")
        if confirm:
            self.save_all_data()
            self.menu_win.destroy()
            self.win.deiconify()

    def main_menu(self):
        self.load_all_data()
        self.menu_win = tk.Toplevel()
        self.menu_win.geometry('1200x800')
        self.menu_win.title('Ekspedisi/Pengiriman')
        self.menu_win.config(bg='white')
        title_label = tk.Label(self.menu_win, text="🚚 LAJU KIRIM 🚚", font=('Arial', 25), border=12, relief=tk.GROOVE, bg='#19376D', fg='white')
        title_label.pack(side=tk.TOP, fill=tk.X, pady=4)
        logout_button = tk.Button(self.menu_win, text="Logout", bg="#FF4B4B", fg="white", font=("Arial", 10, "bold"), command=self.logout)
        logout_button.place(relx=1.0, x=-10, y=10, anchor="ne")

        self.notebook = ttk.Notebook(self.menu_win)
        self.tab_penerima = ttk.Frame(self.notebook)
        self.tab_pengirim = ttk.Frame(self.notebook)
        self.tab_ekspedisi = ttk.Frame(self.notebook)
        self.tab_pembayaran = ttk.Frame(self.notebook)
        self.tab_laporan = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_penerima, text="Data Penerima")
        self.notebook.add(self.tab_pengirim, text="Data Pengirim")
        self.notebook.add(self.tab_ekspedisi, text="Data Ekspedisi")
        self.notebook.add(self.tab_pembayaran, text="Data Pembayaran")
        self.notebook.add(self.tab_laporan, text="Laporan")
        self.notebook.pack(fill='both', expand=True, padx=12, pady=12)

        self.setup_tab_penerima()
        self.setup_tab_pengirim()
        self.setup_tab_ekspedisi()
        self.setup_tab_pembayaran()
        self.setup_tab_laporan()
        self.update_comboboxes()

    def save_txt(self, filename, datalist):
        with open(filename, "w", encoding="utf-8") as f:
            for row in datalist:
                f.write("\t".join([str(item) for item in row]) + "\n")

    def load_txt(self, filename):
        data = []
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        data.append(tuple(line.strip().split("\t")))
        return data

    def save_all_data(self):
        self.save_txt(FILE_PENERIMA, self.data_penerima)
        self.save_txt(FILE_PENGIRIM, self.data_pengirim)
        self.save_txt(FILE_EKSPEDISI, self.data_ekspedisi)
        self.save_txt(FILE_PEMBAYARAN, self.data_pembayaran)

    def load_all_data(self):
        self.data_penerima = self.load_txt(FILE_PENERIMA)
        self.data_pengirim = self.load_txt(FILE_PENGIRIM)
        self.data_ekspedisi = self.load_txt(FILE_EKSPEDISI)
        self.data_pembayaran = self.load_txt(FILE_PEMBAYARAN)

    # Tab Penerima
    def setup_tab_penerima(self):
        frame = self.tab_penerima
        tk.Label(frame, text="Cari Nama Penerima:").pack(anchor="w", padx=10, pady=3)
        self.search_penerima_var = tk.StringVar()
        search_entry = tk.Entry(frame, textvariable=self.search_penerima_var)
        search_entry.pack(anchor="w", padx=10)
        search_entry.bind("<KeyRelease>", lambda e: self.refresh_tree_penerima())

        form = tk.Frame(frame)
        form.pack(side=tk.TOP, fill=tk.X, padx=12, pady=8)
        self.nama_penerima_ent = self._make_label_entry(form, "Nama Penerima", 0)
        self.alamat_penerima_ent = self._make_label_entry(form, "Alamat", 1)
        self.provinsi_penerima_ent = self._make_label_entry(form, "Provinsi", 2)
        self.kabupaten_penerima_ent = self._make_label_entry(form, "Kabupaten", 3)
        self.kode_pos_penerima_ent = self._make_label_entry(form, "Kode POS", 4)
        self.tlpn_penerima_ent = self._make_label_entry(form, "Telepon", 5)
        tk.Button(form, text="Tambah", bg="#00FF00", command=self.add_penerima).grid(row=0, column=2, padx=8, pady=2)
        tk.Button(form, text="Hapus", bg="#FF0000", command=self.del_penerima).grid(row=1, column=2, padx=8, pady=2)
        tk.Button(form, text="Update", bg="#E8D35D", command=self.update_penerima).grid(row=2, column=2, padx=8, pady=2)
        tk.Button(form, text="Clear", bg="#F15715", command=self.clear_penerima_fields).grid(row=3, column=2, padx=8, pady=2)

        self.tree_penerima = ttk.Treeview(frame, columns=("Nama", "Alamat", "Provinsi", "Kabupaten", "Kode POS", "Telepon"), show='headings', height=7)
        for col in self.tree_penerima["columns"]:
            self.tree_penerima.heading(col, text=col)
            self.tree_penerima.column(col, width=120, anchor="center")
        self.tree_penerima.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)
        self.tree_penerima.bind("<<TreeviewSelect>>", self.fill_fields_penerima)
        self.refresh_tree_penerima()

    def _make_label_entry(self, parent, label, row):
        tk.Label(parent, text=label).grid(row=row, column=0, sticky="w", padx=3, pady=2)
        entry = tk.Entry(parent)
        entry.grid(row=row, column=1, padx=3, pady=2)
        return entry

    def add_penerima(self):
        values = (
            self.nama_penerima_ent.get().strip(),
            self.alamat_penerima_ent.get().strip(),
            self.provinsi_penerima_ent.get().strip(),
            self.kabupaten_penerima_ent.get().strip(),
            self.kode_pos_penerima_ent.get().strip(),
            self.tlpn_penerima_ent.get().strip()
        )
        if not all(values):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        if not values[4].isdigit():
            messagebox.showwarning("Peringatan", "Kode POS harus berupa angka!")
            return
        if not values[5].isdigit():
            messagebox.showwarning("Peringatan", "Telepon harus berupa angka!")
            return
        self.data_penerima.append(values)
        self.refresh_tree_penerima()
        self.clear_penerima_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()
        self.save_all_data()

    def update_penerima(self):
        selected = self.tree_penerima.selection()
        updated_values = (
            self.nama_penerima_ent.get().strip(),
            self.alamat_penerima_ent.get().strip(),
            self.provinsi_penerima_ent.get().strip(),
            self.kabupaten_penerima_ent.get().strip(),
            self.kode_pos_penerima_ent.get().strip(),
            self.tlpn_penerima_ent.get().strip()
        )
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data penerima yang ingin diupdate!")
            return
        idx = self.tree_penerima.index(selected)
        if not all(updated_values):
            messagebox.showwarning("Peringatan", "Semua field harus diisi untuk update!")
            return
        if not updated_values[4].isdigit():
            messagebox.showwarning("Peringatan", "Kode POS harus berupa angka!")
            return
        if not updated_values[5].isdigit():
            messagebox.showwarning("Peringatan", "Telepon harus berupa angka!")
            return
        self.data_penerima[idx] = updated_values
        self.refresh_tree_penerima()
        self.clear_penerima_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()
        self.save_all_data()
        messagebox.showinfo("Info", "Data penerima berhasil diupdate.")

    def del_penerima(self):
        selected = self.tree_penerima.selection()
        if not selected: return
        idx = self.tree_penerima.index(selected)
        del self.data_penerima[idx]
        self.refresh_tree_penerima()
        self.clear_penerima_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()
        self.save_all_data()

    def fill_fields_penerima(self, event):
        selected = self.tree_penerima.selection()
        if not selected: return
        idx = self.tree_penerima.index(selected)
        vals = self.data_penerima[idx]
        self.nama_penerima_ent.delete(0, tk.END); self.nama_penerima_ent.insert(0, vals[0])
        self.alamat_penerima_ent.delete(0, tk.END); self.alamat_penerima_ent.insert(0, vals[1])
        self.provinsi_penerima_ent.delete(0, tk.END); self.provinsi_penerima_ent.insert(0, vals[2])
        self.kabupaten_penerima_ent.delete(0, tk.END); self.kabupaten_penerima_ent.insert(0, vals[3])
        self.kode_pos_penerima_ent.delete(0, tk.END); self.kode_pos_penerima_ent.insert(0, vals[4])
        self.tlpn_penerima_ent.delete(0, tk.END); self.tlpn_penerima_ent.insert(0, vals[5])

    def clear_penerima_fields(self):
        for field in [self.nama_penerima_ent, self.alamat_penerima_ent, self.provinsi_penerima_ent, self.kabupaten_penerima_ent, self.kode_pos_penerima_ent, self.tlpn_penerima_ent]:
            field.delete(0, tk.END)

    def refresh_tree_penerima(self):
        keyword = self.search_penerima_var.get().lower() if hasattr(self, "search_penerima_var") else ""
        for item in self.tree_penerima.get_children():
            self.tree_penerima.delete(item)
        for row in self.data_penerima:
            if keyword in row[0].lower():
                self.tree_penerima.insert("", "end", values=row)

    # Tab Pengirim
    def setup_tab_pengirim(self):
        frame = self.tab_pengirim
        tk.Label(frame, text="Cari Nama Pengirim:").pack(anchor="w", padx=10, pady=3)
        self.search_pengirim_var = tk.StringVar()
        search_entry = tk.Entry(frame, textvariable=self.search_pengirim_var)
        search_entry.pack(anchor="w", padx=10)
        search_entry.bind("<KeyRelease>", lambda e: self.refresh_tree_pengirim())

        form = tk.Frame(frame)
        form.pack(side=tk.TOP, fill=tk.X, padx=12, pady=8)
        self.nama_pengirim_ent = self._make_label_entry(form, "Nama Pengirim", 0)
        self.alamat_pengirim_ent = self._make_label_entry(form, "Alamat", 1)
        self.provinsi_pengirim_ent = self._make_label_entry(form, "Provinsi", 2)
        self.kabupaten_pengirim_ent = self._make_label_entry(form, "Kabupaten", 3)
        self.kode_pos_pengirim_ent = self._make_label_entry(form, "Kode POS", 4)
        self.tlpn_pengirim_ent = self._make_label_entry(form, "Telepon", 5)
        tk.Button(form, text="Tambah", bg="#00FF00", command=self.add_pengirim).grid(row=0, column=2, padx=8, pady=2)
        tk.Button(form, text="Hapus", bg="#FF0000", command=self.del_pengirim).grid(row=1, column=2, padx=8, pady=2)
        tk.Button(form, text="Update", bg="#E8D35D", command=self.update_pengirim).grid(row=2, column=2, padx=8, pady=2)
        tk.Button(form, text="Clear", bg="#F15715", command=self.clear_pengirim_fields).grid(row=3, column=2, padx=8, pady=2)

        self.tree_pengirim = ttk.Treeview(frame, columns=("Nama", "Alamat", "Provinsi", "Kabupaten", "Kode POS", "Telepon"), show='headings', height=7)
        for col in self.tree_pengirim["columns"]:
            self.tree_pengirim.heading(col, text=col)
            self.tree_pengirim.column(col, width=120, anchor="center")
        self.tree_pengirim.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)
        self.tree_pengirim.bind("<<TreeviewSelect>>", self.fill_fields_pengirim)
        self.refresh_tree_pengirim()

    def add_pengirim(self):
        values = (
            self.nama_pengirim_ent.get().strip(),
            self.alamat_pengirim_ent.get().strip(),
            self.provinsi_pengirim_ent.get().strip(),
            self.kabupaten_pengirim_ent.get().strip(),
            self.kode_pos_pengirim_ent.get().strip(),
            self.tlpn_pengirim_ent.get().strip()
        )
        if not all(values):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        if not values[4].isdigit():
            messagebox.showwarning("Peringatan", "Kode POS harus berupa angka!")
            return
        if not values[5].isdigit():
            messagebox.showwarning("Peringatan", "Telepon harus berupa angka!")
            return
        self.data_pengirim.append(values)
        self.refresh_tree_pengirim()
        self.clear_pengirim_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()
        self.save_all_data()

    def update_pengirim(self):
        selected = self.tree_pengirim.selection()
        updated_values = (
            self.nama_pengirim_ent.get().strip(),
            self.alamat_pengirim_ent.get().strip(),
            self.provinsi_pengirim_ent.get().strip(),
            self.kabupaten_pengirim_ent.get().strip(),
            self.kode_pos_pengirim_ent.get().strip(),
            self.tlpn_pengirim_ent.get().strip()
        )
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data pengirim yang ingin diupdate!")
            return
        idx = self.tree_pengirim.index(selected)
        if not all(updated_values):
            messagebox.showwarning("Peringatan", "Semua field harus diisi untuk update!")
            return
        if not updated_values[4].isdigit():
            messagebox.showwarning("Peringatan", "Kode POS harus berupa angka!")
            return
        if not updated_values[5].isdigit():
            messagebox.showwarning("Peringatan", "Telepon harus berupa angka!")
            return
        self.data_pengirim[idx] = updated_values
        self.refresh_tree_pengirim()
        self.clear_pengirim_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()
        self.save_all_data()
        messagebox.showinfo("Info", "Data pengirim berhasil diupdate.")

    def del_pengirim(self):
        selected = self.tree_pengirim.selection()
        if not selected: return
        idx = self.tree_pengirim.index(selected)
        del self.data_pengirim[idx]
        self.refresh_tree_pengirim()
        self.clear_pengirim_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()
        self.save_all_data()

    def fill_fields_pengirim(self, event):
        selected = self.tree_pengirim.selection()
        if not selected: return
        idx = self.tree_pengirim.index(selected)
        vals = self.data_pengirim[idx]
        self.nama_pengirim_ent.delete(0, tk.END); self.nama_pengirim_ent.insert(0, vals[0])
        self.alamat_pengirim_ent.delete(0, tk.END); self.alamat_pengirim_ent.insert(0, vals[1])
        self.provinsi_pengirim_ent.delete(0, tk.END); self.provinsi_pengirim_ent.insert(0, vals[2])
        self.kabupaten_pengirim_ent.delete(0, tk.END); self.kabupaten_pengirim_ent.insert(0, vals[3])
        self.kode_pos_pengirim_ent.delete(0, tk.END); self.kode_pos_pengirim_ent.insert(0, vals[4])
        self.tlpn_pengirim_ent.delete(0, tk.END); self.tlpn_pengirim_ent.insert(0, vals[5])

    def clear_pengirim_fields(self):
        for field in [self.nama_pengirim_ent, self.alamat_pengirim_ent, self.provinsi_pengirim_ent, self.kabupaten_pengirim_ent, self.kode_pos_pengirim_ent, self.tlpn_pengirim_ent]:
            field.delete(0, tk.END)

    def refresh_tree_pengirim(self):
        keyword = self.search_pengirim_var.get().lower() if hasattr(self, "search_pengirim_var") else ""
        for item in self.tree_pengirim.get_children():
            self.tree_pengirim.delete(item)
        for row in self.data_pengirim:
            if keyword in row[0].lower():
                self.tree_pengirim.insert("", "end", values=row)

    # Tab Ekspedisi
    def setup_tab_ekspedisi(self):
        frame = self.tab_ekspedisi
        form = tk.Frame(frame)
        form.pack(side=tk.TOP, fill=tk.X, padx=12, pady=12)

        tk.Label(form, text="Nama Penerima:").grid(row=0, column=0, sticky="w")
        self.eksp_cbox_penerima = ttk.Combobox(form, values=[], state="readonly", width=25)
        self.eksp_cbox_penerima.grid(row=0, column=1, padx=5)
        tk.Label(form, text="Nama Pengirim:").grid(row=1, column=0, sticky="w")
        self.eksp_cbox_pengirim = ttk.Combobox(form, values=[], state="readonly", width=25)
        self.eksp_cbox_pengirim.grid(row=1, column=1, padx=5)
        tk.Label(form, text="Nama Barang:").grid(row=2, column=0, sticky="w")
        self.eksp_nama_barang = tk.Entry(form, width=35)
        self.eksp_nama_barang.grid(row=2, column=1, padx=5)
        tk.Label(form, text="Berat Barang:").grid(row=3, column=0, sticky="w")
        self.eksp_berat_barang = tk.Entry(form, width=35)
        self.eksp_berat_barang.grid(row=3, column=1, padx=5)
        tk.Label(form, text="Jumlah Barang:").grid(row=4, column=0, sticky="w")
        self.eksp_jumlah_barang = tk.Entry(form, width=35)
        self.eksp_jumlah_barang.grid(row=4, column=1, padx=5)
        tk.Label(form, text="Alamat Penerima:").grid(row=5, column=0, sticky="w")
        self.eksp_alamat_penerima = tk.Entry(form, width=35)
        self.eksp_alamat_penerima.grid(row=5, column=1, padx=5)
        tk.Label(form, text="Tanggal Kirim:").grid(row=6, column=0, sticky="w")
        self.eksp_tgl = tk.Entry(form, width=35)
        self.eksp_tgl.grid(row=6, column=1, padx=5)
        tk.Label(form, text="Ongkos Kirim:").grid(row=7, column=0, sticky="w")
        self.eksp_ongkos = tk.Entry(form, width=35)
        self.eksp_ongkos.grid(row=7, column=1, padx=5)
        tk.Button(form, text="Tambah Ekspedisi", bg="#4CAF50", fg="white", command=self.add_ekspedisi).grid(row=8, column=0, pady=4, sticky='ew')
        tk.Button(form, text="Update Ekspedisi", bg="#E8D35D", fg="black", command=self.update_ekspedisi).grid(row=9, column=0, pady=4, sticky='ew')
        tk.Button(form, text="Hapus Ekspedisi", bg="#FF0000", fg="white", command=self.del_ekspedisi).grid(row=10, column=0, pady=4, sticky='ew')

        self.tree_ekspedisi = ttk.Treeview(frame, columns=("Nama Penerima", "Nama Pengirim", "Nama Barang", "Berat Barang", "Jumlah Barang", "Alamat Penerima", "Tanggal Kirim", "Ongkos Kirim"), show='headings')
        for col in self.tree_ekspedisi["columns"]:
            self.tree_ekspedisi.heading(col, text=col)
            self.tree_ekspedisi.column(col, width=130, anchor="center")
        self.tree_ekspedisi.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)
        self.tree_ekspedisi.bind("<<TreeviewSelect>>", self.fill_fields_ekspedisi)
        tk.Button(frame, text="Cetak Resi", bg="#1a73e8", fg="white", command=self.cetak_struk_ekspedisi).pack(pady=6)
        self.refresh_tree_ekspedisi()
    
    def del_ekspedisi(self):
        selected = self.tree_ekspedisi.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data ekspedisi yang ingin dihapus!")
            return
        idx = self.tree_ekspedisi.index(selected)
        confirm = messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ekspedisi ini?")
        if confirm:
            del self.data_ekspedisi[idx]
            self.refresh_tree_ekspedisi()
            self.refresh_tab_laporan()
            self.save_all_data()
            # Kosongkan field input
            for entry in [self.eksp_nama_barang, self.eksp_berat_barang, self.eksp_jumlah_barang, self.eksp_alamat_penerima, self.eksp_tgl, self.eksp_ongkos]:
                entry.delete(0, tk.END)
            self.eksp_cbox_penerima.set("")
            self.eksp_cbox_pengirim.set("")


    def add_ekspedisi(self):
        penerima = self.eksp_cbox_penerima.get()
        pengirim = self.eksp_cbox_pengirim.get()
        nama_barang = self.eksp_nama_barang.get()
        berat_barang = self.eksp_berat_barang.get()
        jumlah_barang = self.eksp_jumlah_barang.get()
        alamat = self.eksp_alamat_penerima.get()
        tanggal_kirim = self.eksp_tgl.get()
        ongkos_kirim = self.eksp_ongkos.get()
        if not all([penerima, pengirim, nama_barang, berat_barang, jumlah_barang, alamat, tanggal_kirim, ongkos_kirim]):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        try:
            int(jumlah_barang)
        except ValueError:
            messagebox.showwarning("Peringatan", "Jumlah Barang harus berupa angka bulat!")
            return
        try:
            float(berat_barang)
        except ValueError:
            messagebox.showwarning("Peringatan", "Berat Barang harus berupa angka!")
            return
        try:
            datetime.datetime.strptime(tanggal_kirim, "%d-%m-%Y")
        except ValueError:
            messagebox.showwarning("Peringatan", "Tanggal Kirim harus dalam format DD-MM-YYYY!")
            return
        try:
            float(ongkos_kirim)
        except ValueError:
            messagebox.showwarning("Peringatan", "Ongkos Kirim harus berupa angka (boleh desimal)!")
            return
        data = (penerima, pengirim, nama_barang, berat_barang, jumlah_barang, alamat, tanggal_kirim, ongkos_kirim)
        self.data_ekspedisi.append(data)
        self.refresh_tree_ekspedisi()
        for entry in [self.eksp_nama_barang, self.eksp_berat_barang, self.eksp_jumlah_barang, self.eksp_alamat_penerima, self.eksp_tgl, self.eksp_ongkos]:
            entry.delete(0, tk.END)
        self.eksp_cbox_penerima.set("")
        self.eksp_cbox_pengirim.set("")
        self.refresh_tab_laporan()
        self.save_all_data()
        messagebox.showinfo("Info", "Data ekspedisi berhasil ditambahkan.")

    def update_ekspedisi(self):
        selected = self.tree_ekspedisi.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data ekspedisi yang ingin diupdate!")
            return
        idx = self.tree_ekspedisi.index(selected)
        updated_values = (
            self.eksp_cbox_penerima.get(),
            self.eksp_cbox_pengirim.get(),
            self.eksp_nama_barang.get(),
            self.eksp_berat_barang.get(),
            self.eksp_jumlah_barang.get(),
            self.eksp_alamat_penerima.get(),
            self.eksp_tgl.get(),
            self.eksp_ongkos.get()
        )
        if not all(updated_values):
            messagebox.showwarning("Peringatan", "Semua field harus diisi untuk update!")
            return
        try:
            int(updated_values[4])
            float(updated_values[3])
            datetime.datetime.strptime(updated_values[6], "%d-%m-%Y")
            float(updated_values[7])
        except:
            messagebox.showwarning("Peringatan", "Ada field numerik yang tidak valid atau format tanggal salah!")
            return
        self.data_ekspedisi[idx] = updated_values
        self.refresh_tree_ekspedisi()
        for entry in [self.eksp_nama_barang, self.eksp_berat_barang, self.eksp_jumlah_barang, self.eksp_alamat_penerima, self.eksp_tgl, self.eksp_ongkos]:
            entry.delete(0, tk.END)
        self.eksp_cbox_penerima.set("")
        self.eksp_cbox_pengirim.set("")
        self.refresh_tab_laporan()
        self.save_all_data()
        messagebox.showinfo("Info", "Data ekspedisi berhasil diupdate.")

    def fill_fields_ekspedisi(self, event):
        selected = self.tree_ekspedisi.selection()
        if not selected: return
        idx = self.tree_ekspedisi.index(selected)
        vals = self.data_ekspedisi[idx]
        self.eksp_cbox_penerima.set(vals[0])
        self.eksp_cbox_pengirim.set(vals[1])
        self.eksp_nama_barang.delete(0, tk.END)
        self.eksp_nama_barang.insert(0, vals[2])
        self.eksp_berat_barang.delete(0, tk.END)
        self.eksp_berat_barang.insert(0, vals[3])
        self.eksp_jumlah_barang.delete(0, tk.END)
        self.eksp_jumlah_barang.insert(0, vals[4])
        self.eksp_alamat_penerima.delete(0, tk.END)
        self.eksp_alamat_penerima.insert(0, vals[5])
        self.eksp_tgl.delete(0, tk.END)
        self.eksp_tgl.insert(0, vals[6])
        self.eksp_ongkos.delete(0, tk.END)
        self.eksp_ongkos.insert(0, vals[7])

    def refresh_tree_ekspedisi(self):
        if not hasattr(self, "tree_ekspedisi"):
            return
        for item in self.tree_ekspedisi.get_children():
            self.tree_ekspedisi.delete(item)
        for row in self.data_ekspedisi:
            self.tree_ekspedisi.insert("", "end", values=row)

    def cetak_struk_ekspedisi(self):
        selected = self.tree_ekspedisi.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih dulu data ekspedisi yang ingin dicetak struknya!")
            return
        values = self.tree_ekspedisi.item(selected, "values")
        struk_window = tk.Toplevel(self.menu_win)
        struk_window.title("Resi Pengiriman")
        struk_window.resizable(False, False)
        teks_struk = (
            "====== RESI PENGIRIMAN ======\n"
            f"Nama Penerima  : {values[0]}\n"
            f"Nama Pengirim  : {values[1]}\n"
            f"Nama Barang    : {values[2]}\n"
            f"Berat Barang   : {values[3]}\n"
            f"Jumlah Barang  : {values[4]}\n"
            f"Alamat Penerima: {values[5]}\n"
            f"Tanggal Kirim  : {values[6]}\n"
            f"Ongkos Kirim   : {values[7]}\n"
            "=============================="
        )
        label = tk.Label(struk_window, text=teks_struk, font=('Courier', 13), justify="left", fg='black')
        label.pack(padx=15, pady=30)
        tk.Button(struk_window, text="Tutup", command=struk_window.destroy, bg="#e57373", fg="black").pack(pady=10)

    # Tab Pembayaran
    def setup_tab_pembayaran(self):
        frame = self.tab_pembayaran
        form = tk.Frame(frame)
        form.pack(side=tk.TOP, fill=tk.X, padx=12, pady=8)

        tk.Label(form, text="Nama Pembayar").grid(row=0, column=0, sticky="w", padx=3, pady=2)
        self.nama_pembayar_var = tk.StringVar()
        self.nama_pembayar_ent = ttk.Combobox(form, textvariable=self.nama_pembayar_var, state="readonly")
        self.nama_pembayar_ent.grid(row=0, column=1, padx=3, pady=2)

        tk.Label(form, text="Metode Pembayaran").grid(row=1, column=0, sticky="w", padx=3, pady=2)
        self.metode_pembayaran_var = tk.StringVar()
        self.metode_pembayaran_ent = ttk.Combobox(form, textvariable=self.metode_pembayaran_var, state="readonly")
        self.metode_pembayaran_ent["values"] = ["Qris", "Debit", "TF", "Cash"]
        self.metode_pembayaran_ent.grid(row=1, column=1, padx=3, pady=2)
        self.jumlah_bayar_ent = self._make_label_entry(form, "Jumlah Bayar (Rp)", 2)
        self.tanggal_bayar_ent = self._make_label_entry(form, "Tanggal Pembayaran", 3)

        tk.Button(form, text="Tambah", bg="#00FF00", command=self.add_pembayaran).grid(row=0, column=2, padx=8)
        tk.Button(form, text="Hapus", bg="#FF0000", command=self.del_pembayaran).grid(row=1, column=2, padx=8)
        tk.Button(form, text="Update", bg="#E8D35D", command=self.update_pembayaran).grid(row=2, column=2, padx=8)
        tk.Button(form, text="Clear", bg="#F15715", command=self.clear_pembayaran_fields).grid(row=3, column=2, padx=8)

        self.tree_pembayaran = ttk.Treeview(frame, columns=("Nama", "Metode", "Jumlah", "Tanggal"), show='headings', height=7)
        for col in self.tree_pembayaran["columns"]:
            self.tree_pembayaran.heading(col, text=col)
            self.tree_pembayaran.column(col, width=150)
        self.tree_pembayaran.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)
        self.tree_pembayaran.bind("<<TreeviewSelect>>", self.fill_fields_pembayaran)
        tk.Button(frame, text="Cetak Struk", bg="#1a73e8", fg="white", command=self.cetak_struk_pembayaran).pack(pady=6)
        self.refresh_tree_pembayaran()

    def add_pembayaran(self):
        values = (
            self.nama_pembayar_ent.get().strip(),
            self.metode_pembayaran_ent.get().strip(),
            self.jumlah_bayar_ent.get().strip(),
            self.tanggal_bayar_ent.get().strip()
        )
        if not all(values):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        if not values[2].replace(".", "", 1).isdigit():
            messagebox.showwarning("Peringatan", "Jumlah Bayar harus berupa angka!")
            return
        try:
            datetime.datetime.strptime(values[3], "%d-%m-%Y")
        except:
            messagebox.showwarning("Peringatan", "Tanggal Pembayaran harus dalam format DD-MM-YYYY!")
            return
        self.data_pembayaran.append(values)
        self.refresh_tree_pembayaran()
        self.clear_pembayaran_fields()
        self.refresh_tab_laporan()
        self.save_all_data()

    def update_pembayaran(self):
        selected = self.tree_pembayaran.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data pembayaran yang ingin diupdate!")
            return
        idx = self.tree_pembayaran.index(selected)
        updated_values = (
            self.nama_pembayar_ent.get().strip(),
            self.metode_pembayaran_ent.get().strip(),
            self.jumlah_bayar_ent.get().strip(),
            self.tanggal_bayar_ent.get().strip()
        )
        if not all(updated_values):
            messagebox.showwarning("Peringatan", "Semua field harus diisi untuk update!")
            return
        if not updated_values[2].replace(".", "", 1).isdigit():
            messagebox.showwarning("Peringatan", "Jumlah Bayar harus berupa angka!")
            return
        try:
            datetime.datetime.strptime(updated_values[3], "%d-%m-%Y")
        except:
            messagebox.showwarning("Peringatan", "Tanggal Pembayaran harus dalam format DD-MM-YYYY!")
            return
        self.data_pembayaran[idx] = updated_values
        self.refresh_tree_pembayaran()
        self.clear_pembayaran_fields()
        self.refresh_tab_laporan()
        self.save_all_data()
        messagebox.showinfo("Info", "Data pembayaran berhasil diupdate.")

    def del_pembayaran(self):
        selected = self.tree_pembayaran.selection()
        if not selected: return
        idx = self.tree_pembayaran.index(selected)
        del self.data_pembayaran[idx]
        self.refresh_tree_pembayaran()
        self.clear_pembayaran_fields()
        self.refresh_tab_laporan()
        self.save_all_data()

    def fill_fields_pembayaran(self, event):
        selected = self.tree_pembayaran.selection()
        if not selected: return
        idx = self.tree_pembayaran.index(selected)
        vals = self.data_pembayaran[idx]
        self.nama_pembayar_ent.set(vals[0])
        self.metode_pembayaran_ent.set(vals[1])
        self.jumlah_bayar_ent.delete(0, tk.END); self.jumlah_bayar_ent.insert(0, vals[2])
        self.tanggal_bayar_ent.delete(0, tk.END); self.tanggal_bayar_ent.insert(0, vals[3])

    def clear_pembayaran_fields(self):
        self.nama_pembayar_var.set("")
        self.metode_pembayaran_var.set("")
        for field in [self.jumlah_bayar_ent, self.tanggal_bayar_ent]:
            field.delete(0, tk.END)

    def refresh_tree_pembayaran(self):
        if not hasattr(self, "tree_pembayaran"):
            return
        for item in self.tree_pembayaran.get_children():
            self.tree_pembayaran.delete(item)
        for row in self.data_pembayaran:
            self.tree_pembayaran.insert("", "end", values=row)

    def cetak_struk_pembayaran(self):
        selected = self.tree_pembayaran.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih dulu data pembayaran yang ingin dicetak struknya!")
            return
        values = self.tree_pembayaran.item(selected, "values")
        struk_window = tk.Toplevel(self.menu_win)
        struk_window.title("Struk Pembayaran")
        struk_window.resizable(False, False)
        teks_struk = (
            "====== STRUK PEMBAYARAN ======\n"
            f"Nama Pembayar    : {values[0]}\n"
            f"Metode Pembayaran: {values[1]}\n"
            f"Jumlah Bayar     : Rp {values[2]}\n"
            f"Tanggal          : {values[3]}\n"
            "=============================="
        )
        label = tk.Label(struk_window, text=teks_struk, font=('Courier', 12), justify="left", fg='black')
        label.pack(padx=15, pady=30)
        tk.Button(struk_window, text="Tutup", command=struk_window.destroy, bg="#e57373", fg="black").pack(pady=10)

    # Comboboxes update
    def update_comboboxes(self):
        if hasattr(self, "eksp_cbox_pengirim"):
            self.eksp_cbox_pengirim["values"] = [x[0] for x in self.data_pengirim]
        if hasattr(self, "eksp_cbox_penerima"):
            self.eksp_cbox_penerima["values"] = [x[0] for x in self.data_penerima]
        if hasattr(self, "nama_pembayar_ent"):
            self.nama_pembayar_ent['values'] = [x[0] for x in self.data_pengirim]

    # Tab Laporan
    def setup_tab_laporan(self):
        frame = self.tab_laporan
        for widget in frame.winfo_children():
            widget.destroy()
        tk.Label(frame, text="Laporan Data Lengkap", font=('Arial', 16, 'bold')).pack(pady=10)
        self.laporan_text_area = tk.Text(frame, wrap=tk.WORD, font=('Courier', 11))
        self.laporan_text_area.pack(expand=True, fill='both', padx=10, pady=10)
        self.refresh_tab_laporan()

    def refresh_tab_laporan(self):
        if not hasattr(self, 'laporan_text_area') or not self.laporan_text_area.winfo_exists():
            self.setup_tab_laporan()
            return
        self.laporan_text_area.config(state='normal')
        self.laporan_text_area.delete(1.0, tk.END)
        laporan_teks = ""
        if not self.data_ekspedisi and not self.data_pembayaran:
            laporan_teks = "Tidak ada data ekspedisi atau pembayaran untuk dilaporkan."
        else:
            if self.data_ekspedisi:
                laporan_teks += f"{'No':<4} {'Penerima':<15} {'Pengirim':<15} {'Nama Barang':<14} {'Jumlah':<8} {'Tanggal':<12} {'Ongkir':<10}\n"
                laporan_teks += "-"*85 + "\n"
                for i, d in enumerate(self.data_ekspedisi):
                    laporan_teks += f"{i+1:<4} {d[0]:<15} {d[1]:<15} {d[2]:<14} {d[4]:<8} {d[6]:<12} {d[7]:<10}\n"
            if self.data_pembayaran:
                laporan_teks += "\n"
                laporan_teks += f"{'No':<4} {'Nama Pembayar':<15} {'Metode':<10} {'Jumlah':<12} {'Tanggal':<12}\n"
                laporan_teks += "-"*60 + "\n"
                for i, d in enumerate(self.data_pembayaran):
                    laporan_teks += f"{i+1:<4} {d[0]:<15} {d[1]:<10} Rp {d[2]:<8} {d[3]:<12}\n"
        self.laporan_text_area.insert(tk.END, laporan_teks)
        self.laporan_text_area.config(state='disabled')

    def on_close(self):
        self.save_all_data()
        self.win.destroy()

if __name__ == "__main__":
    win = tk.Tk()
    app = EkspedisiApp(win)
    win.protocol("WM_DELETE_WINDOW", app.on_close)
    win.mainloop()
