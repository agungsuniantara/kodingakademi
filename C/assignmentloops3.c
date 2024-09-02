#include <stdio.h>
#include <math.h>

int main() {
    int parameter, n, store[20], i = 0;

    printf("pilih salah satu dari kondisi : \n");

    printf("1. Decimal to binary \n");
    printf("2. Decimal to octal \n");
    printf("3. Decimal to hex \n");

    printf("masukkan parameter (nomer 1 / 2 / 3) : ");
    scanf("%d", &parameter);

    if (parameter == 1){
        printf("masukan angka decimal : ");
        scanf("%d", &n);

        while (n > 0){
            store[i] = n % 2;
            n = n / 2;
            i++;
        }

        printf("hasil decimal ke binary = %d", n);
        // printing octal number array in reverse order
        for (int j = i - 1; j >= 0; j--)
            printf("%d", store[j]);

    }
    else if(parameter == 3){
        long long bin = 0;
        int rem, i = 1;

        printf("masukan angka decimal : ");
        scanf("%d", &n);

        while (n!=0) {
            rem = n % 2;
            n /= 2;
            bin += rem * i;
            i *= 10;
        }

        printf("hasil decimal ke hex = %x", bin);

    }

  return 0;
}

