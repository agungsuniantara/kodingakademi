// Struct: Membuat tipe data Nasabah yang berisi:
// 1. char nama[50]
// 2. char pin[10]
// 3. int saldo

// String Comparison: Menggunakan strcmp untuk memvalidasi Login (PIN benar/salah).

// Pointer:
// Fungsi transaksi (Setor/Tarik) WAJIB menggunakan parameter pointer (int *saldo).
// Tidak boleh me-return nilai saldo baru, tapi harus mengubah langsung di alamat memori.

// File Handling:
// Mode Read (r): Membaca data nasabah saat program mulai.
// Mode Write (w): Menyimpan update saldo terakhir saat keluar.
// Mode Append (a): Menambahkan catatan riwayat transaksi tanpa menghapus data lama (Fitur Log).

// fitur sistem

// 1. Login System (String & Loop)
// Saat program dimulai, minta user memasukkan PIN.
// Bandingkan input user dengan data di Struct menggunakan strcmp.
// Berikan kesempatan 3x percobaan. Jika salah 3x, program berhenti (Exit).

// 2. Cek Saldo
// Menampilkan nama nasabah dan saldo terakhir.

// 3. Setor Tunai (Deposit) - Lanjutan
// Minta input jumlah uang yang akan disetor.
// Wajib: Gunakan fungsi updateSaldo(int *saldo_asli, int jumlah_tambah) yang menggunakan Pointer.
// Setelah saldo bertambah, simpan catatan ke file riwayat.txt menggunakan mode Append (a).
// Format log: Setor: [jumlah]

// 4. Tarik Tunai (Withdrawal)
// Minta input jumlah uang yang akan ditarik.
// Logika Validasi: Cek apakah saldo cukup. Jika saldo tidak cukup, tampilkan pesan error.
// Jika saldo cukup, gunakan fungsi pointer untuk mengurangi nilai saldo.
// Simpan catatan ke file riwayat.txt menggunakan mode Append (a).
// Format log: Tarik: [jumlah]

// 5. Lihat Riwayat Transaksi (File Reading)
// Program membuka file riwayat.txt dengan mode Read (r).
// Program menampilkan seluruh baris riwayat transaksi yang pernah dilakukan (menggunakan fgets dalam loop).

// 6. Simpan & Keluar
// Program menuliskan saldo terakhir nasabah ke file utama nasabah.txt (Mode w).
// Program berhenti.

#include <stdio.h>
#include <string.h>

// --- KONSTANTA FILE ---
#define FILE_NASABAH "nasabah.txt"
#define FILE_RIWAYAT "riwayat_transaksi.txt"

// --- 1. MATERI STRUCT ---
typedef struct {
    char nama[50];
    char pin[10];
    int saldo;
} Nasabah;

// Variabel Global
Nasabah user;

// --- PROTOTYPE FUNGSI ---
void muatData();
void simpanData();
void catatRiwayat(char *jenis, int nominal);
void lihatRiwayat();
int login();
void setorUang(int *saldo, int nominal); // Wajib pakai Pointer
void tarikUang(int *saldo, int nominal); // Wajib pakai Pointer
void bersihkanEnter(char *str);

// --- MAIN PROGRAM ---
int main() {
    int pilihan, nominal;

    // 1. Load data nasabah
    muatData();

    // 2. Proses Login (Materi String & Loop)
    if (login() == 0) {
        printf("\n[SISTEM] Akses Ditolak. Program Berhenti.\n");
        return 0; 
    }

    // 3. Menu Utama (Control Flow)
    do {
        printf("\n=== ATM BANK C-SECURE ===\n");
        printf("Nasabah: %s\n", user.nama);
        printf("-------------------------\n");
        printf("1. Cek Saldo\n");
        printf("2. Setor Tunai\n");
        printf("3. Tarik Tunai\n");
        printf("4. Lihat Riwayat Transaksi\n");
        printf("5. Keluar & Simpan\n");
        printf("Pilih menu: ");
        scanf("%d", &pilihan);
        getchar(); // Bersihkan buffer enter

        switch (pilihan) {
            case 1:
                printf("\n>>> Sisa Saldo Anda: Rp %d\n", user.saldo);
                break;
            
            case 2:
                printf("Masukkan jumlah setor: Rp ");
                scanf("%d", &nominal);
                if (nominal > 0) {
                    // Panggil fungsi dengan ALAMAT variabel saldo (&)
                    setorUang(&user.saldo, nominal);
                    printf("Setor tunai berhasil!\n");
                } else {
                    printf("Nominal tidak valid.\n");
                }
                break;

            case 3:
                printf("Masukkan jumlah tarik: Rp ");
                scanf("%d", &nominal);
                if (nominal > 0 && nominal <= user.saldo) {
                    // Panggil fungsi dengan ALAMAT variabel saldo (&)
                    tarikUang(&user.saldo, nominal);
                    printf("Penarikan berhasil, silakan ambil uang Anda.\n");
                } else {
                    printf("Transaksi Gagal! Saldo tidak cukup atau nominal salah.\n");
                }
                break;

            case 4:
                lihatRiwayat();
                break;

            case 5:
                simpanData();
                printf("Terima kasih telah menggunakan ATM kami.\n");
                break;

            default:
                printf("Pilihan tidak tersedia.\n");
        }

    } while (pilihan != 5);

    return 0;
}

// --- IMPLEMENTASI FUNGSI ---

// Helper: Membersihkan enter di string (Materi String)
void bersihkanEnter(char *str) {
    int len = strlen(str);
    if (len > 0 && str[len - 1] == '\n') {
        str[len - 1] = '\0';
    }
}

// --- FUNGSI POINTER (Pass by Reference) ---
// Mengubah nilai asli saldo di struct menggunakan pointer
void setorUang(int *saldo, int nominal) {
    *saldo = *saldo + nominal; // Ubah value di alamat memori
    catatRiwayat("Setor Tunai", nominal);
}

void tarikUang(int *saldo, int nominal) {
    *saldo = *saldo - nominal; // Ubah value di alamat memori
    catatRiwayat("Tarik Tunai", nominal);
}

// --- FUNGSI LOGIN ---
int login() {
    char inputPin[10];
    int percobaan = 0;

    printf("\n=== SILAKAN LOGIN ===\n");
    
    while (percobaan < 3) {
        printf("Masukkan PIN: ");
        fgets(inputPin, 10, stdin);
        bersihkanEnter(inputPin);

        // Bandingkan string (strcmp)
        if (strcmp(inputPin, user.pin) == 0) {
            printf("Login Berhasil!\n");
            return 1; // Sukses
        } else {
            printf("PIN Salah!\n");
            percobaan++;
        }
    }
    
    printf("Anda salah memasukkan PIN 3 kali.\n");
    return 0; // Gagal
}

// --- FILE HANDLING: LOAD ---
void muatData() {
    FILE *file = fopen(FILE_NASABAH, "r");
    
    // Jika file tidak ada, buat akun default (Simulasi nasabah baru)
    if (file == NULL) {
        printf("[Info] Data nasabah tidak ditemukan. Membuat akun default...\n");
        strcpy(user.nama, "User Baru");
        strcpy(user.pin, "1234"); // PIN Default
        user.saldo = 0;
        simpanData(); // Simpan agar file terbentuk
        return;
    }

    // Baca 3 baris: Nama, PIN, Saldo
    fgets(user.nama, 50, file);
    bersihkanEnter(user.nama);

    fgets(user.pin, 10, file);
    bersihkanEnter(user.pin);

    fscanf(file, "%d", &user.saldo);
    
    fclose(file);
}

// --- FILE HANDLING: WRITE (Save State) ---
void simpanData() {
    FILE *file = fopen(FILE_NASABAH, "w"); // Mode "w" menimpa data lama
    
    if (file == NULL) {
        printf("Error menyimpan data!\n");
        return;
    }

    fprintf(file, "%s\n", user.nama);
    fprintf(file, "%s\n", user.pin);
    fprintf(file, "%d\n", user.saldo);

    fclose(file);
}

// --- FILE HANDLING: APPEND (Log Transaksi) ---
void catatRiwayat(char *jenis, int nominal) {
    // Mode "a" (append) menambahkan data di akhir file, TIDAK menimpa
    FILE *file = fopen(FILE_RIWAYAT, "a");
    
    if (file == NULL) {
        printf("Gagal mencatat riwayat.\n");
        return;
    }

    // Format log: [Jenis Transaksi] : Rp [Nominal]
    fprintf(file, "%s : Rp %d\n", jenis, nominal);
    
    fclose(file);
}

// --- FILE HANDLING: READ (History) ---
void lihatRiwayat() {
    FILE *file = fopen(FILE_RIWAYAT, "r");
    char buffer[100];

    if (file == NULL) {
        printf("\nBelum ada riwayat transaksi.\n");
        return;
    }

    printf("\n--- RIWAYAT TRANSAKSI ---\n");
    // Loop baca per baris sampai habis
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }
    printf("-------------------------\n");

    fclose(file);
}
