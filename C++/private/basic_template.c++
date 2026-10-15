#include <iostream>
#include <string>
using namespace std;

// Fungsi generic: bekerja dengan tipe apa pun asalkan kedua parameter sama tipenya
template <typename T>
T get_max(T a, T b) {
    if (a > b) {
        return a;
    }
    return b;
}

int main() {
    // T otomatis menjadi int
    cout << get_max(3, 7) << endl;        // Output: 7

    // T otomatis menjadi double
    cout << get_max(2.2, 4.9) << endl;    // Output: 4.9

    // T otomatis menjadi string
    cout << get_max(string("apel"), string("jeruk")) << endl;  // Output: jeruk

    // ERROR jika tipenya beda:
    // cout << get_max(2.2, 'c') << endl;
    // error: deduced conflicting types for parameter 'T' ('double' vs. 'char')

    return 0;
}