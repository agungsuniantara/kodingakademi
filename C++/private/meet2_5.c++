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

void insertion_sort_buggy(int arr[], int n) {
    for (int first_unsorted_index = 1; first_unsorted_index < n; first_unsorted_index++) {
        int value_to_insert = arr[first_unsorted_index];
        int j = first_unsorted_index - 1;
        while (arr[j] > value_to_insert) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = value_to_insert;
    }
}

int main() {
    int arr1[] = {7, 2, 9, 4, 1};
    insertion_sort(arr1, 5);
    for (int i = 0; i < 5; i++) {
        cout << arr1[i] << " ";
    }
    cout << endl; // Output: 1 2 4 7 9

    int arr2[] = {1, 2, 3, 4, 5}; // array already sorted
    insertion_sort_buggy(arr2, 5);
    // j keeps decreasing past index 0: reads arr[-1], arr[-2], ...
    // Undefined behavior: crash or garbage results
    for (int i = 0; i < 5; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;

    return 0;
}
