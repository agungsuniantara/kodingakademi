# Assignment: AutoML Benchmarking for Clustering
## Case Study: Country Socio-Economic Segmentation

### Dataset: `country_data.csv`
Dataset ini berisi indikator sosial dan ekonomi dari berbagai negara yang digunakan untuk menentukan tingkat pembangunan suatu negara.
*   **country**: Nama negara.
*   **child_mort**: Kematian anak di bawah usia 5 tahun per 1000 kelahiran.
*   **exports**: Ekspor barang dan jasa (% dari PDB per kapita).
*   **health**: Total pengeluaran kesehatan (% dari PDB per kapita).
*   **imports**: Impor barang dan jasa (% dari PDB per kapita).
*   **income**: Pendapatan bersih per orang.
*   **inflation**: Laju inflasi tahunan.
*   **life_expec**: Harapan hidup rata-rata.
*   **total_fer**: Jumlah kelahiran per wanita.
*   **gdpp**: PDB per kapita.

---

### Tugas Anda:

1.  **Exploratory Data Analysis (EDA)**:
    *   Tampilkan 5 data teratas dan informasi dataset.
    *   Identifikasi korelasi antar fitur menggunakan heatmap (terutama hubungan antara `income`, `child_mort`, dan `gdpp`).

2.  **Preprocessing**:
    *   Pisahkan fitur numerik (drop kolom `country`).
    *   Lakukan **Scaling** menggunakan `StandardScaler` agar perbedaan skala antar fitur (misal: `gdpp` vs `total_fer`) tidak mendominasi perhitungan jarak.

3.  **AutoML Benchmarking**:
    *   Gunakan fungsi benchmark untuk membandingkan algoritma **KMeans** dan **AgglomerativeClustering**.
    *   Uji rentang jumlah kluster (K) dari **2 hingga 5**.
    *   Tampilkan **Leaderboard** berdasarkan nilai **Silhouette Score** tertinggi.

4.  **Final Modelling & Profiling**:
    *   Pilih model dan jumlah K terbaik dari leaderboard.
    *   Latih model tersebut pada data dan tambahkan label segmen ke dataframe asli.
    *   Lakukan **Profiling** dengan menghitung rata-rata setiap fitur per segmen.

5.  **Visualisasi & Analisis**:
    *   Buat scatter plot antara `income` vs `gdpp` dengan warna berdasarkan segmen.
    *   Berikan analisis singkat: Berdasarkan profil rata-rata, segmen mana yang menunjukkan negara-negara yang membutuhkan bantuan pembangunan paling mendesak? (Petunjuk: Cek `child_mort` tinggi dan `income` rendah).

---

### Format Pengumpulan:
Buatlah solusi Anda dalam sebuah Jupyter Notebook (`.ipynb`). Berikan narasi yang jelas pada setiap langkah pengerjaannya.
