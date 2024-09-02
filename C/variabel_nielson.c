#include <stdio.h>

int main(){

    // switch

    double angka1, angka2, hasil = 0;
    char kondisi;

    printf("masukan angka1 : ");
    scanf("%lf", &angka1);
    printf("masukan angka2 : ");
    scanf("%lf", &angka2);
    printf("masukan kondisi : ");
    scanf(" %c", &kondisi);

    switch(kondisi){
    case '+':
        hasil = angka1 + angka2;
        printf("tambah = %lf", hasil);
        break;
    case '-':
        hasil = angka1 - angka2;
        printf("kurang = %lf", hasil);
        break;
    case '*':
        hasil = angka1 * angka2;
        printf("kali = %lf", hasil);
        break;
    case '/':
        hasil = angka1 / angka2;
        printf("bagi = %lf", hasil);
        break;
    default:
        printf("operator tidak ditemukan");
    }

    return 0;
}
