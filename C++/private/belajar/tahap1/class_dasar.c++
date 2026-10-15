#include <iostream>
#include <string>
using namespace std;

class PostAnalyser {
private:
    int batch_size;   // hanya bisa diakses dari dalam class

public:
    // Constructor dengan initialization list
    PostAnalyser(int n) : batch_size(n) {
        cout << "Analyser created with batch size " << batch_size << endl;
    }

    // Member function (method)
    int get_batch_size() const {   // 'const' = tidak mengubah objek
        return batch_size;
    }

    void set_batch_size(int n) {
        if (n > 0) {
            batch_size = n;
        }
    }
};

int main() {
    PostAnalyser analyser(5);          // constructor dipanggil otomatis
    cout << analyser.get_batch_size() << endl;  // 5

    analyser.set_batch_size(10);
    cout << analyser.get_batch_size() << endl;  // 10

    // analyser.batch_size = -1;  // ERROR: batch_size private
    return 0;
}