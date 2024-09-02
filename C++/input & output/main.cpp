#include <iostream>

using namespace std;

int main()
{
    int angka, angka2;
    string kata1, kata2;

    cout << "masukkan angka1 : " << endl;
    cin >> angka;

    cout << "masukkan angka2 : " << endl;
    cin >> angka2;

    cout << "masukan kata1 : " << endl;
    cin >> kata1;

    cout << "masukan kata2 : " << endl;
    cin >> kata2;

    cout << "angka adalah : " << angka << angka2 << endl;

    cout << "kata adalah : " << kata1 << kata2 << endl;

    printf("angka adalah : %d%d", angka, angka2);

    return 0;
}
