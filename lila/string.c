#include <stdio.h>
#include <string.h>

int main(){
    char nama[10] = "Budi"; // ["B", "u", "d", "i", "\0"]

    // char copy_nama[10] = nama; // salah karena array tidak bisa diassign langsung

    int total = 0;
    for (int i = 0; nama[i] != '\0'; i++){
        total++;
    }
    printf("Panjang nama: %d\n", total); // cara panjang string manual

    // strlen (digunakan untuk menghitung panjang string)
    int panjang = strlen(nama);
    printf("Panjang nama menggunakan strlen: %d\n", panjang);

    // strcpy(digunakan untuk menyalin string)
    char copy_nama[10];
    strcpy(copy_nama, nama); // (tujuan, sumber)
    printf("copy_nama: %s\n", copy_nama);

    // strcmp(digunakan untuk membandingkan string)
    char nama2[10] = "Budi";
    int hasil = strcmp(nama, nama2); // (string1, string2)
    if (hasil == 0){
        printf("nama dan nama2 sama\n");
    } else {
        printf("nama dan nama2 berbeda\n");
    }

    // strcat(digunakan untuk menggabungkan string)
    char teks[20] = "Hello, ";
    strcat(teks, nama); // (tujuan, sumber)
    printf("salam: %s\n", teks);

    // studi kasus 

    char username[20];
    char password[20];

    printf("Masukkan username: ");
    scanf("%s", username);

    printf("Masukkan password: ");
    scanf("%s", password);

    if (strcmp(username, "admin") == 0 && strcmp(password, "password123") == 0){
        printf("Login berhasil!\n");
    } else if (strcmp(username, "user") == 0 && strcmp(password, "user123") == 0){
        printf("Login berhasil sebagai user!\n");
    } else {
        printf("Login gagal!\n");
    }

    // assignment

    // Buat program yang meminta input kalimat, lalu hitung ada berapa huruf vokal (a, i, u, e, o) di dalamnya.
    // Hint: Gunakan Array Loop + If (kata[i] == 'a' || kata[i] == 'i' ...)

    // asignment 2

    // Buat program yang meminta input kata, lalu menampilkannya secara terbalik.
    // Input: "KASUR"
    // Output: "RUSAK"
    // Hint: Gunakan Loop for mundur, dimulai dari strlen(kata) - 1 sampai 0.

    char kata[100];
    printf("Masukkan sebuah kata: ");
    scanf("%s", kata);

    int len = strlen(kata);
    printf("Kata terbalik: ");
    for (int i = len - 1; i >= 0; i--){
        printf("%c", kata[i]);
    }

    // assignment 3

    // buat program untuk berapa jumlah huruf konsonan dalam sebuah kalimat.

    // assignment 4

    // buat program untuk mengganti kalimat dengan format tertentu.
    // contoh: ganti semua huruf 'a' menjadi 'o' dalam kalimat

    return 0;
}