import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.deterministic import DeterministicProcess
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Dataset Pertumbuhan Produksi (20 Hari)
waktu = pd.date_range(start='2026-05-01', periods=20, freq='D')

produksi = [10, 12, 15, 19, 25, 30, 38, 47, 55, 66, 
            78, 89, 105, 120, 135, 155, 175, 198, 220, 245]

df_produksi = pd.DataFrame({'Volume': produksi}, index=waktu)

dp_proses = DeterministicProcess(
    index=df_produksi.index, 
    constant=True, 
    order=2, 
    drop=True
)

X_in = dp_proses.in_sample()
y = df_produksi['Volume']

# Forecasting 5 hari ke depan
X_out = dp_proses.out_of_sample(steps=5)

# fit_intercept=False wajib agar tidak bertabrakan dengan fitur 'const'
model_tren = LinearRegression(fit_intercept=False)
model_tren.fit(X_in, y)

# Mengevaluasi seberapa baik tren dipelajari pada data historis
prediksi_historis = model_tren.predict(X_in)
mae_historis = mean_absolute_error(y, prediksi_historis)

# Prediksi masa depan
prediksi_masa_depan = model_tren.predict(X_out)

df_forecast = pd.DataFrame({
    'Prediksi_Volume': np.round(prediksi_masa_depan, 2)
}, index=X_out.index)

# Visualisasi
plt.figure(figsize=(12, 6))

# Plot data historis
plt.scatter(df_produksi.index, df_produksi['Volume'], color='black', label='Data Produksi (Aktual)', zorder=5)

# Plot tren historis (fitted)
plt.plot(df_produksi.index, prediksi_historis, color='blue', linestyle='--', label='Tren (In-Sample Fit)')

# Plot hasil forecasting
plt.plot(df_forecast.index, df_forecast['Prediksi_Volume'], color='red', marker='o', label='Forecasting (5 Hari)')

# Menambahkan detail grafik
plt.title('Forecasting Pertumbuhan Produksi dengan Tren Kuadratik', fontsize=14)
plt.xlabel('Tanggal', fontsize=12)
plt.ylabel('Volume Produksi', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# Menyimpan gambar
plt.savefig('visualisasi_forecasting_produksi.png')
print("Visualisasi telah disimpan sebagai 'visualisasi_forecasting_produksi.png'")

# Menampilkan hasil di terminal
print("\n=== Evaluasi Model Tren pada Data Historis ===")
print(f"Mean Absolute Error (MAE): {mae_historis:.2f}")
print("\n=== Hasil Forecasting (5 Hari ke Depan) ===")
print(df_forecast)
