#include <stdio.h>

int main(){
    printf("Hello, World!\n");
    printf("Welcome to C programming.\n");

    // tipe data dasar di C :
    // integer (int) = bilangan bulat
    // floating point (float, double) = bilangan desimal
    // character (char) = karakter tunggal
    // boolean (bool) = nilai benar/salah
    // void = tipe data kosong

    char nama[50] = "alice";
    char alamat[50] = "denpasar";
    printf("Nama: %s\nAlamat: %s\n", nama, alamat);

    char huruf[10] = "hello";
    int angka_int = 10;
    float angka_float = 10.5;
    double angka_double = 20.99;
    int nilai_bool = 1; // 1 untuk true, 0 untuk false

    huruf[0] = 'H';
    huruf[1] = '\0'; // menandai akhir string

    angka_int = 20;
    angka_float = 15.75;
    nilai_bool = 0;

    // output
    printf("Huruf: %s\n", huruf);
    printf("Angka Integer: %d\n", angka_int);
    printf("Angka Float: %.2f\n", angka_float);
    printf("Angka Double: %.2lf\n", angka_double);
    printf("Nilai Boolean: %d\n", nilai_bool);

    // input
    int angka1, angka2;
    char nama_input[50];
    float angka_float_input;
    printf("masukan angka1 : ");
    scanf("%d", &angka1);
    printf("masukan angka2 : ");
    scanf("%d", &angka2);
    printf("masukan nama : ");
    scanf("%s", nama_input);
    printf("masukan angka float : ");
    scanf("%f", &angka_float_input);

    printf("angka1 : %d\n", angka1);
    printf("angka2 : %d\n", angka2);
    printf("nama : %s\n", nama_input);
    printf("angka float : %.2f\n", angka_float_input);

    // operator (aritmatika, relasional, logika)
    // aritmatika: +, -, *, /, %
    // relasional: ==, !=, >, <, >=, <=
    // logika: &&, ||, !

    // operator aritmatika
    int a = 10, b = 3;
    printf("a + b = %d\n", a + b);
    printf("a - b = %d\n", a - b);
    printf("a * b = %d\n", a * b);
    printf("a / b = %d\n", a / b);
    printf("a %% b = %d\n", a % b);

    // operator relasional
    printf("a == b : %d\n", a == b);
    printf("a != b : %d\n", a != b);
    printf("a > b : %d\n", a > b);
    printf("a < b : %d\n", a < b);
    printf("a >= b : %d\n", a >= b);
    printf("a <= b : %d\n", a <= b);

    // operator logika
    // && (AND) = jika salah satu kondisi false, maka hasilnya false
    // || (OR) = jika salah satu kondisi true, maka hasilnya true
    // ! (NOT) = membalik nilai, true menjadi false, false menjadi true

    printf("(a > b) && (a != b) : %d\n", (a > b) && (a < b));
    printf("(a < b) || (a == b) : %d\n", (a < b) || (a > b));
    printf("!(a == b) : %d\n", !(a == b));

    return 0;
}