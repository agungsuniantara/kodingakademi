#include <iostream>

using namespace std;

int main(){
    // int (integer) = tipe data untuk menyimpan bilangan bulat
    // float = tipe data untuk menyimpan bilangan koma
    // double = tipe data untuk menyimpan bilangan koma yang lebih banyak
    // string = tipe data untuk menyimpan huruf / teks
    // char = tipe data untuk menyimpan 1 karakter
    // boolean = tipe data untuk menyimpan true / false
    
    int angka1 = 20;
    float angka2 = 10.5f;
    double angka3 = 90.5;
    string nama = "buja";
    char huruf = 'a';
    bool benar = true;

    cout << "angka 1 = " << angka1 << "\n";
    cout << "angka 2 = " << angka2 << "\n";
    cout << "angka 3 = " << angka3 << "\n";
    cout << "nama = " << nama << "\n";
    cout << "huruf = " << huruf << "\n";
    cout << "benar = " << benar << "\n";

    double angka5 = 40.5;
    int angka5_int = int(angka5);

    int angka6 = 10;
    double angka6_double = double(angka6);

    cout << "angka5 = " << angka5 << "\n";
    cout << "angka5 int = " << angka5_int << "\n";

    cout << "angka6 = " << angka6 << "\n";
    cout << "angka6 double = " << angka6_double << "\n";

    int test1, test2;

    test1 = 10;
    test2 = 20;

    cout << "test1 = " << test1 << "\n";
    cout << "test2 = " << test2 << "\n";
}