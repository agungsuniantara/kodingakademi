#include <iostream>
using namespace std;

int main() {
    string kata;
    int jumlah;

    cout << "Masukan kata : "; cin >> kata;
    cout << endl;
    cout << "Tentukan jumlah huruf yang muncul : "; cin >> jumlah;

    for (int j = jumlah; j > 0; j--) {
        for (int i = 0; i < j; i++) {
            cout << kata[i];
        }
        cout << endl;
    }

    return 0;
}