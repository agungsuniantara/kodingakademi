#include <stdio.h>

int main(){

    // w = write, membuat file baru atau menimpa file lama
    // r = read, membaca file
    // a = append, menambahkan data di akhir file

    // fopen() = fungsi untuk membuka file
    // fwrite() = fungsi untuk menulis ke file
    // fread() = fungsi untuk membaca dari file
    // fclose() = fungsi untuk menutup file
    // fprintf() = fungsi untuk menulis ke file dengan format

    // membuat file
    FILE *filePtr;

    filePtr = fopen("data.txt", "w"); // membuka / membuat file data.txt untuk ditulis

    if (filePtr == NULL){
        printf("Gagal membuka file.\n");
        return 1; // keluar dari program dengan kode error 1
    }

    fprintf(filePtr, "Nama : lila\n");
    fprintf(filePtr, "Umur : 25\n");
    fprintf(filePtr, "Kota : Jakarta\n");

    fclose(filePtr); // menutup file

    // membaca file
    FILE *baca;

    baca = fopen("data.txt", "r"); // membuka file data.txt untuk dibaca

    printf("isi biodata telah ditulis ke file data.txt\n");

    char buffer[100];

    // fgets(buffer, sizeof(buffer), baca); 
    // printf("%s \n", buffer);
    // fgets(buffer, sizeof(buffer), baca); 
    // printf("%s \n", buffer);

    while (fgets(buffer, sizeof(buffer), baca) != NULL){
        printf("%s", buffer);
    }   

    fclose(baca); // menutup file

    return 0;
}