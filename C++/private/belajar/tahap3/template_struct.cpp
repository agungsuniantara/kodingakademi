#include <iostream>
#include <string>
using namespace std;

template <typename T>
struct Pair {
    T first;
    T second;

    T get_max() const {
        if (first > second) {
            return first;
        }
        return second;
    }
};

template <typename T>
struct Node {
    T data;
    Node<T>* next;   // pointer ke node bertipe sama
};

int main() {
    // Pair<int>
    Pair<int> p1;
    p1.first = 10;
    p1.second = 25;
    cout << p1.get_max() << endl;   // 25

    // Pair<string>
    Pair<string> p2 = {"apple", "banana"};
    cout << p2.get_max() << endl;   // banana

    // Node<int>: 2 node terhubung
    Node<int>* n1 = new Node<int>{1, nullptr};
    Node<int>* n2 = new Node<int>{2, nullptr};
    n1->next = n2;

    cout << n1->data << " -> " << n1->next->data << endl;   // 1 -> 2

    delete n2;
    delete n1;

    return 0;
}