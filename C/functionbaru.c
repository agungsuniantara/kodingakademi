#include <stdio.h>

void hitung1(){  // function void
    int angka = 10;
    printf("hasil = %d \n", angka);
}

void hitung2(int a, int b){ // function parameter
    int hasil = a + b;
    printf("hasil = %d \n", hasil);
}

int hitung3(int a , int b){ // function return
    int hasil = a + b;
    return hasil;
}

void tampil(int a);

int main(){
    hitung1();
    hitung2(10,20);
    int test = hitung3(30,40);
    printf("hasil = %d \n", test);
    tampil(20);
    return 0;
}

void tampil(int a){
    printf("angka : %d", a);
}