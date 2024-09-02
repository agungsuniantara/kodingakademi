#include <stdio.h>

void main(){

    // linear search

    // dapat dilakukan dengan nilai array yang tidak berurutan

    int arr[] = {1,2,3,4,5};
    int jumlah_data = sizeof(arr) / sizeof(arr[0]);
    int target = 3;

    for (int i = 0; i < jumlah_data; i++){
        if(arr[i] == target){
            printf("angka %d ditemukan pada array indeks ke-%d \n",target,i);
        }
    }
}
