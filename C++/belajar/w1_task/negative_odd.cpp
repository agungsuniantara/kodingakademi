#include <iostream>
using namespace std;

// GOAL: Print how many numbers in the array are even.
// SKILLS: if inside a loop, counter variable, modulo operator.
int main() {
    int n;
    int arr[100000];

    cout << "How many numbers do we have?" << endl;
    cin >> n;
    cout << "Enter the numbers one by one:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0 && arr[i] % 2 != 0) {   
            count++;
        }
    }

    cout << "Negative and odd: " << count << endl;
    return 0;
}