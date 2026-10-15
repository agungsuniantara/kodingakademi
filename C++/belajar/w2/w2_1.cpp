#include <iostream>
#include <string>
using namespace std;

// GOAL: Define a custom type and use it like any other variable.
// SKILLS: struct definition, attributes, dot syntax.
struct User {
    string username;
    string password;
    int created_at;
    bool banned;
};

int main() {
    User first_user;   // creating an object = creating an instance of the type

    first_user.username = "cool-username";
    first_user.password = "secret_password";
    first_user.created_at = 1000000;
    first_user.banned = false;

    // From now on, first_user.username is just a normal string variable.
    cout << "Username: " << first_user.username << endl;
    cout << "Account age (2 s): " << first_user.created_at << endl;

    if (first_user.banned) {
        cout << "This user is banned." << endl;
    } else {
        cout << "This user is active." << endl;
    }
    return 0;
}