#include <iostream>
#include <string>

using namespace std;

int main() {
    string kata;
    cout << "Enter a string: ";
    getline(cin, kata);

    cout << "String terbalik: ";

    for (int i = kata.length() - 1; i >= 0; --i) {
        cout << kata[i];
    }

    cout << endl;

    return 0;
}
