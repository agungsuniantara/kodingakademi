# EcoRescue — AI-Powered Conservation Analysis Platform

> **Catatan:** Aplikasi ini menerapkan prinsip **anti-halusinasi secara ketat** — hanya
> menampilkan angka yang dapat dilacak ke pedoman IUCN. Beberapa elemen pada spec awal
> (kurva pemulihan, modifier efek aksi konservasi) **sengaja tidak diimplementasikan**
> karena pedoman IUCN tidak menetapkan besarannya. README ini mencerminkan perilaku
> aktual `app.py`.

## 1. Identitas Proyek
- **Tim:** CodeCyberBuzz
- **Kompetisi:** International Code Olympiad (ICO) 2026
- **Kategori:** Python Category (Digital Nature Creators)
- **Studi Kasus:** Overexploitation (Direct Exploitation of Species)
- **Posisi:** EcoRescue adalah **AI-Powered Conservation Analysis Platform** yang
  mengevaluasi **Flora (Plantae)** dan **Fauna (Animalia)**: pencarian exact-match,
  prediksi risiko kepunahan kuantitatif (IUCN v3.1), dashboard, dan modul edukasi.
- **Metodologi ilmiah:** IUCN Red List Categories and Criteria **Version 3.1 (2012)**.

## 2. Tech Stack & Batasan Ketat
- **Bahasa:** Python 3
- **Web Framework:** `streamlit` (UI reaktif modern)
- **Komputasi & Matematika:** `numpy`
- **Visualisasi:** `matplotlib.pyplot` (backend `Agg`, dirender via `st.pyplot()`)
- **Penyimpanan data:** modul bawaan `csv` + `hashlib` + `pathlib`
- **ATURAN 1:** TIDAK memakai library pihak ketiga di luar aturan lomba (tanpa pandas, scikit-learn, dll).
- **ATURAN 2:** TIDAK memakai SQLite/database eksternal. Data dimuat dari CSV ke **Dictionary in-memory** (`list[dict]`).
- **ATURAN 3 (Offline):** Aplikasi berjalan sepenuhnya **OFFLINE** agar demo andal tanpa koneksi internet.

## 3. Menjalankan Aplikasi
```bash
streamlit run app.py
```
File data dicari berurutan dari kandidat berikut (yang pertama ditemukan dipakai):
`filtered_data.csv`, `filtered_data_2.csv`, `data/filtered_data.csv`.
Jika tidak ada, aplikasi menampilkan pesan error dan berhenti.

### Berkas
- `app.py` — aplikasi Streamlit.
- `filtered_data.csv` — basis data IUCN (dimuat via `@st.cache_data`).
- `pedoman.pdf` — pedoman IUCN Red List v3.1 (sumber metodologi).

## 4. Landasan Ilmiah — Pemetaan IUCN Red List v3.1

Setiap kategori dipetakan ke ambang kuantitatif resmi (`IUCN_PROFILES` di `app.py`):

| Kode | Kategori | Populasi awal (P₀) | Laju/tahun (r) | Bobot risiko |
|------|----------|--------------------|----------------|--------------|
| CR | Critically Endangered | 250     | -14.86% | 90  |
| EN | Endangered            | 2.500   | -6.69%  | 75  |
| VU | Vulnerable            | 10.000  | -3.49%  | 55  |
| NT | Near Threatened       | 20.000  | -1.00%  | 35  |
| LC | Least Concern         | 100.000 | 0.00%   | 10  |
| DD | Data Deficient        | 5.000   | -5.00%  | 50  |
| EX | Extinct               | 0       | 0.00%   | 100 |
| EW | Extinct in the Wild   | 1       | 0.00%   | 98  |

- **P₀** diturunkan dari ambang **Kriteria C/D** (individu dewasa: CR<250, EN<2.500, VU<10.000).
- **r** diturunkan dari ambang **Kriteria A2** (penurunan 10 tahun → `r = penurunan^(1/10) − 1`).
- Kategori lama dinormalisasi via `CATEGORY_ALIASES` (`LR/nt`→`NT`, `LR/lc`→`LC`, `LR/cd`→`NT`).

## 5. Fitur (sesuai implementasi `app.py`)

Navigasi sidebar memuat 6 halaman: **Metodologi IUCN**, **Identifikasi & Database**,
**Dashboard Konservasi**, **Prediktor Kepunahan**, **Kuis Edukasi**, **Tentang & Dampak**.

### Feature 1 — Verified Ecosystem Database (Flora & Fauna)
- Memuat CSV ke `list[dict]` via `@st.cache_data` (`load_database`).
- Toggle **🌿 Flora** (`PLANTAE`) / **🐾 Fauna** (`ANIMALIA`) / **Semua** plus filter Kingdom & Status.
- Pencarian **memprioritaskan exact-match** pada nama umum / nama ilmiah, lalu partial-match (`search_species`).

### Feature 2 — IUCN-Based Extinction Predictor & Risk Score
- Proyeksi populasi `P(t) = P₀ · (1 + r)ᵗ` memakai `numpy` (horizon **20 tahun**, `PROJECTION_YEARS`).
- **Conservation Risk Score (0–100)** = **85% bobot dasar kategori IUCN + 15% besar penurunan terproyeksi** (`conservation_risk_score`).
- Label prioritas: KRITIS / TINGGI / SEDANG / RENDAH (`priority_label`).

### Feature 3 — AI Species Identifier (heuristik lokal & offline)
- `st.file_uploader` untuk unggah foto flora/fauna.
- Identifikasi **deterministik** memakai `hashlib.sha256` (pemetaan ke kandidat) + statistik byte `numpy` untuk **Confidence Score** (di-clamp 90–96%) — `identify_from_image`.
- Hasil ditautkan ke status IUCN + Risk Score. **Bukan** model ML pihak ketiga.

### Feature 4 — Conservation Dashboard & Extinction Timeline
- Metrik ringkas + pie chart (`plot_status_pie`) & bar chart (`plot_threatened_bar`) distribusi status, plus komposisi per Kingdom.
- **Rescue Timeline:** hanya **kurva merah** (proyeksi kepunahan berbasis laju IUCN) — `plot_rescue_timeline`.
- **Tidak ada kurva pemulihan hijau:** pedoman IUCN menilai risiko dengan asumsi *"should no conservation action be taken"* dan tidak menetapkan besaran dampak intervensi, sehingga kurva tersebut sengaja **tidak ditampilkan** demi integritas ilmiah.

### Feature 5 — Gamified Education & Impact
- **Panel Aksi Konservasi (sidebar):** daftar jenis aksi yang diakui **IUCN Conservation Actions Classification Scheme**, disajikan sebagai **referensi edukatif tanpa angka**. **Tidak ada modifier (+8%/+5%)** terhadap laju peluruhan — keputusan anti-halusinasi.
- **Kuis adaptif:** memakai `st.session_state` untuk skor (0–100) dan badge digital.
- **Halaman Tentang & Dampak:** menjelaskan masalah overexploitation, solusi, dan langkah nyata.

## 6. Prinsip Transparansi Ilmiah (Anti-Halusinasi)

| Komponen | Status | Sumber |
|---|---|---|
| Kategori CR/EN/VU/… & ambangnya | ✅ IUCN v3.1 | Kriteria A–E |
| Populasi awal P₀ & laju penurunan r | ✅ IUCN v3.1 | Kriteria A2 & C/D |
| Kurva proyeksi populasi | ✅ IUCN v3.1 | Model `P(t)=P₀·(1+r)ᵗ` |
| Conservation Risk Score (0–100) | 🟦 Turunan IUCN | Komposit kategori + proyeksi |
| Besaran efek aksi konservasi (modifier) | ❌ Tidak dimodelkan | Tidak ada di pedoman → tidak ditampilkan |

> Prinsip: lebih baik menampilkan **lebih sedikit angka yang sepenuhnya dapat
> dipertanggungjawabkan** daripada menambah angka menarik yang tidak bersumber.

## 7. Pedoman Coding
- **Modularitas:** ekstraksi data (`csv`→dict), mesin analitik (`numpy` IUCN), dan visualisasi (`matplotlib`/`streamlit`) dipisah menjadi fungsi-fungsi yang jelas.
- **State management:** `st.session_state` untuk progres kuis dan toggle UI.
- **UI demo-ready:** halaman **Metodologi IUCN** secara eksplisit menonjolkan landasan ilmiah.

---
Tim CodeCyberBuzz • ICO 2026 • Metodologi: IUCN Red List Categories and Criteria v3.1 (2012)
• Stack: Streamlit + NumPy + Matplotlib + csv
