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

// bubble sort

int bubble_sort(int data[], int n){
    for (int i = 0; i < n-1; i++){
        for (int j = 0; j < n-i-1; j++){
            if (data[j] > data[j+1]){
                // swap
                int temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
            }
        }
    }
}

int selection_sort(int data[], int n){
    for (int i = 0; i < n-1; i++){
        int min_idx = i;
        for (int j = i+1; j < n; j++){
            if (data[j] < data[min_idx]){
                min_idx = j;
            }
        }
        // swap
        int temp = data[i];
        data[i] = data[min_idx];
        data[min_idx] = temp;
    }
}

int main(){
    int data[] = {10, 20, 30, 40, 50};
    int target = 30;
    int n = sizeof(data) / sizeof(data[0]);

    linear_search(data, target, n);
    binary_search(data, target, n);

    int data2[] = {5,3,8,6,2,7,4,1,10,9};
    int m = sizeof(data2) / sizeof(data2[0]);

    int hasil_bubble = bubble_sort(data2, m);

    printf("Data setelah diurutkan menggunakan bubble sort: \n ");
    for (int i = 0; i < m; i++){
        printf("%d ", data2[i]);
    }
    printf("\n");

    int data3[] = {5,3,8,6,2,7,4,1,10,9};
    int z = sizeof(data3) / sizeof(data3[0]);

    int hasil_selection = selection_sort(data3, z);

    printf("Data setelah diurutkan menggunakan selection sort: \n ");
    for (int i = 0; i < z; i++){
        printf("%d ", data3[i]);
    }
    printf("\n");

    // assignment

    // 1. buatlah array untuk menyimpan nama.
    // 2. buatlah inputan untuk memasukkan nama ke dalam array tersebut.
    // 3. buatlah menu untuk memilih metode pencarian yang ingin digunakan.
    // 4. buatlah fungsi untuk mencari nama dalam array tersebut menggunakan linear search & binary search.

    // assignment
    // buatlah program yang mencari angka 10 pada array = {8,2,7,6,2,10,4,5,9,1} menggunakan binary search.
    // sebelum melakukan binary search, urutkan terlebih dahulu array tersebut menggunakan bubble sort atau selection sort.

    return 0;
}