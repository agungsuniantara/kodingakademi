#include <iostream>

using namespace std;

int main(){
    int angka = 10;
    int *p;
    p = &angka;
    int arr[3] = {1,2,3};
    int *a;
    a = &arr[0];
    
    cout << "alamat = " << &angka << " nilai = " << angka << "\n";
    *p = 50;
    cout << "alamat = " << p << " nilai = " << angka << "\n";
    cout << "nilai array = " << *a << "\n";
    *a = 30;
    cout << "nilai array = " << *a << "\n";
    cout << "nilai array asli = " << arr[0] << "\n";
}