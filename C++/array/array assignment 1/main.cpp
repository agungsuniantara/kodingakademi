#include <iostream>

using namespace std;

int main() {
    int a = 10; // Ukuran array
    int arr[a] = {5, 10, 3, 15, 20, 25, 30, 35, 40, 45};

    // Menginisialisasi elemen terbesar dengan elemen pertama dari array
    int maxElement = arr[0];

    // Mencari elemen terbesar dalam array
    for (int i = 1; i < a; i++) {
        if (arr[i] > maxElement) {
            maxElement = arr[i];
        }
    }
    // Menampilkan elemen terbesar
    cout << "Elemen terbesar dalam array adalah: " << maxElement << endl;

    return 0;
}
