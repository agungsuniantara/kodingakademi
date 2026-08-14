# Extinction Predictor — Dokumentasi Lengkap

## 1. Gambaran Umum

Extinction Predictor adalah fitur inti dari EcoRescue yang memproyeksikan trajektori populasi spesies berdasarkan **IUCN Red List Categories and Criteria v3.1 (2012)**. Fitur ini menggunakan model matematika eksponensial untuk mengestimasi jumlah individu dewasa yang matang di masa depan, dan menghitung skor risiko kepunahan (0–100) untuk setiap spesies.

**Rujukan utama:** *IUCN Red List Categories and Criteria: Version 3.1 (Second edition). Gland, Switzerland and Cambridge, UK: IUCN.*

---

## 2. Kategori IUCN yang Didukung

Fitur ini menyediakan proyeksi untuk empat kategori ancaman:

| Kode | Label | Deskripsi IUCN |
|------|-------|----------------|
| **CR** | Critically Endangered | Menghadapi risiko kepunahan **sangat tinggi** di alam liar |
| **EN** | Endangered | Menghadapi risiko kepunahan **sangat tinggi** di alam liar |
| **VU** | Vulnerable | Menghadapi risiko kepunahan **tinggi** di alam liar |
| **NT** | Near Threatened | Mendekati atau kemungkinan memenuhi kriteria terancam di masa dekat |

Kategori lain (LC, DD, EX, EW) tidak ditampilkan di Extinction Predictor karena tidak memiliki kriteria kuantitatif proyeksi populasi yang ditetapkan IUCN.

---

## 3. Sumber Data IUCN yang Digunakan

### 3.1 Kriteria A — Penurunan Ukuran Populasi

IUCN menetapkan tingkat penurunan populasi minimum berdasarkan sub-kriteria A2–A4:

| Kategori | A1 (penyebab berhenti) | A2–A4 (penyebab belum berhenti) | Rentang Waktu |
|----------|----------------------|-------------------------------|---------------|
| **CR** | ≥90% | ≥80% | 10 tahun atau 3 generasi |
| **EN** | ≥70% | ≥50% | 10 tahun atau 3 generasi |
| **VU** | ≥50% | ≥30% | 10 tahun atau 3 generasi |

Sistem menggunakan **A2–A4** (penyebab belum berhenti/ belum dipahami/ belum dapat dibalikkan) karena merupakan skenario yang paling relevan untuk konservasi.

### 3.2 Kriteria C — Ukuran Populasi Kecil dan Penurunan

Batas jumlah individu dewasa matang:

| Kategori | Jumlah Individu Dewasa Matang | Penurunan Berkelanjutan (C1) |
|----------|------------------------------|------------------------------|
| **CR** | <250 | ≥25% dalam 3 tahun atau 1 generasi |
| **EN** | <2.500 | ≥20% dalam 5 tahun atau 2 generasi |
| **VU** | <10.000 | ≥10% dalam 10 tahun atau 3 generasi |

### 3.3 Kriteria D — Populasi Sangat Kecil atau Terbatas

| Kategori | Individu Dewasa Matang (D1) |
|----------|---------------------------|
| **CR** | <50 |
| **EN** | <250 |
| **VU** | <1.000 |

### 3.4 Kriteria E — Analisis Kuantitatif

Probabilitas kepunahan di alam liar:

| Kategori | Probabilitas | Rentang Waktu |
|----------|-------------|---------------|
| **CR** | ≥50% | 10 tahun atau 3 generasi |
| **EN** | ≥20% | 20 tahun atau 5 generasi |
| **VU** | ≥10% | 100 tahun |

---

## 4. Model Matematika

### 4.1 Formula Proyeksi Populasi

```
P(t) = P₀ × (1 + r)^t
```

Di mana:
- **P(t)** = jumlah populasi pada tahun ke-t
- **P₀** = populasi awal (jumlah individu dewasa matang)
- **r** = laju penurunan tahunan (annual decay rate)
- **t** = waktu dalam tahun

Populasi dibatasi minimum 0 (`np.clip`).

### 4.2 Penentuan P₀ (Populasi Awal)

P₀ diambil dari **ambang batas Kriteria C/D**:

| Kategori | P₀ | Sumber |
|----------|-----|--------|
| CR | 250 | Kriteria C: <250 individu dewasa matang |
| EN | 2.500 | Kriteria C: <2.500 individu dewasa matang |
| VU | 10.000 | Kriteria C: <10.000 individu dewasa matang |
| NT | 20.000 | Estimate fallback (di atas ambang VU) |
| LC | 100.000 | Estimate fallback (spesies melimpah) |
| DD | 5.000 | Estimate fallback (data tidak memadai) |
| EX | 0 | Sudah punah |
| EW | 1 | Hanya tersisa di penangkaran |

### 4.3 Penentuan r (Laju Penurunan Tahunan)

Laju tahunan dihitung dari **total penurunan Kriteria A2–A4** yang terjadi selama rentang waktu IUCN:

```
r = (1 - decline_pct / 100)^(1 / years) - 1
```

Contoh perhitungan:

| Kategori | Total Decline | Periode | r (tahunan) |
|----------|--------------|---------|-------------|
| CR | 80% | 10 tahun | -14,87%/tahun |
| EN | 50% | 20 tahun | -3,41%/tahun |
| VU | 30% | 100 tahun | -0,36%/tahun |

**Verifikasi:** Setelah periode penuh, P(t)/P₀ = (1 + r)^years = persentase sisa yang benar:
- CR: (1 - 0,1487)^10 ≈ 0,20 → 20% tersisa (80% penurunan) ✓
- EN: (1 - 0,0341)^20 ≈ 0,50 → 50% tersisa (50% penurunan) ✓
- VU: (1 - 0,0036)^100 ≈ 0,70 → 70% tersisa (30% penurunan) ✓

### 4.4 Perioda Proyeksi per Kategori

| Kategori | Perioda Proyeksi | Keterangan |
|----------|-----------------|------------|
| **CR** | 10 tahun | Sesuai IUCN Criterion A/C |
| **EN** | 20 tahun | Sesuai IUCN Criterion E |
| **VU** | 100 tahun | Sesuai IUCN Criterion E |
| **NT/LC/DD** | 20 tahun (fallback) | Tidak ada spesifikasi IUCN |

---

## 5. Skor Risiko Kepunahan (Conservation Risk Score)

### 5.1 Formula

```python
score = e_prob × 0,85 + decline_frac × 100 × 0,15
```

Komponen:
- **e_prob** (85%): Probabilitas kepunahan dari Kriteria E (CR=50, EN=20, VU=10, NT=5, LC=1, DD=15)
- **decline_frac** (15%): Fraksi penurunan aktual berdasarkan proyeksi = `1 - (P末 / P₀)`

**Catatan:** Formula ini adalah **metrik komposit kustom**, bukan bagian dari standar IUCN. IUCN menetapkan bahwa spesies memenuhi kriteria terancam jika memenuhi **salah satu** dari Kriteria A–E, bukan kombinasi.

### 5.2 Label Prioritas

| Skor | Label | Warna |
|------|-------|-------|
| ≥80 | CRITICAL | Merah (#dc2626) |
| ≥60 | HIGH | Oranye (#f59e0b) |
| ≥40 | MEDIUM | Kuning (#eab308) |
| <40 | LOW | Hijau (#22c55e) |

---

## 6. Arsitektur Kode

### 6.1 Fungsi Inti

| Fungsi | Lokasi | Tugas |
|--------|--------|-------|
| `_get_projection_years(cat)` | `app.py:91` | Mengembalikan perioda proyeksi IUCN per kategori |
| `_get_decay(cat)` | `app.py:95` | Menghitung laju penurunan tahunan dari Kriteria A2 |
| `_get_pop0(cat)` | `app.py:105` | Mengembalikan populasi awal dari Kriteria C/D |
| `_get_e_prob(cat)` | `app.py:113` | Mengembalikan probabilitas kepunahan dari Kriteria E |
| `project_population(category, years)` | `app.py:207` | Membuat array proyeksi populasi P(t) |
| `conservation_risk_score(category, trajectory)` | `app.py:217` | Menghitung skor risiko 0–100 |
| `priority_label(score)` | `app.py:228` | Mengelompokkan skor ke label prioritas |
| `plot_rescue_timeline(category, years)` | `app.py:303` | Membuat grafik garis proyeksi populasi |

### 6.2 Alur Proses (Extinction Predictor UI)

```
1. User memilih organisme group (Flora/Fauna/All)
2. Filter spesies → hanya CR, EN, VU, NT
3. User memilih spesies dari dropdown
4. Hitung: P₀ ← _get_pop0(category)
5. Hitung: r ← _get_decay(category)
6. Hitung: years ← _get_projection_years(category)
7. Proyeksi: trajectory = project_population(category)
8. Hitung: risk_score = conservation_risk_score(category, trajectory)
9. Tampilkan: 3 metrik + grafik garis + expander penjelasan
```

### 6.3 Struktur Data IUCN_PROFILES

```python
IUCN_PROFILES = {
    "CR": {
        "kriteria_A_penurunan_populasi_persen": {"A1": 90, "A2_A4": 80},
        "kriteria_C_maks_individu_dewasa": 250,
        "kriteria_D_maks_individu_dewasa": 50,
        "kriteria_E_probabilitas_punah_persen": 50,
        "kriteria_E_rentang_waktu": "10 years or 3 generations",
    },
    # ... EN, VU, NT, LC, DD, EX, EW
}
```

---

## 7. Komponen UI

### 7.1 Tiga Metrik Utama

| Metrik | Deskripsi |
|--------|-----------|
| **IUCN Status** | Kode dan label kategori IUCN |
| **Current Risk Score** | Skor 0–100 + label prioritas |
| **Population Projection yr-N** | Estimasi populasi akhir N tahun + delta dari awal |

### 7.2 Grafik Garis (Rescue Timeline)

- Sumbu X: Tahun (0 hingga perioda proyeksi)
- Sumbu Y: Estimasi jumlah individu dewasa matang
- Garis merah: Proyeksi populasi berdasarkan laju penurunan IUCN
- Area merah muda: Area di bawah kurva proyeksi
- Judul: "Population Projection {N} Years — {Kategori} ({Label})"

### 7.3 Expander Penjelasan Ilmiah

Menampilkan:
- Model matematika yang digunakan
- Nilai P₀ dan r untuk kategori tersebut
- Sumber data IUCN (Kriteria A2, C/D, E)
- Catatan bahwa Risk Score adalah metrik kustom

---

## 8. Perbedaan dengan Standar IUCN

| Aspek | IUCN Standar | Implementasi EcoRescue | Catatan |
|-------|-------------|----------------------|---------|
| Kriteria A2 threshold | Tabel spesifik per kategori | Sama persis | ✓ |
| Kriteria C/D/E threshold | Tabel spesifik per kategori | Sama persis | ✓ |
| Proyeksi populasi | PVA (Population Viability Analysis) | Model eksponensial sederhana | PVA memerlukan data demografi lengkap |
| Perioda proyeksi | Per kategori (10/20/100 tahun) | Dinamis sesuai kategori | ✓ |
| Laju penurunan | Total decline over N years | Annualized via `(1-D)^(1/T)-1` | ✓ |
| Risk Score | Tidak ada (A–E bersifat diskrit) | Formula kustom 85%E + 15%decline | Metrik tambahan, bukan pengganti |
| Fallback NT/LC/DD | Tidak ada kriteria kuantitatif | Estimasi konservatif | Perlu validasi lebih lanjut |

---

## 9. Keterbatasan dan Path Upgrade

1. **Model eksponensial** tidak mempertimbangkan fluktuasi stokastik, carrying capacity, atau interaksi spesies. Path upgrade: integrasi PVA (Population Viability Analysis) atau model Leslie matrix.

2. **P₀ dari ambang Kriteria C** adalah estimasi konservatif, bukan populasi aktual. Path upgrade: input populasi aktual dari data lapangan.

3. **Laju penurunan diasumsikan konstan** sepanjang waktu. Path upgrade: model density-dependent atau time-varying rate.

4. **Risk Score adalah metrik kustom** yang tidak ada di standar IUCN. Path upgrade: gunakan scoring yang diakui seperti RAMAS Red List.

5. **Generasi (generation length)** tidak diperhitungkan secara spesifik — digunakan 10 tahun sebagai minimum. Path upgrade: input generation length per spesies.
