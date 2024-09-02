#include <stdio.h>

int main() {

    int num, i = 1;
    printf("Enter a positive integer: ");
    scanf("%d", &num);

    if(num % 2 == 0){
        printf("ini bilangan genap \n");
        printf("faktor dari angka %d adalah : ", num);

        while(i <= num){
            if(num % i == 0){

                printf("%-2d", i);
            }
            i++;
       }
    }
    else {
        printf("ini bilangan ganjil \n");
        printf("faktor dari angka %d adalah : ", num);

        for (i = 1; i <= num; i++) {
        if (num % i == 0) {

            printf("%-2d ", i);
        }
        }
    }
    return 0;
}
