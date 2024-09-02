#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

int main() {
    string kata;
    int i;

    cout << "masukan kata : ";
    getline(cin, kata);

    for (i = 0; i < kata.length(); i++){
        int ascii_int = static_cast<int>(kata[i]);

        if (ascii_int > 47 && ascii_int < 58){
            cout << "angka";
        }
        else{
            cout << "bukan angka / kalimat";
        }
    }

    return 0;
}
