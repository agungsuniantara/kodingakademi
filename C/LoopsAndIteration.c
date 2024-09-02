#include <stdio.h>

int main(){
    int i;
    double number, sum = 0.0;

    while(i <= 10){
        printf("%d \n", i);
        i++;
    }

    for(i = 1; i <= 10; i++){
        printf("%d \n", i);
    }

    for(i = 1; i <= 5; i++){
        printf("masukkan angka %d : ", i);
        scanf("%lf", &number);

        if(number < 0.0){
            break;
        }

        sum += number; // sum = sum + number;

    }

    printf("sum = %.2lf", sum);

    return 0;
}
