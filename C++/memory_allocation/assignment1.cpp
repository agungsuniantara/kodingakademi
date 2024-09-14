#include <iostream>

using namespace std;

int main() {
    int N;
    
    // Meminta pengguna memasukkan ukuran array
    cout << "Masukkan jumlah elemen (N): ";
    cin >> N;
    
    // Alokasi dinamis array dengan ukuran N
    int* array = new int[N];
    
    // Meminta pengguna memasukkan nilai ke dalam array
    cout << "Masukkan " << N << " bilangan bulat:" << endl;
    for (int i = 0; i < N; i++) {
        cout << "Elemen ke-" << i + 1 << ": ";
        cin >> array[i];
    }
    
    // Menghitung jumlah semua elemen dalam array
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += array[i];
    }
    
    // Menampilkan hasil jumlah
    cout << "Jumlah dari semua elemen: " << sum << endl;
    
    // Menghapus memori yang dialokasikan secara dinamis
    delete[] array;
    
    return 0;
}
