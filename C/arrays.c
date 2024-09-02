#include <stdio.h>

int main(){
    int array[10] = {0};

    int ukuranTipe = sizeof(int);
    int ukuranArray = sizeof(array);
    int elemenNum = ukuranArray / ukuranTipe;

    printf("sizeof(int) = %2d bytes\n", ukuranTipe);
    printf("sizeof(array) = %2d bytes\n", ukuranArray);
    printf("array[] has %d elements\n\n", elemenNum);

    float array2[] = {1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0};

    int floatTipe = sizeof(float);
    int ukuranArray2 = sizeof(array2);
    int elemenNum2 = ukuranArray2 / floatTipe;

    printf("sizeof(float) = %d bytes\n", floatTipe);
    printf("sizeof(array) = %d bytes\n", ukuranArray2);
    printf("array[] has %d elements\n\n", elemenNum2);
}
