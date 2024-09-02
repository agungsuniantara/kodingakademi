#include <iostream>
#include <string>

using namespace std;

int main() {
    int x[] = {1,2,3,4,5};
    int a[6] = {1,2,3,4,5,6};
    int c[6] = {1,2,3};
    int panjang = sizeof(x) / sizeof(x[0]);

    for (int i = 0; i < panjang; i++) {
        cout << x[i] << " ";
    }

    cout << "\n";

    int hasil[6];

    cout << "enter value : ";
    cin >> hasil[0];

    int panjang2 = sizeof(hasil) / sizeof(hasil[0]);

    for (int i = 0; i < panjang2; i++) {
        cout << hasil[i] << " ";
    }

    return 0;
}
