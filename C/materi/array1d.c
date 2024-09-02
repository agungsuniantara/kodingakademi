#include <stdio.h>

int main() {
    FILE *file = fopen("array1d.txt", "w");
    int array1D[] = {1, 2, 3, 4, 5};
    int length = sizeof(array1D) / sizeof(array1D[0]);
    for (int i = 0; i < length; i++) {
        fprintf(file, "%d\n", array1D[i]);
    }
    fclose(file);
    return 0;
}
