#pragma once
#include <iostream>
#include <string>
using namespace std;

struct SPNode {
    SPNode* next = nullptr;
    string key;
    string value;
};

struct HashTable {
    const int table_size = 10000019;
    SPNode** table = new SPNode*[table_size];

    HashTable() {
        for (int i = 0; i < table_size; i++) {
            table[i] = nullptr;
        }
    }

    int hash(string key) {
        const int base = 271;
        long long hash_value = 0;
        for (int i = 0; i < key.length(); i++) {
            int ascii_code = key[i];
            hash_value = (hash_value * base) + ascii_code;
            hash_value %= table_size;
        }
        return hash_value;
    }

    void insert(string key, string value) {
        int table_position = hash(key);
        SPNode* current_node = table[table_position];
        while (current_node != nullptr) {
            if (current_node->key == key) {
                current_node->value = value;
                return;
            }
            current_node = current_node->next;
        }
        SPNode* node = new SPNode;
        node->key = key;
        node->value = value;
        node->next = table[table_position];
        table[table_position] = node;
    }

    string search(string key) {
        int position = hash(key);
        SPNode* current_node = table[position];
        while (current_node != nullptr) {
            if (current_node->key == key) {
                return current_node->value;
            }
            current_node = current_node->next;
        }
        throw string("Key not found!");
    }

    void del(string key) {
        int position = hash(key);
        SPNode* current_node = table[position];
        SPNode* prev_node = nullptr;
        while (current_node != nullptr) {
            if (current_node->key == key) {
                if (prev_node == nullptr) {
                    table[position] = current_node->next;
                } else {
                    prev_node->next = current_node->next;
                }
                delete current_node;
                return;
            }
            prev_node = current_node;
            current_node = current_node->next;
        }
        throw string("Key not found!");
    }
};