#include <iostream>

using namespace std;

int main(){
    int baru[7] = {2,10,3,4,1,7,8};

    // ascending
    for (int i = 0; i < 6; i++) {
        for (int z = 0; z < 6 - i; z++) { 
            if (baru[z] > baru[z + 1]) { 
                int temp = baru[z];
                baru[z] = baru[z + 1];
                baru[z + 1] = temp;
            }
        }
    }

    for (int i = 0; i < 7; i++){
        cout << baru[i] << "\n";
    }

    int data[7] = {2,10,3,4,1,7};

    // max number 
    int max = data[0];

    for (int i = 1; i < 6; i++) {
        if (data[i] > max) {
            max = data[i];
        }
    }

    cout << "max number : " << max << "\n";
}