#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;

struct RangeAnswer {
    int min_value;
    int max_value;
};

// Enable debugging the RangeAnswer object.
// This way, you can do cerr << rangeAnswer and it will print the min/max values rather than the raw struct
ostream & operator << (ostream & outs, const RangeAnswer & vs) {
    return outs << "[" << vs.min_value << ", " << vs.max_value << "]";
}

struct Node {
    int value;
    Node* left = nullptr;
    Node* right = nullptr;

    bool has_left() {
        // if left is something other than null, that means there is a child
        return left != nullptr;
    }

    bool has_right() {
        return right != nullptr;
    }

    bool is_leaf() {
        // If it doesn't have a left child and it doesn't have a right child, it
        // must be a leaf node.
        return !has_left() && !has_right();
    }

    int node_count() {
        // TASK 1
        int count = 1;
        if (has_left()) count += left->node_count();
        if (has_right()) count += right->node_count();
        return count;
    }

    RangeAnswer value_range() {
        // TASK 1
        RangeAnswer answer = {value, value};
        if (has_left()) {
            RangeAnswer left_range = left->value_range();
            answer.min_value = min(answer.min_value, left_range.min_value);
            answer.max_value = max(answer.max_value, left_range.max_value);
        }
        if (has_right()) {
            RangeAnswer right_range = right->value_range();
            answer.min_value = min(answer.min_value, right_range.min_value);
            answer.max_value = max(answer.max_value, right_range.max_value);
        }
        return answer;
    }

    // TASK 2 - Maintain these values correctly through insertion
    RangeAnswer stored_value_range = {INT_MAX, INT_MIN};
    int stored_node_count = 0;
};

struct BinarySearchTree {
    Node* root = nullptr;

    /// Return the node in the tree with this value. If there is no such node, return nullptr
    Node* search(int value) {
        return _search_helper(root, value);
    }

    Node* _search_helper(Node* current_node, int value) {
        // If we are outside the tree, that means the value can't be found
        if (current_node == nullptr) return nullptr;

        // If current_node node has the value, return it
        if (current_node->value == value) return current_node;

        // Otherwise, check which child we should go to.
        if (value > current_node->value) {
            return _search_helper(current_node->right, value);
        } else {
            return _search_helper(current_node->left, value);
        }
    }

    bool insert(int value) {
        // First, if the tree is empty, just make this the root node
        if (root == nullptr) {
            root = new Node;
            root->value = value;
            // TASK 2 - the root is its own subtree, so cache its properties
            root->stored_node_count = 1;
            root->stored_value_range = {value, value};
            // The item wasn't found, so we return true (indicating an insert happened)
            return true;
        }
        // Again, I need a helper function to handle my recursion input
        return _insert_helper(root, value);
    }

    bool _insert_helper(Node* current_node, int value) {
        // If this node has the key, return as the key is already in the tree.
        // Tell the caller that the key is not a new node.
        // We are defining that if the function returns false, that means the item was already in the tree
        if (current_node->value == value) return false;

        // Check which direction we should go
        if (value > current_node->value) {
            // We should go to the right
            // If there is no right child, that means this is exactly where
            // the new node should be inserted
            if (current_node->right == nullptr) {
                current_node->right = new Node;
                current_node->right->value = value;
                // TASK 2 - initialize the new leaf's cached properties
                current_node->right->stored_node_count = 1;
                current_node->right->stored_value_range = {value, value};
                // TASK 2 - this node is an ancestor of the new node, so refresh its cache
                current_node->stored_node_count += 1;
                current_node->stored_value_range.min_value = min(current_node->stored_value_range.min_value, value);
                current_node->stored_value_range.max_value = max(current_node->stored_value_range.max_value, value);
                // Item was unique and an insertion happened, so we return true.
                return true;
            }
            // Otherwise, if there is a right child, continue there
            bool inserted = _insert_helper(current_node->right, value);
            // TASK 2 - only ancestors on the insertion path change, update on the way back up
            if (inserted) {
                current_node->stored_node_count += 1;
                current_node->stored_value_range.min_value = min(current_node->stored_value_range.min_value, value);
                current_node->stored_value_range.max_value = max(current_node->stored_value_range.max_value, value);
            }
            return inserted;
        } else {
            // We should go to the left
            // If there is no left child, that means this is exactly where
            // the new node should be inserted
            if (current_node->left == nullptr) {
                current_node->left = new Node;
                current_node->left->value = value;
                // TASK 2 - initialize the new leaf's cached properties
                current_node->left->stored_node_count = 1;
                current_node->left->stored_value_range = {value, value};
                // TASK 2 - this node is an ancestor of the new node, so refresh its cache
                current_node->stored_node_count += 1;
                current_node->stored_value_range.min_value = min(current_node->stored_value_range.min_value, value);
                current_node->stored_value_range.max_value = max(current_node->stored_value_range.max_value, value);
                return true;
            }
            // Otherwise, if there is a left child, continue there
            bool inserted = _insert_helper(current_node->left, value);
            // TASK 2 - only ancestors on the insertion path change, update on the way back up
            if (inserted) {
                current_node->stored_node_count += 1;
                current_node->stored_value_range.min_value = min(current_node->stored_value_range.min_value, value);
                current_node->stored_value_range.max_value = max(current_node->stored_value_range.max_value, value);
            }
            return inserted;
        }
    }

    int count_lt(int x) {
        // TASK 3 - How many nodes have a value less than x?
        // Your answer should have a complexity of O(h), where h is the height of the tree
        int count = 0;
        Node* current = root;
        while (current != nullptr) {
            if (current->value < x) {
                // This node and its entire left subtree are less than x,
                // so jump over the left subtree using its stored count
                if (current->has_left()) count += current->left->stored_node_count;
                count += 1;
                current = current->right;
            } else {
                // This node and its right subtree are >= x, go left
                current = current->left;
            }
        }
        return count;
    }

    int count_range(int x, int y) {
        // TASK 4 - Count of nodes with value v satisfying x <= v <= y
        // Your answer should have a complexity of O(h), where h is the height of the tree
        // Traverse once, using the same subtree-jumping idea as count_lt
        int count = 0;
        Node* current = root;
        while (current != nullptr) {
            if (current->value < x) {
                // Entire left subtree is below the range, go right
                current = current->right;
            } else if (current->value > y) {
                // Entire right subtree is above the range, go left
                current = current->left;
            } else {
                // current->value is inside [x, y]: everything in the left
                // subtree is < current->value, so nodes >= x there are
                // (left subtree size) - (nodes < x in it)
                if (current->has_left()) {
                    Node* left_child = current->left;
                    int below_x = 0;
                    Node* walker = left_child;
                    while (walker != nullptr) {
                        if (walker->value < x) {
                            if (walker->has_left()) below_x += walker->left->stored_node_count;
                            below_x += 1;
                            walker = walker->right;
                        } else {
                            walker = walker->left;
                        }
                    }
                    count += left_child->stored_node_count - below_x;
                }
                count += 1;
                // For the right subtree, everything is > current->value,
                // so nodes <= y there are found the same way as count_lt
                Node* walker = current->right;
                while (walker != nullptr) {
                    if (walker->value <= y) {
                        if (walker->has_left()) count += walker->left->stored_node_count;
                        count += 1;
                        walker = walker->right;
                    } else {
                        walker = walker->left;
                    }
                }
                break;
            }
        }
        return count;
    }
};

int main(int argc, char** argv) {
    if (argc == 1) {
        BinarySearchTree bst;
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);

        cout << bst.search(40)->value << endl; // Should print 40

        try {
            bst.insert(40); // Should throw an error
        } catch (const char* msg) {
            cout << msg << endl; // Should print "Value already present in BST"
        }

        cout << "=== TASK 1 ===" << endl;
        cout << "Node Count: " << bst.root->node_count() << ", Range: " << bst.root->value_range() << endl;
        cout << "Left Count: " << bst.root->left->node_count() << ", Range: " << bst.root->left->value_range() << endl;
        cout << "Right Count: " << bst.root->right->node_count() << ", Range: " << bst.root->right->value_range() << endl;

        cout << "=== TASK 2 ===" << endl;
        cout << "Node Count: " << bst.root->stored_node_count << ", Range: " << bst.root->stored_value_range << endl;
        cout << "Left Count: " << bst.root->left->stored_node_count << ", Range: " << bst.root->left->stored_value_range << endl;
        cout << "Right Count: " << bst.root->right->stored_node_count << ", Range: " << bst.root->right->stored_value_range << endl;

        cout << "=== TASK 3 ===" << endl;
        cout << "Amount Less Than 50: " << bst.count_lt(50) << endl;
        cout << "Amount Less Than 35: " << bst.count_lt(35) << endl;
        cout << "Amount Less Than 65: " << bst.count_lt(65) << endl;

        cout << "=== TASK 4 ===" << endl;
        cout << "Amount between 0 and 50: " << bst.count_range(0, 50) << endl;
        cout << "Amount between 25 and 65: " << bst.count_range(25, 65) << endl;
        cout << "Amount between 70 and 70: " << bst.count_range(70, 70) << endl;
        cout << "Amount between 30 and 70: " << bst.count_range(30, 70) << endl;
        return 0;
    } else {
        // Ontrack test cases DO NOT MODIFY
        int command = 0;
        BinarySearchTree bst;
        Node* context_node = nullptr;
        string menu = "0. Show this menu\n1. Insert a value into bst\n2. Search for a value\n3. Show node count of context node\n4. Show stored node count of context node\n5. Show value range of context node\n6. Show stored value range of context node\n7. Count less than\n8. Count range\n9. Quit\n";
        int value;
        while (command != 9) {
            try {
                if (command == 0) {
                    cout << menu << endl;
                } else if (command == 1) {
                    cout << "Enter value to insert: " << endl;
                    cin >> value;
                    bst.insert(value);
                } else if (command == 2) {
                    cout << "Enter value to search for: " << endl;
                    cin >> value;
                    context_node = bst.search(value);
                    if (context_node) {
                        cout << "Found node with " << context_node->value << endl;
                    } else {
                        cout << "Could not find node with value " << value << endl;
                    }
                } else if (command == 3) {
                    if (context_node) {
                        cout << "Node count called as " << context_node->node_count() << endl;
                    } else throw "ERROR: Context node is null";
                } else if (command == 4) {
                    if (context_node) {
                        cout << "Node count stored as " << context_node->stored_node_count << endl;
                    } else throw "ERROR: Context node is null";
                } else if (command == 5) {
                    if (context_node) {
                        cout << "Value range called as " << context_node->value_range() << endl;
                    } else throw "ERROR: Context node is null";
                } else if (command == 6) {
                    if (context_node) {
                        cout << "Value range stored as " << context_node->stored_value_range << endl;
                    } else throw "ERROR: Context node is null";
                } else if (command == 7) {
                    cout << "Enter upper bound: " << endl;
                    cin >> value;
                    cout << "Amount less than " << value << " is " << bst.count_lt(value) << endl;
                } else if (command == 8) {
                    cout << "Enter lower bound: " << endl;
                    cin >> value;
                    int ub;
                    cout << "Enter upper bound: " << endl;
                    cin >> ub;
                    cout << "Number of nodes between " << value << " and " << ub << " is " << bst.count_range(value, ub) << endl;
                }
            } catch (const char* msg) {
                cout << msg << endl;
            }
            cout << "Enter command (0-9): " << endl;
            if (!(cin >> command)) {
                cout << "ERROR: Could read next command" << endl;
                return 1;
            }
        }
        return 0;
    }
}