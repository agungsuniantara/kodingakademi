#include <stdio.h>

int main(){
    int angka1 = 10;
    int angka2 = 2;
    char parameter;

    printf("masukkan parameter (+,-,%,/) : ");
    scanf("%c", &parameter);

    switch(parameter){
    case '+':
        printf("hasil perhitungan + adalah %d", angka1 + angka2);
        break;
    case '-':
        printf("hasil perhitungan - adalah %d", angka1 - angka2);
        break;
    case '%':
        printf("hasil perhitungan % adalah %d", angka1 % angka2);
        break;
    case '/':
        if(angka2 == 0.0){
            printf("angka error !!!");
        }
        else{
            printf("hasil perhitungan / adalah %d", angka1 / angka2);
        }
        break;
    case '*':
        printf("hasil perhitungan * adalah %d", angka1 * angka2);
        break;
    default:
        printf("operator tidak diketahui !");
    }
}
