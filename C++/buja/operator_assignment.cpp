#include <iostream>

using namespace std;

int main(){
    char input;

    cout << "input : ";
    cin >> input;

    bool huruf = (input >= 'a') && (input <= 'z');
    bool angka = (input >= '0') && (input <= '9');

    cout << huruf << "\n";
    cout << angka << "\n";

    int n = 2;

    n *= n; // n = n * n
    cout << n;
}