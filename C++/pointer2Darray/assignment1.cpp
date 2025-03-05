#include <iostream>
using namespace std;

int main() {
    int M, N;

    // Meminta ukuran array dari user
    cout << "Masukkan jumlah baris (M): ";
    cin >> M;
    cout << "Masukkan jumlah kolom (N): ";
    cin >> N;

    // Alokasi dinamis untuk array 2D
    int** arr = new int*[M];
    
    for (int i = 0; i < M; i++) {
        arr[i] = new int[N];
    }

    cout << "Masukkan angka : ";
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}
