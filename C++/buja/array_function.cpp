#include <iostream>

using namespace std;

void tampil_array(int data[5]){
    for (int i = 0; i < 5; i++){
        cout << data[i] << "\n";
    }
}

void tampil_array2d(int data[2][2]){
    for (int i = 0; i < 2; i++){
        for (int z = 0; z < 2; z++){
            cout << data[i][z] << "\n";
        }
    }
}

void total (int data[5]){
    int hasil = 0;
    for (int i = 0; i < 5; i++){
        hasil += data[i]; // hasil = hasil + data[i]
    }
    cout << "Total = " << hasil << "\n";
}

int main(){
    int arr[5] = {1,2,3,4,5};
    tampil_array(arr);

    int arr2[2][2] = {{1,2}, {3,4}};

    cout << "akses index array 2 dimensi : " << "\n";
    cout << arr2[0][0] << "\n";

    cout << "for di dalam for array 2d" << "\n";
    tampil_array2d(arr2);

    return 0;
}