#include <iostream>

using namespace std;

int main(){
    int angka1a, angka1b, angka2a, angka2b;
    double hasil;

    cout << "angka 1 (dua angka dipisah spasi): ";
    cin >> angka1a >> angka1b;
    cout << "angka 2 (dua angka dipisah spasi): ";
    cin >> angka2a >> angka2b;

    hasil = (angka1a + angka1b) + (angka2a + angka2b);

    cout << "hasil : " << hasil << endl;
    cout << "rata-rata : " << hasil / 4;
}