#pragma once

// Merge sort and binary search helpers for PostAnalyser
// All algorithms are generic and work with any type that supports operator<

// Merge two sorted subarrays into one sorted array
// left..mid is the first sorted part
// mid+1..right is the second sorted part
// After this function, arr[left..right] is fully sorted
template <typename T>
void merge(T arr[], int left, int mid, int right) {
    int left_size = mid - left + 1;
    int right_size = right - mid;

    // Create temporary arrays to hold the two halves
    T* left_arr = new T[left_size];
    T* right_arr = new T[right_size];

    // Copy data from the original array into the temporary arrays
    for (int i = 0; i < left_size; i++) {
        left_arr[i] = arr[left + i];
    }
    for (int j = 0; j < right_size; j++) {
        right_arr[j] = arr[mid + 1 + j];
    }

    // Merge the two temporary arrays back into arr[left..right]
    int i = 0;
    int j = 0;
    int k = left;
    while (i < left_size && j < right_size) {
        // Pick the smaller element from either left_arr or right_arr
        if (left_arr[i] < right_arr[j]) {
            arr[k] = left_arr[i];
            i++;
        } else {
            arr[k] = right_arr[j];
            j++;
        }
        k++;
    }
    // If any elements remain in left_arr, copy them over
    while (i < left_size) {
        arr[k] = left_arr[i];
        i++;
        k++;
    }
    // If any elements remain in right_arr, copy them over
    while (j < right_size) {
        arr[k] = right_arr[j];
        j++;
        k++;
    }

    // Clean up the temporary arrays
    delete[] left_arr;
    delete[] right_arr;
}

// Recursively sort an array using merge sort
// Splits the array in half, sorts each half, then merges them back together
template <typename T>
void merge_sort(T arr[], int left, int right) {
    // Base case: a single element is already sorted
    if (left >= right) {
        return;
    }
    // Find the middle point to split the array into two halves
    int mid = left + (right - left) / 2;
    // Recursively sort the left half
    merge_sort(arr, left, mid);
    // Recursively sort the right half
    merge_sort(arr, mid + 1, right);
    // Merge the two sorted halves
    merge(arr, left, mid, right);
}

// Search for the smallest likes value that is strictly greater than threshold
// The array must already be sorted in ascending order by likes
// Uses a modified binary search that keeps track of the best candidate seen so far
// Returns the index of that candidate, or -1 if every element is <= threshold
template <typename T>
int binary_search_over_threshold(const T* arr, int size, int threshold) {
    int result = -1;
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid].likes > threshold) {
            // This element is above the threshold
            // Record it as a candidate and look for a smaller one on the left
            result = mid;
            high = mid - 1;
        } else {
            // This element is not above the threshold
            // Look for candidates on the right instead
            low = mid + 1;
        }
    }
    return result;
}

// Search for an element with exactly the given likes value
// The array must already be sorted in ascending order by likes
// Standard binary search: compare the middle element and narrow the search range
// Returns the index of the matching element, or -1 if not found
template <typename T>
int binary_search_exact_likes(const T* arr, int size, int likes) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid].likes == likes) {
            return mid;
        } else if (arr[mid].likes < likes) {
            // The target must be in the right half
            low = mid + 1;
        } else {
            // The target must be in the left half
            high = mid - 1;
        }
    }
    return -1;
}


