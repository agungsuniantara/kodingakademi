#include <stdio.h>
#include <stdbool.h>

int main(){
    int num = 10;
    bool status = true;

    if (num % 2 == 0){
        printf("angka genap");
    }
    else{
        printf("angka ganjil");
    }

    char operator = '-';
    int hasil;

    switch(operator){
        case '+':
            hasil = 10 + 20;
            printf("hasil = %d", hasil);
            break;
        case '-':
            hasil = 10 - 20;
            printf("hasil = %d", hasil);
            break;
        default:
            printf("operator tidak sesuai");
    }

    char huruf;

    printf("masukan karakter : ");
    scanf(" %c", &huruf);

    if (huruf >= 'a' && huruf <= 'z'){
        printf("karakter tapi belum capital");
    }
    else if(huruf >= 'A' && huruf <= 'Z'){
        printf("karakter tapi sudah capital");
    }
    else{
         printf("bukan karakter");
    }
}