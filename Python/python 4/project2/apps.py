import tkinter as tk
from tkinter import ttk, messagebox
import cv2
import dlib
import numpy as np
from PIL import Image, ImageTk
from datetime import datetime
import torch
from scripts.model import build_model
from torchvision import transforms

class ObesityDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Deteksi Obesitas")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        # Inisialisasi model face detection
        self.detector = dlib.get_frontal_face_detector()

        # Inisialisasi model
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = build_model()
        self.model.load_state_dict(torch.load('data/model.pth', map_location=self.device))
        self.model.to(self.device)
        self.model.eval()

        # Transformasi gambar
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5], std=[0.5])
        ])

        
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
        
        # Tombol start/stop
        self.start_button = ttk.Button(self.button_frame, 
                                    text="Mulai Deteksi", 
                                    command=self.toggle_detection)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.capture_button = ttk.Button(self.button_frame, 
                                      text="Ambil Foto", 
                                      command=self.capture_image,
                                      state=tk.DISABLED)
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
                                font=('Helvetica', 10),
                                anchor='w')
        self.info_label.pack(fill=tk.X, pady=2)
        
        self.weight_label = tk.Label(self.result_frame, 
                                  text="Perkiraan Berat Badan: -", 
                                  font=('Helvetica', 10),
                                  anchor='w')
        self.weight_label.pack(fill=tk.X, pady=2)
        
        self.category_label = tk.Label(self.result_frame, 
                                    text="Kategori Berat Badan: -", 
                                    font=('Helvetica', 10),
                                    anchor='w')
        self.category_label.pack(fill=tk.X, pady=2)
        
        self.calorie_label = tk.Label(self.result_frame, 
                                    text="Rekomendasi Kalori Harian: -", 
                                    font=('Helvetica', 10),
                                    anchor='w')
        self.calorie_label.pack(fill=tk.X, pady=2)
        
        # Footer
        self.footer_label = tk.Label(self.main_frame, 
                                   text=f"© {datetime.now().year} Aplikasi Deteksi Obesitas - v1.0",
                                   font=('Helvetica', 8),
                                   fg='gray')
        self.footer_label.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')
        
        # Variabel untuk video capture
        self.video_capture = None
        self.detecting = False
        self.face_detected = False
        self.captured_image = None
    
    def toggle_detection(self):
        if not self.detecting:
            self.start_detection()
        else:
            self.stop_detection()
    
    def start_detection(self):
        # Validasi form
        if not self.validate_form():
            return
            
        self.detecting = True
        self.start_button.config(text="Stop Deteksi")
        self.capture_button.config(state=tk.NORMAL)
        self.video_capture = cv2.VideoCapture(0)
        self.update_frame()
    
    def stop_detection(self):
        self.detecting = False
        self.start_button.config(text="Mulai Deteksi")
        self.capture_button.config(state=tk.DISABLED)
        if self.video_capture:
            self.video_capture.release()
        # Reset display
        black_image = Image.new('RGB', (640, 480), (0, 0, 0))
        imgtk = ImageTk.PhotoImage(image=black_image)
        self.video_label.imgtk = imgtk
        self.video_label.configure(image=imgtk)
    
    def capture_image(self):
        if self.detecting and self.face_detected:
            ret, frame = self.video_capture.read()
            if ret:
                # Deteksi wajah
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                faces = self.detector(rgb_frame)

                if len(faces) > 0:
                    face = faces[0]
                    x, y, w, h = face.left(), face.top(), face.width(), face.height()
                    face_img = rgb_frame[y:y+h, x:x+w]
                    face_pil = Image.fromarray(face_img)
                    input_tensor = self.transform(face_pil).unsqueeze(0).to(self.device)

                    with torch.no_grad():
                        bmi_pred = self.model(input_tensor).item()

                    # Estimasi berat badan dari BMI dan tinggi badan (misalnya, tinggi = 1.7 m)
                    height = 1.7  # Anda dapat meminta input tinggi dari pengguna
                    weight = bmi_pred * (height ** 2)

                    self.update_results(weight)
                    messagebox.showinfo("Info", "Foto berhasil diambil dan BMI diprediksi!")

    
    def validate_form(self):
        nama = self.nama_entry.get().strip()
        alamat = self.alamat_entry.get().strip()
        umur = self.umur_entry.get().strip()
        
        if not nama:
            messagebox.showerror("Error", "Nama harus diisi!")
            return False
        if not alamat:
            messagebox.showerror("Error", "Alamat harus diisi!")
            return False
        if not umur or not umur.isdigit():
            messagebox.showerror("Error", "Umur harus angka!")
            return False
            
        return True
    
    def update_frame(self):
        if self.detecting:
            ret, frame = self.video_capture.read()
            if ret:
                # Resize frame agar sesuai dengan box
                frame = cv2.resize(frame, (640, 480))
                
                # Konversi warna dari BGR ke RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Deteksi wajah
                faces = self.detector(rgb_frame)
                
                if len(faces) > 0:
                    self.face_detected = True
                    # Gambar kotak di sekitar wajah
                    for face in faces:
                        x, y, w, h = face.left(), face.top(), face.width(), face.height()
                        cv2.rectangle(rgb_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    
                    # Estimasi berat badan berdasarkan ukuran wajah
                    face_width = faces[0].width()
                    estimated_weight = self.estimate_weight(face_width)
                    
                    # Update UI dengan hasil
                    self.update_results(estimated_weight)
                else:
                    self.face_detected = False
                    self.update_empty_results()
                
                # Konversi frame ke format yang bisa ditampilkan di Tkinter
                img = Image.fromarray(rgb_frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
            
            # Update frame setiap 15 ms
            self.root.after(15, self.update_frame)
    
    def estimate_weight(self, face_width):
        # Estimasi sederhana berdasarkan ukuran wajah
        # Hanya untuk demonstrasi - tidak akurat!
        if face_width > 180:
            return np.random.randint(90, 100)  # >90 kg
        elif face_width > 170:
            return np.random.randint(80, 90)  # 80-89 kg
        elif face_width > 160:
            return np.random.randint(70, 80)  # 70-79 kg
        elif face_width > 150:
            return np.random.randint(60, 70)  # 60-69 kg
        else:
            return np.random.randint(50, 60)  # 50-59 kg
    
    def update_results(self, weight):
        # Update info pasien
        nama = self.nama_entry.get()
        umur = self.umur_entry.get()
        self.info_label.config(text=f"Informasi Pasien: {nama}, {umur} tahun")
        
        # Update label berat badan
        weight_text = f"Perkiraan Berat Badan: {weight} kg"
        self.weight_label.config(text=weight_text)
        
        # Tentukan kategori berat badan
        if weight >= 90:
            category = ">90 kg (Obesitas Tingkat III)"
            calorie_needs = "1500-1800 kkal/hari (Konsultasi dokter diperlukan)"
        elif 80 <= weight <= 89:
            category = "80-89 kg (Obesitas Tingkat II)"
            calorie_needs = "1800-2000 kkal/hari"
        elif 70 <= weight <= 79:
            category = "70-79 kg (Obesitas Tingkat I)"
            calorie_needs = "2000-2200 kkal/hari"
        elif 60 <= weight <= 69:
            category = "60-69 kg (Berat Badan Normal)"
            calorie_needs = "2200-2500 kkal/hari"
        elif 50 <= weight <= 59:
            category = "50-59 kg (Berat Badan Normal)"
            calorie_needs = "2500-2800 kkal/hari"
        else:
            category = "Di bawah 50 kg (Underweight)"
            calorie_needs = "Konsultasi dokter diperlukan"
        
        # Update label kategori dan kalori
        self.category_label.config(text=f"Kategori Berat Badan: {category}")
        self.calorie_label.config(text=f"Rekomendasi Kalori Harian: {calorie_needs}")
    
    def update_empty_results(self):
        self.weight_label.config(text="Perkiraan Berat Badan: -")
        self.category_label.config(text="Kategori Berat Badan: -")
        self.calorie_label.config(text="Rekomendasi Kalori Harian: -")
    
    def on_closing(self):
        if self.video_capture is not None:
            self.video_capture.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ObesityDetectionApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()