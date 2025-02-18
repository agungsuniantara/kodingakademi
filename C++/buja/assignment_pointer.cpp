#include <iostream>

using namespace std;

void hasil(int arr[5], int size){
    int *a[5];
    int hasil = 0;
    for (int i = 0; i < 5; i++){
        a[i] = &arr[i];
    }
    for (int i = 0; i < 5; i++){
        hasil += *a[i];
    }
    cout << hasil << "\n";
}

int main(){
    int arr[5] = {1,2,3,4,5};
    int *a;

    hasil(arr, 5);
}