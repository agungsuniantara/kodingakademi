#include <stdio.h>

// function adalah sekumpulan kode yang dibuat untuk melakukan tugas tertentu.
// function bisa dipanggil berkali - kali tanpa harus menulis ulang kode tersebut.
// function (void, parametger, return)

// variabel global (variabel yang bisa diakses di semua function)
int angkaGlobal = 10;

// function void (function yang tidak mengembalikan nilai)
void sapa(){
    printf("halo semua ! \n");
    printf("angka global : %d \n", angkaGlobal);
}

// function parameter (function yang dapat menerima inputan)
void sapa2(char nama[]){
    printf("halo %s ! \n", nama);
    printf("angka global : %d \n", angkaGlobal);
}

// function return (function yang mengembalikan nilai)
int tambah(int a, int b){
    int hasil = a + b + angkaGlobal; // variabel lokal (variabel yang hanya bisa diakses di dalam function tambah)
    return hasil; // mengembalikan hasil penjumlahan a, b, dan angkaGlobal
}

int main(){
    sapa(); // memanggil function sapa

    sapa2("dimas");
    sapa2("budi");

    int hasil1 = tambah(10, 20);
    printf("hasil penjumlahan : %d \n", hasil1);

    int hasil2 = tambah(5, 15);
    printf("hasil penjumlahan : %d \n", hasil2);

    int angka = 100; // variabel lokal (variabel yang hanya bisa diakses di dalam function main)
    int hasil3 = tambah(angka, 50);
    printf("hasil penjumlahan : %d \n", hasil3);

    printf("angka global di main : %d \n", angkaGlobal); // mengakses variabel global di function main

    
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


    return 0;
}