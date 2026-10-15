#include <iostream>
using namespace std;

// Menggabungkan dua bagian terurut:
// arr[left..mid] dan arr[mid+1..right] menjadi satu bagian terurut
void merge(int arr[], int left, int mid, int right) {
    int left_size = mid - left + 1;
    int right_size = right - mid;

    // Array sementara untuk masing-masing bagian
    int* left_arr = new int[left_size];
    int* right_arr = new int[right_size];

    for (int i = 0; i < left_size; i++) {
        left_arr[i] = arr[left + i];
    }
    for (int j = 0; j < right_size; j++) {
        right_arr[j] = arr[mid + 1 + j];
    }

    // Bandingkan elemen terdepan kedua array, ambil yang lebih kecil
    int i = 0;
    int j = 0;
    int k = left;
    while (i < left_size && j < right_size) {
        if (left_arr[i] <= right_arr[j]) {
            arr[k] = left_arr[i];
            i++;
        } else {
            arr[k] = right_arr[j];
            j++;
        }
        k++;
    }

    // Salin sisa elemen (hanya salah satu loop ini yang jalan)
    while (i < left_size) {
        arr[k] = left_arr[i];
        i++;
        k++;
    }
    while (j < right_size) {
        arr[k] = right_arr[j];
        j++;
        k++;
    }

    delete[] left_arr;
    delete[] right_arr;
}

void merge_sort(int arr[], int left, int right) {
    if (left >= right) {
        return;   // base case: 0 atau 1 elemen = sudah terurut
    }
    int mid = left + (right - left) / 2;   // hindari overflow
    merge_sort(arr, left, mid);            // urutkan setengah kiri
    merge_sort(arr, mid + 1, right);       // urutkan setengah kanan
    merge(arr, left, mid, right);          // gabungkan
}

void print_array(const int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[8] = {38, 27, 43, 3, 9, 82, 10, 1};
    merge_sort(arr, 0, 7);
    print_array(arr, 8);
    return 0;
}