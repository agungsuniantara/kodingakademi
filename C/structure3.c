#include <stdio.h>

struct rumus{
    int alas;
    int tinggi;
    char nama[50];
};

void main(){
    struct rumus segitiga1;
    struct rumus segitiga2;

    segitiga1.alas = 10;
    segitiga1.tinggi = 20;
    strcpy(segitiga1.nama, "segitiga 1");

    segitiga2.alas = 50;
    segitiga2.tinggi = 100;
    strcpy(segitiga2.nama, "segitiga 2");

    int hasil_segitiga1 = segitiga1.alas * segitiga1.tinggi;
    int hasil_segitiga2 = segitiga2.alas * segitiga2.tinggi;

    printf("hasil = %d, nama = %s \n", hasil_segitiga1, segitiga1.nama);
    printf("hasil = %d, nama = %s \n", hasil_segitiga2, segitiga2.nama);


}
