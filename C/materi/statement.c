#include <stdio.h>

int main() {
    int a = 10;
    int b = 20;

    if (a == 10){
        printf("angka = %d", a);
    }
    else if (b == 20){
        printf("angka = %d", b);
    }
    else{
        printf("bukan 10 dan bukan 20");
    }

    switch (a){
        case 10:
            printf("angka = %d", a);
            break;
        case 20:
            printf("angka = %d", a);
            break;
        default:
            printf("angka beda");
    }

    return 0;
}
