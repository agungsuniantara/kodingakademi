#include <iostream>
#include <string>
using namespace std;

// ================= Node generik =================
template <typename T>
struct Node {
    T data;
    Node<T>* next;

    Node(const T& value) : data(value), next(nullptr) {}
};

// ================= Linked List generik =================
template <typename T>
class LinkedList {
private:
    Node<T>* head;
    int count;

public:
    LinkedList() : head(nullptr), count(0) {}

    // Destructor: bebaskan semua node agar tidak memory leak
    ~LinkedList() {
        Node<T>* current = head;
        while (current != nullptr) {
            Node<T>* to_delete = current;
            current = current->next;
            delete to_delete;
        }
        head = nullptr;
    }

    // Tambah elemen di akhir list
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

    // Kembalikan pointer ke node pada index tertentu,
    // nullptr jika index di luar jangkauan
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

    // Ubah data pada index tertentu.
    // Return true jika berhasil, false jika index tidak valid.
    bool set_index(int index, const T& value) {
        Node<T>* node = get_node_at_index(index);
        if (node == nullptr) {
            return false;
        }
        node->data = value;
        return true;
    }

    int get_count() const {
        return count;
    }

    // Cetak seluruh isi list
    void display() const {
        Node<T>* current = head;
        while (current != nullptr) {
            cout << current->data;
            if (current->next != nullptr) {
                cout << " -> ";
            }
            current = current->next;
        }
        cout << endl;
    }
};

// ================= Struct untuk pengujian tipe custom =================
struct Rectangle {
    int width;
    int height;

    int get_area() const {
        return width * height;
    }

    bool operator<(const Rectangle& right) const {
        return get_area() < right.get_area();
    }

    bool operator>(const Rectangle& right) const {
        return get_area() > right.get_area();
    }
};

// Agar Rectangle bisa dicetak oleh display()
ostream& operator<<(ostream& os, const Rectangle& r) {
    os << r.width << "x" << r.height;
    return os;
}

int main() {
    // Uji 1: LinkedList<int>
    LinkedList<int> int_list;
    int_list.append(10);
    int_list.append(20);
    int_list.append(30);
    cout << "Int list: ";
    int_list.display();   // 10 -> 20 -> 30

    // get_node_at_index
    Node<int>* node1 = int_list.get_node_at_index(1);
    cout << "Node at index 1: " << node1->data << endl;   // 20

    // set_index
    int_list.set_index(1, 99);
    cout << "After set_index(1, 99): ";
    int_list.display();   // 10 -> 99 -> 30

    // Index tidak valid
    Node<int>* bad = int_list.get_node_at_index(10);
    if (bad == nullptr) {
        cout << "get_node_at_index(10): nullptr (out of range)" << endl;
    }
    cout << "set_index(10, 5): " << (int_list.set_index(10, 5) ? "ok" : "failed") << endl;

    // Uji 2: LinkedList<string>
    LinkedList<string> str_list;
    str_list.append("apple");
    str_list.append("banana");
    str_list.append("cherry");
    cout << "String list: ";
    str_list.display();   // apple -> banana -> cherry

    // Uji 3: LinkedList<Rectangle> (tipe custom)
    LinkedList<Rectangle> rect_list;
    rect_list.append({2, 3});     // area 6
    rect_list.append({4, 5});     // area 20
    rect_list.append({1, 2});     // area 2
    cout << "Rectangle list: ";
    rect_list.display();          // 2x3 -> 4x5 -> 1x2

    rect_list.set_index(0, {7, 7});
    cout << "After set_index(0, {7,7}): ";
    rect_list.display();          // 7x7 -> 4x5 -> 1x2

    return 0;
}   // destructor otomatis menghapus semua node di sini