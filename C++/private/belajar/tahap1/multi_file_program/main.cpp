#include <iostream>
#include "algorithms.h"
#include "data_structures.h"
using namespace std;

int main() {
    int arr[4] = {5, 12, 3, 9};
    cout << find_max(arr, 4) << endl;   // 12

    ItemList list(10);
    list.add(Item{1, "post_A"});
    list.add(Item{2, "post_B"});
    cout << list.get_count() << endl;   // 2

    return 0;
}   // destructor ItemList otomatis dipanggil di sini

// terminal : g++ -std=c++11 -o program main.cpp algorithms.cpp data_structures.cpp
// run program : ./program

