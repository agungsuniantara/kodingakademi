#include <stdio.h>

int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i; // Mengembalikan indeks elemen jika ditemukan
        }
    }
    return -1; // Mengembalikan -1 jika elemen tidak ditemukan
}

int main() {
    int arr[] = {2, 5, 1, 9, 3, 7, 6, 8, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 7;

    int result = linearSearch(arr, n, target);
    if (result != -1) {
        printf("Elemen %d ditemukan pada indeks %d.\n", target, result);
    } else {
        printf("Elemen %d tidak ditemukan dalam array.\n", target);
    }
    return 0;
}
