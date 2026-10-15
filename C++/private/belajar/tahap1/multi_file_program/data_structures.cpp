#include "data_structures.h"

ItemList::ItemList(int initial_capacity) {
    capacity = initial_capacity;
    count = 0;
    items = new Item[capacity];
}

// Destructor dipanggil otomatis saat objek keluar dari scope.
// Ini tempat membebaskan memori yang dialokasi constructor.
ItemList::~ItemList() {
    delete[] items;
    items = nullptr;
}

void ItemList::add(const Item& item) {
    if (count < capacity) {
        items[count] = item;
        count++;
    }
}

int ItemList::get_count() const {
    return count;
}