#include <iostream>
using namespace std;

int main() {
    int M, N;

    // Meminta pengguna memasukkan ukuran M dan N
    cout << "Masukkan jumlah baris (M): ";
    cin >> M;
    cout << "Masukkan jumlah kolom (N): ";
    cin >> N;

    // Alokasi dinamis untuk array 2D
    int** arr = new int*[N];
    
    for (int i = 0; i < M; i++) {
        arr[i] = new int[N];
    }

    // Mengisi array dengan angka berurutan mulai dari 1
    int num = 1;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            arr[i][j] = num++;
        }
    }

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }

    // Menghapus memori yang dialokasikan secara dinamis
    for (int i = 0; i < M; i++) {
        delete[] arr[i];
    }

    delete[] arr;


    return 0;
}
