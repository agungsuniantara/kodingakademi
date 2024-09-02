#include <iostream>
using namespace std;

int main(){
    int arr[] = {1,4,2,5,13,39,3};
    int n = 7;

    // NO 1

    int first = arr[0];

    for (int i = 0; i < n; i++){
        if (arr[i] > first){
            first = arr[i];
        }
    }

    cout << first;

    // NO 2

    cout << arr[0];
    cout << arr[6];

    cout << endl;

    // NO 3

    for (int i = 0; i < 6; i++){
        for (int j = 0; j < 6 - i; j++){
            if (arr[j] > arr[j + 1]){
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < 7; i++){
        cout << arr[i] << " ";
    }


}