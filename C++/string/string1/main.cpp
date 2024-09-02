#include <iostream>

using namespace std;

int main()
{
    char kata[100];
    char kata1[100];
    char *str100 = "jijijiji";
    char str1[] = "C++";
    char str2[4] = {'C', '+', '+'};
    char str3[4] = "C++";
    char str4[100] = "C++";
    string kata6;

    cout << str1 << endl;
    cout << str2 << endl;
    cout << str3 << endl;
    cout << str4 << endl;

    // cout << "enter a string : ";
    // cin >> kata;
    // cout << kata << endl;

    // cout << "enter a string : ";
    // cin.get(kata1, 100);
    // cout << kata1 << endl;

    cout << "enter a string : ";
    getline(cin, kata6);
    cout << kata6;

    return 0;
}
