#include <iostream>
using namespace std;

// invariant
int total_coins(int coins[], int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total = total + coins[i];
    }
    return total;
}

// not invariant
int total_coins_buggy(int coins[], int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total = total + coins[i];
        if (total > 15) {
            total = 0; // reset: this is where the invariant breaks
        }
    }
    return total;
}

int main() {
    int coins[] = {5, 3, 8, 2};
    cout << "Total: " << total_coins(coins, 4) << endl; // Output: 18
    cout << "Total: " << total_coins_buggy(coins, 4) << endl; // Output: 2 (WRONG, should be 18)
    
    return 0;
}
