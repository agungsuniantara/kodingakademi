#include <iostream>

using namespace std;

int main(){
    // for (int i = 1; i <= 9; i++){
    //     for (int z = 1; z <= 9; z++){
    //         cout << i << " x " << z << " = " << i * z << "\n";
    //     }
    // }

    for (int i = 0; i < 5; i++){
        for (int z = 0; z < 5; z++){
            if (i >= z){
                cout << "*";
            }
        }
        cout << "\n";
    }
}