# Assignment: Analisis Musiman (Seasonality) Data Time Series

## Deskripsi Tugas
Dalam tugas ini, Anda akan melanjutkan analisis data harga saham Microsoft (`Microsoft_Stock.csv`) dengan fokus pada **ekstraksi fitur musiman (seasonality)**. Setelah sebelumnya melakukan ekstraksi fitur tren, lag, dan rolling window, sekarang Anda akan mengeksplorasi pola musiman menggunakan **variabel dummy musiman** dan **deret Fourier**.

## Dataset
- **File**: `Microsoft_Stock.csv`
- **Kolom**: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`

## Prasyarat
Pastikan Anda telah menyelesaikan **Assignment: Ekstraksi Fitur Data Time Series** sebelum mengerjakan tugas ini.

## Instruksi Tugas

### 1. Persiapan Data
- Load dataset menggunakan pandas.
- Ubah kolom `Date` menjadi tipe data datetime dan set sebagai index.
- Lakukan resampling data menjadi **bulanan** (Month Start / 'MS') dengan mengambil rata-rata harga `Close` setiap bulan.
- Tampilkan 5 baris pertama data setelah resampling.

### 2. Ekstraksi Fitur Tren (Review dari Materi Sebelumnya)
Gunakan `DeterministicProcess` untuk membuat fitur tren:
- Buat fitur tren **kuadratik** (order=2) yang mencakup: `const`, `trend`, dan `trend_squared`.
- Tampilkan matriks fitur tren yang dihasilkan.

### 3. Ekstraksi Fitur Musiman dengan Variabel Dummy
Gunakan `DeterministicProcess` dengan parameter `seasonal=True`:
- Buat variabel dummy musiman untuk data bulanan dengan `period=12`.
- Tampilkan matriks variabel dummy yang dihasilkan (akan ada 11 kolom dummy untuk 12 bulan).
- Jelaskan secara singkat apa yang merepresentasikan setiap kolom dummy.

### 4. Ekstraksi Fitur Musiman dengan Deret Fourier
Gunakan `Fourier` dari `statsmodels.tsa.deterministic`:
- Buat deret Fourier dengan `period=12` (siklus tahunan untuk data bulanan).
- Eksperimen dengan **2 orde berbeda**: `order=1` dan `order=3`.
- Tampilkan matriks Fourier untuk masing-masing orde.
- Jelaskan perbedaan jumlah kolom yang dihasilkan antara orde 1 dan orde 3.

### 5. Visualisasi Perbandingan Deret Fourier
Buat visualisasi yang membandingkan kemampuan deret Fourier dalam menangkap pola musiman:
- Gunakan data `Close` yang sudah di-resample bulanan.
- Latih model `LinearRegression` menggunakan fitur Fourier **orde 1** dan **orde 3** secara terpisah.
- Buat plot yang menampilkan:
  - Data aktual (`Close`)
  - Prediksi menggunakan Fourier Orde 1
  - Prediksi menggunakan Fourier Orde 3
- Berikan analisis: model mana yang lebih baik menangkap pola musiman? Apakah orde yang lebih tinggi selalu lebih baik?

### 6. Model Terpadu: Tren + Musiman
Gabungkan fitur tren dan fitur musiman dalam satu model:
- Gunakan `DeterministicProcess` dengan parameter:
  - `constant=True`
  - `order=2` (tren kuadratik)
  - `additional_terms=[Fourier(period=12, order=2)]`
- Tampilkan matriks fitur lengkap (tren + Fourier).
- Latih model `LinearRegression` pada seluruh data.
- Visualisasikan hasilnya: data aktual vs prediksi model terpadu.

### 7. Forecasting dengan Train-Test Split
Lakukan evaluasi model menggunakan data splitting:
- Bagi data menjadi **data latih** dan **data uji** (80% train, 20% test) dengan `shuffle=False`.
- Latih model menggunakan fitur tren + Fourier (orde 2) pada data latih.
- Lakukan prediksi pada data uji.
- Hitung metrik evaluasi **MAE (Mean Absolute Error)**.
- Visualisasikan:
  - Data latih (Training)
  - Data uji aktual (Testing - Aktual)
  - Hasil prediksi (Forecasting)

### 8. True Forecasting (Peramalan Masa Depan)
Lakukan peramalan ke masa depan:
- Gunakan `DeterministicProcess` dengan parameter `out_of_sample` untuk membuat fitur masa depan.
- Buat peramalan untuk **12 bulan ke depan**.
- Visualisasikan:
  - Seluruh data historis
  - Garis pemisah antara data historis dan peramalan
  - Hasil peramalan 12 bulan ke depan
- Berikan interpretasi: apakah model menangkap pola musiman dengan baik pada hasil peramalan?

---

## Kriteria Penilaian
| Aspek | Bobot |
|-------|-------|
| Kebenaran kode Python | 30% |
| Kelengkapan implementasi variabel dummy musiman | 15% |
| Kelengkapan implementasi deret Fourier (2 orde) | 15% |
| Kualitas visualisasi perbandingan | 15% |
| Implementasi forecasting yang benar | 15% |
| Kualitas analisis dan interpretasi | 10% |

---

## Tips Pengerjaan
1. **Resampling**: Gunakan `df.resample('MS').mean()` untuk mengubah data harian menjadi bulanan.
2. **DeterministicProcess**: Pastikan parameter `fit_intercept=False` pada `LinearRegression` jika menggunakan `constant=True` pada `DeterministicProcess`.
3. **Fourier Order**: Orde rendah = kurva halus (underfitting), orde tinggi = kurva kompleks (overfitting).
4. **Out-of-sample**: Gunakan `dp.out_of_sample(steps=12)` untuk membuat fitur masa depan.

---

## Referensi
- `statsmodels.tsa.deterministic.DeterministicProcess`
- `statsmodels.tsa.deterministic.Fourier`
- `sklearn.linear_model.LinearRegression`
- `sklearn.metrics.mean_absolute_error`