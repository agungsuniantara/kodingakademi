#include <stdio.h>
#include <string.h>

#define maks 1000
#define batas 20

int main() {
    FILE *file = fopen("teks.txt", "r");
    char data[maks];
    char simpan[batas];
    fread(data, sizeof(char), sizeof(data), file);

    strncpy(simpan, data, batas);
    simpan[batas] = '\0';

    printf("%s \n\n", data);
    printf("20 Karakter Awal: %s", simpan);
    fclose(file);
    return 0;
}
