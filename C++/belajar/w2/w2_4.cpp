#include <iostream>
using namespace std;

// GOAL: See with your own eyes why stack memory dies when a function ends.
// SKILLS: recognising a dangling pointer, understanding the stack vs heap.

int* cool_func() {
    int* my_int = new int; 
    *my_int = 10;          
    
    return my_int;
}

// This function just performs some other operations.
void another_func() {
    int arr[100];
    for (int i = 0; i < 100; i++) arr[i] = 0;
}

int main() {
    int* cool_int_ptr = cool_func();

    // Do some unrelated work that will reuse that stack space:
    another_func();

    // Is my int still there? Run it and find out.
    cout << (*cool_int_ptr) << endl;
    
    // untuk menghindari memory leak.
    delete cool_int_ptr;

    return 0;
}