#include <iostream>
using namespace std;

int main() {
    int rows, cols;

    // Meminta input jumlah baris dan kolom
    cout << "Masukkan jumlah baris: ";
    cin >> rows;
    cout << "Masukkan jumlah kolom: ";
    cin >> cols;

    // Alokasi dinamis untuk matrix 2D
    char** matrix = new char*[rows];
    for (int i = 0; i < rows; ++i) {
        matrix[i] = new char[cols];
    }

    // Meminta input elemen matrix dari pengguna
    cout << "Masukkan elemen matrix:" << endl;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) { 
            cout << "Elemen [" << i << "][" << j << "]: ";
            cin >> matrix[i][j];
        }
    }

    if (rows != cols) {
        cout << "Matrix ini tidak simetris." << endl;  // Matrix tidak simetris jika jumlah baris tidak sama dengan jumlah kolom
        return 0;
    }
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (matrix[i][j] != matrix[j][i]) {
                cout << "Matrix ini tidak simetris." << endl;  // Jika elemen di posisi (i, j) tidak sama dengan elemen di (j, i)
                return 0;
            }
        }
    }

    cout << "Matrix ini simetris." << endl;

    // Menghapus alokasi dinamis
    for (int i = 0; i < rows; ++i) {
        delete[] matrix[i];
    }
    delete[] matrix;

    return 0;
}
