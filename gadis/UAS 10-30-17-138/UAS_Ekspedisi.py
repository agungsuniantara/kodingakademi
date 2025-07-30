import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 

class EkspedisiApp:
    def __init__(self, win):
        self.win = win
        self.win.title("Login Ekspedisi")
        self.win.geometry("1000x600")

        #background image
        self.bg_img = Image.open("UAS_Ekspedisi\gambar3.jpg").resize((1400, 700))
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(self.win, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        #judul login
        self.login_title = tk.Label(self.win, text="🚚 LAJU KIRIM 🚚", font=("Montserrat", 14, "bold"), 
                            fg="#19376D")
        self.login_title.place(x=165, y=20)

        #login form
        form_frame = tk.Frame(self.win, bg="#68BBD6", bd=0)
        form_frame.place(x=97, y=50, width=310, height=220)

        tk.Label(form_frame, text="Username", bg="#68BBD6", font=("Arial", 11)).pack(pady=(20, 5))
        self.username_entry = tk.Entry(form_frame)
        self.username_entry.pack(pady=2)
        tk.Label(form_frame, text="Password", bg="#68BBD6", font=("Arial", 11)).pack(pady=(20, 5))
        self.password_entry = tk.Entry(form_frame, show="*")
        self.password_entry.pack(pady=2)
        tk.Button(form_frame, text="Login", command=self.login, bg="#19376D", fg="white", width=20).pack(pady=24)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "12345":
            messagebox.showinfo("Login Berhasil", "Selamat datang di Aplikasi Ekspedisi/Pengiriman!")
            self.win.destroy()
            self.main_menu()
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")

    def main_menu(self):
        self.menu_win = tk.Tk()
        self.menu_win.geometry('1200x800')
        self.menu_win.title('Ekspedisi/Pengiriman')
        self.menu_win.config(bg='white')

        title_label = tk.Label(self.menu_win, text="🚚 LAJU KIRIM 🚚",
                               font=('Arial', 25), border=12, relief=tk.GROOVE, bg='#19376D', fg='white')
        title_label.pack(side=tk.TOP, fill=tk.X, pady=4)

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

        self.data_penerima = []
        self.data_pengirim = []
        self.data_pembayaran = []
        self.data_ekspedisi = []

        self.setup_tab_penerima()
        self.setup_tab_pengirim()
        self.setup_tab_ekspedisi()
        self.setup_tab_pembayaran()
        self.setup_tab_laporan()
        self.update_comboboxes()

#     #TAB PENERIMA
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

        add_btn = tk.Button(form, text="Tambah", bg="#00FF00", command=self.add_penerima)
        add_btn.grid(row=0, column=2, padx=8, pady=2)
        del_btn = tk.Button(form, text="Hapus", bg="#FF0000", command=self.del_penerima)
        del_btn.grid(row=1, column=2, padx=8, pady=2)
        update_btn = tk.Button(form, text="Update", bg="#E8D35D", command=self.update_penerima)
        update_btn.grid(row=2, column=2, padx=8, pady=2)
        clear_btn = tk.Button(form, text="Clear", bg="#F15715", command=self.clear_penerima_fields)
        clear_btn.grid(row=3, column=2, padx=8, pady=2)

        self.tree_penerima = ttk.Treeview(frame, columns=("Nama", "Alamat", "Provinsi", "Kabupaten", "Kode POS", "Telepon"), show='headings', height=7)
        for col in self.tree_penerima["columns"]:
            self.tree_penerima.heading(col, text=col)
            self.tree_penerima.column(col, width=120)
        self.tree_penerima.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)
        self.tree_penerima.bind("<<TreeviewSelect>>", self.fill_fields_penerima)

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
        self.data_penerima.append(values)
        self.refresh_tree_penerima()
        self.clear_penerima_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()

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
        
        idx= self.tree_penerima.index(selected)

        if not all(updated_values):
            messagebox.showwarning("Peringatan", "Semua field harus diisi untuk update!")
            return
            
        self.data_penerima[idx] = updated_values
        self.refresh_tree_penerima()
        self.clear_penerima_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()
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
        keyword = self.search_penerima_var.get().lower()
        for item in self.tree_penerima.get_children():
            self.tree_penerima.delete(item)
        for row in self.data_penerima:
            if keyword in row[0].lower():
                self.tree_penerima.insert("", "end", values=row)

    #TAB PENGIRIM
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

        add_btn = tk.Button(form, text="Tambah", bg="#00FF00", command=self.add_pengirim)
        add_btn.grid(row=0, column=2, padx=8, pady=2)
        del_btn = tk.Button(form, text="Hapus", bg="#FF0000", command=self.del_pengirim)
        del_btn.grid(row=1, column=2, padx=8, pady=2)
        # update_btn = tk.Button(form, text="Update", bg="#E8D35D", command=self.update_pegirim)
        # update_btn.grid(row=2, column=2, padx=8, pady=2)
        clear_btn = tk.Button(form, text="Clear", bg="#F15715", command=self.clear_pengirim_fields)
        clear_btn.grid(row=3, column=2, padx=8, pady=2)

        self.tree_pengirim = ttk.Treeview(frame, columns=("Nama", "Alamat", "Provinsi", "Kabupaten", "Kode POS", "Telepon"), show='headings', height=7)
        for col in self.tree_pengirim["columns"]:
            self.tree_pengirim.heading(col, text=col)
            self.tree_pengirim.column(col, width=120)
        self.tree_pengirim.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)
        self.tree_pengirim.bind("<<TreeviewSelect>>", self.fill_fields_pengirim)
        self.data_pengirim = []

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
        self.data_pengirim.append(values)
        self.refresh_tree_pengirim()
        self.clear_pengirim_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()

    # def update_pengirim(self):
    #     selected = self.tree_pengirim.selection()
        
    #     updated_values = (
    #         self.nama_pengirim_ent.get().strip(),
    #         self.alamat_pengirim_ent.get().strip(),
    #         self.provinsi_pengirim_ent.get().strip(),
    #         self.kabupaten_pengirim_ent.get().strip(),
    #         self.kode_pos_pengirim_ent.get().strip(),
    #         self.tlpn_pengirim_ent.get().strip()
    #     )

    #     if not selected:
    #         messagebox.showwarning("Peringatan", "Pilih data pengirim yang ingin diupdate!")
    #         return
        
    #     idx= self.tree_pengirim.index(selected)

    #     if not all(updated_values):
    #         messagebox.showwarning("Peringatan", "Semua field harus diisi untuk update!")
    #         return
            
    #     self.data_pengirim[idx] = updated_values
    #     self.refresh_tree_pengirim()
    #     self.clear_pengirim_fields()
    #     self.update_comboboxes()
    #     self.refresh_tab_laporan()
    #     messagebox.showinfo("Info", "Data penerima berhasil diupdate.")

    def del_pengirim(self):
        selected = self.tree_pengirim.selection()
        if not selected: return
        idx = self.tree_pengirim.index(selected)
        del self.data_pengirim[idx]
        self.refresh_tree_pengirim()
        self.clear_pengirim_fields()
        self.update_comboboxes()
        self.refresh_tab_laporan()

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
        keyword = self.search_pengirim_var.get().lower()
        for item in self.tree_pengirim.get_children():
            self.tree_pengirim.delete(item)
        for row in self.data_pengirim:
            if keyword in row[0].lower():
                self.tree_pengirim.insert("", "end", values=row)

    #TAB EKSPEDISI
    def setup_tab_ekspedisi(self):
        frame = self.tab_ekspedisi
        form = tk.Frame(frame)
        form.pack(side=tk.TOP, fill=tk.X, padx=12, pady=12)

        tk.Label(form, text="Nama Penerima:").grid(row=0, column=0, sticky="w")
        self.eksp_cbox_penerima = ttk.Combobox(form, values=[], state="readonly", width=25)
        self.eksp_cbox_penerima.grid(row=0, column=1, padx=5)
        self.eksp_cbox_penerima.bind("<<ComboboxSelected>>") #self.fill_penerima_to_ekspedisi)

        tk.Label(form, text="Nama Pengirim:").grid(row=1, column=0, sticky="w")
        self.eksp_cbox_pengirim = ttk.Combobox(form, values=[], state="readonly", width=25)
        self.eksp_cbox_pengirim.grid(row=1, column=1, padx=5)
        self.eksp_cbox_pengirim.bind("<<ComboboxSelected>>") #self.fill_pengirim_to_ekspedisi)

        tk.Label(form, text="Nama Barang:").grid(row=2, column=0, sticky="w")
        self.eksp_alamat = tk.Entry(form, width=35)
        self.eksp_alamat.grid(row=2, column=1, padx=5)

        tk.Label(form, text="Berat Barang:").grid(row=3, column=0, sticky="w")
        self.eksp_provinsi = tk.Entry(form, width=35)
        self.eksp_provinsi.grid(row=3, column=1, padx=5)

        tk.Label(form, text="Jumlah Barang:").grid(row=4, column=0, sticky="w")
        self.eksp_kabupaten = tk.Entry(form, width=35)
        self.eksp_kabupaten.grid(row=4, column=1, padx=5)

        tk.Label(form, text="Alamat Penerima:").grid(row=5, column=0, sticky="w")
        self.eksp_kode_pos = tk.Entry(form, width=35)
        self.eksp_kode_pos.grid(row=5, column=1, padx=5)

        tk.Label(form, text="Tanggal Kirim:").grid(row=6, column=0, sticky="w")
        self.eksp_tlpn = tk.Entry(form, width=35)
        self.eksp_tlpn.grid(row=6, column=1, padx=5)

        tk.Label(form, text="Ongkos Kirim:").grid(row=7, column=0, sticky="w")
        self.eksp_pelunasan = tk.Entry(form, width=35)
        self.eksp_pelunasan.grid(row=7, column=1, padx=5)

        add_btn = tk.Button(form, text="Tambah Ekspedisi", bg="#4CAF50", fg="white", command=self.add_ekspedisi)
        add_btn.grid(row=8, column=0, columnspan=2, pady=8)

        self.tree_ekspedisi = ttk.Treeview(frame, columns=("Nama Penerima", "Nama Pengirim", "Nama Barang", "Berat Barang", "Jumlah Barang", "Alamat Penerima", "Tanggal Kirim", "Ongkos Kirim"), show='headings')
        for col in self.tree_ekspedisi["columns"]:
            self.tree_ekspedisi.heading(col, text=col)
            self.tree_ekspedisi.column(col, width=130)
        self.tree_ekspedisi.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)

        #posisi tombol di bawah tabel (sejajar style sm tab pembayaran)
        cetak_btn = tk.Button(frame, text="Cetak Struk", bg="#1a73e8", fg="white", command=self.cetak_struk_ekspedisi)
        cetak_btn.pack(pady=6)
        
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
            f"Nama Baranng   : {values[2]}\n"
            f"Berat Barang   : {values[3]}\n"
            f"Jumlah Kirim   : {values[4]}\n"
            f"Alamat Penerima: {values[5]}\n"
            f"Tanggal Kirim  : {values[6]}\n"
            f"Ongkos Kirim   : {values[7]}\n"
            "=============================="
        )

        label = tk.Label(struk_window, text=teks_struk, font=('Courier', 20), justify="left", fg='black')
        label.pack(padx=15, pady=30)

        btn_close = tk.Button(struk_window, text="Tutup", command=struk_window.destroy, bg="#e57373", fg="black")
        btn_close.pack(pady=10)
    
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
        btn_close = tk.Button(struk_window, text="Tutup", command=struk_window.destroy, bg="#e57373", fg="black")
        btn_close.pack(pady=10)

    def fill_penerima_to_ekspedisi(self, event):
        nama = self.eksp_cbox_penerima.get()
        for row in self.data_penerima:
            if row[0] == nama:
                self.eksp_alamat.delete(0, tk.END)
                self.eksp_provinsi.delete(0, tk.END)
                self.eksp_kabupaten.delete(0, tk.END)
                self.eksp_kode_pos.delete(0, tk.END)
                self.eksp_tlpn.delete(0, tk.END)
                self.eksp_pelunasan.delete(0, tk.END)
                self.eksp_alamat.insert(0, row[1])
                self.eksp_provinsi.insert(0, row[2])
                self.eksp_kabupaten.insert(0, row[3])
                self.eksp_kode_pos.insert(0, row[4])
                self.eksp_tlpn.insert(0, row[5])
                self.eksp_pelunasan.insert(0, row[6])
                break

    def fill_pengirim_to_ekspedisi(self, event):
        nama = self.eksp_cbox_pengirim.get()
        for row in self.data_pengirim:
            if row[0] == nama: #kalo pengen field otomatis isinya dari data pengirim, bisa atur disini
                break

    def add_ekspedisi(self):
        values = (
            self.eksp_cbox_penerima.get(),
            self.eksp_cbox_pengirim.get(),
            self.eksp_alamat.get(),
            self.eksp_provinsi.get(),
            self.eksp_kabupaten.get(),
            self.eksp_kode_pos.get(),
            self.eksp_tlpn.get(),
            self.eksp_pelunasan.get()
        )
        if not all(values):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        self.tree_ekspedisi.insert("", "end", values=values)
        for entry in [self.eksp_alamat, self.eksp_provinsi, self.eksp_kabupaten, self.eksp_kode_pos, self.eksp_tlpn]:
            entry.delete(0, tk.END)
        self.eksp_cbox_penerima.set("")
        self.eksp_cbox_pengirim.set("")

    def update_comboboxes(self):
        names_penerima = [x[0] for x in self.data_penerima]
        self.eksp_cbox_penerima["values"] = names_penerima
        names_pengirim = [x[0] for x in self.data_pengirim]
        self.eksp_cbox_pengirim["values"] = names_pengirim

    #TAB PEMBAYARAN
    def setup_tab_pembayaran(self):
        frame = self.tab_pembayaran
        form = tk.Frame(frame)
        form.pack(side=tk.TOP, fill=tk.X, padx=12, pady=8)

        self.nama_pembayar_ent = self._make_label_entry(form, "Nama Pembayar", 0)
        self.metode_pembayaran_ent = self._make_label_entry(form, "Metode Pembayaran", 1)
        self.jumlah_bayar_ent = self._make_label_entry(form, "Jumlah Bayar (Rp)", 2)
        self.tanggal_bayar_ent = self._make_label_entry(form, "Tanggal Pembayaran", 3)

        add_btn = tk.Button(form, text="Tambah", bg="#00FF00", command=self.add_pembayaran)
        add_btn.grid(row=0, column=2, rowspan=2, padx=8)
        del_btn = tk.Button(form, text="Hapus", bg="#FF0000", command=self.del_pembayaran)
        del_btn.grid(row=1, column=2, rowspan=2, padx=8)
        clear_btn = tk.Button(form, text="Clear", bg="#F15715",  command=self.clear_pembayaran_fields)
        clear_btn.grid(row=2, column=2, rowspan=2, padx=8)

        self.tree_pembayaran = ttk.Treeview(frame, columns=("Nama", "Metode", "Jumlah", "Tanggal"), show='headings', height=7)
        for col in self.tree_pembayaran["columns"]:
            self.tree_pembayaran.heading(col, text=col)
            self.tree_pembayaran.column(col, width=150)
        self.tree_pembayaran.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)

        self.tree_pembayaran.bind("<<TreeviewSelect>>", self.fill_fields_pembayaran)
        
        cetak_btn = tk.Button(frame, text="Cetak Struk", bg="#1a73e8", fg="white", command=self.cetak_struk_pembayaran)
        cetak_btn.pack(pady=6)

        self.data_pembayaran = []

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
        self.data_pembayaran.append(values)
        self.refresh_tree_pembayaran()
        self.clear_pembayaran_fields()
        self.refresh_tab_laporan()

    def del_pembayaran(self):
        selected = self.tree_pembayaran.selection()
        if not selected: return
        idx = self.tree_pembayaran.index(selected)
        del self.data_pembayaran[idx]
        self.refresh_tree_pembayaran()
        self.clear_pembayaran_fields()
        self.refresh_tab_laporan

    def fill_fields_pembayaran(self, event):
        selected = self.tree_pembayaran.selection()
        if not selected: return
        idx = self.tree_pembayaran.index(selected)
        vals = self.data_pembayaran[idx]
        self.nama_pembayar_ent.delete(0, tk.END); self.nama_pembayar_ent.insert(0, vals[0])
        self.metode_pembayaran_ent.delete(0, tk.END); self.metode_pembayaran_ent.insert(0, vals[1])
        self.jumlah_bayar_ent.delete(0, tk.END); self.jumlah_bayar_ent.insert(0, vals[2])
        self.tanggal_bayar_ent.delete(0, tk.END); self.tanggal_bayar_ent.insert(0, vals[3])

    def clear_pembayaran_fields(self):
        for field in [self.nama_pembayar_ent, self.metode_pembayaran_ent, self.jumlah_bayar_ent, self.tanggal_bayar_ent]:
            field.delete(0, tk.END)

    def refresh_tree_pembayaran(self):
        for item in self.tree_pembayaran.get_children():
            self.tree_pembayaran.delete(item)
        for row in self.data_pembayaran:
            self.tree_pembayaran.insert("", "end", values=row)
        
    #tambah tab laporan
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
            #LAPORAN DATA PENERIMA
            if self.data_penerima:
                laporan_teks += "LAPORAN DATA PENERIMA\n\n"
                for i, penerima_data in enumerate(self.data_penerima):
                    laporan_teks += f"--- Data Penerima Ke-{i+1} ---\n"
                    laporan_teks += f"Nama Penerima : {penerima_data[0]}\n"
                    laporan_teks += f"Alamat        : {penerima_data[1]}\n"
                    laporan_teks += f"Provinsi      : {penerima_data[2]}\n"
                    laporan_teks += f"Kabupaten     : {penerima_data[3]}\n"
                    laporan_teks += f"Kode POS      : {penerima_data[4]}\n"
                    laporan_teks += f"Telepon       : {penerima_data[5]}\n"
                    laporan_teks += "------------------------------\n\n"

            #LAPORAN DATA PENGIRIM
            if self.data_pengirim:
                laporan_teks += "\nLAPORAN DATA PENGIRIM\n\n"
                for i, pengirim_data in enumerate(self.data_pengirim):
                    laporan_teks += f"--- Data Pengirim Ke-{i+1} ---\n"
                    laporan_teks += f"Nama Pengirim : {pengirim_data[0]}\n"
                    laporan_teks += f"Alamat        : {pengirim_data[1]}\n"
                    laporan_teks += f"Provinsi      : {pengirim_data[2]}\n"
                    laporan_teks += f"Kabupaten     : {pengirim_data[3]}\n"
                    laporan_teks += f"Kode POS      : {pengirim_data[4]}\n"
                    laporan_teks += f"Telepon       : {pengirim_data[5]}\n"
                    laporan_teks += "------------------------------\n\n"

            #LAPORAN DATA EKSPEDISI
            if self.data_ekspedisi:
                laporan_teks += "\nLAPORAN DATA EKSPEDISI\n\n"
                for i, ekspedisi_data in enumerate(self.data_ekspedisi):
                    laporan_teks += f"--- Data Pengiriman Ke-{i+1} ---\n"
                    laporan_teks += f"Nama Penerima : {ekspedisi_data[0]}\n"
                    laporan_teks += f"Nama Pengirim : {ekspedisi_data[1]}\n"
                    laporan_teks += f"Alamat        : {ekspedisi_data[2]}\n"
                    laporan_teks += f"Provinsi      : {ekspedisi_data[3]}\n"
                    laporan_teks += f"Kabupaten     : {ekspedisi_data[4]}\n"
                    laporan_teks += f"Kode POS      : {ekspedisi_data[5]}\n"
                    laporan_teks += f"Telepon       : {ekspedisi_data[6]}\n"
                    laporan_teks += f"Pelunasan     : {ekspedisi_data[7]}\n"
                    laporan_teks += "------------------------------\n\n"

            #LAPORAN DATA PEMBAYARAN
            if self.data_pembayaran:
                laporan_teks += "\nLAPORAN DATA PEMBAYARAN\n\n"
                for i, pembayaran_data in enumerate(self.data_pembayaran):
                    laporan_teks += f"--- Data Pembayaran Ke-{i+1} ---\n"
                    laporan_teks += f"Nama Pembayar       : {pembayaran_data[0]}\n"
                    laporan_teks += f"Metode Pembayaran   : {pembayaran_data[1]}\n"
                    laporan_teks += f"Jumlah Bayar        : Rp {pembayaran_data[2]}\n"
                    laporan_teks += f"Tanggal Pembayaran  : {pembayaran_data[3]}\n"
                    laporan_teks += "------------------------------\n\n"

            if not self.data_penerima and not self.data_pengirim and not self.data_ekspedisi and not self.data_pembayaran:
                laporan_teks = "Tidak ada data untuk dilaporkan."


            self.laporan_text_area.insert(tk.END, laporan_teks)
            self.laporan_text_area.config(state='disabled')

if __name__ == "__main__":
    win = tk.Tk()
    app = EkspedisiApp(win)
    win.mainloop()