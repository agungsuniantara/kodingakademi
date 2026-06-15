#include <stdio.h>

// algoritma = langkah-langkah penyelesaian masalah
// searching = pencarian data di dalam struktur data

void linear_search(int target, int data[], int n){
    // linear search (sequential search)
    // mencari data dengan cara mengecek satu per satu dari awal hingga akhir

    int found = 0;
    for (int i = 0; i < n; i++){
        if (data[i] == target){
            found = 1;
            printf("Data %d ditemukan pada indeks ke-%d\n", target, i);
            break;
        }
    }

    if (!found){
        printf("Data %d tidak ditemukan\n", target);
    }
}

void binary_search(int target, int data[], int n){
    // binary search
    // mencari data dengan cara membagi dua bagian dari data yang sudah terurut

    int left = 0;
    int right = n - 1;

    while (left <= right){
        int mid = left + (right - left) / 2;

        if (data[mid] == target){
            printf("Data %d ditemukan pada indeks ke-%d\n", target, mid);
            break;
        } else if (data[mid] < target){
            left = mid + 1; // cari di bagian kanan
        } else {
            right = mid - 1; // cari di bagian kiri
        }

        if (left > right){
            printf("Data %d tidak ditemukan\n", target);
            break;
        }
    }
}

// sorting = pengurutan data dalam struktur data

int bubble_sort(int data[], int n){
    // bubble sort
    // mengurutkan data dengan cara menukar elemen yang berdekatan jika urutannya salah

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
    // selection sort
    // mengurutkan data dengan cara mencari elemen terkecil dan menukarnya dengan elemen pertama yang belum terurut

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
    int data[] = {1,2,3,4,5,6,7,8,9,10}; // data harus terurut untuk binary search
    int n = sizeof(data) / sizeof(data[0]); // menghitung jumlah elemen dalam array

    linear_search(5, data, n); 
    binary_search(7, data, n);

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
    // buatlah program yang mencari angka 10 pada array = {8,2,7,6,2,10,4,5,9,1} menggunakan binary search.
    // sebelum melakukan binary search, urutkan terlebih dahulu array tersebut menggunakan bubble sort atau selection sort.

    return 0;
}