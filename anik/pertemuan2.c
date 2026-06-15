#include <stdio.h>

int main(){

    // control flow (if else, switch, looping (for, while, do while))

    // if ,else if, else

    if (1){
        printf("angka lebih besar dari 5 \n");
    }
    else if(1){
        printf("angka lebih besar dari 5 \n");
    }
    else{
        printf("salah \n");
    }

    if(1){
        printf("angka lebih besar dari 5 \n");
    }
    else{
        printf("angka lebih kecil dari 5 \n");
    }

    int angka1 = 15;
    int angka2 = 20;
    int angka3 = 90;

    if (angka1 > 10){ // 0
        printf("angka %d lebih besar dari 10 \n", angka1);
    }
    else if(angka1 > 5){ // 0
        printf("angka %d lebih besar dari 5 \n", angka1);
    }
    else if (angka1 > 1){ // 0
        printf("angka %d lebih besar dari 1 \n", angka1);
    }
    else {
        printf("angka %d lebih besar atau lebih kecil dari 0 \n", angka1);
    }

    if ((angka1 > 10) && (angka2 < 20)){ // 0
        printf("angka %d lebih besar dari 10 & lebih kecil dari 20 \n", angka1);
    }
    else if((angka1 > 5) && (angka2 <= 20) || (angka3 < 100)){ // 1
        printf("angka %d lebih besar dari 5 & lebih kecil dari 20 \n", angka1);
    }
    else{
       printf("angka %d lebih besar atau lebih kecil dari 0 \n", angka1);
    }

    // switch

    int umur = 10;

    switch(umur){
        case 10:
            printf("umur %d tergolong anak - anak \n", umur);
            break;
        case 20:
            printf("umur %d tergolong dewasa \n", umur);
            break;
        default:
            printf("umur tidak terdefinisi \n");
    }

    // looping (for , while, do while)

    // for (perulangan yang jumlahnya perulangannya sudah diketahui)

    // for (int i = 0; i < 5; i++){
    //     printf("perulangan ke - %d \n", i);
    // }

    for (int i = 0; i < 5; i++){
        printf("perulangan ke - %d \n", i);
        for (int z = 0; z < 2; z++){
            printf("perulangan ke - %d \n", z);
        }
    }

    // while (perulangan jika kondisinya benar akan terus berulang)

    int jumlah = 0;

    while (jumlah < 5){
        printf("ulang \n");
        jumlah += 1;
    }

    // do while (perulangan yang akan berjalan minimal 1 kali)

    printf("do while : \n");

    int angka5 = 6;

    do {
        printf("ulang \n");
        angka5 += 1;
    } while (angka5 < 5);

    return 0;
}