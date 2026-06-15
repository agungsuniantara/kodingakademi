# Assignment: Time Series Preprocessing & Forecasting

## Deskripsi Tugas
Dalam tugas ini, Anda akan mempraktikkan teknik preprocessing data Time Series dan membangun model peramalan sederhana menggunakan dataset iklim harian di Delhi.

## Dataset
- **File**: `DailyDelhiClimateTest.csv`
- **Kolom Utama**:
    - `date`: Tanggal observasi
    - `meantemp`: Suhu rata-rata harian (Target yang akan diprediksi)
    - `humidity`: Kelembaban rata-rata
    - `wind_speed`: Kecepatan angin
    - `meanpressure`: Tekanan udara rata-rata

## Instruksi Tugas
1. **Load Data**: Baca file `DailyDelhiClimateTest.csv` menggunakan pandas.
2. **Set Index**: Ubah kolom `date` menjadi tipe data datetime dan tetapkan sebagai index dari DataFrame.
3. **Feature Engineering**:
    - Buat kolom `Time_Dummy` yang berisi urutan angka dari 0 hingga akhir data (sebagai representasi waktu linear).
    - Buat kolom `Lag_1` yang berisi nilai `meantemp` dari hari sebelumnya (menggunakan fungsi `.shift(1)`).
4. **Data Cleaning**: Hapus baris yang mengandung nilai `NaN` (akibat dari pembuatan kolom Lag).
5. **Data Splitting**: Bagi data menjadi fitur (`X`) dan target (`y`).
    - `X`: Kolom `Time_Dummy` dan `Lag_1`
    - `y`: Kolom `meantemp`
    - Gunakan proporsi **80% untuk Train** dan **20% untuk Test**.
    - **PENTING**: Pastikan `shuffle=False` agar urutan waktu tetap terjaga.
6. **Modelling**: Bangun model `LinearRegression` dari scikit-learn dan latih menggunakan data Train.
7. **Prediction & Evaluation**:
    - Lakukan prediksi pada data Test.
    - Hitung nilai **Mean Absolute Error (MAE)** dan **Root Mean Squared Error (RMSE)**.
8. **Output**: Tampilkan tabel perbandingan antara nilai Aktual dan hasil Prediksi.

## Format Pengumpulan
Simpan kode Anda dalam file Python dengan nama `jawaban_assignment_ts.py` atau dalam format Jupyter Notebook.
