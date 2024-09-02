#include <stdio.h>

void main(){
    int bin = 0, n, rem, i = 1;

    printf("Enter a decimal number: ");
    scanf("%d", &n);

    while (n!=0) {
        rem = n % 2;
        n /= 2;
        bin += rem * i;
        i *= 10;
    }

    printf("hasil convert hex = %d", bin);
}
