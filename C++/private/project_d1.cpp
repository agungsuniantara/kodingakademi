#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;

struct RangeAnswer {
    int min_value;
    int max_value;
};

ostream & operator << (ostream & outs, const RangeAnswer & vs) {
    return outs << "[" << vs.min_value << ", " << vs.max_value << "]";
}

struct Node {
    int value;
    Node* left = nullptr;
    Node* right = nullptr;
    
    bool has_left() {
        return left != nullptr;
    }
    
    bool has_right() {
        return right != nullptr;
    }
    
    bool is_leaf() {
        return !has_left() && !has_right();
    }
    
    int node_count() {
        int left_count = has_left() ? left->node_count() : 0;
        int right_count = has_right() ? right->node_count() : 0;
        return 1 + left_count + right_count;
    }
    
    RangeAnswer value_range() {
        RangeAnswer answer;
        if (is_leaf()) {
            answer.min_value = value;
            answer.max_value = value;
        } else if (has_left() && has_right()) {
            RangeAnswer left_range = left->value_range();
            RangeAnswer right_range = right->value_range();
            answer.min_value = min({value, left_range.min_value, right_range.min_value});
            answer.max_value = max({value, left_range.max_value, right_range.max_value});
        } else if (has_left()) {
            RangeAnswer left_range = left->value_range();
            answer.min_value = min(value, left_range.min_value);
            answer.max_value = max(value, left_range.max_value);
        } else {
            RangeAnswer right_range = right->value_range();
            answer.min_value = min(value, right_range.min_value);
            answer.max_value = max(value, right_range.max_value);
        }
        return answer;
    }
    
    RangeAnswer stored_value_range = {INT_MAX, INT_MIN};
    int stored_node_count = 0;
};

struct BinarySearchTree {
    Node* root = nullptr;
    
    Node* search(int value) {
        return search_helper(root, value);
    }
    
    Node* search_helper(Node* current_node, int value) {
        if (current_node == nullptr) return nullptr;
        if (current_node->value == value) return current_node;
        if (value > current_node->value) {
            return search_helper(current_node->right, value);
        } else {
            return search_helper(current_node->left, value);
        }
    }
    
    bool insert(int value) {
        if (root == nullptr) {
            root = new Node;
            root->value = value;
            root->stored_node_count = 1;
            root->stored_value_range = {value, value};
            return true;
        }
        return insert_helper(root, value);
    }
    
    void update_node(Node* node) {
        node->stored_node_count = 1;
        int new_min = node->value;
        int new_max = node->value;
        if (node->has_left()) {
            node->stored_node_count += node->left->stored_node_count;
            new_min = min(new_min, node->left->stored_value_range.min_value);
            new_max = max(new_max, node->left->stored_value_range.max_value);
        }
        if (node->has_right()) {
            node->stored_node_count += node->right->stored_node_count;
            new_min = min(new_min, node->right->stored_value_range.min_value);
            new_max = max(new_max, node->right->stored_value_range.max_value);
        }
        node->stored_value_range.min_value = new_min;
        node->stored_value_range.max_value = new_max;
    }
    
    bool insert_helper(Node* current_node, int value) {
        if (current_node->value == value) {
            throw "Value already present in BST";
        }
        
        if (value > current_node->value) {
            if (current_node->right == nullptr) {
                current_node->right = new Node;
                current_node->right->value = value;
                current_node->right->stored_node_count = 1;
                current_node->right->stored_value_range = {value, value};
                update_node(current_node);
                return true;
            }
            bool inserted = insert_helper(current_node->right, value);
            if (inserted) {
                update_node(current_node);
            }
            return inserted;
        } else {
            if (current_node->left == nullptr) {
                current_node->left = new Node;
                current_node->left->value = value;
                current_node->left->stored_node_count = 1;
                current_node->left->stored_value_range = {value, value};
                update_node(current_node);
                return true;
            }
            bool inserted = insert_helper(current_node->left, value);
            if (inserted) {
                update_node(current_node);
            }
            return inserted;
        }
    }
    
    int count_lt(int x) {
        return count_lt_helper(root, x);
    }
    
    int count_lt_helper(Node* current, int x) {
        if (current == nullptr) return 0;
        if (current->value < x) {
            int left_count = current->has_left() ? current->left->stored_node_count : 0;
            return 1 + left_count + count_lt_helper(current->right, x);
        } else {
            return count_lt_helper(current->left, x);
        }
    }
    
    int count_le(int y) {
        return count_le_helper(root, y);
    }
    
    int count_le_helper(Node* current, int y) {
        if (current == nullptr) return 0;
        if (current->value <= y) {
            int left_count = current->has_left() ? current->left->stored_node_count : 0;
            return 1 + left_count + count_le_helper(current->right, y);
        } else {
            return count_le_helper(current->left, y);
        }
    }
    
    int count_range(int x, int y) {
        return count_le(y) - count_lt(x);
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
        cout << bst.search(40)->value << endl;
        try {
            bst.insert(40);
        } catch (const char* msg) {
            cout << msg << endl;
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
