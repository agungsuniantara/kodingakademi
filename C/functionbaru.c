#include <stdio.h>

void hitung1(){
    int angka = 10;
    printf("hasil = %d \n", angka);
}

void hitung2(int angka1){
    int angka2 = 10;
    int hasil = angka1 + angka2;
    printf("hasil = %d \n", hasil);
}

int hitung3(){
    int angka = 10;
    return angka;
}

int hitung4(int angka1){
    int angka2 = 10;
    int hasil = angka1 + angka2;
    return hasil;
}

void main(){
    hitung1();
    hitung2(30);
    int simpan3 = hitung3();
    int simpan4 = hitung4(50);
    printf("hasil = %d \n", simpan3);
    printf("hasil = %d", simpan4);
}
