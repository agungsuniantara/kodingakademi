#include "algorithms.h"

// Implementasi (definisi): kode aslinya
int find_max(const int* arr, int size) {
    int max_val = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max_val) {
            max_val = arr[i];
        }
    }
    return max_val;
}