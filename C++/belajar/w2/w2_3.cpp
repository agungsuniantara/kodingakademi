#include <iostream>
#include <string>
using namespace std;

// GOAL: Understand that a variable and its object are two different things.
// SKILLS: & (address of), * (go to the object), -> (shortcut).
struct User {
    string name;
};

int main() {
    // This creates a User object AND glues the variable jane to it.
    User jane;
    jane.name = "Jane";

    // Now we take the address ourselves:
    User* jane_ptr = &jane;

    // Printing the pointer shows an address, not a name:
    cout << jane_ptr << endl;              // something like 0x16ae06f08

    // We can't use dot on a pointer directly:
    // cout << jane_ptr.name << endl;      // <-- uncomment me: won't compile!

    // Two equivalent ways to go through the address to the object:
    cout << (*jane_ptr).name << endl;      // explicit: go to object, then dot
    cout << jane_ptr->name << endl;        // shortcut: the -> does both steps

    // Change the object THROUGH the pointer:
    jane_ptr->name = "Not Jane";

    // Jane's name changed too, because there is only ONE object in memory:
    cout << jane.name << endl;
    cout << jane_ptr->name << endl;
    return 0;
}