#include <stdio.h>

int main(){
    FILE *file = fopen("teks.txt", "r");
    char data[100];
    while(fgets(data, sizeof(data), file)) {
        printf("%s", data);
    }
    fclose(file);
    return 0;
}
