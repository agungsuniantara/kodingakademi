#include <stdio.h>

void main(){
    int ulang = 0;
    int ulang2 = 0;

    while(ulang < 3){
        printf("while tanpa break \n");
        ulang += 1;
    }

    while(ulang2 < 3){
        printf("while pakai break \n");
        ulang2 += 1;
        break;
    }

    for (int i = 0; i < 3; i++){
        printf("for tanpa break \n");
    }

    for (int i = 0; i < 3; i++){
        printf("for pakai break \n");
        break;
    }
}
