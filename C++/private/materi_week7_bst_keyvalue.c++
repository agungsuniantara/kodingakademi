#include <iostream>
#include <string>
using namespace std;

struct Product {
    string name;
    double weight;
    string sku;
    double price;
    string category;
    double rating;
};

struct Node {
    string key;        
    Product* value;    
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

    Product* search(string key) {
        if (root == nullptr) return nullptr;
        return _search_helper(root, key);
    }

    Product* _search_helper(Node* current_node, string key) {
        if (current_node->key == key) {
            return current_node->value;
        }

        if (key > current_node->key) {
            if (current_node->right == nullptr) return nullptr;
            return _search_helper(current_node->right, key);
        } else {
            if (current_node->left == nullptr) return nullptr;
            return _search_helper(current_node->left, key);
        }
    }

    bool insert(string key, Product* prod) {
        if (root == nullptr) {
            root = new Node;
            root->key = key;
            root->value = prod;
            return true;
        }
        return _insert_helper(root, key, prod);
    }

    bool _insert_helper(Node* current_node, string key, Product* prod) {
        if (current_node->key == key) return false;

        if (key > current_node->key) {
            if (current_node->right == nullptr) {
                current_node->right = new Node;
                current_node->right->key = key;
                current_node->right->value = prod;
                return true;
            }
            return _insert_helper(current_node->right, key, prod);
        } else {
            if (current_node->left == nullptr) {
                current_node->left = new Node;
                current_node->left->key = key;
                current_node->left->value = prod;
                return true;
            }
            return _insert_helper(current_node->left, key, prod);
        }
    }
};

int main() {

    Product* laptop = new Product;
    laptop->name = "Laptop Pro";
    laptop->weight = 1.8;
    laptop->sku = "abcxyz";
    laptop->price = 15000000;
    laptop->category = "Electronics";
    laptop->rating = 4.7;

    Product* mouse = new Product;
    mouse->name = "Wireless Mouse";
    mouse->weight = 0.1;
    mouse->sku = "aaa111";
    mouse->price = 250000;
    mouse->category = "Accessories";
    mouse->rating = 4.3;

    Product* keyboard = new Product;
    keyboard->name = "Mech Keyboard";
    keyboard->weight = 0.9;
    keyboard->sku = "zzz999";
    keyboard->price = 1200000;
    keyboard->category = "Accessories";
    keyboard->rating = 4.9;

    BinarySearchTree bst;

    bst.insert(laptop->sku, laptop);
    bst.insert(mouse->sku, mouse);
    bst.insert(keyboard->sku, keyboard);

    Product* result = bst.search("abcxyz");
    if (result != nullptr) {
        cout << "Found: " << result->name
             << " (Rp" << result->price
             << ", rating " << result->rating << ")" << endl;
    } else {
        cout << "not found" << endl;
    }

    Product* result2 = bst.search("mmm111");
    if (result2 != nullptr) {
        cout << "Found" << endl;
    } else {
        cout << "key mmm111 not found" << endl;
    }

    delete laptop;
    delete mouse;
    delete keyboard;
    return 0;
}