#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* left;
    Node* right;

    bool has_left() {
        return left != nullptr;
    }
    bool has_right() {
        return right != nullptr;
    }
    bool is_leaf() {
        return !has_left() && !has_right();
    }
};

struct BinarySearchTree {
    Node* root = nullptr;

    Node* search(int value) {
    if (root == nullptr) return nullptr;
        return _search_helper(root, value);
    }

    Node* _search_helper(Node* current_node, int value) {

    if (current_node->value == value) return current_node;

    if (value > current_node->value) {

        if (current_node->right == nullptr) return nullptr;
            return _search_helper(current_node->right, value);
        } else {

        if (current_node->left == nullptr) return nullptr;
            return _search_helper(current_node->left, value);
        }
    }

    bool insert(int value) {
        if (root == nullptr) {
            root = new Node;
            root->value = value;
            return true;
        }
        return _insert_helper(root, value);
    }

    bool _insert_helper(Node* current_node, int value) {
        if (current_node->value == value) return false;

        if (value > current_node->value) {
            if (current_node->right == nullptr) {
                current_node->right = new Node;
                current_node->right->value = value;
                return true;
            }
            return _insert_helper(current_node->right, value);
        } else {
            if (current_node->left == nullptr) {
                current_node->left = new Node;
                current_node->left->value = value;
                return true;
            }
            return _insert_helper(current_node->left, value);
        }
    }

    void delete_value(int value) {
        if (root == nullptr) {
            throw "Value not found, tree is empty";
        }

        _delete_helper(nullptr, root, value);
    }

    void _delete_helper(Node* parent_node, Node* current_node, int value) {
        if (current_node->value == value) {
            
            // Scenario 1: if it's a leaf, nothing needs to be done.
            if (current_node->is_leaf()) {
                // Update its parent's link FIRST
                if (parent_node == nullptr) {
                    // It's the root node, and it doesn't have children
                    root = nullptr;
                } else if (parent_node->left == current_node) {
                    // It was the left child of its parent
                    parent_node->left = nullptr;
                } else if (parent_node->right == current_node) {
                    // It was the right child of its parent
                    parent_node->right = nullptr;
                }
                // NOW we can safely delete the node
                delete current_node;
            }
            
            // Scenario 2: it only has one child, which we should move up
            else if (current_node->has_left() && !current_node->has_right()) {
                // It has a left child
                if (parent_node == nullptr) {
                    root = current_node->left;
                } else if (parent_node->left == current_node) {
                    parent_node->left = current_node->left;
                } else if (parent_node->right == current_node) {
                    parent_node->right = current_node->left;
                }
                delete current_node; // Move delete to the end
            } 

            else if (!current_node->has_left() && current_node->has_right()) {
                // It has a right child
                if (parent_node == nullptr) {
                    root = current_node->right;
                } else if (parent_node->left == current_node) {
                    parent_node->left = current_node->right;
                } else if (parent_node->right == current_node) {
                    parent_node->right = current_node->right;
                }
                delete current_node; // Move delete to the end
            }
            
            // Scenario 3: the node has both children, find the successor
            else if (current_node->has_left() && current_node->has_right()) {
                Node* successor = successor_of(current_node);
                
                // Remember its value
                int successor_value = successor->value;
                
                // Delete the successor recursively
                delete_value(successor_value);
                
                // Put its value in the current node
                current_node->value = successor_value;
            }
            return;
        }
        
        // Otherwise, we need to continue our search for the node:
        if (value < current_node->value) {
            // If we need to go left, but there is no left, throw error
            if (!current_node->has_left()) throw "Value not found";
            
            // Recurse. current_node becomes the new parent_node.
            _delete_helper(current_node, current_node->left, value);
        } else {
            if (!current_node->has_right()) throw "Value not found";
            
            _delete_helper(current_node, current_node->right, value);
        }
    }

    // Returns the node that contains the successor value of the input node
    // Based on the logic above, it is assumed that the input `node`
    // has both children.
    Node* successor_of(Node* node) {
        // Go right once (no need to check there is a right - there must be)
        node = node->right;

        // Go left as much as possible
        while (node->has_left()) {
            node = node->left;
        }
        
        // Return
        return node;
    }
};

int main() {

    BinarySearchTree bst;

    bst.root = new Node;
    bst.root->value = 12;
    bst.root->left = new Node;
    bst.root->left->value = 5;
    bst.root->left->left = nullptr;
    bst.root->left->right = nullptr;
    bst.root->right = new Node;
    bst.root->right->value = 19;
    bst.root->right->left = new Node;
    bst.root->right->left->value = 14;
    bst.root->right->left->left = nullptr;
    bst.root->right->left->right = nullptr;
    bst.root->right->right = new Node;
    bst.root->right->right->value = 42;
    bst.root->right->right->left = nullptr;
    bst.root->right->right->right = nullptr;

    Node* result = bst.search(5);
    if (result != nullptr) {
        cout << "found" << endl;
    } else {
        cout << "not found" << endl;
    }

    cout << "Insert 30: " << bst.insert(30) << endl;
    Node* result2 = bst.search(30);
    if (result2 != nullptr) {
        cout << "found" << endl;
    } else {
        cout << "not found" << endl;
    }

    // === Delete Scenario 1: delete a leaf node (30) ===
    // Tree now: 12, 5, 19, 14, 42, 30 (30 is left child of 42, a leaf)
    bst.delete_value(30);
    cout << (bst.search(30) == nullptr ? "30 deleted" : "30 still there") << endl;

    // === Delete Scenario 2: delete a node with one child (19) ===
    // 19 has only a left child (14) after 30 was removed
    bst.delete_value(19);
    cout << (bst.search(19) == nullptr ? "19 deleted" : "19 still there") << endl;
    // 14 must have moved up: it is now the right child of 12
    cout << (bst.search(14) != nullptr ? "14 still found" : "14 lost!") << endl;

    // === Delete Scenario 3: delete a node with two children (12, the root) ===
    // 12 has two children (5 and 14). Its successor is 14.
    // The successor is deleted first, then its value (14) is copied into the root.
    bst.delete_value(12);
    cout << (bst.search(12) == nullptr ? "12 deleted" : "12 still there") << endl;
    cout << (bst.search(14) != nullptr ? "14 still found" : "14 lost!") << endl;

    return 0;
}