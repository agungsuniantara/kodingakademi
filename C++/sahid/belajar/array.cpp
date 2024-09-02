#include <iostream>

using namespace std;

int main(){
    int angka[3] = {10,20,30};

    cout << angka[0];
    cout << angka[1];
    cout << angka[2];

    for (int i = 0; i < 3; i++){
        cout << angka[i] << endl;
    }
}