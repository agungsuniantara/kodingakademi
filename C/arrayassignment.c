#include <stdio.h>

int main(){
    int panjang, elemen, average, tambah = 0;

    printf("panjang array : ");
    scanf("%d", &panjang);
    int array[panjang];


    for(int i = 0; i < panjang; i++){
        printf("elemen array : ");
        scanf("%d", &array[i]);
    }

    printf("\n");

    for(int i = 0; i < panjang; i++){
        tambah = tambah + array[i];
    }

    printf("jumlah penambahan array = %d \n", tambah);
    average = tambah / panjang;
    printf("jumlah average adalah = %d", average);



}
