#include <iostream>
#include <string>

using namespace std;

int main()
{
    //variabel

    int x[] = {1,2,3,4,5};
    int a[5] = {1,2,3,4,5};
    int c[5] = {1,2,3};
    int d[10];

    //akses manual

    cout << x[0] << endl;
    cout << x[1] << endl;

    x[1] = 10;
    cout << x[1] << endl;

    //input manual

    cout << "masukan value : ";
    cin >> d[0];
    cout << d[0] << endl;

    //akses for

    int panjang_array = sizeof(a) / sizeof(a[0]);

    for (int i = 0; i < panjang_array; i++){
        cout << a[i] << " ";
    }

    cout << "\n";

    //input for

    for (int i = 0; i < 10; i++){
        cout << "masukan value : ";
        cin >> d[i];
    }

    int panjang_array2 = sizeof(d) / sizeof(d[0]);

    for (int i = 0; i < panjang_array2; i++){
        cout << d[i] << " ";
    }

    return 0;
}
