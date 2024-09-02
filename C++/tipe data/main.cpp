#include <iostream>

using namespace std;

int main()
{
    int angka = 10;
    char *teks = "hello world";
    string teks2 = "hallo world2";
    char karakter = 'd';
    float nilai = 3.12f;
    double coba = 3.2323232;

    cout << "angka : " << angka << endl;
    cout << "teks : " << teks << endl;
    cout << "teks2 : " << teks2 << endl;
    cout << "karakter : " << karakter << endl;

    printf("teks = %s \n", teks);
    printf("angka = %d \n", angka);
    printf("angka = %.3f \n", nilai);
    printf("angka = %.4f \n", coba);

    // konversi tipe data

    double angka2 = (double) angka;

    printf("angka2 = %.4f", angka2);


}
