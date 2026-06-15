#include <stdio.h>
#include <string.h>

int main(){
    char nama[10] = "Budi"; // ["B", "u", "d", "i", "\0"]

    // copy manual pakai looping
    char copy[10];
    for (int i = 0; i < 5; i++){
        copy[i] = nama[i];
    }
    printf("isi copy = %s \n", copy);

    // copy pakai strcpy
    char copy2[10];
    strcpy(copy2, nama);
    printf("isi copy pakai fungsi strcpy = %s \n", copy2);

    // cek panjang string (strlen)

    int panjang = strlen(nama);
    printf("Panjang nama : %d \n", panjang);

    // membandingkan string (strcmp)

    char nama2[10] = "Budi";
    int hasil = strcmp(nama, nama2);
    
    if (hasil == 0){
        printf("nama dan nama2 sama \n");
    }
    else{
        printf("nama dan nama2 berbeda \n");
    }

    // menggabungkan string (strcat)

    char teks[20] = "Hello, ";
    strcat(teks, nama);
    printf("salam: %s\n", teks);

    // studi kasus

    char username[20];
    char password[20];

    printf("Masukkan username : ");
    scanf("%s", username);

    printf("Masukkan password : ");
    scanf("%s", password);

    if ( strcmp(username, "admin") == 0 && strcmp(password, "password123") == 0 ){
        printf("Login berhasil ! \n");
    }
    else if ( strcmp(username, "user") == 0 && strcmp(password, "user123") == 0 ){
        printf("Login berhasil sebagai user ! \n");
    }
    else{
        printf("Login gagal ! \n");
    }

    // assignment 1

    // Buat program yang meminta input kalimat, lalu hitung ada berapa huruf vokal (a, i, u, e, o) di dalamnya.
    // Hint: Gunakan Array Loop + If (kata[i] == 'a' || kata[i] == 'i' ...)

    char kalimat[100];
    int vokal = 0;

    printf("Masukkan kalimat : ");
    scanf("%s", kalimat);

    for (int i = 0; i < strlen(kalimat); i++){
        if (kalimat[i] == 'a' || kalimat[i] == 'i' || kalimat[i] == 'u' || kalimat[i] == 'e' || kalimat[i] == 'o'){
            vokal++;
        }
    }

    printf("Jumlah huruf vokal dalam kalimat tersebut adalah %d\n", vokal);

    // asignment 2

    // Buat program yang meminta input kata, lalu menampilkannya secara terbalik.
    // Input: "KASUR"
    // Output: "RUSAK"
    // Hint: Gunakan Loop for mundur, dimulai dari strlen(kata) - 1 sampai 0.

    char kata[100];
    printf("Masukkan kata : ");
    scanf("%s", kata);

    printf("Kata terbalik : ");
    for (int i = strlen(kata) - 1; i >= 0; i--){
        printf("%c", kata[i]);
    }
    printf("\n");

    // assignment 3

    // buat program untuk mengganti kalimat dengan format tertentu.
    // contoh: ganti semua huruf 'a' menjadi 'o' dalam kalimat

    char kalimat2[100]; // "h", "o", "l", "o", "\0"
    printf("Masukkan kalimat : ");
    scanf("%s", kalimat2); // halo

    for (int i = 0; i < strlen(kalimat2); i++){
        if (kalimat2[i] == 'a'){
            kalimat2[i] = 'o';
        }
    }

    printf("Kalimat setelah diganti: %s\n", kalimat2);

    return 0;
}