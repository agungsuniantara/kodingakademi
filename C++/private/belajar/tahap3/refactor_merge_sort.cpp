#include <iostream>
using namespace std;

// ================= Merge Sort generik =================

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
        if (left_arr[i] < right_arr[j]) {   // butuh operator< pada T
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

// ================= Struct Rectangle (soal C1) =================

struct Rectangle {
    int width;
    int height;

    int get_area() const {
        return width * height;
    }

    bool operator<(const Rectangle& right) const {
        return get_area() < right.get_area();
    }
};

int main() {
    // Uji 1: int
    int ints[6] = {38, 27, 43, 3, 9, 82};
    merge_sort(ints, 0, 5);
    for (int i = 0; i < 6; i++) {
        cout << ints[i] << " ";
    }
    cout << endl;

    // Uji 2: Rectangle, terurut berdasarkan area
    Rectangle rects[4] = {
        {2, 3},    // area 6
        {4, 5},    // area 20
        {1, 2},    // area 2
        {3, 3}     // area 9
    };
    merge_sort(rects, 0, 3);
    for (int i = 0; i < 4; i++) {
        cout << rects[i].width << "x" << rects[i].height
             << " (area " << rects[i].get_area() << ")" << endl;
    }

    return 0;
}