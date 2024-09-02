#include <stdio.h>
#include <math.h>

int jumpSearch(int arr[], int n, int target) {
    int step = sqrt(n); // Tentukan ukuran langkah dengan akar kuadrat dari panjang array
    int prev = 0;

    // Melompati elemen-elemen dengan interval langkah sampai menemukan blok yang berpotensi mengandung target
    while (arr[min(step, n) - 1] < target) {
        prev = step;
        step += sqrt(n);
        if (prev >= n) {
            return -1; // Jika melebihi panjang array, target tidak ditemukan
        }
    }

    // Melakukan pencarian linear dalam blok yang potensial mengandung target
    while (arr[prev] < target) {
        prev++;

        if (prev == min(step, n)) {
            return -1; // Jika melebihi panjang array, target tidak ditemukan
        }
    }

    // Jika elemen yang diinginkan ditemukan
    if (arr[prev] == target) {
        return prev;
    }

    return -1; // Jika elemen tidak ditemukan
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 7;

    // Panggil jumpSearch untuk mencari target dalam array
    int index = jumpSearch(arr, n, target);

    if (index != -1) {
        printf("Elemen %d ditemukan di indeks %d.\n", target, index);
    } else {
        printf("Elemen %d tidak ditemukan dalam array.\n", target);
    }

    return 0;
}
