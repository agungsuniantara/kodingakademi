import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from datetime import datetime
import torch
import dlib
import numpy as np
from scripts.models import get_model
from scripts.loader import vit_transforms
from torchvision.transforms import ToTensor
from PIL import Image, ImageTk 

class ObesityDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Deteksi Obesitas")
        self.root.geometry("900x700")

        # Inisialisasi model
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = get_model()  # dari repo asli
        self.model.load_state_dict(torch.load('weights/aug_epoch_7.pt', map_location=self.device))
        self.model.to(self.device)
        self.model.eval()

        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor("weights/shape_predictor_68_face_landmarks.dat")

        self.transform = vit_transforms  # dari vit_transforms.py

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
            'Sedentari',      # Minim aktivitas
            'Ringan',         # Aktivitas ringan
            'Sedang',         # Aktivitas sedang
            'Aktif',          # Aktivitas berat
            'Sangat Aktif'    # Aktivitas sangat berat
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
                                      text="Ambil Foto", 
                                      command=self.capture_image)
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
        
        self.video_capture = cv2.VideoCapture(0)
        self.show_video()
        
    def show_video(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = cv2.resize(frame_rgb, (self.video_label.winfo_width(), self.video_label.winfo_height()))
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.config(image=imgtk)
        self.root.after(30, self.show_video)
        
    def capture_image(self):
        if not self.validate_form():
            return
        
        ret, frame = self.video_capture.read()
        if not ret:
            messagebox.showerror("Error", "Gagal mengambil gambar dari webcam.")
            return

        # Convert BGR (OpenCV) to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Deteksi wajah menggunakan dlib
        dets = self.detector(frame_rgb, 1)
        if len(dets) == 0:
            messagebox.showwarning("Peringatan", "Wajah tidak terdeteksi.")
            return

        # Ambil wajah pertama yang terdeteksi
        d = dets[0]
        shape = self.shape_predictor(frame_rgb, d)

        # Ambil titik landmark wajah
        landmarks = np.array([[pt.x, pt.y] for pt in shape.parts()])

        # Hitung bounding box persegi dari wajah (mengikuti pendekatan square face di repo)
        left = np.min(landmarks[:, 0])
        top = np.min(landmarks[:, 1])
        right = np.max(landmarks[:, 0])
        bottom = np.max(landmarks[:, 1])
        size = max(right - left, bottom - top)

        # Pastikan bounding box berada dalam frame
        center_x = (left + right) // 2
        center_y = (top + bottom) // 2
        half_size = size // 2
        x1 = max(center_x - half_size, 0)
        y1 = max(center_y - half_size, 0)
        x2 = min(center_x + half_size, frame_rgb.shape[1])
        y2 = min(center_y + half_size, frame_rgb.shape[0])

        # Crop wajah persegi
        face_crop = frame_rgb[y1:y2, x1:x2]

        # Resize dan transformasi untuk ViT
        image = ToTensor()(face_crop)
        input_tensor = self.transform(image).unsqueeze(0).to(self.device)

        # Prediksi BMI
        with torch.no_grad():
            bmi_pred = self.model(input_tensor).item()
        
        # Ambil tinggi dari input dan konversi ke meter
        umur = int(self.umur_entry.get())
        tinggi_cm = float(self.tinggi_entry.get())
        tinggi_m = tinggi_cm / 100
        jenis_kelamin = self.gender_var.get()
        tingkat_aktivitas = self.aktivitas_var.get()

        # Hitung berat badan dari BMI
        berat_kg = bmi_pred * (tinggi_m ** 2)
        
        batas_kurus = 18.5 * (tinggi_m ** 2)
        batas_normal_atas = 24.9 * (tinggi_m ** 2)
        batas_overweight_atas = 29.9 * (tinggi_m ** 2)
        batas_obesitas = 30 * (tinggi_m ** 2)
        
        if berat_kg < batas_kurus:
            kategori_berat = f"< {batas_kurus:.2f}"
            kategori_bmi = "Kekurangan Berat Badan"
            kalori = self.hitung_kalori_harian(jenis_kelamin, umur, tinggi_cm, berat_kg, tingkat_aktivitas)
        elif batas_kurus <= berat_kg < batas_normal_atas:
            kategori_berat = f"{batas_kurus:.2f} - {batas_normal_atas:.2f}"
            kategori_bmi = "Berat Badan Normal"
            kalori = self.hitung_kalori_harian(jenis_kelamin, umur, tinggi_cm, berat_kg, tingkat_aktivitas)
        elif batas_normal_atas <= berat_kg < batas_overweight_atas:
            kategori_berat = f"{batas_normal_atas:.2f} - {batas_overweight_atas:.2f}"
            kategori_bmi = "Kelebihan Berat Badan"
            kalori = self.hitung_kalori_harian(jenis_kelamin, umur, tinggi_cm, berat_kg, tingkat_aktivitas)
        else:
            kategori_berat = f"{batas_obesitas:.2f} >"
            kategori_bmi = "Obesitas"
            kalori = self.hitung_kalori_harian(jenis_kelamin, umur, tinggi_cm, berat_kg, tingkat_aktivitas)

        # Tampilkan hasil
        self.info_label.config(text=f"Informasi Pasien: {self.nama_entry.get()} - {self.umur_entry.get()} th",
                               font=("Helvetica", 16))
        self.bmi.config(text=f"BMI: {bmi_pred:.2f}",
                        font=("Helvetica", 16))
        self.weight_label.config(text=f"Perkiraan Berat Badan: {kategori_berat} kg",
                                 font=("Helvetica", 16))
        self.category_label.config(text=f"Kategori Berat Badan: {kategori_bmi}",
                                   font=("Helvetica", 16))
        self.calorie_label.config(text=f"Rekomendasi Kalori Harian: {kalori:.0f} kcal",
                                  font=("Helvetica", 16))
    
    def hitung_kalori_harian(self, jenis_kelamin, umur, tinggi_cm, berat_kg, tingkat_aktivitas):
        if jenis_kelamin.lower() == 'pria':
            bmr = 66.47 + (13.75 * berat_kg) + (5.003 * tinggi_cm) - (6.755 * umur)
        else:  # wanita
            bmr = 655.1 + (9.563 * berat_kg) + (1.850 * tinggi_cm) - (4.676 * umur)

        faktor_aktivitas = {
            'sedentari': 1.2,
            'ringan': 1.375,
            'sedang': 1.55,
            'aktif': 1.725,
            'sangat aktif': 1.9
        }

        kalori_harian = bmr * faktor_aktivitas[tingkat_aktivitas.lower()]
        return round(kalori_harian, 2)

    def validate_form(self):
        """Validate form inputs"""
        errors = []
        
        if not self.nama_entry.get().strip():
            errors.append("Nama harus diisi")
        if not self.alamat_entry.get().strip():
            errors.append("Alamat harus diisi")
        if not self.umur_entry.get().strip().isdigit():
            errors.append("Umur harus berupa angka")
        elif int(self.umur_entry.get()) <= 0:
            errors.append("Umur harus lebih dari 0")
        if not self.tinggi_entry.get().strip().isdigit():
            errors.append("Tinggi badan harus berupa angka")
        elif int(self.tinggi_entry.get()) <= 0:
            errors.append("Tinggi badan harus lebih dari 0")
            
        if errors:
            messagebox.showerror("Error Validasi", "\n".join(errors))
            return False
            
        return True
    
    def on_closing(self):
        if self.video_capture is not None:
            self.video_capture.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ObesityDetectionApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()