"""
app.py
FaunaRescue - aplikasi GUI Tkinter dengan grafik Matplotlib.
Menggabungkan data_loader (data) dan simulation (hitungan).
Jalankan: python3 app.py
"""

import os
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import data_loader
import simulation

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "filtered_data.csv")

# warna
MERAH = "#d62728"   # garis kepunahan
HIJAU = "#2ca02c"   # garis pemulihan
BG = "#f4f6f7"
PANEL = "#ffffff"
AKSEN = "#1b5e20"

# state global aplikasi (dipakai antar fungsi, ganti peran class)
data = None              # hasil load_data
spesies_aktif = None     # baris spesies yang sedang dipilih
rescue_vars = {}         # key aksi -> BooleanVar
widget = {}              # simpan widget penting (entry, figure, ax, canvas, dll)


# ---------------------------------------------------------------- aksi
def cari():
    q = widget["search_var"].get().strip()
    if not q:
        return
    sp = data_loader.search(data, q)
    if sp is None:
        messagebox.showinfo(
            "Tidak ditemukan",
            "Tidak ada hasil persis untuk '%s'.\n"
            "Pencarian hanya cocok persis pada nama umum, "
            "nama ilmiah, atau taxonid." % q,
        )
        return
    global spesies_aktif
    spesies_aktif = sp
    reset_aksi_diam()
    tampilkan_info(sp)
    gambar_grafik()


def ketik(event):
    if event.keysym in ("Return", "Up", "Down", "Left", "Right"):
        return
    widget["suggest"].delete(0, tk.END)
    for nama in data_loader.suggest(data, widget["search_var"].get(), limit=8):
        widget["suggest"].insert(tk.END, nama)


def pilih_saran(event):
    sel = widget["suggest"].curselection()
    if sel:
        widget["search_var"].set(widget["suggest"].get(sel[0]))
        cari()


def reset_aksi_diam():
    for v in rescue_vars.values():
        v.set(False)


def reset_aksi():
    reset_aksi_diam()
    gambar_grafik()


def aksi_aktif():
    return [k for k, v in rescue_vars.items() if v.get()]


# ---------------------------------------------------------------- tampilan
def tampilkan_info(sp):
    baris = [
        "> " + data_loader.display_name(sp),
        "   Nama ilmiah : " + (sp["scientific_name"] or "-"),
        "   Famili      : " + (sp["family_name"].title() or "-"),
        "   Kategori    : " + (sp["category"] or "-"),
    ]
    if sp["population"]:
        baris.append("   Catatan pop : " + sp["population"])
    if not simulation.bisa_disimulasi(sp["category"]):
        baris.append("")
        baris.append("! Kategori ini bukan CR/EN/VU, tidak ada simulasi.")
    widget["info"].configure(text="\n".join(baris))


def gambar_grafik():
    ax = widget["ax"]
    ax.clear()  # bersihkan dulu supaya tidak menumpuk di memori

    if spesies_aktif is None or not simulation.bisa_disimulasi(spesies_aktif["category"]):
        pesan = "Pilih spesies CR / EN / VU untuk menjalankan simulasi."
        if spesies_aktif is not None:
            pesan = "%s berstatus %s - tidak bisa disimulasikan (hanya CR/EN/VU)." % (
                data_loader.display_name(spesies_aktif),
                spesies_aktif["category"] or "N/A",
            )
        ax.text(0.5, 0.5, pesan, ha="center", va="center",
                fontsize=11, color="#666666", transform=ax.transAxes)
        ax.set_xticks([])
        ax.set_yticks([])
        widget["canvas"].draw()
        return

    kategori = spesies_aktif["category"]
    tahun = widget["tahun_var"].get()
    aktif = aksi_aktif()

    t, base = simulation.baseline(kategori, tahun)
    _, res = simulation.rescue(kategori, aktif, tahun)
    r = simulation.ringkasan(kategori, aktif, tahun)

    ax.plot(t, base, color=MERAH, linewidth=2.4, marker="o", markersize=3,
            label="Baseline (menuju kepunahan)")
    ax.plot(t, res, color=HIJAU, linewidth=2.4, marker="o", markersize=3,
            label="Skenario rescue (dengan intervensi)")
    ax.fill_between(t, base, res, where=(res >= base), color=HIJAU, alpha=0.10)

    ax.set_title("%s  [%s - %s]" % (data_loader.display_name(spesies_aktif),
                                    r["kategori"], r["nama_kategori"]),
                 fontsize=12, fontweight="bold")
    ax.set_xlabel("Tahun dari sekarang")
    ax.set_ylabel("Perkiraan populasi (individu dewasa)")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_ylim(bottom=0)

    status = "PULIH" if r["pulih"] else "masih menurun"
    catatan = ("Laju dasar %.2f%%/thn  ->  efektif %.2f%%/thn  (%s)\n"
               "Tahun %d:  baseline %.0f  vs  rescue %.0f  (selisih %+.0f)") % (
        r["laju_dasar_persen"], r["laju_efektif_persen"], status,
        tahun, r["akhir_baseline"], r["akhir_rescue"], r["selisih"])
    ax.text(0.02, -0.16, catatan, transform=ax.transAxes,
            fontsize=9, color="#333333", va="top")

    widget["figure"].subplots_adjust(bottom=0.22)
    widget["canvas"].draw()


# ---------------------------------------------------------------- susun UI
def buat_header(root):
    h = tk.Frame(root, bg=AKSEN)
    h.pack(side=tk.TOP, fill=tk.X)
    tk.Label(h, text="  FaunaRescue", bg=AKSEN, fg="white",
             font=("Helvetica", 18, "bold")).pack(side=tk.LEFT, padx=12, pady=10)
    tk.Label(h, text="Status konservasi IUCN -> simulasi populasi   |   %d taxa" % len(data["list"]),
             bg=AKSEN, fg="#d7ffd9", font=("Helvetica", 10)).pack(side=tk.LEFT, pady=10)


def buat_panel_kiri(root):
    kiri = tk.Frame(root, bg=PANEL, width=320)
    kiri.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
    kiri.pack_propagate(False)

    # --- pencarian ---
    tk.Label(kiri, text="Basis Data Spesies", bg=PANEL,
             font=("Helvetica", 13, "bold")).pack(anchor="w", padx=12, pady=(12, 2))
    tk.Label(kiri, text="Cari nama umum / ilmiah (harus persis):", bg=PANEL,
             font=("Helvetica", 9)).pack(anchor="w", padx=12)

    widget["search_var"] = tk.StringVar()
    entry = ttk.Entry(kiri, textvariable=widget["search_var"], font=("Helvetica", 11))
    entry.pack(fill=tk.X, padx=12, pady=(4, 0))
    entry.bind("<Return>", lambda e: cari())
    entry.bind("<KeyRelease>", ketik)

    ttk.Button(kiri, text="Cari", command=cari).pack(fill=tk.X, padx=12, pady=(6, 0))

    widget["suggest"] = tk.Listbox(kiri, height=5, font=("Helvetica", 10),
                                   activestyle="none", highlightthickness=0)
    widget["suggest"].pack(fill=tk.X, padx=12, pady=(6, 0))
    widget["suggest"].bind("<<ListboxSelect>>", pilih_saran)

    # --- info spesies ---
    widget["info"] = tk.Label(kiri, justify="left", anchor="w", bg=PANEL,
                              font=("Helvetica", 10), wraplength=290,
                              text="> Belum ada spesies dipilih.\n\n"
                                   "Coba: White Seraya, Indian Sandalwood,\n"
                                   "Yellow Meranti, atau Santalum album.")
    widget["info"].pack(fill=tk.X, padx=12, pady=(12, 6))

    # --- panel rescue ---
    tk.Label(kiri, text="Modul Penyelamatan", bg=PANEL,
             font=("Helvetica", 13, "bold")).pack(anchor="w", padx=12, pady=(6, 2))
    tk.Label(kiri, text="Centang intervensi untuk mengubah kurva:", bg=PANEL,
             font=("Helvetica", 9)).pack(anchor="w", padx=12)

    for aksi in simulation.AKSI_RESCUE:
        v = tk.BooleanVar(value=False)
        rescue_vars[aksi["key"]] = v
        tk.Checkbutton(kiri, text="%s  (+%.0f%%)" % (aksi["label"], aksi["modifier"] * 100),
                       variable=v, bg=PANEL, anchor="w", font=("Helvetica", 10),
                       activebackground=PANEL,
                       command=gambar_grafik).pack(fill=tk.X, padx=12)

    tk.Label(kiri, text="Rentang waktu (tahun):", bg=PANEL,
             font=("Helvetica", 9)).pack(anchor="w", padx=12, pady=(10, 0))
    widget["tahun_var"] = tk.IntVar(value=simulation.TAHUN_DEFAULT)
    tk.Scale(kiri, from_=10, to=20, orient=tk.HORIZONTAL, variable=widget["tahun_var"],
             bg=PANEL, highlightthickness=0,
             command=lambda v: gambar_grafik()).pack(fill=tk.X, padx=12)

    ttk.Button(kiri, text="Reset Intervensi",
               command=reset_aksi).pack(fill=tk.X, padx=12, pady=(8, 12))


def buat_panel_grafik(root):
    kanan = tk.Frame(root, bg=PANEL)
    kanan.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    widget["figure"] = Figure(figsize=(7.2, 5.4), dpi=100)
    widget["ax"] = widget["figure"].add_subplot(111)
    widget["canvas"] = FigureCanvasTkAgg(widget["figure"], master=kanan)
    widget["canvas"].get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


def main():
    global data
    try:
        data = data_loader.load_data(CSV_PATH)
    except FileNotFoundError as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Gagal memuat", str(e))
        root.destroy()
        return

    root = tk.Tk()
    root.title("FaunaRescue - Predictive Action System")
    root.geometry("1180x720")
    root.minsize(1040, 640)
    root.configure(bg=BG)

    try:
        ttk.Style(root).theme_use("clam")
    except tk.TclError:
        pass

    buat_header(root)

    body = tk.Frame(root, bg=BG)
    body.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    buat_panel_kiri(body)
    buat_panel_grafik(body)

    gambar_grafik()  # tampilan awal
    root.mainloop()


if __name__ == "__main__":
    main()
