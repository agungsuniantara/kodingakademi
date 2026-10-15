#include <iostream>
using namespace std;

// GOAL: Return n with its digits read right-to-left.
// 12345 -> 54321, and 1230 -> 321 (leading zeros disappear, that's correct!).
// SKILLS: % 10 extracts the last digit, / 10 removes it.
int digit_reverse(int n) {
    int result = 0;
    while (n > 0) {
        int last_digit = n % 10;   // peel off the last digit: 12345 % 10 = 5
        result = result * 10 + last_digit;  // shift result left, attach the digit
        n = n / 10;                // chop the last digit off: 12345 / 10 = 1234
    }
    return result;
}

int main() {
    cout << digit_reverse(12345) << endl;  // Should print 54321
    cout << digit_reverse(1230) << endl;   // Should print 321
    cout << digit_reverse(7) << endl;      // Should print 7
    return 0;
}