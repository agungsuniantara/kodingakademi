import tkinter as tk
from tkinter import ttk
from datetime import datetime

class ObesityDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Deteksi Obesitas")
        self.root.geometry("900x700")

        # Main container
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Configure grid weights for main frame
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        # Title
        self.title_label = tk.Label(self.main_frame, 
                                 text="APLIKASI DETEKSI OBESITAS",
                                 font=('Helvetica', 18, 'bold'),
                                 fg='#2c3e50')
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='ew')
        
        # Frame untuk form input
        self.form_frame = tk.LabelFrame(self.main_frame, 
                                      text="Data Pasien",
                                      padx=15,
                                      pady=15,
                                      font=('Helvetica', 10, 'bold'))
        self.form_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        
        # Configure grid weights for form frame
        self.form_frame.grid_columnconfigure(1, weight=1)
        
        # Form input
        tk.Label(self.form_frame, text="Nama Lengkap:", anchor='w').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.nama_entry = ttk.Entry(self.form_frame, width=40)
        self.nama_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        
        tk.Label(self.form_frame, text="Alamat:", anchor='w').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.alamat_entry = ttk.Entry(self.form_frame, width=40)
        self.alamat_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        
        tk.Label(self.form_frame, text="Umur:", anchor='w').grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.umur_entry = ttk.Entry(self.form_frame, width=10)
        self.umur_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        tk.Label(self.form_frame, text="Tinggi Badan (cm):", anchor='w').grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.tinggi_entry = ttk.Entry(self.form_frame, width=10)
        self.tinggi_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        
        # Jenis Kelamin
        tk.Label(self.form_frame, text="Jenis Kelamin:", anchor='w').grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(self.form_frame, textvariable=self.gender_var, width=15)
        self.gender_combobox['values'] = ('Pria', 'Wanita')
        self.gender_combobox.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        # Tingkat Aktivitas
        tk.Label(self.form_frame, text="Tingkat Aktivitas:", anchor='w').grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.aktivitas_var = tk.StringVar()
        self.aktivitas_combobox = ttk.Combobox(self.form_frame, textvariable=self.aktivitas_var, width=20)
        self.aktivitas_combobox['values'] = (
            'Minim aktivitas',      # Minim aktivitas
            'Aktivitas ringan',         # Aktivitas ringan
            'Aktivitas sedang',         # Aktivitas sedang
            'Aktivitas berat',          # Aktivitas berat
            'Aktivitas sangat berat'    # Aktivitas sangat berat
        )
        self.aktivitas_combobox.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        
        # Frame untuk deteksi wajah
        self.detection_frame = tk.LabelFrame(self.main_frame, 
                                          text="Deteksi Wajah",
                                          padx=15,
                                          pady=15,
                                          font=('Helvetica', 10, 'bold'))
        self.detection_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
        
        # Configure grid weights for detection frame
        self.detection_frame.grid_columnconfigure(0, weight=1)
        self.detection_frame.grid_rowconfigure(0, weight=1)
        self.detection_frame.grid_rowconfigure(1, weight=0)
        
        # Box untuk video dengan border
        self.video_container = tk.Frame(self.detection_frame, 
                                      bd=2, 
                                      relief=tk.SUNKEN,
                                      bg='black')
        self.video_container.grid(row=0, column=0, sticky='nsew', pady=(0, 10))
        
        # Label untuk video
        self.video_label = tk.Label(self.video_container, bg='black')
        self.video_label.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
        
        # Frame untuk tombol kontrol
        self.button_frame = tk.Frame(self.detection_frame)
        self.button_frame.grid(row=1, column=0, sticky='ew')
        
        self.capture_button = ttk.Button(self.button_frame, 
                                      text="Ambil Foto")
        self.capture_button.pack(side=tk.LEFT, padx=5)
        
        # Hasil deteksi
        self.result_frame = tk.LabelFrame(self.main_frame, 
                                       text="Hasil Deteksi",
                                       padx=15,
                                       pady=15,
                                       font=('Helvetica', 10, 'bold'))
        self.result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
        
        # Grid layout untuk hasil
        self.info_label = tk.Label(self.result_frame, 
                                text="Informasi Pasien: -", 
                                font=('Helvetica', 16),
                                anchor='w')
        self.info_label.pack(fill=tk.X, pady=2)
        
        self.bmi = tk.Label(self.result_frame, 
                                  text="BMI: -", 
                                  font=('Helvetica', 16),
                                  anchor='w')
        self.bmi.pack(fill=tk.X, pady=2)
        
        self.weight_label = tk.Label(self.result_frame, 
                             text="Perkiraan Berat Badan: -", 
                             font=('Helvetica', 16),
                             anchor='w')
        self.weight_label.pack(fill=tk.X, pady=2)

        self.category_label = tk.Label(self.result_frame, 
                                    text="Kategori Berat Badan: -", 
                                    font=('Helvetica', 16),
                                    anchor='w')
        self.category_label.pack(fill=tk.X, pady=2)

        self.calorie_label = tk.Label(self.result_frame, 
                                    text="Rekomendasi Kalori Harian: -", 
                                    font=('Helvetica', 16),
                                    anchor='w')
        self.calorie_label.pack(fill=tk.X, pady=2)

        
        # Footer
        self.footer_label = tk.Label(self.main_frame, 
                                   text=f"© {datetime.now().year} Aplikasi Deteksi Obesitas - v1.0",
                                   font=('Helvetica', 8),
                                   fg='gray')
        self.footer_label.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')

if __name__ == "__main__":
    root = tk.Tk()
    app = ObesityDetectionApp(root)
    root.mainloop()