import tkinter as tk
import os
folder = r"D:\Python\Eka GUI Design\Teks"

# Membuat jendela utama
root = tk.Tk()
root.title("Portal Pendaftaran Mahasiswa KKN")

# Menentukan ukuran jendela
root.geometry("800x600")


# Kumpulan Fungsi
# Mengisi Nama Kelompok, Ketua, Anggota, Tema Edukasi, Lokasi KKN
def create_text():
    try:
        nama_kelompok = f"{teks_nama_kelompok.get()}.txt"
        if nama_kelompok != "":
            teks = ketua_kelompok.get("1.0", tk.END)
            teks_2 = anggota1_kelompok.get("1.0", tk.END)
            teks_3 = anggota2_kelompok.get("1.0", tk.END)
            teks_4 = anggota3_kelompok.get("1.0", tk.END)
            teks_5 = checkbox1.get("1.0", tk.END)
            teks_6 = checkbox2.get("1.0", tk.END)
            teks_7 = checkbox3.get("1.0", tk.END)
            with open(os.path.join(folder, nama_kelompok), "w") as file:
                file.write(teks)
            kolom_tampil.delete("1.0", tk.END)
            read_text()
    except Exception as e:
        print("Error:", e)

def append_text():
    try:
        nama_file = f"{teks_nama_kelompok.get()}.txt"
        if nama_file != "":
            teks = kolom_tampil.get("1.0", tk.END)
            with open(os.path.join(folder, nama_kelompok), "a") as file:
                file.write(teks)
            kolom_tampil.delete("1.0", tk.END)
            read_text()
    except Exception as e:
        print("Error:", e)

def read_text():
    try:
        nama_file = f"{teks_nama_kelompok.get()}.txt"
        if nama_file != "":
            with open(os.path.join(folder, nama_kelompok), "r") as file:
                data = file.read()
                
        else:
            kolom_tampil.delete("1.0", tk.END)
    except Exception as e:
        print("Error:", e)

def update_txt():
    try:
        nama_file = f"{teks_nama_kelompok.get()}.txt"
        if nama_file != "":
            search = teks_search.get()
            new = teks_search.get()
            with open(os.path.join(folder, nama_file), "r") as file:
                data = file.read()
                data = data.replace(search, new)
            with open(os.path.join(folder, nama_file), "w") as file:
                file.write(data)
            teks_search.delete(0, tk.END) 
            teks_update.delete(0, tk.END)  
            read_text()
    except Exception as e:
        print("Error:", e)



#membuat option menu lokasi KKN kab/kota
options = ["Kota Denpasar", "Kab. Badung", "Kab. Tabanan", "Kab. Gianyar", "Kab. Bangli", "Kab. Karangasem", "Kab. Klungkung", "Kab. Buleleng", "Kab. Jembrana"]
var_options = tk.StringVar(root)
var_options.set("Pilih Lokasi Kab/Kota")
option_menu = tk.OptionMenu(root, var_options, *options)
option_menu.place(x=300, y=80)

# lokasi Kecamatan KKN
kecamatan_kkn = tk.Label(
    root,
    text="Kecamatan KKN : ",
)
kecamatan_kkn.place(x=300, y=120)

#membuat option menu lokasi kecamatan
data_kecamatan = {
    "Badung": ["Kuta", "Kuta Utara", "Kuta Selatan", "Mengwi", "Abiansemal", "Petang"],
    "Denpasar": ["Denpasar Utara", "Denpasar Timur", "Denpasar Barat", "Denpasar Selatan"],
    "Gianyar": ["Blahbatuh", "Gianyar", "Payangan", "Sukawati", "Tampaksiring", "Tegallalang", "Ubud"],
    "Bangli": ["Susut", "Bangli", "Tembuku", "Kintamani"],
    "Buleleng": ["Gerokgak", "Seririt", "Busungbiu", "Banjar", "Sukasada", "Buleleng", "Sawan", "Kubutambahan", "Tejakula"],
    "Jembrana": ["Negara", "Mendoyo", "Pekutatan", "Melaya", "Jembrana"],
    "Karangasem": ["Rendang", "Sidemen", "Manggis", "Karangasem", "Abang", "Bebandem", "Selat", "Kubu"],
    "Klungkung": ["Nusa Penida", "Banjarangkan", "Klungkung", "Dawan"],
    "Tabanan": ["Selemadeg", "Selemadeg Timur", "Selemadeg Barat", "Kerambitan", "Tabanan", "Kediri", "Marga", "Penebel", "Baturiti", "Pupuan"],
}

# Fungsi untuk memperbarui dropdown Kecamatan
def update_kecamatan(*args):
    selected_kabupaten = var_options.get()
    kecamatan_options = data_kecamatan.get(selected_kabupaten, ["Pilih Lokasi Kecamatan"])

# Update menu kecamatan
    menu = option_menu_kecamatan["menu"]
    menu.delete(0, "end")  # Hapus semua item di menu dropdown kecamatan
    for kecamatan in kecamatan_options:
        menu.add_command(label=kecamatan, command=lambda value=kecamatan: var_data_kecamatan.set(value))
    var_data_kecamatan.set("Pilih Lokasi Kecamatan")  # Reset kecamatan selection

# Menambahkan listener untuk perubahan pada dropdown Kabupaten/Kota
var_options.trace_add("write", update_kecamatan)

var_data_kecamatan = tk.StringVar(root)
var_data_kecamatan.set("Pilih Lokasi Kecamatan")


# Desain Tampilan

# nama kelompok
nama_kelompok = tk.Label(
    root,
    text="Nama Kelompok : ",
)
nama_kelompok.place(x=10, y=10)

# teks nama kelompok
teks_nama_kelompok = tk.Entry(root, width=100)
teks_nama_kelompok.place(x=150, y=10)

# daftar anggota kelompok
anggota_kelompok = tk.Label(
    root,
    text="Daftar Anggota Kelompok : ",
)
anggota_kelompok.place(x=10, y=40)

# ketua kelompok
ketua_kelompok = tk.Label(
    root,
    text="Ketua Kelompok : ",
)
ketua_kelompok.place(x=10, y=60)

# teks ketua kelompok
teks_ketua_kelompok = tk.Entry(root, width=40)
teks_ketua_kelompok.place(x=10, y=80)

# anggota kelompok ke-1
anggota1_kelompok = tk.Label(
    root,
    text="Anggota 1 : ",
)
anggota1_kelompok.place(x=10, y=100)

# teks anggota kelompok ke-1
teks_anggota1_kelompok = tk.Entry(root, width=40)
teks_anggota1_kelompok.place(x=10, y=120)

# anggota kelompok ke-2
anggota2_kelompok = tk.Label(
    root,
    text="Anggota 2 : ",
)
anggota2_kelompok.place(x=10, y=140)

# teks anggota kelompok ke-2
teks_anggota2_kelompok = tk.Entry(root, width=40)
teks_anggota2_kelompok.place(x=10, y=160)

# anggota kelompok ke-3
anggota3_kelompok = tk.Label(
    root,
    text="Anggota 3 : ",
)
anggota3_kelompok.place(x=10, y=180)

# teks anggota kelompok ke-3
teks_anggota3_kelompok = tk.Entry(root, width=40)
teks_anggota3_kelompok.place(x=10, y=200)

# checkbox tema edukasi
tema_edukasi = tk.Label(
    root,
    text="Tema Edukasi ke Masyarakat : ",
)
tema_edukasi.place(x=10, y=240)

# Check button Tema Edukasi
checkbox1 = tk.Checkbutton(root, text="Waspada Investasi Bodong")
checkbox1.place(x=10, y=260)
checkbox2 = tk.Checkbutton(root, text="Pengelolaan Keuangan")
checkbox2.place(x=10, y=280)
checkbox3 = tk.Checkbutton(root, text="Financial Technology")
checkbox3.place(x=10, y=300)

# lokasi Dati II KKN
lokasi_kkn = tk.Label(
    root,
    text="Informasi Lokasi KKN : "
)
lokasi_kkn.place(x=300, y=60)

option_menu_kecamatan = tk.OptionMenu(root, var_data_kecamatan, "Pilih Lokasi Kecamatan")
option_menu_kecamatan.place(x=300, y=140)

# tampilan data
tampil = tk.Label(
    root,
    text="Tampil : ",
)
tampil.place(x=300, y=190)

# kolom teks tampil
kolom_tampil = tk.Text(root, width=60, height=15)  
kolom_tampil.place(x=300, y=210)

# search 
search = tk.Label(
    root,
    text="Search text : ",
)
search.place(x=300, y=470)

# teks search
teks_search = tk.Entry(root, width=30)
teks_search.place(x=300, y=490)

# update 
update = tk.Label(
    root,
    text="Update text : ",
)
update.place(x=500, y=470)

# teks update
teks_update = tk.Entry(root, width=30)
teks_update.place(x=500, y=490)

#berbagai button
button_read = tk.Button(root, text="Read")
button_read.place(x=620, y=40)

button_create = tk.Button(root, text="Create", command=create_text)
button_create.place(x=670, y=40)

button_append = tk.Button(root, text="Append", command=append_text)
button_append.place(x=620, y=70)

button_update = tk.Button(root, text="Update", command=update_txt)
button_update.place(x=700, y=490)

# Menjalankan aplikasi GUI
root.mainloop()