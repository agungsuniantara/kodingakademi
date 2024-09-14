#include <iostream>

using namespace std;

int main() {
    
    int data[2][3];
    // Meminta pengguna memasukkan nilai ke dalam array

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++){
            cin >> data[i][j];
        }
    }
    
    // Menghitung jumlah semua elemen dalam array
    int sum = 0;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++){
            sum += data[i][j];
        }
    }

    // Menampilkan hasil jumlah
    cout << "Jumlah dari semua elemen: " << sum << endl;
    
    return 0;
}
