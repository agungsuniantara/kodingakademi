#include <iostream>
using namespace std;

// GOAL: Read n numbers from the user and print their sum.
// SKILLS: cin >> , cout << , for loop, running total.
int main() {
    int n;
    cout << "How many numbers?" << endl;
    cin >> n;

    int sum = 0;
    for (int i = 0; i < n; i++) {
        int value;
        cout << "Enter number " << i + 1 << ":" << endl;
        cin >> value;      // notice: >> points INTO the variable
        sum += value;
    }

    cout << "The sum is: " << sum << endl;   // notice: << points OUT of the variable
    return 0;
}