#include <stdio.h>

int main(){
    char huruf;

    printf("masukkan huruf : ");
    scanf("%c", &huruf);

    if(huruf == 'a' || huruf == 'i' || huruf == 'u' || huruf == 'e' || huruf == '0'){
        printf("ini huruf vokal");
    }
    else if(huruf == 'A' || huruf == 'I' || huruf == 'U' || huruf == 'E' || huruf == 'O'){
        printf("ini huruf vokal");
    }
    else{
        printf("ini huruf konsonan");
    }
}
