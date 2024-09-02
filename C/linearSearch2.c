#include <stdio.h>

int main(){
    int array[] = {1,2,3,4,5,6};

    int size = sizeof(array) / sizeof(array[0]);
    int x = 5;
    int i;

    for(i = 0; i < size; i++){
        if(array[i] == x){
            printf("angka 5 berada di index = %d", i);
            break;
        }
    }

    if(i == size){
        printf("elemen tidak ditemukan");
    }
}
