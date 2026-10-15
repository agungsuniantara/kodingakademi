#include <iostream>

using namespace std;

int main(){
    // variabel = tempat untuk menyimpan value
    // tipe data = jenis data yang ada di dalam variabel
    // jenis - jenis tipe data:
    // int(integer) = tipe data untuk menyimpan bilangan bulat
    // float = tipe data untuk menyimpan bilangan koma
    // double = tipe data untuk menyimpan bilangan koma lebih banyak
    // string = tipe data untuk menyimpan teks / huruf
    // boolean = tipe data untuk menyimpan true / false
    // char = tipe data untuk menyimpan 1 karakter

    int angka = 20;
    float angka_desimal = 10.5f;
    double angka_double = 10.5;
    string nama = "agung";
    char huruf = 'a';
    bool benar = true;

    cout << "angka int = " << angka << "\n";
    cout << "angka float = " << angka_desimal << "\n";
    cout << "angka double = " << angka_double << "\n";
    cout << "nama string = " << nama << "\n";
    cout << "huruf char = " << huruf << "\n";
    cout << "benar boolean = " << benar << "\n";

    int angka_baru = 30;
    double angka_new = double(angka_baru);

    cout << "angka_baru = " << angka_baru << "\n";
    cout << "angka_new = " << angka_new << "\n";
}