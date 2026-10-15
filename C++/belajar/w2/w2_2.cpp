#include <iostream>
#include <string>
using namespace std;

// GOAL: Give your type actions, not just data.
// SKILLS: member functions, attributes accessed inside methods.
struct User {
    string username;
    string password;
    int created_at;
    bool banned;

    // Call this when a user should be banned.
    void ban() {
        banned = true;
        password = "";   // wipe the password too
    }

    // Call this to check if the user can log in.
    bool can_login(string attempted_password) {
        if (banned) return false;
        return password == attempted_password;
    }
};

int main() {
    User jane;
    jane.username = "jane";
    jane.password = "kitten42";
    jane.created_at = 1000000;
    jane.banned = false;

    cout << (jane.can_login("kitten42") ? "Logged in" : "Denied") << endl;

    jane.ban();
    cout << (jane.can_login("kitten42") ? "Logged in" : "Denied") << endl;

    // The ban method cleared the password:
    cout << "Password is now: '" << jane.password << "'" << endl;
    return 0;
}