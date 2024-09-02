#include <iostream>

using namespace std;

int main(){
    int x = 1, y = 2, z[10];
    int *ip;          /* ip is a pointer to int*/

    ip = &x;          /* ip now points to x */
    cout << ip << endl;

    y = *ip;          /* y is now 1 */
    cout << y << endl;

    *ip = 0;          /* x is now 0 */
    cout << x << endl;

    ip = &z[0];       /* ip now points to z[0] */
    cout << ip << endl;

    *ip = 100;
    cout << z[0] << endl;

    
}