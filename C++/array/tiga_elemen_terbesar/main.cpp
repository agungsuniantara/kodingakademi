#include <iostream>

using namespace std;

int main() {
    const int size = 10; // Ukuran array
    int arr[size] = {5, 10, 3, 15, 20, 25, 30, 35, 40, 45};

    // Menemukan tiga elemen terbesar dalam array
    int max1 = arr[0];
    int max2 = arr[0];
    int max3 = arr[0];

    for (int i = 1; i < size; ++i) {
        if (arr[i] > max1) {
            max3 = max2;
            max2 = max1;
            max1 = arr[i];
        } else if (arr[i] > max2) {
            max3 = max2;
            max2 = arr[i];
        } else if (arr[i] > max3) {
            max3 = arr[i];
        }
    }

    // Menampilkan tiga elemen terbesar
    cout << "Tiga elemen terbesar dalam array adalah: " << max1 << ", " << max2 << ", " << max3 << endl;

    return 0;
}
