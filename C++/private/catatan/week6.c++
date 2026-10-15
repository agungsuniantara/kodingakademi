#include <iostream>
using namespace std;

void insertion_sort(int arr[], int n) {
    for (int first_unsorted_index = 1; first_unsorted_index < n; first_unsorted_index++) {
        int value_to_insert = arr[first_unsorted_index];
        int j = first_unsorted_index - 1;
        while (j >= 0 && arr[j] > value_to_insert) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = value_to_insert;
    }
}

int main() {
    int arr[] = {7, 2, 9, 4, 1};
    insertion_sort(arr, 5);
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    cout << endl; // Output: 1 2 4 7 9
    return 0;
}