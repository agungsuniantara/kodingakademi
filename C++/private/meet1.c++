#include <iostream>
using namespace std;

int factor(int n){
    if (n <= 1){
        return 1;
    }
    return n * factor(n - 1);
}

int largest_of_array(int arr[], int start, int end) {
    if (end == start + 1) {
        return arr[start];
    }

    int largest_of_left = largest_of_array(arr, start, (start + end) / 2);
    int largest_of_right = largest_of_array(arr, (start + end) / 2, end);

    if (largest_of_left > largest_of_right) {
        return largest_of_left;
    } else {
        return largest_of_right;
    }
}

// largest_of_left = arr, start(0) , end(4)
// {3, 8, 2, 7} [0, 4]
// {3,8} [0, 2]
// {2,7} [2, 4]

// largest_of_right = arr, start(5) , end(9)

int main(){
    int n;
    cout << "insert positive number : ";
    cin >> n;

    if (n < 0){
        cout << "factor negative number." << endl;
        return 1;
    }

    cout << n << "! = " << factor(n) << endl;

    int arr[] = {3, 8, 2, 7, 5, 9, 1, 6, 4};
    int a = sizeof(arr) / sizeof(arr[0]); // 45 / 5

    cout << "array : ";
    for (int i = 0; i < a; i++){
        cout << arr[i] << " ";
    }
    cout << endl;

    int terbesar = largest_of_array(arr, 0, a);
    cout << "elemen terbesar : " << terbesar << endl;
}