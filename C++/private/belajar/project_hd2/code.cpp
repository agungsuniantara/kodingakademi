#include <iostream>
#include <random>
using namespace std;

template <typename T>
struct Node {
    int key;
    T value;
    int priority;
    Node<T>* left = nullptr;
    Node<T>* right = nullptr;
    Node<T>* parent = nullptr;
    inline static mt19937 gen{random_device{}()};
    Node(int k, T v, int p = -1): key{k}, value{v} {
        priority = (p >= 0) ? p : uniform_int_distribution<int>(1, 10000)(gen);
    }
    bool has_left() {
        // if left is something other than null, that means there is a child
        return left != nullptr;
    }
    bool has_right() {
        return right != nullptr;
    }
    bool has_parent() {
        return parent != nullptr;
    }
    bool is_leaf() {
        // If it doesn't have a left child and it doesn't have a right child, it
        // must be a leaf node.
        return !has_left() && !has_right();
    }
};

template <typename T>
struct BinarySearchTree {
    Node<T>* root = nullptr;

    /// Return the node in the tree with this value. If there is no such node, return
    Node<T>* search(int key) {
        return _search_helper(root, key);
    }

    Node<T>* _search_helper(Node<T>* current_node, int key) {
        if (current_node == nullptr) return nullptr;
        if (key == current_node->key) return current_node;
        if (key < current_node->key) return _search_helper(current_node->left, key);
        return _search_helper(current_node->right, key);
    }

    void insert(int key, T value, int priority = -1) {
        Node<T>* val = new Node<T>(key, value, priority);
        // First, if the tree is empty, just make this the root node
        if (root == nullptr) {
            root = val;
            return;
        }
        // Again, I need a helper function to handle my recursion input
        return _insert_helper(root, val);
    }

    void _insert_helper(Node<T>* current_node, Node<T>* inserting) {
        // Phase 1: standard BST placement as a leaf
        if (inserting->key < current_node->key) {
            if (current_node->has_left()) {
                _insert_helper(current_node->left, inserting);
                return;
            }
            current_node->left = inserting;
        } else {
            if (current_node->has_right()) {
                _insert_helper(current_node->right, inserting);
                return;
            }
            current_node->right = inserting;
        }
        inserting->parent = current_node;

        // Phase 2: rise the node by priority via rotations (inline, no helper).
        // Each rotation swaps 'inserting' with its parent while preserving BST
        // ordering and updating left, right AND parent pointers.
        while (inserting->has_parent() && inserting->priority > inserting->parent->priority) {
            Node<T>* parent = inserting->parent;
            Node<T>* grandparent = parent->parent;
            if (inserting == parent->left) {
                // right rotation: inserting takes parent's place
                parent->left = inserting->right;
                if (inserting->right) inserting->right->parent = parent;
                inserting->right = parent;
            } else {
                // left rotation: inserting takes parent's place
                parent->right = inserting->left;
                if (inserting->left) inserting->left->parent = parent;
                inserting->left = parent;
            }
            parent->parent = inserting;
            inserting->parent = grandparent;
            if (grandparent == nullptr) {
                root = inserting;
            } else if (grandparent->left == parent) {
                grandparent->left = inserting;
            } else {
                grandparent->right = inserting;
            }
        }
    }

    void remove(int key) {
        return _remove_helper(root, key);
    }

    void _remove_helper(Node<T>* current_node, int key) {
        if (current_node == nullptr) return;
        if (key < current_node->key) {
            _remove_helper(current_node->left, key);
            return;
        }
        if (key > current_node->key) {
            _remove_helper(current_node->right, key);
            return;
        }
        // Found the node. Per HD2 hint: change its priority to force the easy
        // 0-child case, then rotate it down to a leaf (inline), then detach.
        current_node->priority = -1;
        while (!current_node->is_leaf()) {
            // pick the child with the larger priority to swap down with
            Node<T>* swap_child = nullptr;
            if (!current_node->has_left()) {
                swap_child = current_node->right;
            } else if (!current_node->has_right()) {
                swap_child = current_node->left;
            } else {
                swap_child = (current_node->left->priority >= current_node->right->priority)
                             ? current_node->left : current_node->right;
            }
            // inline rotation: swap_child takes current_node's place
            Node<T>* parent = current_node->parent;
            if (swap_child == current_node->left) {
                current_node->left = swap_child->right;
                if (swap_child->right) swap_child->right->parent = current_node;
                swap_child->right = current_node;
            } else {
                current_node->right = swap_child->left;
                if (swap_child->left) swap_child->left->parent = current_node;
                swap_child->left = current_node;
            }
            current_node->parent = swap_child;
            swap_child->parent = parent;
            if (parent == nullptr) {
                root = swap_child;
            } else if (parent->left == current_node) {
                parent->left = swap_child;
            } else {
                parent->right = swap_child;
            }
        }
        // now a leaf: detach and free
        if (current_node->has_parent()) {
            if (current_node->parent->left == current_node) {
                current_node->parent->left = nullptr;
            } else {
                current_node->parent->right = nullptr;
            }
        } else {
            root = nullptr;
        }
        delete current_node;
    }

    void update(int key, T value) {
        Node<T>* node = search(key);
        if (node) node->value = value;
        else insert(key, value);
    }
};

int ontrack_test() {
    // Ontrack tests, do not change
    BinarySearchTree<string> bst;
    Node<string>* context_node = nullptr;
    string menu = "0. Show this menu\n1. Insert a key\n2. Update a key\n3. Search for a key\n4. Remove a key\n5. Exit";
    int command = 0;
    while (command != 5) {
        if (command == 0) {
            cout << menu << endl;
        } else if (command == 1) {
            //insert
            int key;
            string value;
            int priority;
            cout << "Enter key, value, priority: " << endl;
            cin >> key;
            cin >> value;
            cin >> priority;
            bst.insert(key, value, priority);
        } else if (command == 2) {
            //update
            int key;
            string value;
            cout << "Enter key, value: " << endl;
            cin >> key;
            cin >> value;
            bst.update(key, value);
        } else if (command == 3) {
            //search
            cout << "Enter key to search: " << endl;
            int key;
            cin >> key;
            context_node = bst.search(key);
            if (context_node) {
                cout << "Found node (" << context_node->key << ", " << context_node->value
                     << ", " << context_node->priority << ")" << endl;
                cout << "Parent: " << (context_node->parent ? to_string(context_node->parent->key) : "none") << endl;
            } else cout << "Could not find node with key: " << key << endl;
        } else if (command == 4) {
            //remove
            cout << "Enter key to remove: " << endl;
            int key;
            cin >> key;
            bst.remove(key);
        }
        cout << "Enter command (0-5)" << endl;
        if (!(cin >> command)) {
            cout << "ERROR: could not read command" << endl;
            return 1;
        }
    }
    return 0;
}

int main(int argc, char** argv) {
    if (argc == 2) return ontrack_test();
    BinarySearchTree<string> bst;
    bst.insert(3, "a", 8);
    bst.insert(11, "b", 6);
    bst.insert(8, "c", 10);
    // At this point, c should be the root, and a/b should be left/right
    cerr << "Root: (" << bst.root->value << ", " << bst.root->priority << ")" << endl;
    cerr << "Left: (" << bst.root->left->value << ", " << bst.root->left->priority << ")" << endl;
    cerr << "Right: (" << bst.root->right->value << ", " << bst.root->right->priority << ")" << endl;
    bst.insert(7, "d", 5);
    bst.insert(9, "e", 4);
    bst.insert(5, "f", 2);
    // Now we should see the final structure of the tree.
    cerr << "===" << endl;
    cerr << "Root: (" << bst.root->value << ", " << bst.root->priority << ")" << endl;
    cerr << "Left: (" << bst.root->left->value << ", " << bst.root->left->priority << ")" << endl;
    cerr << "Right: (" << bst.root->right->value << ", " << bst.root->right->priority << ")" << endl;
    cerr << "Left->Right: (" << bst.root->left->right->value << ", " << bst.root->left->right->priority << ")" << endl;
    cerr << "Left->Right->Left: (" << bst.root->left->right->left->value << ", " << bst.root->left->right->left->priority << ")" << endl;
    cerr << "Right->Left: (" << bst.root->right->left->value << ", " << bst.root->right->left->priority << ")" << endl;
    return 0;
}