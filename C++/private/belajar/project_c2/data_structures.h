#pragma once

// A node stores one item and a pointer to the next node in the list
// T is the type of the item being stored
template <typename T>
struct Node {
    T data;
    Node<T>* next;

    // Create a new node holding a copy of the given value
    Node(const T& value) : data(value), next(nullptr) {}
};

// A singly linked list that stores items of type T
// Reused from the C1 generic linked list implementation
template <typename T>
struct LinkedList {
    // Pointer to the first node in the list, or nullptr if empty
    Node<T>* head;
    // Number of nodes currently in the list
    int count;

    // Start with an empty list
    LinkedList() : head(nullptr), count(0) {}

    // Walk through every node and delete it to avoid memory leaks
    ~LinkedList() {
        Node<T>* current = head;
        while (current != nullptr) {
            Node<T>* to_delete = current;
            current = current->next;
            delete to_delete;
        }
        head = nullptr;
    }

    // Add a new item to the end of the list
    // Allocate a new node, then walk to the last node and link the new one there
    void append(const T& value) {
        Node<T>* new_node = new Node<T>(value);
        if (head == nullptr) {
            head = new_node;
        } else {
            Node<T>* current = head;
            while (current->next != nullptr) {
                current = current->next;
            }
            current->next = new_node;
        }
        count++;
    }

    // Return the node at the given index, or nullptr if the index is out of range
    // Start at the head and move forward index times
    Node<T>* get_node_at_index(int index) const {
        if (index < 0 || index >= count) {
            return nullptr;
        }
        Node<T>* current = head;
        for (int i = 0; i < index; i++) {
            current = current->next;
        }
        return current;
    }

    // Replace the item at the given index with a new value
    // Returns true if the index was valid, false otherwise
    bool set_index(int index, const T& value) {
        Node<T>* node = get_node_at_index(index);
        if (node == nullptr) {
            return false;
        }
        node->data = value;
        return true;
    }

    // Remove the first node whose data equals value
    // Keep track of the previous node so we can relink around the removed node
    // Returns true if a node was removed, false if no matching node was found
    bool remove_value(const T& value) {
        Node<T>* current = head;
        Node<T>* prev = nullptr;

        while (current != nullptr) {
            if (current->data == value) {
                if (prev == nullptr) {
                    head = current->next;
                } else {
                    prev->next = current->next;
                }
                delete current;
                count--;
                return true;
            }
            prev = current;
            current = current->next;
        }
        return false;
    }

    // Return how many items are currently stored in the list
    int get_count() const {
        return count;
    }

    // Copy every item from the linked list into a new dynamically allocated array
    // The caller must free the returned array with delete[]
    T* to_array() const {
        T* arr = new T[count];
        Node<T>* current = head;
        for (int i = 0; i < count; i++) {
            arr[i] = current->data;
            current = current->next;
        }
        return arr;
    }

    // Return the head node so callers can iterate manually with Node<T>* 
    Node<T>* get_head() const {
        return head;
    }
};


