import tkinter as tk
from tkinter import ttk, messagebox

class EkspedisiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Ekspedisi")
        self.root.geometry("350x200")
        self.root.configure(bg="#68BBD6")

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
        self.menu_win = tk.Tk()
        self.menu_win.geometry('1200x650')
        self.menu_win.title('Ekspedisi/Pengiriman')
        self.menu_win.config(bg='white')

        title_label = tk.Label(self.menu_win, text="Ekspedisi/Pengiriman",
                               font=('Arial', 25), border=12, relief=tk.GROOVE, bg='#19376D', fg='white')
        title_label.pack(side=tk.TOP, fill=tk.X, pady=4)

        self.notebook = ttk.Notebook(self.menu_win)
        self.tab_penerima = ttk.Frame(self.notebook)
        self.tab_pengirim = ttk.Frame(self.notebook)
        self.tab_ekspedisi = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_penerima, text="Data Penerima")
        self.notebook.add(self.tab_pengirim, text="Data Pengirim")
        self.notebook.add(self.tab_ekspedisi, text="Data Ekspedisi")
        self.notebook.pack(fill='both', expand=True, padx=12, pady=12)

        self.data_penerima = []
        self.data_pengirim = []

        self.setup_tab_penerima()
        self.setup_tab_pengirim()
        self.setup_tab_ekspedisi()

    # ---------------- TAB PENERIMA ----------------
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

        add_btn = tk.Button(form, text="Tambah", command=self.add_penerima)
        add_btn.grid(row=0, column=2, rowspan=2, padx=8)
        del_btn = tk.Button(form, text="Hapus", command=self.del_penerima)
        del_btn.grid(row=2, column=2, rowspan=2, padx=8)
        clear_btn = tk.Button(form, text="Clear", command=self.clear_penerima_fields)
        clear_btn.grid(row=4, column=2, rowspan=2, padx=8)

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

    def del_penerima(self):
        selected = self.tree_penerima.selection()
        if not selected: return
        idx = self.tree_penerima.index(selected)
        del self.data_penerima[idx]
        self.refresh_tree_penerima()
        self.clear_penerima_fields()
        self.update_comboboxes()

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

    # ---------------- TAB PENGIRIM ----------------
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

        add_btn = tk.Button(form, text="Tambah", command=self.add_pengirim)
        add_btn.grid(row=0, column=2, rowspan=2, padx=8)
        del_btn = tk.Button(form, text="Hapus", command=self.del_pengirim)
        del_btn.grid(row=2, column=2, rowspan=2, padx=8)
        clear_btn = tk.Button(form, text="Clear", command=self.clear_pengirim_fields)
        clear_btn.grid(row=4, column=2, rowspan=2, padx=8)

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

    def del_pengirim(self):
        selected = self.tree_pengirim.selection()
        if not selected: return
        idx = self.tree_pengirim.index(selected)
        del self.data_pengirim[idx]
        self.refresh_tree_pengirim()
        self.clear_pengirim_fields()
        self.update_comboboxes()

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

    # ---------------- TAB EKSPEDISI ----------------
    def setup_tab_ekspedisi(self):
        frame = self.tab_ekspedisi
        form = tk.Frame(frame)
        form.pack(side=tk.TOP, fill=tk.X, padx=12, pady=12)

        tk.Label(form, text="Nama Penerima:").grid(row=0, column=0, sticky="w")
        self.eksp_cbox_penerima = ttk.Combobox(form, values=[], state="readonly", width=25)
        self.eksp_cbox_penerima.grid(row=0, column=1, padx=5)
        self.eksp_cbox_penerima.bind("<<ComboboxSelected>>", self.fill_penerima_to_ekspedisi)

        tk.Label(form, text="Nama Pengirim:").grid(row=1, column=0, sticky="w")
        self.eksp_cbox_pengirim = ttk.Combobox(form, values=[], state="readonly", width=25)
        self.eksp_cbox_pengirim.grid(row=1, column=1, padx=5)
        self.eksp_cbox_pengirim.bind("<<ComboboxSelected>>", self.fill_pengirim_to_ekspedisi)

        tk.Label(form, text="Alamat:").grid(row=2, column=0, sticky="w")
        self.eksp_alamat = tk.Entry(form, width=35)
        self.eksp_alamat.grid(row=2, column=1, padx=5)

        tk.Label(form, text="Provinsi:").grid(row=3, column=0, sticky="w")
        self.eksp_provinsi = tk.Entry(form, width=35)
        self.eksp_provinsi.grid(row=3, column=1, padx=5)

        tk.Label(form, text="Kabupaten:").grid(row=4, column=0, sticky="w")
        self.eksp_kabupaten = tk.Entry(form, width=35)
        self.eksp_kabupaten.grid(row=4, column=1, padx=5)

        tk.Label(form, text="Kode POS:").grid(row=5, column=0, sticky="w")
        self.eksp_kode_pos = tk.Entry(form, width=35)
        self.eksp_kode_pos.grid(row=5, column=1, padx=5)

        tk.Label(form, text="Telepon:").grid(row=6, column=0, sticky="w")
        self.eksp_tlpn = tk.Entry(form, width=35)
        self.eksp_tlpn.grid(row=6, column=1, padx=5)

        add_btn = tk.Button(form, text="Tambah Ekspedisi", bg="#4CAF50", fg="white", command=self.add_ekspedisi)
        add_btn.grid(row=7, column=0, columnspan=2, pady=8)

        self.tree_ekspedisi = ttk.Treeview(frame, columns=("Nama Penerima", "Nama Pengirim", "Alamat", "Provinsi", "Kabupaten", "Kode POS", "Telepon"), show='headings')
        for col in self.tree_ekspedisi["columns"]:
            self.tree_ekspedisi.heading(col, text=col)
            self.tree_ekspedisi.column(col, width=130)
        self.tree_ekspedisi.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

    def fill_penerima_to_ekspedisi(self, event):
        nama = self.eksp_cbox_penerima.get()
        for row in self.data_penerima:
            if row[0] == nama:
                self.eksp_alamat.delete(0, tk.END)
                self.eksp_provinsi.delete(0, tk.END)
                self.eksp_kabupaten.delete(0, tk.END)
                self.eksp_kode_pos.delete(0, tk.END)
                self.eksp_tlpn.delete(0, tk.END)
                self.eksp_alamat.insert(0, row[1])
                self.eksp_provinsi.insert(0, row[2])
                self.eksp_kabupaten.insert(0, row[3])
                self.eksp_kode_pos.insert(0, row[4])
                self.eksp_tlpn.insert(0, row[5])
                break

    def fill_pengirim_to_ekspedisi(self, event):
        nama = self.eksp_cbox_pengirim.get()
        for row in self.data_pengirim:
            if row[0] == nama:
                # Jika ingin field otomatis isi dari data pengirim, bisa diatur di sini.
                break

    def add_ekspedisi(self):
        values = (
            self.eksp_cbox_penerima.get(),
            self.eksp_cbox_pengirim.get(),
            self.eksp_alamat.get(),
            self.eksp_provinsi.get(),
            self.eksp_kabupaten.get(),
            self.eksp_kode_pos.get(),
            self.eksp_tlpn.get()
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

if __name__ == "__main__":
    root = tk.Tk()
    app = EkspedisiApp(root)
    root.mainloop()
