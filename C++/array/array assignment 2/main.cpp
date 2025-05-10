#include <iostream>
using namespace std;

int main(){
    // int arr[] = {1,4,2,5,13,39,3};
    // int n = 7;

    // // NO 1

    // int first = arr[0];

    // for (int i = 0; i < n; i++){
    //     if (arr[i] > first){
    //         first = arr[i];
    //     }
    // }

    // cout << first;

    // // NO 2

    // cout << arr[0];
    // cout << arr[6];

    // cout << endl;

    // // NO 3

    // for (int i = 0; i < 6; i++){
    //     for (int j = 0; j < 6 - i; j++){
    //         if (arr[j] > arr[j + 1]){
    //             int temp = arr[j];
    //             arr[j] = arr[j + 1];
    //             arr[j + 1] = temp;
    //         }
    //     }
    // }

    // for (int i = 0; i < 7; i++){
    //     cout << arr[i] << " ";
    // }

    // No 5

    int size, position, value;
    
    cout << "size = ";
    cin >> size;
    
    int arr2[size]; // Declare array with size from user input
    
    for (int i = 0; i < size; i++){
        cout << "masukkan nilai index ke-" << i << ": ";
        cin >> arr2[i];
    }
    
    cout << "\nArray sekarang: ";
    for (int i = 0; i < size; i++){
        cout << arr2[i] << " ";
    }
    cout << endl;
    
    cout << "position = ";
    cin >> position;
    
    if(position >= 0 && position < size) {
        cout << "masukan nilai: ";
        cin >> value;
        
        arr2[position] = value;
        
        cout << "\nArray setelah perubahan: ";
        for (int i = 0; i < size; i++){
            cout << arr2[i] << " ";
        }
        cout << endl;
    } else {
        cout << "Posisi tidak valid! Harus antara 0 dan " << (size-1) << endl;
    }

}