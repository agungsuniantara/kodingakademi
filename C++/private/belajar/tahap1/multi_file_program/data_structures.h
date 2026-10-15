#ifndef DATA_STRUCTURES_H
#define DATA_STRUCTURES_H

#include <string>

struct Item {
    int id;
    std::string name;
};

class ItemList {
private:
    Item* items;
    int count;
    int capacity;

public:
    ItemList(int initial_capacity);
    ~ItemList();                    // destructor: bebaskan memori saat objek mati
    void add(const Item& item);
    int get_count() const;
};

#endif  // DATA_STRUCTURES_H