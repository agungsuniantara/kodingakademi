#include <stdio.h>


void main(){
    // jump search

    // note : jump search efektif dilakukan ketika nilai array sudah terurut
    // sebelum melakukan jump search harus melakukan sorting terlebih dahulu

    int arr[] = {1,2,3,4,5};
    int jumlah_data = sizeof(arr) / sizeof(arr[0]);
    int target = 3;
    int step = sqrt(jumlah_data); // mencari langkah dengan akar

    while(arr[step-1] < target){ // mencari nilai pada setiap langkah
        step += sqrt(jumlah_data);
        if (step >= jumlah_data){
            printf("elemen %d tidak ada \n", target);
        }
    }

    for (int i = 0; i < step; i++){ // mencari nilai pada langkah yang sudah dilewati
        if(arr[i] == target){
            printf("angka %d ditemukan pada index ke-%d \n",target, i);
        }
    }
}

