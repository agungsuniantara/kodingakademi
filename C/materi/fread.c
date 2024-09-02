#include <stdio.h>

int main(){
    FILE *file = fopen("teks.txt", "r");
    char data[1000];
    fread(data, sizeof(char), sizeof(data), file);
    printf("%s", data);
    fclose(file);
    return 0;
}
