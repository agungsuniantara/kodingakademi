#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* left;
    Node* right;

    bool is_leaf() {
        return left == nullptr && right == nullptr;
    }
};

struct BinaryTree {
    Node* root;

    int get_max_value() {
        return get_max_value_helper(root);
    }

    int get_max_value_helper(Node* current_node) {

        if (current_node->is_leaf()) {
            return current_node->value;
        }

        int current_max = current_node->value;

        // Check the left subtree
        if (current_node->left != nullptr) {
            int left_max = get_max_value_helper(current_node->left);
            if (left_max > current_max) {
                current_max = left_max;
            }
        }

        // Check the right subtree
        if (current_node->right != nullptr) {
            int right_max = get_max_value_helper(current_node->right);
            if (right_max > current_max) {
                current_max = right_max;
            }
        }
        return current_max;
    }

    // ============ Exercise 1: Sum of all values ============
    int get_sum() {
        return _get_sum_helper(root);
    }

    int _get_sum_helper(Node* current_node) {
        if (current_node == nullptr) {
            return 0;
        }

        return current_node->value
             + _get_sum_helper(current_node->left)
             + _get_sum_helper(current_node->right);
    }

    // ============ Exercise 2: Height of the tree ============
    int get_height() {
        return _get_height_helper(root);
    }

    int _get_height_helper(Node* current_node) {
        if (current_node == nullptr) {
            return -1;
        }
        int left_height = _get_height_helper(current_node->left);
        int right_height = _get_height_helper(current_node->right);
        return 1 + max(left_height, right_height);
    }

    // ============ Exercise 3: Is the tree balanced? ============
    bool is_balanced() {
        return _is_balanced_helper(root);
    }

    bool _is_balanced_helper(Node* current_node) {
        if (current_node == nullptr) {
            return true;
        }

        int left_height = _get_height_helper(current_node->left);
        int right_height = _get_height_helper(current_node->right);
        int diff = left_height - right_height;
        if (diff > 1 || diff < -1) {
            return false;
        }

        return _is_balanced_helper(current_node->left)
            && _is_balanced_helper(current_node->right);
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
};

int main() {

    BinaryTree tree;
    tree.root = new Node;
    tree.root->value = 12;
    tree.root->left = new Node;
    tree.root->left->value = 19;
    tree.root->left->left = new Node;
    tree.root->left->left->value = 5;
    tree.root->left->left->left = nullptr;
    tree.root->left->left->right = nullptr;
    tree.root->left->right = new Node;
    tree.root->left->right->value = 42;
    tree.root->left->right->left = nullptr;
    tree.root->left->right->right = nullptr;
    tree.root->right = new Node;
    tree.root->right->value = 8;
    tree.root->right->left = nullptr;
    tree.root->right->right = new Node;
    tree.root->right->right->value = 14;
    tree.root->right->right->left = nullptr;

    tree.root->right->right->right = nullptr;

    cout << "Max value: " << tree.get_max_value() << endl;
    cout << "Sum: " << tree.get_sum() << endl;
    cout << "Height: " << tree.get_height() << endl;
    cout << "Balanced: " << tree.is_balanced() << endl;

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

    return 0;
}