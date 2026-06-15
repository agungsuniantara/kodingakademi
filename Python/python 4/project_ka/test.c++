#include "HX711.h"

// --- KONFIGURASI PIN SENSOR ---
const int trigPin = 9;
const int echoPin = 10;
const int loadcell_DT = 4;
const int loadcell_SCK = 5;

// Konstanta panjang maksimal papan pengukur (misal 100 cm)
// Jarak ultrasonik ke telapak kaki bayi akan dikurangi dari nilai ini
const float PANJANG_PAPAN = 100.0; 

HX711 scale;

// --- 1. MENYIMPAN DATA TABEL (DATABASE MINI) ---
// Membuat struktur data untuk menyimpan nilai M dan S
struct DataWHO {
  float M;
  float S;
};

// Array untuk umur 0, 1, dan 2 bulan (Index array mewakili umur dalam bulan)
DataWHO dataLaki[3] = {
  {49.8842, 0.03795}, // Umur 0
  {54.7244, 0.03557}, // Umur 1
  {58.4249, 0.03424}  // Umur 2
};

DataWHO dataPerempuan[3] = {
  {49.1477, 0.03790}, // Umur 0
  {53.6872, 0.03640}, // Umur 1
  {57.0673, 0.03568}  // Umur 2
};

void setup() {
  Serial.begin(9600);
  
  // Setup Ultrasonik
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  // Setup Loadcell
  scale.begin(loadcell_DT, loadcell_SCK);
  // Masukkan faktor kalibrasi loadcell Anda di sini
  scale.set_scale(2280.f); 
  scale.tare(); // Reset timbangan ke 0
  
  Serial.println("Sistem Pengukur Stunting Otomatis Siap!");
  Serial.println("---------------------------------------");
}

// --- 2. FUNGSI UNTUK MENGHITUNG Z-SCORE DAN STATUS GIZI ---
void cekStunting(char jenis_kelamin, int umur, float panjang_bayi) {
  // Cek apakah umur ada di database kita (0-2 bulan)
  if (umur < 0 || umur > 2) {
    Serial.println("Error: Data umur belum tersedia di sistem.");
    return;
  }

  float nilai_M = 0.0;
  float nilai_S = 0.0;

  // Memilih database berdasarkan jenis kelamin
  if (jenis_kelamin == 'L' || jenis_kelamin == 'l') {
    nilai_M = dataLaki[umur].M;
    nilai_S = dataLaki[umur].S;
  } else if (jenis_kelamin == 'P' || jenis_kelamin == 'p') {
    nilai_M = dataPerempuan[umur].M;
    nilai_S = dataPerempuan[umur].S;
  } else {
    Serial.println("Error: Jenis kelamin tidak valid.");
    return;
  }

  // Menghitung Z-Score: Z = ((X / M) - 1) / S
  float z_score = ((panjang_bayi / nilai_M) - 1.0) / nilai_S;

  // Menentukan Status
  String status = "";
  if (z_score < -3.0) {
    status = "Sangat Pendek (Severely Stunted)";
  } else if (z_score < -2.0) {
    status = "Pendek (Stunting)";
  } else {
    status = "Normal";
  }

  // Menampilkan Hasil
  Serial.print("Nilai Z-Score : ");
  Serial.println(z_score, 2); // Print dengan 2 angka di belakang koma
  Serial.print("Status Gizi   : ");
  Serial.println(status);
}

// Fungsi pembantu untuk membaca Ultrasonik
float bacaPanjangBayi() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  long duration = pulseIn(echoPin, HIGH);
  float distance = duration * 0.034 / 2; // Menghitung jarak dalam cm
  
  // Panjang bayi = Panjang total alat - Jarak dari atas kepala ke kaki
  float panjang_bayi = PANJANG_PAPAN - distance; 
  return panjang_bayi;
}

void loop() {
  // --- SIMULASI INPUT DATA (Bisa diganti dengan keypad/Bluetooth) ---
  // Untuk contoh ini, kita asumsikan (Hardcode): Laki-laki, Umur 1 bulan
  char jk_input = 'L';
  int umur_input = 1;

  // --- 3. MEMBACA SENSOR ---
  float panjang_terukur = bacaPanjangBayi();
  float berat_terukur = scale.get_units(5); // Rata-rata dari 5 pembacaan

  // --- 4. MENAMPILKAN DATA KE SERIAL MONITOR ---
  Serial.println("\n--- Data Pasien Baru ---");
  Serial.print("Jenis Kelamin : "); Serial.println(jk_input);
  Serial.print("Umur (Bulan)  : "); Serial.println(umur_input);
  Serial.print("Berat Badan   : "); Serial.print(berat_terukur, 2); Serial.println(" kg");
  Serial.print("Panjang Badan : "); Serial.print(panjang_terukur, 1); Serial.println(" cm");
  
  // --- 5. PROSES KALKULASI ---
  cekStunting(jk_input, umur_input, panjang_terukur);

  // Tunggu 5 detik sebelum pengukuran berikutnya
  delay(5000); 
}