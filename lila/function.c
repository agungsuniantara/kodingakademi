#include <stdio.h>

// function adalah sekumpulan kode yang dibuat untuk melakukan tugas tertentu
// function bisa dipanggil berkali-kali tanpa perlu menulis ulang kodenya
// function (void, parameter, return)

int total = 10; // variabel global (bisa diakses di mana saja)

// function void (function yang tidak mengembalikan nilai)
void sapa(){
    printf("Halo, selamat datang!\n");
}

// function dengan parameter (function yang menerima inputan)
void sapa_nama(char x[]){
    printf("Halo, %s! Selamat datang!\n", x);
}

// function dengan return (function yang mengembalikan nilai)
int angka(int number1, int number2){
    int hasil = number1 + number2;
    return hasil;
}

// buat function pertambahan
void tambah(int a, int b){
    int hasil = a + b;
    printf("Hasil penjumlahan: %d\n", hasil);
}


int main(){
    sapa(); 
    sapa();

    char nama[50]; // variabel lokal (hanya bisa diakses di dalam function main)
    printf("masukan nama : ");
    scanf("%s", nama);

    sapa_nama(nama);

    angka(10,20);
    printf("Hasil penjumlahan: %d\n", angka(10, 20));

    // assignment 1

    // buat fungsi untuk menghitung luas persegi panjang
    // function dengan parameter dan return
    // rumus luas = panjang * lebar 

    // assignment 2

    // buat fungsi konversi suhu dari celcius ke fahrenheit
    // rumus fahrenheit = (9/5 * celcius) + 32

    // assignment 3

    // buat fungsi untuk cek bilangan ganjil / genap

    // asignment 4

    // buat sistem kalkulator sederhana dengan function

    int kondisi = 1;

    while (kondisi){
        print("Menu Kalkulator Sederhana\n");
        print("1. Penjumlahan\n");
        print("2. Pengurangan\n");
        pirntf("5. Keluar\n");

        int choice, num1, num2;
        print("Pilih operasi (1/2): ");
        scan("%d", &choice);

        if (choice == 1){
            printf("Masukkan angka pertama: ");
            scanf("%d", &num1);
            printf("Masukkan angka kedua: ");
            scanf("%d", &num2);

            tambah(num1, num2);
        }
        else if(choice == 5){
            kondisi = 0;
            printf("Keluar dari program kalkulator.\n");
        }
        
    }

    return 0;
}