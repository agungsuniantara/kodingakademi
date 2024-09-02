#include <stdio.h>

int hasil(int b){
    int angka1 = b;
    int hasil = angka1 * 10; // 100

    return hasil;
}

int main(){
    int a;

    printf("masukan angka : ");
    scanf("%d", &a);

    int luas = hasil(a);

    printf("%d", luas);


}
