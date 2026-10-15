#include <iostream>
#include <string>
using namespace std;

struct Rectangle {
    int width;
    int height;

    int get_area() const {
        return width * height;
    }

    bool operator>(const Rectangle& right) const {
        return get_area() > right.get_area();
    }
    bool operator<(const Rectangle& right) const {
        return get_area() < right.get_area();
    }
};

struct User {
    string name;
    int age;

    bool operator>(const User& right) const {
        return age > right.age;
    }
    bool operator<(const User& right) const {
        return age < right.age;
    }
};

// SATU fungsi untuk SEMUA tipe yang punya operator>
template <typename T>
T get_max(T a, T b) {
    if (a > b) {
        return a;
    }
    return b;
}

int main() {
    Rectangle r1 = {2, 3};    // area 6
    Rectangle r2 = {4, 5};    // area 20
    Rectangle r_max = get_max(r1, r2);
    cout << "Rectangle max area: " << r_max.get_area() << endl;   // 20

    User u1 = {"Alice", 30};
    User u2 = {"Bob", 25};
    User u_max = get_max(u1, u2);
    cout << "Oldest user: " << u_max.name << endl;   // Alice

    return 0;
}