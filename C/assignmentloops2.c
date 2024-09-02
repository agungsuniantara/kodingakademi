#include <stdio.h>

void main(){
    int angka;

    printf("masukan angka : ");
    scanf("%d",&angka);

    if (angka % 2 == 0){
         printf("%d angka genap \n", angka);
         for (int i = 1; i <= angka; i++){
            if(angka % i == 0){
                printf("%d ", i);
            }
         }
    }
    else{
        printf("%d angka ganjil \n", angka);

        for (int z = 1; z <= angka; z++){
            if(angka % z == 0){
                printf("%d ", z);
            }
        }
    }
}
