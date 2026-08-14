"""
simulation.py
Hitung proyeksi populasi pakai NumPy berdasarkan kategori IUCN.
Tidak ada GUI / baca file di sini.

Acuan IUCN Red List v3.1:
  CR : populasi awal 250   , turun 80% / 10 thn -> ~14.87% per tahun
  EN : populasi awal 2500  , turun 50% / 10 thn -> ~6.70%  per tahun
  VU : populasi awal 10000 , turun 30% / 10 thn -> ~3.49%  per tahun
"""

import numpy as np

# Data acuan tiap kategori
PROFIL = {
    "CR": {"nama": "Critically Endangered", "populasi_awal": 250,   "penurunan_10thn": 0.80},
    "EN": {"nama": "Endangered",            "populasi_awal": 2500,  "penurunan_10thn": 0.50},
    "VU": {"nama": "Vulnerable",            "populasi_awal": 10000, "penurunan_10thn": 0.30},
}

# Daftar aksi penyelamatan (mengurangi laju penurunan)
AKSI_RESCUE = [
    {"key": "anti_poaching",    "label": "Stop Perburuan / Eksploitasi", "modifier": 0.08},
    {"key": "captive_breeding", "label": "Penangkaran (Captive Breeding)", "modifier": 0.06},
    {"key": "habitat_restore",  "label": "Pemulihan Habitat",            "modifier": 0.05},
    {"key": "legal_protection", "label": "Penegakan Perlindungan Hukum", "modifier": 0.03},
    {"key": "community_program", "label": "Konservasi Berbasis Komunitas", "modifier": 0.02},
]

TAHUN_DEFAULT = 15


def laju_tahunan(penurunan_10thn):
    """Laju penurunan per tahun (compound) dari penurunan X% selama 10 tahun."""
    return 1.0 - (1.0 - penurunan_10thn) ** (1.0 / 10.0)


def bisa_disimulasi(kategori):
    return (kategori or "").strip().upper() in PROFIL


def laju_efektif(kategori, aksi_aktif):
    """Laju dasar dikurangi total modifier aksi yang aktif (bisa negatif = pulih)."""
    cat = kategori.strip().upper()
    dasar = laju_tahunan(PROFIL[cat]["penurunan_10thn"])
    bonus = 0.0
    aktif = set(aksi_aktif or [])
    for aksi in AKSI_RESCUE:
        if aksi["key"] in aktif:
            bonus += aksi["modifier"]
    return dasar - bonus


def proyeksi(kategori, laju, tahun=TAHUN_DEFAULT):
    """
    Hitung populasi tiap tahun: P(t) = P0 * (1 - laju)^t
    Kembalikan (array_tahun, array_populasi). Populasi tidak boleh negatif.
    """
    cat = kategori.strip().upper()
    p0 = PROFIL[cat]["populasi_awal"]
    t = np.arange(0, int(tahun) + 1)
    populasi = p0 * (1.0 - laju) ** t
    return t, np.clip(populasi, 0.0, None)


def baseline(kategori, tahun=TAHUN_DEFAULT):
    """Skenario tanpa intervensi (menuju kepunahan)."""
    laju = laju_tahunan(PROFIL[kategori.strip().upper()]["penurunan_10thn"])
    return proyeksi(kategori, laju, tahun)


def rescue(kategori, aksi_aktif, tahun=TAHUN_DEFAULT):
    """Skenario setelah intervensi dipilih."""
    laju = laju_efektif(kategori, aksi_aktif)
    return proyeksi(kategori, laju, tahun)


def ringkasan(kategori, aksi_aktif, tahun=TAHUN_DEFAULT):
    """Angka ringkas untuk ditampilkan di samping grafik."""
    cat = kategori.strip().upper()
    _, base = baseline(cat, tahun)
    _, res = rescue(cat, aksi_aktif, tahun)
    laju_dasar = laju_tahunan(PROFIL[cat]["penurunan_10thn"])
    eff = laju_efektif(cat, aksi_aktif)
    return {
        "kategori": cat,
        "nama_kategori": PROFIL[cat]["nama"],
        "populasi_awal": PROFIL[cat]["populasi_awal"],
        "laju_dasar_persen": laju_dasar * 100.0,
        "laju_efektif_persen": eff * 100.0,
        "pulih": eff < 0,
        "akhir_baseline": float(base[-1]),
        "akhir_rescue": float(res[-1]),
        "selisih": float(res[-1] - base[-1]),
        "tahun": int(tahun),
    }


# uji cepat
if __name__ == "__main__":
    for cat in PROFIL:
        semua = [a["key"] for a in AKSI_RESCUE]
        t, base = baseline(cat)
        _, full = rescue(cat, semua)
        print(cat, PROFIL[cat]["nama"])
        print("  laju dasar:", round(laju_tahunan(PROFIL[cat]["penurunan_10thn"]) * 100, 2), "%/thn")
        print("  baseline thn", t[-1], "->", round(float(base[-1])))
        print("  full rescue ->", round(float(full[-1])),
              "(laju efektif", round(laju_efektif(cat, semua) * 100, 2), "%)")
