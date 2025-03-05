#include <iostream> 

using namespace std;

int main(){
    int n;
    cout << "masukan n :";
    cin >> n;

    int hasil = 2;

    for (int i = 1; i < n; i++){
        hasil *= 2;
    }
    cout << hasil;
}