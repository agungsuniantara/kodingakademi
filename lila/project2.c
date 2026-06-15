#include <stdio.h>
#include <string.h> // Untuk system("cls") jika di Windows

// --- DEFINISI KONSTANTA ---
#define MAX_BARANG 100
#define NAMA_FILE "data_gudang.txt"

// --- 1. MATERI STRUCT (Tipe Data Bentukan) ---
typedef struct {
    char nama[50];
    int harga;
    int stok;
} Barang;

// Variabel Global
Barang gudang[MAX_BARANG];
int jumlahItem = 0;

// --- PROTOTYPE FUNGSI ---
void muatData();
void simpanData();
void tambahBarang();
void lihatBarang();
void cariBarang();
void urutkanBarang(); 
void tukar_pointer(Barang *a, Barang *b); 
void bersihkanEnter(char *str); // Helper untuk string

// --- PROGRAM UTAMA ---
int main() {
    int pilihan;

    // Load data lama dari file saat program dibuka
    muatData();

    // --- 2. MATERI CONTROL FLOW (Do-While) ---
    do {
        printf("\n=== APLIKASI GUDANG ===\n");
        printf("1. Tambah Barang\n");
        printf("2. Lihat Stok Barang\n");
        printf("3. Cari Barang (Search)\n");
        printf("4. Urutkan Barang (Sort Harga)\n");
        printf("5. Simpan & Keluar\n");
        printf("-----------------------\n");
        printf("Pilih menu: ");
        scanf("%d", &pilihan);

        // Membersihkan buffer keyboard setelah scanf angka
        // Agar fgets di menu lain tidak error
        getchar(); 

        switch (pilihan) {
            case 1:
                tambahBarang();
                break;
            case 2:
                lihatBarang();
                break;
            case 3:
                cariBarang();
                break;
            case 4:
                urutkanBarang();
                break;
            case 5:
                simpanData();
                printf("Terima kasih! Sampai jumpa.\n");
                break;
            default:
                printf("Pilihan tidak valid.\n");
        }

    } while (pilihan != 5);

    return 0;
}

// --- IMPLEMENTASI FUNGSI ---

// Helper: Menghapus enter (\n) di akhir string (Materi String & Array)
void bersihkanEnter(char *str) {
    int panjang = strlen(str);
    // Cek karakter terakhir, jika enter, ganti dengan Null (\0)
    if (panjang > 0 && str[panjang - 1] == '\n') {
        str[panjang - 1] = '\0';
    }
}

// --- 3. MATERI FILE HANDLING (Read) ---
void muatData() {
    FILE *file = fopen(NAMA_FILE, "r");
    
    // Jika file belum ada, biarkan saja
    if (file == NULL) {
        printf("[Info] File database baru akan dibuat saat Anda menyimpan.\n");
        return;
    }

    jumlahItem = 0;

    // Loop membaca file
    // Logika: Kita baca Nama dulu pakai fgets. Jika berhasil, lanjut baca Harga & Stok.
    while (fgets(gudang[jumlahItem].nama, 50, file) != NULL) {
        
        // 1. Bersihkan enter di nama yang terbawa fgets
        bersihkanEnter(gudang[jumlahItem].nama);

        // 2. Baca Harga (Baris kedua)
        fscanf(file, "%d", &gudang[jumlahItem].harga);

        // 3. Baca Stok (Baris ketiga)
        fscanf(file, "%d", &gudang[jumlahItem].stok);

        // 4. PENTING: Bersihkan sisa enter setelah membaca angka stok
        // Agar fgets di putaran berikutnya tidak membaca enter kosong
        fgetc(file);

        jumlahItem++;
    }

    fclose(file);
}

// --- 3. MATERI FILE HANDLING (Write) ---
void simpanData() {
    FILE *file = fopen(NAMA_FILE, "w"); // Mode "w" menimpa file lama
    
    if (file == NULL) {
        printf("Error: Tidak bisa menyimpan file.\n");
        return;
    }

    for (int i = 0; i < jumlahItem; i++) {
        // Simpan dengan format 3 baris per barang agar rapi
        fprintf(file, "%s\n", gudang[i].nama);
        fprintf(file, "%d\n", gudang[i].harga);
        fprintf(file, "%d\n", gudang[i].stok);
    }

    fclose(file);
    printf("[Sukses] Data berhasil disimpan ke %s\n", NAMA_FILE);
}

// --- 4. MATERI ARRAY & INPUT ---
void tambahBarang() {
    if (jumlahItem >= MAX_BARANG) {
        printf("Gudang Penuh!\n");
        return;
    }

    printf("\n--- INPUT BARANG BARU ---\n");
    
    printf("Nama Barang: ");
    // Menggunakan fgets agar bisa spasi (Materi Input String)
    fgets(gudang[jumlahItem].nama, 50, stdin);
    bersihkanEnter(gudang[jumlahItem].nama);

    printf("Harga (Rp): ");
    scanf("%d", &gudang[jumlahItem].harga);

    printf("Stok Awal: ");
    scanf("%d", &gudang[jumlahItem].stok);

    jumlahItem++;
    printf("Barang berhasil ditambahkan!\n");
}

void lihatBarang() {
    if (jumlahItem == 0) {
        printf("\nData kosong.\n");
        return;
    }

    printf("\n%-3s | %-20s | %-12s | %-5s\n", "No", "Nama Barang", "Harga", "Stok");
    printf("----------------------------------------------------\n");
    
    for (int i = 0; i < jumlahItem; i++) {
        printf("%-3d | %-20s | Rp%-10d | %-5d\n", 
            i + 1, 
            gudang[i].nama, 
            gudang[i].harga, 
            gudang[i].stok);
    }
}

// --- 5. MATERI ALGORITMA (Linear Search) ---
void cariBarang() {
    char dicari[50];
    int ditemukan = 0;

    printf("\nMasukkan nama barang: ");
    fgets(dicari, 50, stdin);
    bersihkanEnter(dicari); // Hapus enter agar pencarian valid

    printf("\nHasil Pencarian:\n");
    for (int i = 0; i < jumlahItem; i++) {
        // Menggunakan strcmp (Materi String)
        // Jika hasilnya 0, berarti sama persis
        if (strcmp(gudang[i].nama, dicari) == 0) {
            printf("- Ditemukan: %s | Harga: %d | Stok: %d\n", 
            gudang[i].nama, gudang[i].harga, gudang[i].stok);
            ditemukan = 1;
        }
    }

    if (ditemukan == 0) {
        printf("Barang '%s' tidak ditemukan.\n", dicari);
    }
}

// --- 6. MATERI POINTER (Pass by Reference) ---
// Fungsi ini menukar isi data struct langsung di alamat memorinya
void tukar_pointer(Barang *a, Barang *b) {
    Barang temp;
    temp = *a; // Salin isi alamat a ke temp
    *a = *b;   // Isi alamat a ditimpa isi alamat b
    *b = temp; // Isi alamat b ditimpa temp
}

// --- 7. MATERI ALGORITMA (Bubble Sort) ---
void urutkanBarang() {
    // Mengurutkan berdasarkan Harga (Termurah ke Termahal)
    
    for (int i = 0; i < jumlahItem - 1; i++) {
        for (int j = 0; j < jumlahItem - i - 1; j++) {
            
            // Jika harga barang sekarang lebih mahal dari barang depannya
            if (gudang[j].harga > gudang[j+1].harga) {
                // Tukar posisi menggunakan Pointer
                tukar_pointer(&gudang[j], &gudang[j+1]);
            }
        }
    }
    printf("\nBarang telah diurutkan berdasarkan harga!\n");
    lihatBarang(); // Langsung tampilkan hasilnya
}