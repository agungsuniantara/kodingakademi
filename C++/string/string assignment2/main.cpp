#include <iostream>
#include <string>

using namespace std;

int main() {
    string kata;
    string kata2;

    cout << "Enter a string: ";
    getline(cin, kata);

    cout << "String : ";

    for (int i = 0; i < kata.length(); i++) {
        int ascii_value = static_cast<int>(kata[i]) + 1;
        kata2 += static_cast<char>(ascii_value);
    }

    cout << kata2 << endl;

    return 0;
}
