#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int jumlah = sizeof(arr) / sizeof(int);
    FILE *file = fopen("file.txt", "w");
    for (int i = 0; i < jumlah; i++) {
        fprintf(file, "%d\n", arr[i]);
    }
    fclose(file);
    return 0;
}
