#include <iostream>
using namespace std;

int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1; // tidak ditemukan
}

int main() {
    int data[] = {1, 5, 8, 10, 20}; // Data terurut
    int n = 5;
    int cari = 9;

    int hasil = binarySearch(data, n, cari);

    if (hasil != -1)
        cout << "Data ditemukan di indeks: " << hasil << endl;
    else
        cout << "Data tidak ditemukan" << endl;
    return 0;
}
