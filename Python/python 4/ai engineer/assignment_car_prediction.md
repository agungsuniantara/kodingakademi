# Assignment: Data Preprocessing & Supervised Learning
## Case Study: Car Purchase Prediction

### Dataset: `car_data.csv`
Dataset ini berisi informasi nasabah yang mungkin membeli mobil baru berdasarkan beberapa faktor.
*   **User ID**: ID unik nasabah (tidak relevan untuk prediksi).
*   **Gender**: Jenis kelamin (Male/Female).
*   **Age**: Usia nasabah.
*   **AnnualSalary**: Pendapatan tahunan.
*   **Purchased**: Target label (0 = Tidak Membeli, 1 = Membeli).

---

### Tugas Anda:

1.  **Exploratory Data Analysis (EDA)**:
    *   Tampilkan 5 data teratas.
    *   Cek apakah ada nilai kosong (*missing values*) pada dataset.
    *   Tampilkan statistik deskriptif dari dataset.

2.  **Data Preprocessing**:
    *   Hapus kolom `User ID` karena tidak memiliki pengaruh terhadap prediksi.
    *   Pisahkan data menjadi **Features (X)** dan **Target (y)**.
    *   Gunakan **ColumnTransformer** dan **Pipeline** untuk mengolah:
        *   Kolom Numerik (`Age`, `AnnualSalary`): Lakukan **Scaling** menggunakan `StandardScaler`.
        *   Kolom Kategorikal (`Gender`): Lakukan **Encoding** menggunakan `OneHotEncoder`.

3.  **Modelling**:
    *   Bagi data menjadi **Train Set** dan **Test Set** (80:20).
    *   Latih model menggunakan algoritma **Logistic Regression** di dalam sebuah Pipeline.

4.  **Evaluation**:
    *   Tampilkan **Accuracy Score** dari model.
    *   Tampilkan **Confusion Matrix** menggunakan Seaborn Heatmap.
    *   Berikan penjelasan singkat: Apa arti dari nilai-nilai di dalam Confusion Matrix tersebut terkait prediksi pembelian mobil?

---

### Format Pengumpulan:
Buatlah solusi Anda dalam sebuah file Jupyter Notebook (`.ipynb`) atau Python script (`.py`). Pastikan kode Anda rapi dan memiliki komentar penjelasan di setiap langkahnya.
