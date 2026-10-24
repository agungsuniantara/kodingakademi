#include <iostream>

using namespace std;

int main(){

    // control flow (if, else if, else)

    if (false){
        cout << "if berjalan" << endl;
    }
    else if (false){
        cout << "else if berjalan" << endl;
    }
    else {
        cout << "else berjalan" << endl;
    }

    string username = "agung";
    string password = "123";

    if (username == "agung" && password == "123"){
        cout << "halo admin" << endl;
    }
    else if (username == "user" && password == "123"){
        cout << "halo user" << endl;
    }
    else{
        cout << "account not found";
    }

    // control flow (switch)

    int pilih;

    cout << "masukan pilihan : ";
    cin >> pilih;

    switch(pilih){
        case 1:
            cout << "memilih pilihan 1" << endl;
            break;
        case 2:
            cout << "memilih pilihan 2" << endl;
            break;
        default:
            cout << "pilihan tidak tersedia" << endl;
            break;
    }
}