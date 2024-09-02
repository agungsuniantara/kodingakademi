#include <stdio.h>
#include <string.h>

int main() {
    char source[] = "Hello, World!";
    char destination[20];

    strncpy(destination, source, 5); // Menyalin 5 karakter pertama
    destination[5] = '\0'; // Menambahkan karakter null di akhir string tujuan

    printf("Hasil: %s\n", destination);

    return 0;
}
