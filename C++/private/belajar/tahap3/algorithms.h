#ifndef ALGORITHMS_H
#define ALGORITHMS_H

template <typename T>
void merge_sort(T arr[], int left, int right);

template <typename T>
void merge(T arr[], int left, int mid, int right);

// Implementasi langsung di header (wajib untuk template)
template <typename T>
void merge_sort(T arr[], int left, int right) {
    if (left >= right) {
        return;
    }
    int mid = left + (right - left) / 2;
    merge_sort(arr, left, mid);
    merge_sort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

template <typename T>
void merge(T arr[], int left, int mid, int right) {
    int left_size = mid - left + 1;
    int right_size = right - mid;

    T* left_arr = new T[left_size];
    T* right_arr = new T[right_size];

    for (int i = 0; i < left_size; i++) {
        left_arr[i] = arr[left + i];
    }
    for (int j = 0; j < right_size; j++) {
        right_arr[j] = arr[mid + 1 + j];
    }

    int i = 0;
    int j = 0;
    int k = left;
    while (i < left_size && j < right_size) {
        if (left_arr[i] < right_arr[j]) {
            arr[k] = left_arr[i];
            i++;
        } else {
            arr[k] = right_arr[j];
            j++;
        }
        k++;
    }
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

#endif  // ALGORITHMS_H