#include <iostream>

using namespace std;

int main(){
    int angka;
    double hasil;

    cout << "Fahrenheit : ";
    cin >> angka;

    hasil = (5.0 / 9.0) * (angka - 32);

    cout << "Hasil : " << hasil;
}