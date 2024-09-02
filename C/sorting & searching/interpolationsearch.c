#include <stdio.h>

void main(){

    // interpolation search

    // proses interpolation search mirip dengan binary search namun dalam mencari nilai --
    // interpolation search menggunakan rumus untuk menentukan posisi elemen sedangkan binary search --
    // menggunakan nilai tengah untuk menentukan posisi

    // interpolation search dapat dilakukan dengan array terurut dan tidak terurut
    // sebelum melakukan binary search harus melakukan sorting terlebih dahulu


    int arr[] = {1,2,3,4,5};
    int jumlah_data = sizeof(arr) / sizeof(arr[0]);
    int target = 3;

    int kiri = 0;
    int kanan = jumlah_data - 1;
    int result = 0;

    while (kiri <= kanan && target >= arr[kiri] && target <= arr[kanan]) {
        // Menghitung posisi perkiraan menggunakan rumus interpolasi
        int pos = kiri + ((double)(kanan - kiri) / (arr[kanan] - arr[kiri])) * (target - arr[kiri]);

        // Jika target ditemukan di posisi perkiraan
        if (arr[pos] == target) {
            printf("Elemen %d ditemukan pada indeks %d.\n", target, pos);
            result = 1;
            break;
        }

        // Jika target lebih kecil, cari di setengah kiri dari posisi perkiraan
        if (arr[pos] > target) {
            kanan = pos - 1;
        }
        // Jika target lebih besar, cari di setengah kanan dari posisi perkiraan
        else {
            kiri = pos + 1;
        }
    }

    if (result == 0) {
        printf("Elemen %d tidak ditemukan dalam array.\n", target);
    }
}
