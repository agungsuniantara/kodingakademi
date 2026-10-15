#include <iostream>
using namespace std;

// GOAL: Return true if the array is sorted in non-decreasing order.
// NON-DECREASING means: every number is >= the one before it.
// SKILLS: passing arrays to functions, early return, comparing neighbours.
bool is_sorted(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        // Compare each item with the NEXT one.
        // If any neighbour pair is in the wrong order, we can stop immediately.
        if (arr[i] > arr[i + 1]) {
            return false;   // early exit: no need to check the rest
        }
    }
    return true;            // survived every check, so it's sorted
}

int main() {
    int n;
    int arr[100000];

    cout << "How many numbers do we have?" << endl;
    cin >> n;
    cout << "Enter the numbers one by one:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Ternary operator: condition ? value_if_true : value_if_false
    // Research this line if it looks unfamiliar (the readings encourage this!).
    cout << (is_sorted(arr, n) ? "YES" : "NO") << endl;
    return 0;
}