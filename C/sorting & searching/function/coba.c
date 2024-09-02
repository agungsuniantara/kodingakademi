#include <stdio.h>

int jumpSearch(int arr[], int n, int target) {
    int step = sqrt(n); // Menentukan ukuran langkah, biasanya akar dari panjang array
    int prev = 0;

    // Melakukan lompatan untuk mencari blok yang mengandung elemen yang dicari
    while (arr[min(step, n) - 1] < target) {
        prev = step;
        step += sqrt(n);
        if (prev >= n) {
            return -1; // Elemen tidak ditemukan jika melebihi panjang array
        }
    }

    // Melakukan pencarian linear dalam blok yang sesuai
    while (arr[prev] < target) {
        prev++;
        if (prev == min(step, n)) {
            return -1; // Elemen tidak ditemukan dalam blok yang sesuai
        }
    }

    // Jika elemen ditemukan, mengembalikan indeksnya
    if (arr[prev] == target) {
        return prev;
    }

    return -1; // Elemen tidak ditemukan dalam array
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 7;

    int result = jumpSearch(arr, n, target);
    if (result != -1) {
        printf("Elemen %d ditemukan pada indeks %d.\n", target, result);
    } else {
        printf("Elemen %d tidak ditemukan dalam array.\n", target);
    }
    return 0;
}
