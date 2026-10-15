#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int* solve(int n, int gates[], int keycards[]) {
    // Solve the reachability problem described in the spec.
    // n is the number of gates/keycards.
    // gates is the clearance level of each gate, read from top to bottom
    // keycards is the clearance level of each keycard, read from top to bottom
    // You should return an n length array where the ith index tells us how many gates
    // In the example in the spec, the input would be:
    // n: 8
    // gates: [5, 2, 3, 2, 2, 3, 1, 2]
    // keycards: [1, 4, 1, 1, 3, 2, 0, 2]
    // And your function should return:
    // [0, 1, 0, 0, 4, 0, 0, 2]

    int* result = new int[n]();

    struct Block {
        long long need; // lowest gate threshold inside the block
        long long gain; // maximum keycard collectable inside the block
        long long cnt;  // number of gates inside the block
    };

    // front == topmost block (smallest index)
    deque<Block> blocks;

    // Traveling up means facing gates i, i-1, ..., 0, so we process
    // start rooms from top (i = 0) to bottom (i = n-1).
    for (int i = 0; i < n; i++) {
        long long carry = keycards[i];
        long long gain  = keycards[i];
        long long opened = 0;

        // Gate i sits directly above room i, faced with room i's own card.
        if (carry >= gates[i]) {
            opened = 1;
            // Absorb every block above whose entry requirement is met.
            while (!blocks.empty() && carry >= blocks.front().need) {
                Block top = blocks.front();
                blocks.pop_front();
                opened += top.cnt;
                carry   = max(carry, top.gain);
                gain    = max(gain, top.gain);
            }
            result[i] = (int)opened;
            // The fused chain becomes one block anchored at gate i.
            blocks.push_front(Block{gates[i], gain, opened});
        } else {
            // Cannot open own gate: this room is a hard barrier.
            result[i] = 0;
            blocks.push_front(Block{gates[i], carry, 1});
        }
    }
    return result;
}

int ontrack_test() {
    int n;
    int* gates;
    int* keycards;
    cout << "Enter n: " << endl;
    cin >> n;
    gates = new int[n];
    keycards = new int[n];
    cout << "Enter gates: " << endl;
    for (int i = 0; i < n; i++) {
        cin >> gates[i];
    }
    cout << "Enter keycards: " << endl;
    for (int i = 0; i < n; i++) {
        cin >> keycards[i];
    }
    if (!cin) {
        cout << "ERROR: could not read input data" << endl;
        delete[] gates;
        delete[] keycards;
        return 1;
    }
    int* result = solve(n, gates, keycards);
    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    delete[] gates;
    delete[] keycards;
    delete[] result;
    return 0;
}

int main(int argc, char** argv) {
    if (argc != 1) {
        return ontrack_test();
    }
    int n = 8;
    int* gates = new int[] {5, 2, 3, 2, 2, 3, 1, 2};
    int* keycards = new int[] {1, 4, 1, 1, 3, 2, 0, 2};
    int* result = solve(n, gates, keycards);
    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    delete[] gates;
    delete[] keycards;
    delete[] result;
    return 0;
}