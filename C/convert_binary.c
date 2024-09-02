#include <stdio.h>

void main(){
    int angka = 47;
    int index = 0;
    int arr[100];

    for(int i = 0; i <= index; i++){
        int binary = angka % 2;
        arr[i] = binary;

        angka = angka / 2;

        printf("%d ", binary);
        index += 1;

        if (angka == 0){
            break;
        }
    }

    printf("\n");

    printf("hasil reverse : \n");

    for (int z = index - 1; z >= 0; z--){
        printf("%d ", arr[z]);
    }
}
