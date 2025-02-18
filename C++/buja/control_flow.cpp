#include <iostream>

using namespace std;

int main(){
    int a, b, c;

    cout << "angka 1 : ";
    cin >> a;

    cout << "angka 2 : ";
    cin >> b; 

    cout << "angka 3 : ";
    cin >> c; 

    if (a < b){
        cout << "a lebih kecil dari b \n";
    }

    if (a > b){
        cout << "a lebih besar dari b \n";
    }
    else if ((a == b) || (a > c)){
        cout << "a sama dengan b atau a lebih besar dari c \n";
    }
    else{
        cout << "if atau else if salah \n";
    }

    int pilihan;

    cout << "masukan pilihan : ";
    cin >> pilihan;

    switch(pilihan){
        case 1:
            cout << "memilihi pilihan 1";
            break;
        case 2:
            cout << "memilihi pilihan 2";
            break;
        default:
            cout << "pilihan tidak tersedia";
            break;
    }

    return 0;
}