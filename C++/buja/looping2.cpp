#include <iostream>

using namespace std;

int main(){
    string nama = "python";

    for (int i = 0; i < nama.length() - 1; i++){
        char temp = nama[i];
        if (nama[i + 1] > temp){
            nama[i] = nama[i + 1];
            nama[i + 1] = temp;
        }
    }

    cout << nama;

    return 0;
}