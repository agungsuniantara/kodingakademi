#include <stdio.h>
#include <stdbool.h>

int main(){
    int nomer;

    printf("masukkan angka :");
    scanf("%d", &nomer);

    if(((nomer % 2) == 0) == false){
        printf("angka genap");
    }
    else{
        printf("angka ganjil");
    }
}

// note parameter % = perhitungan modulus
// if kondisi angka yang habis dibagi 2 itu genap kalau tidak habis itu ganjil


