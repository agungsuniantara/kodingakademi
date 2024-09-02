#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[] = {100, 102, 99, 89, 192, 938, 107, 241};
    int jumlah = sizeof(arr) / sizeof(int);
    FILE *file = fopen("assignment.txt", "w");
    for (int i = 0; i < jumlah; i++) {
        fprintf(file, "%d\n", arr[i]);
    }
    fclose(file);

    file = fopen("assignment.txt", "r");
    char data[100];
    while(fgets(data, sizeof(data), file) != NULL) {
        int angka = atoi(data);
        if (angka % 2 != 0){
            printf("%d \n", angka);
        }
    }
    fclose(file);
    return 0;
}
