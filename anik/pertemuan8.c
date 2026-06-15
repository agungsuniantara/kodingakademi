#include <stdio.h>

// file handling = metode untuk menyimpan data ke dalam file eksternal

int main(){
    // w = write, membuat file baru atau menimpa file lama
    // r = read, membaca file
    // a = append, menambahkan data di akhir file

    // fopen() = fungsi untuk membuka file
    // fwrite() = fungsi untuk menulis ke file
    // fread() = fungsi untuk membaca dari file
    // fclose() = fungsi untuk menutup file
    // fprintf() = fungsi untuk menulis ke file dengan format

    FILE *file;
    file = fopen("data.txt", "a"); // membuka file dengan mode write ( menulis )

    if (file == NULL) {
        printf("gagal membuka file \n");
        return 1; // keluar dari program dengan kode error
    }

    fprintf(file, "nama : anik \n");
    fprintf(file, "alamat : denpasar \n");
    fprintf(file, "umur : 20 \n");

    fclose(file); // menutup file

    // membaca file

    FILE *baca;

    baca = fopen("data.txt", "r"); // membuka file dengan mode read ( membaca )

    printf("isi biodata : \n");

    char buffer[100]; // untuk menyimpan data yang dibaca dari file

    while (fgets(buffer, sizeof(buffer), baca)) { // membaca file baris per baris
        printf("%s", buffer); // menampilkan isi file
    }
    fclose(baca); // menutup file

    // menambahkan data ke file

    FILE *tambah;
    tambah = fopen("data.txt", "a"); // membuka file dengan mode append ( menambahkan )

    fprintf(tambah, "nama : agung \n");
    fprintf(tambah, "alamat : denpasar \n");
    fprintf(tambah, "umur : 27 \n");

    fclose(tambah); // menutup file

    // assignment

    int pilihan;
    char nama[100], kota[100];
    int umur;

    FILE *data;

    while (1) {
        printf("=== SISTEM PENCATATAN BUKU TAMU === \n");
        printf("1. Buat File Baru \n");
        printf("2. Tambah Data Tamu \n");
        printf("3. Lihat Data Tamu \n");
        printf("4. Keluar \n");
        printf("pilihan Anda : ");
        scanf("%d", &pilihan);

        if (pilihan == 1){
            data = fopen("data_tamu.txt", "w");
            if (data == NULL) {
                printf("gagal membuat file \n");
                return 1; // keluar dari program dengan kode error
            }
            printf("file berhasil dibuat \n");
            fclose(data);
        }
        else if (pilihan == 2){
            data = fopen("data_tamu.txt", "a");
            if (data == NULL) {
                printf("gagal membuka file \n");
                return 1; // keluar dari program dengan kode error
            }
            printf("masukkan nama tamu : ");
            scanf("%s", nama);
            printf("masukkan kota asal tamu : ");
            scanf("%s", kota);
            printf("masukkan umur tamu : ");
            scanf("%d", &umur);

            fprintf(data, "nama : %s \n", nama);
            fprintf(data, "kota asal : %s \n", kota);
            fprintf(data, "umur : %d \n", umur);
            fprintf(data, "------------------------- \n");

            fclose(data);
        }
        else if (pilihan == 3){
            data = fopen("data_tamu.txt", "r");
            if (data == NULL) {
                printf("gagal membuka file \n");
                return 1; // keluar dari program dengan kode error
            }
            printf("=== DATA TAMU === \n");
            char buffer[100];
            while (fgets(buffer, sizeof(buffer), data)) {
                printf("%s", buffer);
            }
            fclose(data);
        }
        else if (pilihan == 4){
            printf("terima kasih telah menggunakan program ini \n");
            break; // keluar dari loop
        }
        else {
            printf("pilihan tidak valid \n");
        }
    }
}