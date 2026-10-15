#include <iostream>
#include <string>
using namespace std;

template <typename T>
T get_max(T a, T b) {
    if (a > b) {
        return a;
    }
    return b;
}

struct User {
    int id;
    string username;
    string email;

    bool operator>(const User& right) {
        if (username > right.username) {
            return true;
        }
        return false;
    }
};

int main() {
    User a, b;
    a.id = 10;
    a.username = "User A";
    a.email = "a@mail.com";

    b.id = 5;
    b.username = "User B";
    b.email = "b@mail.com";

    User larger_user = get_max(a, b);
    cout << larger_user.username << endl; 

    return 0;
}