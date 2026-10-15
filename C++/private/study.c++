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
int largest_of_array(int arr[], int start, int end) {
    if (end == start + 1) {
        return arr[start];
    }

    int largest_of_left = largest_of_array(arr, start, (start + end) / 2);
    int largest_of_right = largest_of_array(arr, (start + end) / 2, end);

    if (largest_of_left > largest_of_right) {
        return largest_of_left;
    } else {
        return largest_of_right;
    }
}

int main() {
    int arr[] = {7, 2, 9, 4, 1};
    insertion_sort(arr, 5);
    cout << "array after sorting : " << endl;
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    int max = largest_of_array(arr, 0, 5);
    cout << "max element : " << max << endl;

    return 0;
}
