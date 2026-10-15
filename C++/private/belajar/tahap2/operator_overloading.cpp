#include <iostream>
using namespace std;

struct Rectangle {
    int width;
    int height;

    int get_area() const {
        return width * height;
    }

    // Rectangle < Rectangle lain: bandingkan berdasarkan area
    bool operator<(const Rectangle& right) const {
        return get_area() < right.get_area();
    }

    bool operator>(const Rectangle& right) const {
        return get_area() > right.get_area();
    }

    bool operator==(const Rectangle& right) const {
        return get_area() == right.get_area();
    }
};

int main() {
    Rectangle a = {2, 3};    // area 6
    Rectangle b = {4, 5};    // area 20

    cout << (a < b) << endl;   // 1 (true)
    cout << (a > b) << endl;   // 0 (false)
    cout << (a == b) << endl;  // 0 (false)

    Rectangle c = {1, 6};    // area 6, sama dengan a
    cout << (a == c) << endl;  // 1 (true, meski dimensi beda)

    return 0;
}