#include <stdio.h>

int main() {
    FILE *file = fopen("array2d.txt", "w");
    int array2D[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int rows = sizeof(array2D) / sizeof(array2D[0]);
    int cols = sizeof(array2D[0]) / sizeof(array2D[0][0]);

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            fprintf(file, "%d ", array2D[i][j]);
        }
        fprintf(file, "\n");
    }
    fclose(file);
    return 0;
}
