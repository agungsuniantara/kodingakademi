#include <stdio.h>

void main(){

     // binary search

    // note : binary search efektif dilakukan ketika nilai array sudah terurut
    // sebelum melakukan binary search harus melakukan sorting terlebih dahulu

    int arr[] = {1,2,3,4,5};
    int jumlah_data = sizeof(arr) / sizeof(arr[0]);
    int target = 3;

    int left = 0;
    int right = jumlah_data - 1;
    int found = 0;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Jika elemen tengah adalah target
        if (arr[mid] == target) {
            printf("Elemen %d ditemukan pada indeks %d.\n", target, mid);
            found = 1;
            break;
        }

        // Jika target lebih kecil, cari di setengah kiri dari mid
        if (arr[mid] > target) {
            right = mid - 1;
        }

        // Jika target lebih besar, cari di setengah kanan dari mid
        if (arr[mid] < target) {
            left = mid + 1;
        }
    }

    if (found == 0) {
        printf("Elemen %d tidak ditemukan dalam array.\n", target);
    }

}

