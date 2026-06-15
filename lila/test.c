#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
   int angka = 10;
   float angka_desimal = 5.5;
   char karakter = 'A';
   double angka_double = 20.99;
   char* nama = "Contoh String";
   int benar = 1; // true
   int salah = 0; // false
   bool benar = true;

    printf("Angka: %d\n", angka);
    printf("Angka Desimal: %.2f\n", angka_desimal);
    printf("Karakter: %c\n", karakter);
    printf("Angka Double: %.2f\n", angka_double);
    printf("Nama: %s\n", nama);

    if (benar && benar) {
        printf("Ini tidak akan dicetak karena salah adalah false.\n");
    } else {
        printf("Benar adalah true dan salah adalah false.\n");
    }

    printf("%d\n", benar); // Output: 1
    printf("%d\n", salah); // Output: 0

    int number = 0;
    number += 1;

    return 0;
}