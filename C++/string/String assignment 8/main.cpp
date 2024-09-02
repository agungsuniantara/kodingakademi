#include <iostream>
#include <string>

using namespace std;

int main() {
    string kata = "November";
    bool ada_e = false;

    // Memeriksa setiap karakter dalam kata
    for (int i = 0; i < kata.length(); i++) {
        if (kata[i] == 'e') {
            ada_e = true;
            break;
        }
    }

    // Menampilkan hasil
    if (ada_e) {
        cout << "Huruf 'e' ditemukan dalam kata 'November'." << endl;
    } else {
        cout << "Huruf 'e' tidak ditemukan dalam kata 'November'." << endl;
    }

    return 0;
}
