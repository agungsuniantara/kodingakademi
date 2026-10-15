#include <iostream>
using namespace std;

int frame_area(int w, int h, int b) {
    int inside_area = w * h;
    int outside_area = (w + 2*b) * (h + 2*b);
    return outside_area - inside_area;
}

int frame_area_fixed(int w, int h, int b) {
    if (w <= 0 || h <= 0 || b < 0) {
        return -1; // error code: invalid input
    }
    int inside_area = w * h;
    int outside_area = (w + 2*b) * (h + 2*b);
    return outside_area - inside_area;
}

int main() {
    // Photo 10 x 8, frame 2: inside = 80, outside = 168, frame = 88
    cout << frame_area(10, 8, 2) << endl; // Output: 88

    // Invalid input: negative photo width, or negative frame
    cout << frame_area(-10, 8, 2) << endl; // Output: 8 (nonsensical: inside = -80, outside = -72, frame = -72 - (-80) = 8)
    cout << frame_area(10, 8, -3) << endl; // Output: -72 (negative frame = "eating" the photo: inside = 80, outside = 8, frame = 8 - 80 = -72)

    cout << frame_area_fixed(10, 8, 2) << endl; // Output: 88
    cout << frame_area_fixed(-10, 8, 2) << endl; // Output: -1 (input rejected)

    return 0;
}


