#include <iostream>
using namespace std;

// GOAL: Print the largest value in the array.
// SKILLS: array indexing, if statements, the "assume then challenge" pattern.
int main() {
    int n;
    int arr[100000];

    cout << "How many numbers do we have?" << endl;
    cin >> n;
    cout << "Enter the numbers one by one:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Assume the first item is the maximum, then challenge that assumption.
    int max_value = arr[0];
    for (int i = 1; i < n; i++) {      // start at 1: index 0 is already our assumption
        if (arr[i] > max_value) {
            max_value = arr[i];        // new champion found
        }
    }

    cout << "Maximum value: " << max_value << endl;
    return 0;
}