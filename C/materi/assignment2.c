#include <stdio.h>
#include <string.h>

int main() {
    FILE *file = fopen("assignment2.txt", "r");

    char data[100];
    int count = 0;

    while (fscanf(file, "%s", data) == 1) {
        char *kata = strstr(data, "gunung");
        if (kata != NULL && strlen(kata) <= strlen("gunung")) {
            printf("%s \n", kata);
            count++;
        }
    }
    fclose(file);
    printf("Jumlah kata gunung yang ada pada teks : %d\n", count);
    return 0;
}
