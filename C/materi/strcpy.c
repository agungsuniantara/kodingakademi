#include <stdio.h>
#include <string.h>

int main() {
    FILE *file = fopen("teks.txt", "r");
    char data[1000];
    char simpan[1000];
    fread(data, sizeof(char), sizeof(data), file);

    strcpy(simpan, data);

    printf("%s \n\n", data);
    printf("string yang disimpan : \n%s", simpan);
    fclose(file);
    return 0;
}
