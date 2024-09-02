#include <stdio.h>

void main(){
    int a, b, n, arr[5], angka;

    printf("masukan batas : ");
    scanf("%d", &n);

    for (a = 0; a < n; a++){
        printf("masukan angka : ");
        scanf("%d", &arr[a]);
    }

    for (b = 0; b < n; b++){
        printf("%d ", arr[b]);
    }
}
