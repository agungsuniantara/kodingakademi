#include <stdio.h>
#include <math.h>

int binary (int n)
{
    // array to store octal number
    int angkaawal = n;
    int binaryNum[32];

    // counter for octal number array
    int i = 0;
    while (n > 0) {
        // storing remainder in binary array
        binaryNum[i] = n % 2;
        n = n / 2;
        i++;
    }

    printf("hasil decimal %d ke octal : ", angkaawal);
    // printing octal number array in reverse order
    for (int j = i - 1; j >= 0; j--)
        printf("%d", binaryNum[j]);
}

int octal (int n)
{
    // array to store octal number
    int angkaawal = n;
    int octalNum[100];

    // counter for octal number array
    int i = 0;
    while (n != 0) {

        // storing remainder in octal array
        octalNum[i] = n % 8;
        n = n / 8;
        i++;
    }

    printf("hasil decimal %d ke binary : ", angkaawal);
    // printing octal number array in reverse order
    for (int j = i - 1; j >= 0; j--)
        printf("%d", octalNum[j]);
}

long long hex (int n) {
  long long bin = 0;
  int rem, i = 1;

  while (n!=0) {
    rem = n % 2;
    n /= 2;
    bin += rem * i;
    i *= 10;
  }

  return bin;
}

int main() {
    int parameter, n, bin;

    printf("pilih salah satu dari kondisi : \n");

    printf("1. Decimal to binary \n");
    printf("2. Decimal to octal \n");
    printf("3. Decimal to hex \n");

    printf("masukkan parameter (nomer 1 / 2 / 3) : ");
    scanf("%d", &parameter);

    switch(parameter){
    case 1:
        printf("Enter a decimal number: ");
        scanf("%d", &n);
        bin = binary(n);
    break;

    case 2:
        printf("Enter a decimal number: ");
        scanf("%d", &n);
        bin = octal(n);
    break;

    case 3:
        printf("Enter a decimal number: ");
        scanf("%d", &n);
        printf("decimal ke hex = %x", n);
    break;

    default:
        printf("operator tidak diketahui !");
    }

  return 0;
}

