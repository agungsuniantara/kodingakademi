#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    
    // Meminta pengguna memasukkan ukuran array
    cout << "Masukkan jumlah elemen (N): ";
    cin >> N;
    
    // Alokasi dinamis array dengan ukuran N
    string* array = new string[N];
    
    // Meminta pengguna memasukkan nilai ke dalam array
    cout << "Masukkan " << N << " string:" << endl;
    for (int i = 0; i < N; i++) {
        cin >> array[i];
    }
    
    // Menampilkan isi array
    cout << "Isi array:" << endl;
    for (int i = 0; i < N; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
    
    // Menghapus memori yang dialokasikan secara dinamis
    delete[] array;
    
    return 0;
}
