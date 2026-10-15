#include <iostream>
using namespace std;

int main() {
    int n;
    int arr[100000];
    cout << "How many numbers do we have?" << endl;
    cin >> n;
    cout << "Enter the numbers one by one:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Swap first with last, second with second-last, ... stop at the middle.
    for (int i = 0; i < n / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - 1 - i];
        arr[n - 1 - i] = temp;
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}