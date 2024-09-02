#include <stdio.h>
#include <string.h>

int main() {
    FILE *file = fopen("teks.txt", "r");
    char data[100];
    while (fscanf(file, "%s", data) == 1) {
        char *kata = strstr(data, "Anna");
        if (kata != NULL) {
            printf("%s \n", kata);
        }
    }

    fclose(file);
    return 0;
}
