#include <stdio.h>

int main(){
    short a;
    long b;
    long long c;
    long double d;

    printf("ukuran dari short = %e bytes\n", sizeof(a));
    printf("ukuran dari long = %e bytes\n", sizeof(b));
    printf("ukuran dari long long = %e bytes\n", sizeof(c));
    printf("ukuran dari long double = %e bytes\n", sizeof(d));
}
