#include <stdio.h>

void main(){
    int batas;

    printf("masukan angka : ");
    scanf("%d", &batas);

    for (int i = 1; i <= batas; i++){
        for (int z = 1; z <= batas; z++){
            if (z == i || z == batas - i + 1){
                printf("#");
            }
            else{
                printf("*");
            }
        }
        printf("\n");
    }
}
