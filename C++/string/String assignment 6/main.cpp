#include <iostream>
#include <string>

using namespace std;

int main() {
    string s1, s2;
    cout << "Masukkan string: ";
    getline(cin, s1);
    s2 = s1;
    cout << "String yang disalin: " << s2 << endl;

    return 0;
}
