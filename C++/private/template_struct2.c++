#include <iostream>
using namespace std;

template <typename T>
struct Pair {
    T first;
    T second;

    void print() {
        cout << "First is " << first << " and second is " << second << endl;
    }
};

int main() {
    Pair<int> pair_int;    
    pair_int.first = 10;
    pair_int.second = 20;
    pair_int.print();      

    Pair<char> pair_char;   
    pair_char.first = 'x';
    pair_char.second = 'y';
    pair_char.print();    

    return 0;
}