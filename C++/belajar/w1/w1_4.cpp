#include <iostream>
using namespace std;

// GOAL: Print the array contents in reverse order.
// SKILLS: counting a loop backwards, index arithmetic.
int main() {
    int n;
    int arr[100000];

    cout << "How many numbers do we have?" << endl;
    cin >> n;
    cout << "Enter the numbers one by one:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Walk backwards: start at the LAST index (n - 1), go down to 0.
    for (int i = n - 1; i >= 0; i--) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}