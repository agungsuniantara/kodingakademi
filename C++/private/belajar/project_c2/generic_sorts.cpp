#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Rectangle {
    int width;
    int height;

    // Used by merge sort to choose the rectangle with the smaller area
    bool operator<(const Rectangle& right) {
        return width * height < right.width * right.height;
    }

    // Used by insertion sort to check if two rectangles need to be swapped
    bool operator>(const Rectangle& right) {
        return width * height > right.width * right.height;
    }
};

// T represents whatever type of array is passed into the function
template <typename T>
void insertion_sort(T arr[], int n) {
    // Go through each item and insert it into the sorted section
    for (int first_unsorted_index = 0; first_unsorted_index < n; first_unsorted_index++) {
        int current_index = first_unsorted_index;

        // Move the current item left while the previous item is larger
        while (current_index - 1 >= 0 && arr[current_index - 1] > arr[current_index]) {
            swap(arr[current_index - 1], arr[current_index]);
            current_index--;
        }
    }
}

// T allows merge sort to work with arrays of different types
template <typename T>
void merge_sort(T arr[], int n) {
    // An array with 0 or 1 item is already sorted
    if (n <= 1) {
        return;
    }

    // Divide the array into two halves
    int left_half_size = n / 2;
    int right_half_size = n - left_half_size;

    // Create temporary arrays using same generic type T
    T* left_half = new T[left_half_size];
    T* right_half = new T[right_half_size];

    // Copy the original items into the two halves
    for (int i = 0; i < n; i++) {
        if (i < left_half_size) {
            left_half[i] = arr[i];
        }
        else {
            right_half[i - left_half_size] = arr[i];
        }
    }

    // Recursively sort both halves
    merge_sort(left_half, left_half_size);
    merge_sort(right_half, right_half_size);

    // Keep track of the current position in both halves and the result
    int left_half_index = 0;
    int right_half_index = 0;
    int result_index = 0;

    // Compare the smallest unused item from each sorted half
    while (left_half_index < left_half_size && right_half_index < right_half_size) {
        // If the right item is smaller, copy it into the result
        if (right_half[right_half_index] < left_half[left_half_index]) {
            arr[result_index] = right_half[right_half_index];
            right_half_index++;
        }
        else {
            // Otherwise use the left item
            arr[result_index] = left_half[left_half_index];
            left_half_index++;
        }

        result_index++;
    }

    // Copy any items remaining in the left half
    while (left_half_index < left_half_size) {
        arr[result_index++] = left_half[left_half_index++];
    }

    // Copy any items remaining in the right half
    while (right_half_index < right_half_size) {
        arr[result_index++] = right_half[right_half_index++];
    }

    // Delete the temporary arrays created on the heap
    delete[] left_half;
    delete[] right_half;
}

// Added more tests to see if the generic sorting functions work with different cases
int main() {
    srand(time(nullptr));

    cout << "RANDOM RECTANGLE TEST" << endl;

    Rectangle rects_1[10], rects_2[10];
    
    for (int i = 0; i < 10; i++) {
        rects_1[i].width = rand() % 20;
        rects_1[i].height = rand() % 20;
        rects_2[i].width = rects_1[i].width;
        rects_2[i].height = rects_1[i].height;
    }
    
    insertion_sort(rects_1, 10);
    merge_sort(rects_2, 10);
    int last_area = -1;
    
    for (int i = 0; i < 10; i++) {
        int cur_area = rects_1[i].width * rects_1[i].height;
        if (cur_area < last_area) {
            cout << "Random Rectangle test failed!" << endl;
            return 1;
        }
        last_area = cur_area;
    }
    
    for (int i = 0; i < 10; i++) {
        if (rects_1[i].width != rects_2[i].width || rects_1[i].height != rects_2[i].height) {
            cout << "Random Rectangle test failed!" << endl;
            return 1;
        }
    }
    
    cout << "Random Rectangle test passed!" << endl;


    cout << endl << "INTEGER TEST" << endl;

    int nums_1[5] = {5, 1, 4, 2, 3};
    int nums_2[5] = {5, 1, 4, 2, 3};
    int expected_nums[5] = {1, 2, 3, 4, 5};

    insertion_sort(nums_1, 5);
    merge_sort(nums_2, 5);

    for (int i = 0; i < 5; i++) {
        if (nums_1[i] != expected_nums[i] ||
            nums_2[i] != expected_nums[i]) {

            cout << "Integer test failed!" << endl;
            return 1;
        }
    }

    cout << "Integer test passed!" << endl;


    cout << endl << "REVERSE RECTANGLE TEST" << endl;

    Rectangle reverse_1[4] = {
        {5, 5},
        {4, 4},
        {3, 3},
        {2, 2}
    };

    Rectangle reverse_2[4] = {
        {5, 5},
        {4, 4},
        {3, 3},
        {2, 2}
    };

    int expected_areas[4] = {4, 9, 16, 25};

    insertion_sort(reverse_1, 4);
    merge_sort(reverse_2, 4);

    for (int i = 0; i < 4; i++) {
        int area_1 = reverse_1[i].width * reverse_1[i].height;
        int area_2 = reverse_2[i].width * reverse_2[i].height;

        if (area_1 != expected_areas[i] ||
            area_2 != expected_areas[i]) {

            cout << "Reverse Rectangle test failed!" << endl;
            return 1;
        }
    }

    cout << "Reverse Rectangle test passed!" << endl;


    cout << endl << "EQUAL AREA TEST" << endl;

    Rectangle equal_1[4] = {
        {2, 6},
        {3, 4},
        {1, 5},
        {2, 3}
    };

    Rectangle equal_2[4] = {
        {2, 6},
        {3, 4},
        {1, 5},
        {2, 3}
    };

    insertion_sort(equal_1, 4);
    merge_sort(equal_2, 4);

    for (int i = 0; i < 4; i++) {
        if (equal_1[i].width != equal_2[i].width ||
            equal_1[i].height != equal_2[i].height) {

            cout << "Equal area test failed!" << endl;
            return 1;
        }
    }

    cout << "Equal area test passed!" << endl;

    cout << "Everything seems fine : )" << endl;
    return 0;
}