#include <iostream>
using namespace std;

int main() {
    int M, N;

    // Meminta ukuran array dari user
    cout << "Masukkan jumlah baris (M): ";
    cin >> M;
    cout << "Masukkan jumlah kolom (N): ";
    cin >> N;

    // Alokasi dinamis array 2D
    int** array = new int*[M];
    for (int i = 0; i < M; ++i) {
        array[i] = new int[N];
    }

    // Input elemen array dari user
    cout << "Masukkan elemen array: " << endl;
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << "Elemen di baris " << i + 1 << " kolom " << j + 1 << ": ";
            cin >> array[i][j];
        }
    }

    // Menghitung dan menampilkan jumlah setiap baris
    cout << "\nJumlah setiap baris:" << endl;
    for (int i = 0; i < M; ++i) {
        int sumRow = 0;
        for (int j = 0; j < N; ++j) {
            sumRow += array[i][j];
        }
        cout << "Jumlah baris " << i + 1 << ": " << sumRow << endl;
    }

    // Menghitung dan menampilkan jumlah setiap kolom
    cout << "\nJumlah setiap kolom:" << endl;
    for (int j = 0; j < N; ++j) {
        int sumCol = 0;
        for (int i = 0; i < M; ++i) {
            sumCol += array[i][j];
        }
        cout << "Jumlah kolom " << j + 1 << ": " << sumCol << endl;
    }

    // Dealokasi memori
    for (int i = 0; i < M; ++i) {
        delete[] array[i];
    }
    delete[] array;

    return 0;
}
