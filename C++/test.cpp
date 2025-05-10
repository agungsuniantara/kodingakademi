#include <iostream>

using namespace std;

int main(){
    // int a = 10;
    // int *c = &a;

    // cout << "alamat a : " << &a << endl;
    // cout << "isi c : " << c << endl;
    // cout << "nilai a : " << *c << endl;

    // *c = 20;
    // cout << "nilai a : " << a << endl;


    int a[2][2] = {
        {1,2},
        {3,4}
    };

    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 2; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }


}