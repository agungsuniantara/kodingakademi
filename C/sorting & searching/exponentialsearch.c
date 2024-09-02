#include <stdio.h>

void main(){

    // exponential search

    // exponential search efektif dilakukan ketika nilai array sudah terurut
    // exponential search membuat rentang data kemudian rentang data tersebut--
    // dicari targetnya menggunakan binary search

    int arr[] = {1,2,3,4,5};
    int jumlah_data = sizeof(arr) / sizeof(arr[0]);
    int target = 3;

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
