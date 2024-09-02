#include <stdio.h>

int main(){
    FILE *file = fopen("teks.txt", "r");
    int data = fgetc(file);
    printf("%c", data);
    fclose(file);
    return 0;
}
