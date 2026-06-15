#include <stdio.h>

// algoritma = langkah-langkah untuk menyelesaikan suatu masalah
// searching = mencari data dalam suatu struktur data

// linear search = mencari data dengan cara membandingkan satu per satu data yang ada

void linear_search(int data[], int target, int n){
    int found = 0;
    for (int i = 0; i < n; i++){
        if (data[i] == target){
            printf("data ditemukan pada index %d \n", i);
            found = 1;
            break; // keluar dari loop
        }
    }
    if (!found){
        printf("data tidak ditemukan \n");
    }
}

// binary search = mencari data dengan cara membagi dua data yang ada, hanya bisa digunakan pada data yang sudah terurut

void binary_search(int data[], int target, int n){
    int left = 0;
    int right = n - 1;
    int found = 0;

    while (left <= right){
        int mid = left + (right - left) / 2; // mencari index tengah
        if (data[mid] == target){
            printf("data ditemukan pada index %d \n", mid);
            found = 1;
            break; // keluar dari loop
        }
        else if (data[mid] < target){
            left = mid + 1; // mencari di bagian kanan
        }
        else {
            right = mid - 1; // mencari di bagian kiri
        }
    }
    if (!found){
        printf("data tidak ditemukan \n");
    }
}

int main(){
    int data[] = {10, 20, 30, 40, 50};
    int target = 30;
    int n = sizeof(data) / sizeof(data[0]);

    linear_search(data, target, n);
    binary_search(data, target, n);

    // assignment

    // 1. buatlah array untuk menyimpan nama.
    // 2. buatlah inputan untuk memasukkan nama ke dalam array tersebut.
    // 3. buatlah menu untuk memilih metode pencarian yang ingin digunakan.
    // 4. buatlah fungsi untuk mencari nama dalam array tersebut menggunakan linear search & binary search.

    return 0;
}