#include <iostream>
using namespace std;

// Constructor = fungsi khusus yang otomatis dipanggil saat objek dibuat
// Namanya SAMA dengan nama class, TANPA return type
class DemoAnalyser {
private:
    int batch_size;   // data yang disimpan saat konstruksi

public:
    // Constructor dengan parameter: dipanggil saat 'DemoAnalyser d(5);'
    DemoAnalyser(int n) {
        batch_size = n;
        cout << "Constructor dipanggil, batch size = " << batch_size << endl;
    }

    int get_batch_size() {
        return batch_size;
    }
};

int main() {
    DemoAnalyser d(5);   // otomatis memanggil constructor dengan n = 5
    cout << "Batch size tersimpan: " << d.get_batch_size() << endl;
    return 0;
}