#include <iostream>
#include <string>

using namespace std;

int main() {
    string s1, s2;

    // Meminta pengguna untuk memasukkan dua string
    cout << "Masukkan string pertama: ";
    getline(cin, s1);

    cout << "Masukkan string kedua: ";
    getline(cin, s2);

    // Membandingkan dua string
    if (s1 == s2) {
        cout << "Kedua string sama." << endl;
    } else {
        cout << "Kedua string berbeda." << endl;
    }

    return 0;
}
