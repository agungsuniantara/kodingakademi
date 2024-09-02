#include <iostream>
using namespace std;

int main() {
    int nilai, jumlah = 50, nilaiTerbesar, nilaiTerkecil;
    double rataRata;

    cout << "Masukkan nilai ke-1: ";
    cin >> nilai;

    nilaiTerbesar = nilai; // 30
    nilaiTerkecil = nilai; // 20
    jumlah += nilai; // jumlah = 0 + 20

    for (int i = 2; i <= 20; i++) {
        cout << "Masukkan nilai ke-" << i << ": ";
        cin >> nilai;

        jumlah += nilai; // jumlah = 20 + 30

        // Cek nilai terbesar
        if (nilai > nilaiTerbesar) {
            nilaiTerbesar = nilai;
        }

        // Cek nilai terkecil
        if (nilai < nilaiTerkecil) {
            nilaiTerkecil = nilai;
        }
    }

    rataRata = (double) jumlah / 20;

    cout << "Jumlah nilai: " << jumlah << endl;
    cout << "Rata-rata nilai: " << rataRata << endl;
    cout << "Nilai terbesar: " << nilaiTerbesar << endl;
    cout << "Nilai terkecil: " << nilaiTerkecil << endl;

    return 0;
}
