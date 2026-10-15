#include <iostream>
using namespace std;

void insertion_sort(int arr[], int size) {
    for (int i = 1; i < size; i++) {
        int key = arr[i];       // elemen yang akan disisipkan
        int j = i - 1;

        // Geser semua elemen > key satu posisi ke kanan
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;       // sisipkan key di posisi yang benar
    }
}

void print_array(const int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[6] = {5, 2, 9, 1, 5, 6};
    insertion_sort(arr, 6);
    print_array(arr, 6);
    return 0;
}