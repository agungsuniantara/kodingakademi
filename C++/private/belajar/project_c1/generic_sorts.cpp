#include <iostream>
using namespace std;

// ================= Struct Rectangle (sesuai soal C1) =================
struct Rectangle {
    int width;
    int height;

    int get_area() const {
        return width * height;
    }

    // Perbandingan berdasarkan area
    bool operator<(const Rectangle& right) const {
        return get_area() < right.get_area();
    }

    bool operator>(const Rectangle& right) const {
        return get_area() > right.get_area();
    }
};

// ================= Insertion Sort Generik =================
// Syarat pada T: punya operator> dan bisa di-copy (assignment)
template <typename T>
void insertion_sort(T arr[], int size) {
    for (int i = 1; i < size; i++) {
        T key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// ================= Merge Sort Generik =================
// Syarat pada T: punya operator< dan bisa di-copy (assignment)
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

// ================= Helper untuk testing =================
template <typename T>
void print_array(const T* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void print_rectangles(const Rectangle* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i].width << "x" << arr[i].height
             << " (area " << arr[i].get_area() << ")" << endl;
    }
}

int main() {
    // Uji 1: Insertion Sort pada int
    int ints1[6] = {5, 2, 9, 1, 5, 6};
    insertion_sort(ints1, 6);
    cout << "Insertion sort ints: ";
    print_array(ints1, 6);

    // Uji 2: Insertion Sort pada Rectangle (per area)
    Rectangle rects1[4] = {
        {2, 3},    // area 6
        {4, 5},    // area 20
        {1, 2},    // area 2
        {3, 3}     // area 9
    };
    insertion_sort(rects1, 4);
    cout << "Insertion sort rectangles:" << endl;
    print_rectangles(rects1, 4);

    // Uji 3: Merge Sort pada int
    int ints2[6] = {38, 27, 43, 3, 9, 82};
    merge_sort(ints2, 0, 5);
    cout << "Merge sort ints: ";
    print_array(ints2, 6);

    // Uji 4: Merge Sort pada Rectangle (per area)
    Rectangle rects2[4] = {
        {2, 3},    // area 6
        {4, 5},    // area 20
        {1, 2},    // area 2
        {3, 3}     // area 9
    };
    merge_sort(rects2, 0, 3);
    cout << "Merge sort rectangles:" << endl;
    print_rectangles(rects2, 4);

    return 0;
}