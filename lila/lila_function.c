#include<stdio.h>

//function adalah sekumpulan kode yg dibuat untuk melakukan tugas tertentu
//function bisa dipanggil berkali kali tanpa perlu menulis ulang kodenya
// funcstion (void, parameter, return)

int total = 10; //variabel global (bisa di akses mana aja)

//function void (fungsi yg tidak mengembalikan nilai)
void sapa(){
    printf("Halo, selamat datang!\n");
}

//fuction dengan parameter (function yg menerima inputan)
void sapa_nama(char x[]){
    printf("halo, %s! selamat datang!\n", x);
}

//function return (yaitu funcstion yg mengembalikan nilai)
int angka (int number1, int number2){
    int hasil = number1 + number2;
    return hasil;
}

int hitung_luas (int panjang, int lebar){
    int luas = panjang * lebar;
    return luas;
}

int suhu (int celcius){
    float konversi = ((9.0/5.0) * celcius) + 32.0;
    return konversi;
}

int cek_bilangan (int angka1){
    if (angka1 % 2 == 0){
        return 1;
    } else {
        return 0;
    }
}
    
void pertambahan(float angka_1, float angka_2){
    float hasil = angka_1 + angka_2;
    printf("Hasil penjumlahan: %.2f\n", hasil);
}

void pengurangan(float angka_1, float angka_2){
    float hasil = angka_1 - angka_2;
    printf("Hasil pengurangan:%.2f\n", hasil);
}

void perkalian(float angka_1, float angka_2){
    float hasil = angka_1 * angka_2;
    printf("Hasil perkalian:%.2f\n", hasil);
}

void pembagian(float angka_1, float angka_2){
    float hasil = angka_1 / angka_2;
    printf("Hasil pembagian:%.2f\n", hasil);
}

int main(){
    sapa();
    sapa();

    char nama[50]; //variabel lokal (hanya bisa diakses didalam function main)
    printf("masukkan nama : ");
    scanf("%s", nama);
    sapa_nama (nama);

    angka(10,20);
    printf("hasil penjumlahan: %d\n", angka(10,20));

    //assignment 1
    //buat fungsi untuk menghitung luas pesergi panjang
    //function dgn parameter dan return
    //rumus luas = panjang * lebar
    hitung_luas (25,10);
    printf("Luas pesergi panjang adalah %d\n", hitung_luas(25,10));

    //assignment 2
    //buat fungsi konversi suhu dari celcius ke farenheit
    //rumus fahrenheit = (9/5 * celcius) + 32
    suhu (45);
    printf ("hasil konversi suhu dari celcius ke farenheit adalah %d\n", suhu(45));

    //assignment 3
    //buat fungsi untuk cek bilangan ganjil/genap
    int hasil_genap = cek_bilangan(2);
    if (hasil_genap == 1){
        printf("bilangan genap\n");
    } else {
        printf("bilangan ganjil\n");
    }

    //assignment 4
    //buat sistem kalkulator sederhana dengan function
while(1){
    printf("Kalkulator sederhana\n");
    printf("1.Penjumlahan\n");
    printf("2.Pengurangan\n");
    printf("3.Perkalian\n");
    printf("4.Pembagian\n");

    int choice;
    float angka_1, angka_2;
    printf("Pilih operasi mana?");
    scanf("%d", &choice);

    if (choice == 1){
        printf("Masukkan angka pertama:");
        scanf("%f", &angka_1);
        printf("Masukkan angka kedua:");
        scanf("%f", &angka_2);
        pertambahan(angka_1, angka_2);
    }
    else if (choice == 2){
     printf("Masukkan angka pertama:");
        scanf("%f", &angka_1);
        printf("Masukkan angka kedua:");
       scanf("%f", &angka_2);
       pengurangan(angka_1, angka_2);    
    }
     else if (choice == 3){
     printf("Masukkan angka pertama:");
        scanf("%f", &angka_1);
        printf("Masukkan angka kedua:");
       scanf("%f", &angka_2);
       perkalian(angka_1, angka_2);    
    }
     else if (choice == 4){
     printf("Masukkan angka pertama:");
        scanf("%f", &angka_1);
        printf("Masukkan angka kedua:");
       scanf("%f", &angka_2);
       pembagian(angka_1, angka_2);    
    }
}
 return 0;

}