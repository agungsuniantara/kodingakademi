#include <stdio.h>

int main() {
    FILE *file = fopen("teks.txt", "r");
    char data[100];
    while(fscanf(file, "%s", data) == 1){
        printf("%s ", data);
    }
    fclose(file);
    return 0;
}
