import tkinter as tk
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.title("Aplikasi Deteksi Obesitas")
root.geometry("900x700")

# Main container
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

# Configure grid weights for main frame
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(1, weight=1)

# Title
title_label = tk.Label(main_frame, 
                       text="APLIKASI DETEKSI OBESITAS",
                       font=('Helvetica', 18, 'bold'),
                       fg='#2c3e50')
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='ew')

# Frame untuk form input
form_frame = tk.LabelFrame(main_frame, 
                           text="Data Pasien",
                           padx=15,
                           pady=15,
                           font=('Helvetica', 10, 'bold'))
form_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
form_frame.grid_columnconfigure(1, weight=1)

# Form input
tk.Label(form_frame, text="Nama Lengkap:", anchor='w').grid(row=0, column=0, padx=5, pady=5, sticky='w')
nama_entry = ttk.Entry(form_frame, width=40)
nama_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

tk.Label(form_frame, text="Alamat:", anchor='w').grid(row=1, column=0, padx=5, pady=5, sticky='w')
alamat_entry = ttk.Entry(form_frame, width=40)
alamat_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

tk.Label(form_frame, text="Umur:", anchor='w').grid(row=2, column=0, padx=5, pady=5, sticky='w')
umur_entry = ttk.Entry(form_frame, width=10)
umur_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

tk.Label(form_frame, text="Tinggi Badan (cm):", anchor='w').grid(row=3, column=0, padx=5, pady=5, sticky='w')
tinggi_entry = ttk.Entry(form_frame, width=10)
tinggi_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

tk.Label(form_frame, text="Jenis Kelamin:", anchor='w').grid(row=4, column=0, padx=5, pady=5, sticky='w')
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(form_frame, textvariable=gender_var, width=15)
gender_combobox['values'] = ('Pria', 'Wanita')
gender_combobox.grid(row=4, column=1, padx=5, pady=5, sticky='w')

tk.Label(form_frame, text="Tingkat Aktivitas:", anchor='w').grid(row=5, column=0, padx=5, pady=5, sticky='w')
aktivitas_var = tk.StringVar()
aktivitas_combobox = ttk.Combobox(form_frame, textvariable=aktivitas_var, width=20)
aktivitas_combobox['values'] = (
    'Minim aktivitas',
    'Aktivitas ringan',
    'Aktivitas sedang',
    'Aktivitas berat',
    'Aktivitas sangat berat'
)
aktivitas_combobox.grid(row=5, column=1, padx=5, pady=5, sticky='w')

# Frame untuk deteksi wajah
detection_frame = tk.LabelFrame(main_frame, 
                                text="Deteksi Wajah",
                                padx=15,
                                pady=15,
                                font=('Helvetica', 10, 'bold'))
detection_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
detection_frame.grid_columnconfigure(0, weight=1)
detection_frame.grid_rowconfigure(0, weight=1)
detection_frame.grid_rowconfigure(1, weight=0)

video_container = tk.Frame(detection_frame, 
                           bd=2, 
                           relief=tk.SUNKEN,
                           bg='black')
video_container.grid(row=0, column=0, sticky='nsew', pady=(0, 10))

video_label = tk.Label(video_container, bg='black')
video_label.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)

button_frame = tk.Frame(detection_frame)
button_frame.grid(row=1, column=0, sticky='ew')

capture_button = ttk.Button(button_frame, text="Ambil Foto")
capture_button.pack(side=tk.LEFT, padx=5)

# Hasil deteksi
result_frame = tk.LabelFrame(main_frame, 
                             text="Hasil Deteksi",
                             padx=15,
                             pady=15,
                             font=('Helvetica', 10, 'bold'))
result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

info_label = tk.Label(result_frame, 
                      text="Informasi Pasien: -", 
                      font=('Helvetica', 16),
                      anchor='w')
info_label.pack(fill=tk.X, pady=2)

bmi_label = tk.Label(result_frame, 
                     text="BMI: -", 
                     font=('Helvetica', 16),
                     anchor='w')
bmi_label.pack(fill=tk.X, pady=2)

weight_label = tk.Label(result_frame, 
                        text="Perkiraan Berat Badan: -", 
                        font=('Helvetica', 16),
                        anchor='w')
weight_label.pack(fill=tk.X, pady=2)

category_label = tk.Label(result_frame, 
                          text="Kategori Berat Badan: -", 
                          font=('Helvetica', 16),
                          anchor='w')
category_label.pack(fill=tk.X, pady=2)

calorie_label = tk.Label(result_frame, 
                         text="Rekomendasi Kalori Harian: -", 
                         font=('Helvetica', 16),
                         anchor='w')
calorie_label.pack(fill=tk.X, pady=2)

footer_label = tk.Label(main_frame, 
                        text=f"© {datetime.now().year} Aplikasi Deteksi Obesitas - v1.0",
                        font=('Helvetica', 8),
                        fg='gray')
footer_label.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')

root.mainloop()
