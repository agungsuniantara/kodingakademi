#include <iostream>
using namespace std;

int frame_area(int w, int h, int b) {
    int inside_area = w * h;
    int outside_area = (w + 2*b) * (h + 2*b);
    return outside_area - inside_area;
}

int largest_frame_area(int w_vals[], int h_vals[], int b_vals[], int n) {
    int largest_frame = 0;
    for (int i = 0; i < n; i++) {
        largest_frame = max(largest_frame, frame_area(w_vals[i], h_vals[i], b_vals[i]));
        cout << largest_frame;
    }
    return largest_frame;
}

int largest_frame_area_buggy(int w_vals[], int h_vals[], int b_vals[], int n) {
    int largest_frame = 0;
    for (int i = 0; i < n - 1; i++) { // WRONG: the last frame is never checked
        largest_frame = max(largest_frame, frame_area(w_vals[i], h_vals[i], b_vals[i]));
        cout << largest_frame;
    }
    return largest_frame;
}

int main() {
    int w[] = {10, 5, 20};
    int h[] = {8, 5, 3};
    int b[] = {2, 1, 2};
    // Areas: 88, 24, 108
    cout << largest_frame_area(w, h, b, 3) << endl; // Output: 108

    cout << largest_frame_area_buggy(w, h, b, 3) << endl; // Output: 88 (WRONG, should be 108)
    return 0;
}
