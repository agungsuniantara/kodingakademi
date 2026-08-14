"""
data_loader.py
Baca filtered_data.csv pakai modul csv bawaan, simpan ke memori (dict + list).
Pencarian hanya exact match (nama umum / nama ilmiah / taxonid), tidak fuzzy.
Tidak pakai pandas sesuai aturan lomba.
"""

import csv
import os

# Kategori terancam yang bisa disimulasikan
THREATENED = ("CR", "EN", "VU")


def _clean(value):
    return (value or "").strip()


def load_data(csv_path):
    """
    Baca CSV, kembalikan dict berisi:
      - "list"        : semua baris (list of dict)
      - "by_common"   : nama umum (huruf kecil)    -> baris
      - "by_scientific": nama ilmiah (huruf kecil)  -> baris
      - "by_id"       : taxonid                     -> baris
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError("File data tidak ditemukan: " + csv_path)

    species_list = []
    by_common = {}
    by_scientific = {}
    by_id = {}

    with open(csv_path, newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sp = {
                "taxonid": _clean(row.get("taxonid")),
                "class_name": _clean(row.get("class_name")),
                "family_name": _clean(row.get("family_name")),
                "genus_name": _clean(row.get("genus_name")),
                "scientific_name": _clean(row.get("scientific_name")),
                "population": _clean(row.get("population")),
                "category": _clean(row.get("category")).upper(),
                "common_name": _clean(row.get("main_common_name")),
            }

            # lewati baris tanpa nama sama sekali
            if not sp["scientific_name"] and not sp["common_name"]:
                continue

            species_list.append(sp)

            # buat index untuk pencarian cepat (yang pertama dipakai)
            if sp["common_name"]:
                key = sp["common_name"].lower()
                if key not in by_common:
                    by_common[key] = sp
            if sp["scientific_name"]:
                key = sp["scientific_name"].lower()
                if key not in by_scientific:
                    by_scientific[key] = sp
            if sp["taxonid"]:
                if sp["taxonid"] not in by_id:
                    by_id[sp["taxonid"]] = sp

    return {
        "list": species_list,
        "by_common": by_common,
        "by_scientific": by_scientific,
        "by_id": by_id,
    }


def display_name(sp):
    """Nama umum kalau ada, kalau tidak pakai nama ilmiah."""
    return sp["common_name"] or sp["scientific_name"]


def search(data, query):
    """Cari satu spesies dengan exact match. Kembalikan baris atau None."""
    if not query:
        return None
    key = query.strip().lower()
    if key in data["by_common"]:
        return data["by_common"][key]
    if key in data["by_scientific"]:
        return data["by_scientific"][key]
    return data["by_id"].get(query.strip())


def suggest(data, prefix, limit=8):
    """Daftar nama yang diawali prefix (untuk bantuan ketik di UI)."""
    if not prefix:
        return []
    p = prefix.strip().lower()
    hasil = []
    sudah = set()
    for sp in data["list"]:
        nama = display_name(sp)
        if nama and nama not in sudah and nama.lower().startswith(p):
            sudah.add(nama)
            hasil.append(nama)
            if len(hasil) >= limit:
                break
    return hasil


def category_counts(data):
    counts = {}
    for sp in data["list"]:
        c = sp["category"]
        counts[c] = counts.get(c, 0) + 1
    return counts


# uji cepat kalau dijalankan langsung
if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    data = load_data(os.path.join(here, "filtered_data.csv"))
    print("Total taxa:", len(data["list"]))
    counts = category_counts(data)
    for c in ("CR", "EN", "VU", "NT", "LC", "DD", "EX", "EW"):
        print(" ", c, counts.get(c, 0))
    for q in ("White Seraya", "Santalum album", "Psidium claraense"):
        print(" search", q, "->", search(data, q))
