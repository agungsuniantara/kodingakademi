# Assignment: Ekstraksi Fitur Data Time Series

## Deskripsi Tugas
Dalam tugas ini, Anda akan melakukan ekstraksi fitur pada data harga saham Microsoft (`Microsoft_Stock.csv`). Ekstraksi fitur sangat penting dalam analisis time series untuk menangkap pola tren, musiman, dan ketergantungan historis.

## Dataset
- **File**: `Microsoft_Stock.csv`
- **Kolom**: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`

## Instruksi Tugas

### 1. Persiapan Data
- Load dataset menggunakan pandas.
- Ubah kolom `Date` menjadi tipe data datetime dan set sebagai index.
- Lakukan resampling data menjadi harian (Daily) jika diperlukan, atau pastikan data terurut berdasarkan waktu.

### 2. Ekstraksi Fitur Berbasis Waktu (DateTime Features)
Ekstrak komponen waktu dari index datetime:
- **Tahun** (Year)
- **Bulan** (Month)
- **Hari** (Day)
- **Hari dalam Minggu** (Day of Week)
- **Kuartal** (Quarter)

### 3. Ekstraksi Fitur Lag (Lag Features)
Buat fitur lag untuk kolom `Close`:
- Buat fitur `Lag_1` (harga penutupan kemarin).
- Buat fitur `Lag_7` (harga penutupan seminggu yang lalu).

### 4. Ekstraksi Fitur Jendela Bergerak (Rolling Window Features)
Hitung statistik moving average pada kolom `Close`:
- **Rolling Mean 7 hari**: Rata-rata harga penutupan dalam 7 hari terakhir.
- **Rolling Mean 30 hari**: Rata-rata harga penutupan dalam 30 hari terakhir.
- **Rolling Standard Deviation 7 hari**: Volatilitas harga dalam 7 hari terakhir.

### 5. Ekstraksi Fitur Turunan (Derived Features)
- Hitung selisih harga harian (Daily Return): `(Close - Open) / Open`.
- Hitung selisih antara harga tertinggi dan terendah (Daily Range): `High - Low`.

### 6. Analisis dan Visualisasi
- Tampilkan 5 baris pertama dari dataframe hasil ekstraksi fitur.
- Buat plot yang membandingkan harga `Close` asli dengan `Rolling Mean 30 hari` untuk melihat tren jangka panjang.
- Berikan analisis singkat mengenai korelasi antara fitur lag yang dibuat dengan harga `Close` saat ini.

### 7. Forecasting dengan Train-Test Split
- Gunakan fitur yang telah diekstrak sebagai input (X) dan `Close` sebagai target (y).
- Gunakan `train_test_split` dari `sklearn.model_selection` dengan parameter `shuffle=False` (penting untuk data time series).
- Latih model `LinearRegression` pada data training.
- Lakukan peramalan (forecasting) pada data testing.
- Visualisasikan seluruh data: Data Training, Data Testing (Aktual), dan Hasil Forecast.
- Hitung metrik evaluasi (MAE).

---

## Kriteria Penilaian
- Kebenaran kode Python.
- Kelengkapan fitur yang diekstrak sesuai instruksi.
- Kualitas visualisasi dan analisis.
- Kebersihan dan keterbacaan kode (dokumentasi/komentar).
