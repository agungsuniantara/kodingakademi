#include <iostream>
using namespace std;

int main(){
    int n;
    cout << "how many numbers? " << endl;
    cin >> n;

    int sum = 0;
    int i = 0;
    while (i < n){
        int value;
        cout << "enter number : " << i + 1 << ":" << endl;
        cin >> value;
        sum += value;
        i++;
    }
    cout << "sum is : " << sum << endl;
}

