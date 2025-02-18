#include <iostream>

using namespace std;

int main(){
    int arr[5] = {1,2,3,4,5}; // array 1d
    int arr2[2][5] = {
        {1,2,3,4,5}, 
        {6,7,8,9,10}
        }; // array 2d
    cout << arr[0] << "\n";
    cout << arr2[0][0] << "\n";
    cout << arr2[1][0] << "\n";

    for (int i = 0; i < 5; i++){
        cout << arr[i] << "\n";
    };

    for (int i = 0; i < 2; i++){
        cout << "baris index = " << i << "\n";
        for (int z = 0; z < 5; z++){
            cout << arr2[i][z];
        }
        cout << "\n";
    };

    int a[2][5] = {
        {1,2,3,4,5},
        {6,7,8,9,10}
    };
    int b[2][5] = {
        {1,2,3,4,5},
        {6,7,8,9,10}
    };

    int c[2][5]; // c = {{ 6, 14, , , }}

    for (int i = 0; i < 1; i++){
        for(int z = 0; z < 5; z++){
            c[i][z] = a[i][z] * a[i + 1][z];
        }
    };

    cout << "hasil : " << "\n";
    for (int i = 0; i < 1; i++){
        for(int z = 0; z < 5; z++){
            cout << c[i][z] << " ";
        }
    };

    return 0;
}