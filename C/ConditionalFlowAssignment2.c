#include <stdio.h>
#include <stdlib.h>

int main() {
    char huruf;

    printf("Masukkan huruf/angka: ");
    scanf("%c", &huruf);

    if (huruf >= 'A' && huruf <= 'Z') {
        printf("Ini huruf besar\n");
    }
    else if (huruf >= 'a' && huruf <= 'z') {
        printf("Ini huruf kecil\n");
    }
    else {
        if (atoi(&huruf)) {
            printf("Ini angka\n");
        }
        else {
            printf("Ini simbol\n");
        }
    }
}

