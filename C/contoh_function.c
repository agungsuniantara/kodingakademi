#include <stdio.h>

void coba1(int num1)
{
   int angka = num1;

    printf("%d", angka);
}

int coba2(int num1)
{
    int angka = num1;

    // printf("%d", angka);

    return angka;
}

int main()
{
   int number;
   printf("Input your number: ");
   scanf("%d", &number);

   // coba1(number);

   coba1(number);

   int contoh = coba2(number);

    int hasil = contoh + 1;

   printf("%d", hasil);

   // int contoh = coba1(number);

   // int contoh2 = coba2(number);

   // printf("%d", contoh2);
}
