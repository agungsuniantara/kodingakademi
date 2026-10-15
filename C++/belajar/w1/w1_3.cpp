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

    int even_count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {   // % gives the remainder: even numbers have remainder 0
            even_count++;
        }
    }

    cout << "Even numbers: " << even_count << endl;
    return 0;
}