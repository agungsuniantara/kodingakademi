#include <iostream>
using namespace std;

int frame_perimeter(int w, int h, int b) {
    int outside_width = w + 2*b;
    int outside_height = h + 2*b;
    return 2 * (outside_width + outside_height);
}

int frame_perimeter_buggy(int w, int h, int b) {
    int outside_width = w + b; // WRONG: only one side
    int outside_height = h + b; // WRONG: only one side
    return 2 * (outside_width + outside_height);
}

int main() {
    // Photo 10 x 8, frame 2: perimeter = 2 * (14 + 12) = 52
    cout << frame_perimeter(10, 8, 2) << endl; // Output: 52

    cout << frame_perimeter_buggy(10, 8, 2) << endl; // Output: 40 (WRONG, should be 52)
    return 0;
}
