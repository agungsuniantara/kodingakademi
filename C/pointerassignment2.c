#include <stdio.h>

double getAverage(int *arr, int size);

int main ()
{
    int var[] = {10, 100, 200};
    double average;

    average = getAverage(var, 3);
    printf("Hasil average = %lf\n", average);

    return 0;
}

double getAverage(int *arr, int size) {
    double tambah = 0;
    
    for (int i = 0; i < size; i++) {
        tambah += *(arr + i);  // *(arr + i) adalah cara lain untuk menulis arr[i]
    }

    return tambah / size;
}
