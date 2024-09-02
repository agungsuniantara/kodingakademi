#include <iostream>

using namespace std;

int main() {
    string input;

    cout << "Enter a string: ";
    getline(cin, input);

    for (char c = 'a'; c <= 'z'; c++) { // c = a
        for (int i = 0; i < input.length(); i++) {
            if (tolower(input[i]) == c) {
                cout << input[i];
            }
        }
    }
    return 0;
}
