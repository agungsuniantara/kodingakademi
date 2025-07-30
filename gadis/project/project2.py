import tkinter as tk
from tkinter import ttk, messagebox
import re

class AplikasiInventori_1234:
    def __init__(self, win):
        self.win = win
        self.win.title("Manajemen Inventori")
        self.win.geometry("1000x700")
        self.win.configure(bg="#f5f5f5")
        self.daftar_barang = []

        self._konfigurasi_gaya_1234()
        self._atur_antarmuka_1234()

    def _konfigurasi_gaya_1234(self):
        self.warna_latar = "#f5f5f5"
        self.warna_kartu = "#ffffff"
        self.warna_utama = "#1a73e8"
        self.warna_aksen = "#34c759"

        style = ttk.Style(self.win)
        style.theme_use('clam')
        style.configure('Card.TFrame', background=self.warna_kartu, relief='groove', borderwidth=1)
        style.configure('TNotebook', background=self.warna_latar, borderwidth=0)
        style.configure('TNotebook.Tab', font=('Segoe UI', 11))
        style.configure('Header.TLabel', font=('Segoe UI', 24, 'bold'), background=self.warna_kartu)
        style.configure('TLabel', font=('Segoe UI', 12), background=self.warna_kartu)
        style.configure('TButton', font=('Segoe UI', 12, 'bold'), background=self.warna_aksen, foreground='white', padding=6)
        style.map('TButton', background=[('active', self.warna_utama)])
        style.configure('Treeview.Heading', font=('Segoe UI', 12, 'bold'))
        style.configure('Treeview', font=('Segoe UI', 12), rowheight=36)
        style.layout('TNotebook.Tab', [
            ('Notebook.tab', {'sticky': 'nswe', 'children': [
                ('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children': [
                    ('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children': [
                        ('Notebook.label', {'side': 'top', 'sticky': ''})
                    ]})
                ]})
            ]})
        ])
    
    def _atur_antarmuka_1234(self):
        self.frame_utama = ttk.Frame(self.win, style='Card.TFrame', padding=16)
        self.frame_utama.pack(padx=24, pady=20, fill='both', expand=True)

        lbl_header = ttk.Label(self.frame_utama, text="Manajemen Inventori", style='Header.TLabel')
        lbl_header.pack(anchor='center', pady=(0, 18))

        self.notebook = ttk.Notebook(self.frame_utama)
        self.tab_tambah = ttk.Frame(self.notebook, style='Card.TFrame')
        self.tab_lihat = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(self.tab_tambah, text='Tambah Barang')
        self.notebook.add(self.tab_lihat, text='Lihat Inventori')
        self.notebook.pack(fill='both', expand=True)
        self._atur_tab_tambah_1234()
        self._atur_tab_lihat_1234()

    def _atur_tab_tambah_1234(self):
        self.var_nama = tk.StringVar()
        self.var_kode = tk.StringVar()
        self.var_jumlah = tk.StringVar()
        self.var_harga = tk.StringVar()
        
        label_opt = {'sticky': 'w', 'pady': 10, 'padx': 10}
        entry_opt = {'sticky': 'ew', 'pady': 10, 'padx': 10}

        self.tab_tambah.columnconfigure(1, weight=1)

        ttk.Label(self.tab_tambah, text='Nama Barang:').grid(row=0, column=0, **label_opt)
        ttk.Entry(self.tab_tambah, textvariable=self.var_nama, width=40).grid(row=0, column=1, **entry_opt)
        
        ttk.Label(self.tab_tambah, text='Kode Barang (BRG-XXX):').grid(row=1, column=0, **label_opt)
        ttk.Entry(self.tab_tambah, textvariable=self.var_kode, width=24).grid(row=1, column=1, **entry_opt)
        
        ttk.Label(self.tab_tambah, text='Jumlah:').grid(row=2, column=0, **label_opt)
        ttk.Entry(self.tab_tambah, textvariable=self.var_jumlah, width=12).grid(row=2, column=1, **entry_opt)
        
        ttk.Label(self.tab_tambah, text='Harga Satuan:').grid(row=3, column=0, **label_opt)
        ttk.Entry(self.tab_tambah, textvariable=self.var_harga, width=18).grid(row=3, column=1, **entry_opt)

        frame_btn = tk.Frame(self.tab_tambah, bg=self.warna_kartu, highlightthickness=0, bd=0)
        frame_btn.grid(row=4, column=0, columnspan=2, pady=24)
        btn_simpan = ttk.Button(frame_btn, text="Simpan", command=self.simpan_barang_1234)
        btn_simpan.grid(row=0, column=0, padx=18)
        btn_reset = ttk.Button(frame_btn, text="Reset", command=self.reset_formulir_1234)
        btn_reset.grid(row=0, column=1, padx=18)

    def _atur_tab_lihat_1234(self):
        columns = ('nama', 'kode', 'jumlah', 'harga', 'total')
        self.tabel = ttk.Treeview(self.tab_lihat, columns=columns, show='headings', height=13)
        for col, text in zip(columns, ["Nama Barang", "Kode Barang", "Jumlah", "Harga Satuan", "Total Harga"]):
            self.tabel.heading(col, text=text)
            self.tabel.column(col, anchor='center')
        vsb = ttk.Scrollbar(self.tab_lihat, orient="vertical", command=self.tabel.yview)
        self.tabel.configure(yscrollcommand=vsb.set)
        self.tabel.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        self.lbl_no_data = ttk.Label(self.tab_lihat, text='Tidak ada data', foreground='gray', font=('Segoe UI', 13), background=self.warna_kartu)
        self.lbl_no_data.place(relx=0.5, rely=0.08, anchor='center')
        self.tab_lihat.grid_rowconfigure(0, weight=1)
        self.tab_lihat.grid_columnconfigure(0, weight=1)
        self._perbarui_tabel_1234(self.daftar_barang)

    def _validasi_input_1234(self, nama, kode, jumlah, harga):
        # Nama barang
        if not nama:
            return "Nama barang tidak boleh kosong!"
        if len(nama) > 50:
            return "Nama barang maksimal 50 karakter!"
        # Kode barang
        if not re.fullmatch(r'BRG-\d{3}', kode):
            return "Kode barang harus dalam format BRG-XXX (X adalah angka)!"
        # Kode unik
        if any(b['kode'].upper() == kode.upper() for b in self.daftar_barang):
            return "Kode %s sudah ada!" % kode
        # Jumlah
        if not jumlah.isdigit():
            return "Jumlah harus berupa angka!"
        if int(jumlah) <= 0:
            return "Jumlah harus bilangan bulat positif!"
        # Harga
        try:
            h = float(harga)
        except:
            return "Harga satuan harus berupa angka!"
        if h <= 0:
            return "Harga satuan harus bilangan positif!"
        return None

    def simpan_barang_1234(self):
        nama = self.var_nama.get().strip()
        kode = self.var_kode.get().strip().upper()
        jumlah = self.var_jumlah.get().strip()
        harga = self.var_harga.get().strip()

        # Cek satu-satu, urutan sesuai screenshot (satu popup tiap error)
        error = self._validasi_input_1234(nama, kode, jumlah, harga)
        if error:
            messagebox.showerror("Error", error)
            return

        # Simpan
        self.daftar_barang.append({
            'nama': nama,
            'kode': kode,
            'jumlah': int(jumlah),
            'harga': float(harga)
        })
        messagebox.showinfo("Sukses", "Barang berhasil ditambahkan!")
        self.reset_formulir_1234()
        self._perbarui_tabel_1234(self.daftar_barang)
        self.notebook.select(self.tab_lihat)

    def reset_formulir_1234(self):
        self.var_nama.set("")
        self.var_kode.set("")
        self.var_jumlah.set("")
        self.var_harga.set("")

    def _perbarui_tabel_1234(self, daftar_barang: list):
        for i in self.tabel.get_children():
            self.tabel.delete(i)
        if not daftar_barang:
            self.lbl_no_data.lift()
            return
        else:
            self.lbl_no_data.lower()
        for idx, b in enumerate(daftar_barang): # idx = 0, b = {nama: 'gadis', kode: 'BRG-001', jumlah: 10, harga: 10000}
            total = b['jumlah'] * b['harga']
            vals = (
                b['nama'],
                b['kode'],
                b['jumlah'],
                f"{b['harga']:.2f}",
                f"{total:.2f}"
            )
            tag = 'genap' if idx % 2 == 0 else 'ganjil'
            self.tabel.insert('', 'end', values=vals, tags=(tag,))
        self.tabel.tag_configure('genap', background='#f8fff4')
        self.tabel.tag_configure('ganjil', background='#ffffff')

if __name__ == "__main__":
    win = tk.Tk()
    app = AplikasiInventori_1234(win)
    win.mainloop()
