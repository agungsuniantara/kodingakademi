#include <iostream>
using namespace std;

int main() {
    string kata = "STIKOMBALI";
    int angka = 10;
    int jumlah;

    cout << "Tentukan jumlah huruf yang muncul : ";
    cin >> jumlah;

    for (int j = jumlah; j > 0; j--) {
        for (int i = 0; i < j; i++) {
            cout << kata[i];
        }
        cout << endl;
    }
    return 0;
}