#include <iostream>
using namespace std;

// function void : function yang tidak mengembalikan nilai / menyelesaikan prosesnya langsung
void nama (){
    string nama = "buja";
    cout << nama << "\n";
}

// function parameter : function yang memiliki parameter untuk menyimpan value
void tampil_data(string nama, string alamat, int umur){
    cout << nama << "\n";
    cout << alamat << "\n";
    cout << umur << "\n";
}

// function return : function yang mengembalikan nilai
string hobi(){
    string data = "memasak";
    return data;
}

int hitung(int a, int b){
    return a + b;
}

int hitung2(int, int); // function prototype

int kali (int a, int b){
    return a * b; 
}

int balok(int p, int l, int t){ // function di dalam function
    int result = kali(p, l) * t;
    return result;
}

int rekursi(int a){ // function yang dapat memanggil dirinya sendiri
    if (a < 1){
        return 0;
    }
    cout << a;
    return rekursi(a - 1);
}

int main(){
    nama(); // panggil function void
    tampil_data("agung", "denpasar", 20); // panggil function parameter
    string hasil = hobi(); // panggil function return tanpa param
    cout << hasil << "\n";
    cout << hobi() << "\n"; // panggil function return tanpa param
    int result = hitung(10,20); // panggil function return pakai param
    cout << result << "\n"; 
    int result2 = hitung2(50,20);
    cout << result2 << "\n"; 
    int volume_balok = balok(30,40,50);
    cout << volume_balok << "\n"; 
    rekursi(10);

    return 0;
}

int hitung2 (int c, int d){
    return c * d;
}

