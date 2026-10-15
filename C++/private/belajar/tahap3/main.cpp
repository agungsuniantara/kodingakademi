#include <iostream>
#include "algorithms.h"
using namespace std;

int main() {
    int ints[5] = {5, 2, 9, 1, 6};
    merge_sort(ints, 0, 4);
    for (int i = 0; i < 5; i++) {
        cout << ints[i] << " ";
    }
    cout << endl;
    return 0;
}

// g++ -o program main.cpp
// ./program