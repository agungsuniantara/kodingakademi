import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data Simulasi (50 Hari)
np.random.seed(42)
hari = pd.date_range('2026-01-01', periods=50)
t = np.arange(1, 51)

# Persamaan Linear 
linear_data = 2 * t + 10 + np.random.normal(0, 6, 50)

# Persamaan Quadratic
quad_data = 0.08 * (t**2) - 1.5 * t + 20 + np.random.normal(0, 8, 50)

# Persamaan Cubic
t_shifted = t - 25 
cubic_data = 0.05 * (t_shifted**3) - 0.2 * (t_shifted**2) + np.random.normal(0, 150, 50) + 1000

# Perhitungan Moving Average (Window = 7 Hari)
df = pd.DataFrame({'Linear': linear_data, 'Quadratic': quad_data, 'Cubic': cubic_data}, index=hari)
df['MA_Linear'] = df['Linear'].rolling(window=7, center=True).mean()
df['MA_Quadratic'] = df['Quadratic'].rolling(window=7, center=True).mean()
df['MA_Cubic'] = df['Cubic'].rolling(window=7, center=True).mean()

# Visualisasi Vertikal (3 baris, 1 kolom)
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Konfigurasi Grafik Linear
axes[0].plot(df.index, df['Linear'], marker='o', markersize=4, linestyle='', color='lightblue', label='Data Asli')
axes[0].plot(df.index, df['MA_Linear'], color='blue', linewidth=3, label='MA (7 Hari)')
axes[0].set_title('Tren Linear (Order 1) - Pergerakan Konstan')

# Konfigurasi Grafik Quadratic
axes[1].plot(df.index, df['Quadratic'], marker='o', markersize=4, linestyle='', color='lightgreen', label='Data Asli')
axes[1].plot(df.index, df['MA_Quadratic'], color='green', linewidth=3, label='MA (7 Hari)')
axes[1].set_title('Tren Quadratic (Order 2) - Percepatan / Lengkungan Tunggal')

# Konfigurasi Grafik Cubic
axes[2].plot(df.index, df['Cubic'], marker='o', markersize=4, linestyle='', color='lightcoral', label='Data Asli')
axes[2].plot(df.index, df['MA_Cubic'], color='red', linewidth=3, label='MA (7 Hari)')
axes[2].set_title('Tren Cubic (Order 3) - Bentuk Huruf S / Kelengkungan Ganda')

for ax in axes:
    ax.tick_params(axis='x', rotation=0) # Rotasi 0 karena layout vertikal lebih luas
    ax.grid(True)
    ax.legend()
    ax.set_ylabel('Nilai')

plt.tight_layout()
plt.show()
