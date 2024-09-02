#include <stdio.h>

int main(){
    FILE *file = fopen("teks.txt", "r");
    int data;
    while ((data = fgetc(file)) != EOF) {
        printf("%c", data);
    }
    fclose(file);
    return 0;
}
