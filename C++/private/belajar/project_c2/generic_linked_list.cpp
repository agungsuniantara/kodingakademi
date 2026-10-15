#include <iostream>
using namespace std;

// T is the type of item stored in each node
template <typename T>
struct Node {
    T item;
    Node<T>* next = nullptr; // Points to next node in linked list
};

// T is the type of item stored in the linked list
template <typename T>
struct LinkedList {
    Node<T>* first_node = nullptr;
    
    int size = 0;
    
    // Add a new item to the end of the linked list
    void append(T item) {
        // Create a new node and store the given item inside it
        Node<T>* new_node = new Node<T>;
        new_node->item = item;

        // If the list is empty, the new node becomes the first node
        if (first_node == nullptr) {
            first_node = new_node;
        } 
        else {
            // Start from the first node
            Node<T>* current = first_node;

            // Move through the list until the last node is reached
            while (current->next != nullptr) {
                current = current->next;
            }
            // Connect the current final node to the new node
            current->next = new_node;
        }

        size++;
    }
    
    // Return the node at the given index
    Node<T>* get_node_at_index(int index) {
        // Reject indexes that are outside the linked list
        if (index < 0 || index >= size) {
            return nullptr;
        }

        Node<T>* current = first_node;

        // Move forward until the requested index is reached
        for (int i = 0; i < index; i++) {
            current = current->next;
        }

        return current;
    }
    
    // Change the item stored at the given index
    void set_index(int index, T item) {
        // Find the node at the requested index
        Node<T>* node = get_node_at_index(index);

        // Only change the value if the index was valid
        if (node != nullptr) {
            node->item = item;
        }
    }
    
    void display() {
        Node<T>* current = first_node;

        // Keep moving through nodes until nullptr is reached
        while (current != nullptr) {
            cout << current->item << " ";
            current = current->next;
        }

        cout << endl;
    }
};

// Added more tests to see if the generic linked list works with different types and edge cases
int main() {
    cout << "INTEGER LIST TEST" << endl;

    LinkedList<int> list;
    list.append(10);
    list.append(20);
    list.append(30);
    
    cout << "Linked List: ";
    list.display();
    
    list.set_index(1, 25);
    cout << "Linked List after setting index 1 to 25: ";
    list.display();
    
    cout << "Item at index 2: " << list.get_node_at_index(2)->item << endl;
    
    
    cout << endl << "STRING LIST TEST" << endl;

    LinkedList<string> names;
    names.append("Apple");
    names.append("Banana");
    names.append("Orange");

    cout << "Original list: ";
    names.display();

    names.set_index(1, "Mango");

    cout << "After setting index 1 to Mango: ";
    names.display();


    cout << endl << "INVALID INDEX TEST" << endl;

    if (list.get_node_at_index(-1) == nullptr) {
        cout << "Negative index correctly rejected" << endl;
    }

    if (list.get_node_at_index(10) == nullptr) {
        cout << "Index outside list correctly rejected" << endl;
    }

    return 0;
}