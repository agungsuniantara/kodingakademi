#include <iostream>
#include <string>
using namespace std;

// T ditentukan oleh argumen saat pemanggilan
template <typename T>
T get_max(T a, T b) {
    if (a > b) {
        return a;
    }
    return b;
}

template <typename T>
T get_min(T a, T b) {
    if (a < b) {
        return a;
    }
    return b;
}

template <typename T>
void swap_values(T& a, T& b) {   // T& = reference, agar pertukaran terlihat pemanggil
    T temp = a;
    a = b;
    b = temp;
}

int main() {
    // T = int
    cout << get_max(3, 7) << endl;        // 7
    cout << get_min(3, 7) << endl;        // 3

    // T = double
    cout << get_max(2.5, 1.8) << endl;    // 2.5

    // T = string
    cout << get_max(string("apple"), string("banana")) << endl;  // banana

    // T = char
    cout << get_min('x', 'a') << endl;    // a

    int i1 = 1;
    int i2 = 99;
    swap_values(i1, i2);
    cout << i1 << " " << i2 << endl;      // 99 1

    // ERROR jika tipe campur: get_max(3, 2.5)
    // -> compiler bingung T = int atau double (tidak ada konversi otomatis ke satu T)
    // Solusi: eksplisitkan tipe
    cout << get_max<double>(3, 2.5) << endl;   // 2.5

    return 0;
}