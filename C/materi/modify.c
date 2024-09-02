#include <stdio.h>

int main() {

    int angka[] = {100, 200, 300};
    char nama[3][6] = {"asu", "lolok", "pepek"}; // Adjusted size to accommodate the strings
    int jumlah = sizeof(nama) / sizeof(char);

    for (int i = 0; i < 3; i++) { // Use the correct size of the first dimension
        for (int j = 0; j < 6; j++) { // Use the correct size of the second dimension
            printf("%c", nama[i][j]); // Use %c to print individual characters
        }
        printf(" "); // Add space between words
    }

    return 0;
}
