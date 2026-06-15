// 1. Struct & Array:
//      Menu: Menyimpan ID, Nama Makanan, Harga.
//      Keranjang: Array of Struct untuk menyimpan apa saja yang dipesan user sementara waktu sebelum bayar.
// 2. Pointer (Pass by Reference):
//      Fungsi hitung biaya harus menggunakan pointer: void hitungBiaya(int subtotal, int *pajak, int *total_akhir).
//      Fungsi ini tidak me-return nilai, tapi mengisi variabel pajak dan total akhir di main.
// 3. String Formatting: 
//      Menggunakan format specifier canggih seperti %-20s (rata kiri) dan %10d (rata kanan) agar struk rapi.
// 4. File Handling (Write):
//      Membuat file struk_pembayaran.txt yang berisi detail pesanan.

// fitur
// 1. Daftar Menu (Hardcoded / File)
//      Tampilkan daftar menu makanan yang tersedia.
//      Contoh:
//          Nasi Goreng (Rp 15.000)
//          Ayam Bakar (Rp 20.000)
//          Es Teh Manis (Rp 5.000)
// 2. Tambah Pesanan (Input Loop)
//      User memilih nomor menu dan memasukkan Jumlah (Qty).
//      Simpan pesanan ke dalam Array Keranjang.
//      Tanya user: "Tambah pesanan lain? (y/n)".
//      Jika 'y', ulangi loop. Jika 'n', lanjut ke pembayaran.
// 3. Hitung Total (Pointer Logic)
//      Jumlahkan semua (harga * qty) menjadi Subtotal.
//      Panggil fungsi pointer hitungBiaya.
//      Di dalam fungsi:
//          Hitung *pajak = subtotal * 0.10 (10%).
//          Hitung *total_akhir = subtotal + *pajak.
// 4. Cetak Struk (File Output)
//      Buat file struk_pembayaran.txt.
//      Gunakan fprintf untuk menulis header, daftar item, garis pemisah, dan total.
//      Wajib Rapi: Nama barang dan Harga harus lurus vertikal.

/**
 * FINAL PROJECT 5: SISTEM KASIR & CETAK STRUK
 * 
 * Fitur Utama:
 * 1. Struct & Array (Menampung pesanan di keranjang)
 * 2. Pointer Pass-by-Reference (Menghitung Pajak & Total)
 * 3. Formatted File Output (Membuat struk .txt yang rapi)
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h> // Untuk system("cls")

// --- KONSTANTA ---
#define MAX_PESANAN 100
#define NAMA_FILE_STRUK "struk_pembayaran.txt"
#define PPN 0.10 // Pajak 10%

// --- STRUCT DATA ---
// Struct ini mewakili satu item yang masuk ke keranjang belanja
typedef struct {
    char namaMakanan[50];
    int hargaSatuan;
    int jumlah;
    int totalHargaItem; // hargaSatuan * jumlah
} Pesanan;

// --- PROTOTYPE FUNGSI ---
void tampilkanMenu();
void bersihkanBuffer();
void hitungBiaya(int subtotal, int *pajak, int *totalAkhir);
void cetakStruk(Pesanan keranjang[], int jumlahItem, int subtotal, int pajak, int totalAkhir);

// --- PROGRAM UTAMA ---
int main() {
    // Variabel Keranjang Belanja
    Pesanan keranjang[MAX_PESANAN];
    int jumlahItemDiKeranjang = 0;
    
    // Variabel Loop & Input
    int pilihanMenu;
    int inputQty;
    char lanjutPesan = 'y';
    
    // Variabel Keuangan
    int subtotal = 0;
    int pajak = 0;
    int totalAkhir = 0;

    // --- MULAI PROSES PEMESANAN ---
    do {
        // Bersihkan layar (Opsional, agar rapi)
        // system("cls"); // Hapus komentar ini jika di Windows
        
        printf("\n=== SELAMAT DATANG DI RESTORAN LEZAT MANTAP ===\n");
        tampilkanMenu();
        
        printf("\nMasukkan Nomor Menu yang dipilih: ");
        scanf("%d", &pilihanMenu);
        
        // Validasi input menu
        if (pilihanMenu < 1 || pilihanMenu > 4) {
            printf("[!] Menu tidak tersedia. Silakan pilih lagi.\n");
            continue; // Ulangi loop
        }

        printf("Masukkan Jumlah Pesanan (Qty): ");
        scanf("%d", &inputQty);

        // Validasi jumlah tidak boleh 0 atau negatif
        if (inputQty <= 0) {
            printf("[!] Jumlah harus lebih dari 0.\n");
            continue;
        }

        // --- PROSES MEMASUKKAN KE ARRAY (KERANJANG) ---
        // Mengisi data berdasarkan pilihan menu
        // Index array saat ini adalah 'jumlahItemDiKeranjang'
        
        if (pilihanMenu == 1) {
            strcpy(keranjang[jumlahItemDiKeranjang].namaMakanan, "Nasi Goreng Spesial");
            keranjang[jumlahItemDiKeranjang].hargaSatuan = 25000;
        } 
        else if (pilihanMenu == 2) {
            strcpy(keranjang[jumlahItemDiKeranjang].namaMakanan, "Ayam Bakar Madu");
            keranjang[jumlahItemDiKeranjang].hargaSatuan = 30000;
        } 
        else if (pilihanMenu == 3) {
            strcpy(keranjang[jumlahItemDiKeranjang].namaMakanan, "Mie Goreng Seafood");
            keranjang[jumlahItemDiKeranjang].hargaSatuan = 28000;
        } 
        else if (pilihanMenu == 4) {
            strcpy(keranjang[jumlahItemDiKeranjang].namaMakanan, "Es Teh Manis Jumbo");
            keranjang[jumlahItemDiKeranjang].hargaSatuan = 5000;
        }

        // Simpan jumlah qty
        keranjang[jumlahItemDiKeranjang].jumlah = inputQty;

        // Hitung total harga per item ini
        keranjang[jumlahItemDiKeranjang].totalHargaItem = keranjang[jumlahItemDiKeranjang].hargaSatuan * inputQty;

        // Tambahkan ke subtotal belanjaan sementara
        subtotal = subtotal + keranjang[jumlahItemDiKeranjang].totalHargaItem;

        // Geser index array untuk item berikutnya
        jumlahItemDiKeranjang++;
        
        printf(">> Berhasil menambahkan ke keranjang.\n");

        // --- KONFIRMASI LANJUT ---
        printf("\nApakah ingin memesan lagi? (y/n): ");
        bersihkanBuffer(); // Membersihkan sisa enter dari scanf sebelumnya
        scanf("%c", &lanjutPesan);

    } while (lanjutPesan == 'y' || lanjutPesan == 'Y');

    // --- HITUNG FINAL (MENGGUNAKAN POINTER) ---
    // Kita mengirim ALAMAT memori (&) dari variabel pajak dan totalAkhir
    // agar fungsi bisa mengubah isinya secara langsung.
    hitungBiaya(subtotal, &pajak, &totalAkhir);

    // --- TAMPILKAN RINGKASAN DI LAYAR ---
    printf("\n--------------------------------\n");
    printf("Total Pesanan: %d Item\n", jumlahItemDiKeranjang);
    printf("Subtotal     : Rp %d\n", subtotal);
    printf("Pajak (10%%)  : Rp %d\n", pajak);
    printf("TOTAL BAYAR  : Rp %d\n", totalAkhir);
    printf("--------------------------------\n");

    // --- CETAK STRUK KE FILE ---
    printf("\n[Sedang mencetak struk...]\n");
    cetakStruk(keranjang, jumlahItemDiKeranjang, subtotal, pajak, totalAkhir);
    
    return 0;
}

// --- IMPLEMENTASI FUNGSI ---

void tampilkanMenu() {
    printf("1. Nasi Goreng Spesial  - Rp 25.000\n");
    printf("2. Ayam Bakar Madu      - Rp 30.000\n");
    printf("3. Mie Goreng Seafood   - Rp 28.000\n");
    printf("4. Es Teh Manis Jumbo   - Rp  5.000\n");
}

// Fungsi Helper untuk membersihkan buffer keyboard
void bersihkanBuffer() {
    int c;
    // Loop membuang karakter sampai ketemu Enter (\n) atau End of File
    while ((c = getchar()) != '\n' && c != EOF) { 
        // Tidak melakukan apa-apa, hanya membuang karakter
    }
}

// --- LOGIKA MATEMATIKA DENGAN POINTER ---
void hitungBiaya(int subtotal, int *pajak, int *totalAkhir) {
    // Menghitung pajak 10% dari subtotal
    // Menggunakan cast (int) agar hasil bulat
    *pajak = (int)(subtotal * PPN);

    // Menghitung Total Akhir
    *totalAkhir = subtotal + *pajak;
}

// --- LOGIKA FILE HANDLING & FORMATTING ---
void cetakStruk(Pesanan keranjang[], int jumlahItem, int subtotal, int pajak, int totalAkhir) {
    // Membuka file untuk ditulis (Mode "w")
    FILE *file = fopen(NAMA_FILE_STRUK, "w");

    // Cek apakah file berhasil dibuat
    if (file == NULL) {
        printf("Error: Gagal membuat file struk.\n");
        return;
    }

    // --- HEADER STRUK ---
    fprintf(file, "======================================\n");
    fprintf(file, "        RESTORAN LEZAT MANTAP         \n");
    fprintf(file, "       Jl. Algoritma No. 1 Code       \n");
    fprintf(file, "======================================\n");
    
    // Header Kolom
    // %-20s : String rata kiri, lebar 20 karakter
    // %5s   : String rata kanan, lebar 5 karakter
    // %10s  : String rata kanan, lebar 10 karakter
    fprintf(file, "%-20s %5s %10s\n", "ITEM", "QTY", "SUBTOTAL");
    fprintf(file, "--------------------------------------\n");

    // --- ISI STRUK (LOOP ARRAY) ---
    for (int i = 0; i < jumlahItem; i++) {
        fprintf(file, "%-20s %5d %10d\n", 
            keranjang[i].namaMakanan, 
            keranjang[i].jumlah, 
            keranjang[i].totalHargaItem
        );
    }

    fprintf(file, "--------------------------------------\n");
    
    // --- FOOTER STRUK (TOTAL) ---
    fprintf(file, "%-26s Rp %8d\n", "Subtotal", subtotal);
    fprintf(file, "%-26s Rp %8d\n", "Pajak (10%)", pajak);
    fprintf(file, "--------------------------------------\n");
    fprintf(file, "%-26s Rp %8d\n", "GRAND TOTAL", totalAkhir);
    fprintf(file, "======================================\n");
    fprintf(file, "      TERIMA KASIH KUNJUNGANNYA       \n");
    fprintf(file, "======================================\n");

    // Menutup file agar data tersimpan permanen
    fclose(file);

    printf("[Sukses] Struk telah dicetak ke file '%s'\n", NAMA_FILE_STRUK);
}