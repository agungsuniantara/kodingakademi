#include <stdio.h>

void main(){

    // linear search

    // dapat dilakukan dengan nilai array yang tidak berurutan

    int arr[] = {1,2,3,4,5};
    int jumlah_data = sizeof(arr) / sizeof(arr[0]);
    int target = 3;

    for (int i = 0; i < jumlah_data; i++){
        if(arr[i] == target){
            printf("angka %d ditemukan pada array indeks ke-%d \n",target,i);
        }
    }

    // jump search

    // note : jump search efektif dilakukan ketika nilai array sudah terurut
    // sebelum melakukan jump search harus melakukan sorting terlebih dahulu

    int step = sqrt(jumlah_data); // mencari langkah dengan akar
    int prev = 0;

    while(arr[step-1] < target){ // mencari nilai pada setiap langkah
        prev = step;
        step += sqrt(jumlah_data);
        if (prev >= jumlah_data){
            printf("elemen %d tidak ada \n", target);
        }
    }

    for (int i = 0; i < step; i++){ // mencari nilai pada langkah yang sudah dilewati
        if(arr[i] == target){
            printf("angka %d ditemukan pada index ke-%d \n",target, i);
        }
    }

    // binary search

    // note : binary search efektif dilakukan ketika nilai array sudah terurut
    // sebelum melakukan binary search harus melakukan sorting terlebih dahulu

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

    // interpolation search


    // proses interpolation search mirip dengan binary search namun dalam mencari nilai --
    // interpolation search menggunakan rumus untuk menentukan posisi elemen sedangkan binary search --
    // menggunakan nilai tengah untuk menentukan posisi

    // interpolation search dapat dilakukan dengan array terurut dan tidak terurut
    // sebelum melakukan binary search harus melakukan sorting terlebih dahulu

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
            right = pos - 1;
        }
        // Jika target lebih besar, cari di setengah kanan dari posisi perkiraan
        else {
            kiri = pos + 1;
        }
    }

    if (result == 0) {
        printf("Elemen %d tidak ditemukan dalam array.\n", target);
    }

    // exponential search

    // exponential search efektif dilakukan ketika nilai array sudah terurut
    // exponential search membuat rentang data kemudian rentang data tersebut--
    // dicari targetnya menggunakan binary search

    // Temukan rentang yang mengandung elemen target
    int i = 1;
    while (i < jumlah_data && arr[i] <= target) {
        i = i * 2;
    }

    // Lakukan binary search dalam rentang yang ditemukan
    int left2 = i / 2;
    int right2 = (i < jumlah_data) ? i : jumlah_data - 1;
    int hasil = 0;

    while (left2 <= right2) {
        int mid = left2 + (right2 - left2) / 2;

        // Jika elemen ditemukan di tengah
        if (arr[mid] == target) {
            printf("Elemen %d ditemukan pada indeks %d.\n", target, mid);
            hasil = 1;
            break;
        }
        // Jika elemen kurang dari target, cari di setengah kanan
        else if (arr[mid] < target) {
            left2 = mid + 1;
        }
        // Jika elemen lebih dari target, cari di setengah kiri
        else {
            right2 = mid - 1;
        }
    }

    if (hasil == 0) {
        printf("Elemen %d tidak ditemukan dalam array.\n", target);
    }
}
