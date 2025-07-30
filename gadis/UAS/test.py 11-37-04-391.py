import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import os
import ast
from PIL import Image, ImageTk
import datetime

# File paths
FILE_PENERIMA = "penerima.txt"
FILE_PENGIRIM = "pengirim.txt"
FILE_EKSPEDISI = "ekspedisi.txt"
FILE_PEMBAYARAN = "pembayaran.txt"

class EkspedisiApp:
    def __init__(self, win):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.win = win
        self.win.title("Login Ekspedisi")
        self.win.geometry("1000x600")

        # Background image
        self.bg_img = Image.new("RGB", (1400, 700), color=(255, 255, 255))
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(self.win, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.custom_font = ctk.CTkFont(family="Arial", size=30, weight="bold")

        form_frame = tk.Frame(self.win, bg="#B7E5F4")
        form_frame.place(x=0, y=0, width=470, relheight=1.0)

        ctk.CTkLabel(
            form_frame, text="🚚 LAJU KIRIM 🚚", font=self.custom_font, text_color="#19376D"
        ).place(relx=0.5, rely=0.15, anchor="center")

        inner_form = tk.Frame(form_frame, bg="#B7E5F4")
        inner_form.place(relx=0.5, rely=0.45, anchor="center")

        self.username_entry = ctk.CTkEntry(inner_form, width=220, height=35, corner_radius=15, placeholder_text="Username")
        self.username_entry.pack(pady=(10, 10))

        self.password_entry = ctk.CTkEntry(inner_form, show="*", width=220, height=35, corner_radius=15, placeholder_text="Password")
        self.password_entry.pack(pady=(0, 20))

        ctk.CTkButton(inner_form, text="Login", command=self.login, fg_color="#19376D", text_color="white", width=220, height=35, corner_radius=15).pack(pady=10)

        self.win.protocol("WM_DELETE_WINDOW", self.on_close)

    def login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "12345":
            messagebox.showinfo("Login Berhasil", "Selamat datang!")
            self.win.withdraw()
            self.main_menu()
        else:
            messagebox.showwarning("Gagal", "Username atau Password salah!")

    def main_menu(self):
        self.menu_win = tk.Toplevel()
        self.menu_win.title("Menu Ekspedisi")
        self.menu_win.geometry("1000x700")

        self.data_penerima = []
        self.data_pengirim = []
        self.data_ekspedisi = []
        self.data_pembayaran = []

        self.notebook = ttk.Notebook(self.menu_win)
        self.tab_penerima = ttk.Frame(self.notebook)
        self.tab_pengirim = ttk.Frame(self.notebook)
        self.tab_ekspedisi = ttk.Frame(self.notebook)
        self.tab_pembayaran = ttk.Frame(self.notebook)
        self.tab_laporan = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_penerima, text="Penerima")
        self.notebook.add(self.tab_pengirim, text="Pengirim")
        self.notebook.add(self.tab_ekspedisi, text="Ekspedisi")
        self.notebook.add(self.tab_pembayaran, text="Pembayaran")
        self.notebook.add(self.tab_laporan, text="Laporan")
        self.notebook.pack(fill='both', expand=True)

        self.setup_tab_penerima()
        self.setup_tab_pengirim()
        self.setup_tab_ekspedisi()
        self.setup_tab_pembayaran()
        self.setup_tab_laporan()

        self.load_data()
        self.update_comboboxes()

    def _make_label_entry(self, parent, label, row):
        tk.Label(parent, text=label).grid(row=row, column=0, sticky="w", padx=3, pady=2)
        entry = tk.Entry(parent)
        entry.grid(row=row, column=1, padx=3, pady=2)
        return entry

    def setup_tab_penerima(self):
        frame = self.tab_penerima
        form = tk.Frame(frame)
        form.pack(pady=10)

        self.ent_penerima = [self._make_label_entry(form, lbl, i) for i, lbl in enumerate(["Nama", "Alamat", "Provinsi", "Kabupaten", "Kode POS", "Telepon"])]

        tk.Button(form, text="Tambah", command=self.add_penerima).grid(row=6, column=0, pady=5)

    def add_penerima(self):
        data = tuple(e.get().strip() for e in self.ent_penerima)
        if not all(data):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        if not data[4].isdigit() or not data[5].isdigit():
            messagebox.showwarning("Peringatan", "Kode POS dan Telepon harus angka!")
            return
        self.data_penerima.append(data)
        self.update_comboboxes()
        for e in self.ent_penerima: e.delete(0, tk.END)
        self.refresh_tab_laporan()

    def setup_tab_pengirim(self):
        frame = self.tab_pengirim
        form = tk.Frame(frame)
        form.pack(pady=10)

        self.ent_pengirim = [self._make_label_entry(form, lbl, i) for i, lbl in enumerate(["Nama", "Alamat", "Provinsi", "Kabupaten", "Kode POS", "Telepon"])]

        tk.Button(form, text="Tambah", command=self.add_pengirim).grid(row=6, column=0, pady=5)

    def add_pengirim(self):
        data = tuple(e.get().strip() for e in self.ent_pengirim)
        if not all(data):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        if not data[4].isdigit() or not data[5].isdigit():
            messagebox.showwarning("Peringatan", "Kode POS dan Telepon harus angka!")
            return
        self.data_pengirim.append(data)
        self.update_comboboxes()
        for e in self.ent_pengirim: e.delete(0, tk.END)
        self.refresh_tab_laporan()

    def setup_tab_ekspedisi(self):
        frame = self.tab_ekspedisi
        form = tk.Frame(frame)
        form.pack(pady=10)

        self.combo_penerima = ttk.Combobox(form, width=30, state="readonly")
        self.combo_pengirim = ttk.Combobox(form, width=30, state="readonly")
        self.entry_barang = [tk.Entry(form, width=30) for _ in range(6)]

        for i, (lbl, widget) in enumerate(zip(
            ["Penerima", "Pengirim", "Nama Barang", "Berat", "Jumlah", "Alamat", "Tanggal", "Ongkos"],
            [self.combo_penerima, self.combo_pengirim] + self.entry_barang
        )):
            tk.Label(form, text=lbl).grid(row=i, column=0, sticky="w")
            widget.grid(row=i, column=1)

        tk.Button(form, text="Tambah", command=self.add_ekspedisi).grid(row=8, column=0, pady=5)

    def add_ekspedisi(self):
        data = (
            self.combo_penerima.get(), self.combo_pengirim.get(),
            *(e.get().strip() for e in self.entry_barang)
        )
        if not all(data):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        try:
            float(data[3])
            int(data[4])
            datetime.datetime.strptime(data[6], "%d-%m-%Y")
            float(data[7])
        except:
            messagebox.showwarning("Peringatan", "Berat, Jumlah, Tanggal (dd-mm-yyyy), dan Ongkos harus valid!")
            return
        self.data_ekspedisi.append(data)
        for e in self.entry_barang: e.delete(0, tk.END)
        self.combo_penerima.set("")
        self.combo_pengirim.set("")
        self.refresh_tab_laporan()

    def setup_tab_pembayaran(self):
        frame = self.tab_pembayaran
        form = tk.Frame(frame)
        form.pack(pady=10)

        self.combo_pembayar = ttk.Combobox(form, width=30, state="readonly")
        self.combo_metode = ttk.Combobox(form, width=30, state="readonly", values=["Qris", "Debit", "TF", "Cash"])
        self.ent_jumlah = tk.Entry(form, width=30)
        self.ent_tanggal = tk.Entry(form, width=30)

        for i, (lbl, widget) in enumerate(zip(
            ["Pembayar", "Metode", "Jumlah Bayar", "Tanggal"],
            [self.combo_pembayar, self.combo_metode, self.ent_jumlah, self.ent_tanggal]
        )):
            tk.Label(form, text=lbl).grid(row=i, column=0, sticky="w")
            widget.grid(row=i, column=1)

        tk.Button(form, text="Tambah", command=self.add_pembayaran).grid(row=4, column=0, pady=5)

    def add_pembayaran(self):
        data = (
            self.combo_pembayar.get(),
            self.combo_metode.get(),
            self.ent_jumlah.get().strip(),
            self.ent_tanggal.get().strip()
        )
        if not all(data):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        try:
            float(data[2])
            datetime.datetime.strptime(data[3], "%d-%m-%Y")
        except:
            messagebox.showwarning("Peringatan", "Jumlah dan Tanggal (dd-mm-yyyy) harus valid!")
            return
        self.data_pembayaran.append(data)
        self.combo_pembayar.set("")
        self.combo_metode.set("")
        self.ent_jumlah.delete(0, tk.END)
        self.ent_tanggal.delete(0, tk.END)
        self.refresh_tab_laporan()

    def setup_tab_laporan(self):
        self.laporan_text_area = tk.Text(self.tab_laporan)
        self.laporan_text_area.pack(fill="both", expand=True)
        self.refresh_tab_laporan()

    def refresh_tab_laporan(self):
        self.laporan_text_area.config(state="normal")
        self.laporan_text_area.delete("1.0", tk.END)
        teks = ""

        if self.data_ekspedisi:
            teks += "\nLAPORAN EKSPEDISI\n"
            teks += f"{'No':<4}{'Penerima':<15}{'Pengirim':<15}{'Barang':<10}{'Tanggal':<12}{'Ongkir':<10}\n"
            teks += "-"*70 + "\n"
            for i, d in enumerate(self.data_ekspedisi):
                teks += f"{i+1:<4}{d[0]:<15}{d[1]:<15}{d[2]:<10}{d[6]:<12}{d[7]:<10}\n"

        if self.data_pembayaran:
            teks += "\nLAPORAN PEMBAYARAN\n"
            teks += f"{'No':<4}{'Pembayar':<15}{'Metode':<10}{'Jumlah':<12}{'Tanggal':<12}\n"
            teks += "-"*60 + "\n"
            for i, d in enumerate(self.data_pembayaran):
                teks += f"{i+1:<4}{d[0]:<15}{d[1]:<10}{d[2]:<12}{d[3]:<12}\n"

        self.laporan_text_area.insert(tk.END, teks or "Tidak ada data.")
        self.laporan_text_area.config(state="disabled")

    def update_comboboxes(self):
        names = [d[0] for d in self.data_pengirim]
        self.combo_pengirim["values"] = names
        self.combo_pembayar["values"] = names
        self.combo_metode["values"] = ["Qris", "Debit", "TF", "Cash"]
        self.combo_penerima["values"] = [d[0] for d in self.data_penerima]

    def on_close(self):
        self.save_data()
        self.win.destroy()

    def save_data(self):
        for fname, data in [
            (FILE_PENERIMA, self.data_penerima),
            (FILE_PENGIRIM, self.data_pengirim),
            (FILE_EKSPEDISI, self.data_ekspedisi),
            (FILE_PEMBAYARAN, self.data_pembayaran)
        ]:
            with open(fname, "w") as f:
                f.write(str(data))

    def load_data(self):
        for fname, attr in [
            (FILE_PENERIMA, "data_penerima"),
            (FILE_PENGIRIM, "data_pengirim"),
            (FILE_EKSPEDISI, "data_ekspedisi"),
            (FILE_PEMBAYARAN, "data_pembayaran")
        ]:
            if os.path.exists(fname):
                with open(fname, "r") as f:
                    try:
                        setattr(self, attr, ast.literal_eval(f.read()))
                    except:
                        setattr(self, attr, [])
        self.refresh_tab_laporan()

if __name__ == "__main__":
    root = tk.Tk()
    app = EkspedisiApp(root)
    root.mainloop()
