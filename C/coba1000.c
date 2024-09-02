#include <stdio.h>

void main(){
    int a = 0, arr[3], rata;

    for (int i = 0; i < 3; i++){
        arr[i] = i + 1;
    }

    for (int i = 0; i < 3; i++){
        a += arr[i];
    }

    rata = a / 3;
    printf("jumlah total array = %d, rata-rata = %d", a, rata);
}
