#include <iostream>

using namespace std;

int main(){
    int data[6] = {2,10,3,4,1};
    int size = sizeof(data) / sizeof(data[0]);

    for (int i = 0; i < size - 1; i++){
        if (data[i] % 2 == 0){
            cout << data[i] << " angka genap." << "\n";
        }
        else{
            cout << data[i] << " angka ganjil." << "\n";
        }
    }
}