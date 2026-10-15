#include <iostream>
using namespace std;

// GOAL: Build a growing collection out of scattered heap nodes.
// SKILLS: new, ->, walking a chain with a while loop, nullptr as "end of chain".
struct Node {
    int item;
    Node* next;
};

struct LinkedList {
    Node* first_node;
    int size;

    void append(int item) {
        // CREATE THE NEW NODE IN THE HEAP (not the stack!)
        Node* new_node_ptr = new Node;
        new_node_ptr->item = item;
        new_node_ptr->next = nullptr;

        // If the chain is empty, this becomes the first node.
        if (first_node == nullptr) {
            first_node = new_node_ptr;
            size++;
            return;
        }

        // Otherwise, walk to the end of the chain.
        Node* current_last = first_node;
        while (current_last->next != nullptr) {
            current_last = current_last->next;
        }
        current_last->next = new_node_ptr;
        size++;
    }

    // Get the node at some index by walking from the front.
    Node* get_node_at_index(int index) {
        Node* current_node = first_node;
        while (index > 0 && current_node != nullptr) {
            current_node = current_node->next;
            index--;
        }
        return current_node;
    }
};

int main() {
    LinkedList list;
    list.first_node = nullptr;
    list.size = 0;

    cout << list.size << endl;      // 0

    list.append(10);
    list.append(20);
    list.append(30);

    cout << list.size << endl;      // 3
    cout << list.first_node->next->next->item << endl;   // 30

    // A cleaner way to reach the same node:
    cout << list.get_node_at_index(2)->item << endl;     // 30
    return 0;
}