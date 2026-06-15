#include <stdio.h> 
#include <stdlib.h>

int main(){
    // assignment 1
    // Buat program untuk mencatat daftar belanjaan.
    // Minta user menginput jumlah barang yang ingin dibeli.
    // Lakukan looping sebanyak jumlah tersebut untuk menginput Nama Barang.
    // Simpan setiap barang ke dalam file belanja.txt.
    // Syarat: Setiap barang harus berada di baris baru (gunakan \n).

    FILE *filePtr;
    filePtr = fopen("belanja.txt", "w");

    if (filePtr == NULL){
        printf("Gagal membuka file.\n");
        return 1;
    }

    int jumlah_barang;
    printf("Masukkan jumlah barang yang ingin dibeli: ");
    scanf("%d", &jumlah_barang);

    for (int i = 0; i < jumlah_barang; i++){
        char nama_barang[100];
        printf("Masukkan nama barang ke-%d: ", i+1);
        scanf("%s", nama_barang);
        fprintf(filePtr, "%s\n", nama_barang);
    }

    fclose(filePtr);

    // assignment 2

    // Buat program buku tamu digital.
    // Minta user memasukkan Nama Pengunjung.
    // Simpan nama tersebut ke file tamu.txt.
    // Gunakan mode Append ("a") agar jika program dijalankan lagi, nama pengunjung sebelumnya tidak hilang.

    FILE *filePtr2;
    filePtr2 = fopen("tamu.txt", "a");

    if (filePtr2 == NULL){
        printf("Gagal membuka file tamu.txt.\n");
        return 1;
    }

    char nama_pengunjung[100];
    printf("Masukkan nama pengunjung: ");
    scanf("%s", nama_pengunjung);
    fprintf(filePtr2, "%s\n", nama_pengunjung);

    fclose(filePtr2);

    // assignment 3

    // Membaca file yang isinya HANYA ANGKA, lalu melakukan perhitungan matematika.
    // Buat file manual bernama nilai_siswa.txt yang isinya beberapa angka (misal: 80, 90, 75, 85).
    // Buat program C untuk membaca file tersebut, lalu:
    // Hitung Rata-rata nilai.
    // Hitung berapa siswa yang LULUS (Nilai >= 70).
    // Hitung berapa siswa yang REMEDIAL (Nilai < 70).
    // output : 
    // Rata-rata Kelas : 70.0
    // Jumlah Lulus    : 3 Siswa
    // Jumlah Remedial : 2 Siswa

    FILE *fileptr3;
    fileptr3 = fopen("nilai_siswa.txt", "w");
    if (fileptr3 == NULL){
        printf("gagal membuka file.\n");
        return 1;
    }

    fprintf(fileptr3, "80\n");
    fprintf(fileptr3, "90\n");
    fprintf(fileptr3, "75\n");
    fprintf(fileptr3, "85\n");

    fclose(fileptr3);

    FILE *baca;
    char membaca[100];
    float jumlah_nilai = 0;
    int count = 0;
    int lulus = 0;
    int remedial = 0;
    baca = fopen("nilai_siswa.txt", "r"); 
    while(fgets(membaca, sizeof(membaca), baca) != NULL){
        int nilai = atoi(membaca);
        jumlah_nilai += nilai;
        count++;
        if (nilai >= 70){
            lulus++;
        } else {
            remedial++;
        }
    }

    float rata_nilai = jumlah_nilai / count;
    printf("Rata-rata Kelas : %.1f\n", rata_nilai);
    printf("Jumlah Lulus    : %d Siswa\n", lulus);
    printf("Jumlah Remedial : %d Siswa\n", remedial);
    fclose(baca);
    return 0;
}