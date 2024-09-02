#include <stdio.h>

int main() {
    FILE *file = fopen("assignment3.txt", "r");
    char kata[100];
    while (fgets(kata, sizeof(kata), file)) {
        for (int i = 0; kata[i] != '\0'; i++) {
            if (kata[i] >= '0' && kata[i] <= '9') {
                printf("%c", kata[i]);
            }
        }
        printf("\n");
    }
    fclose(file);
    return 0;
}
