#include <iostream>
#include <string>
using namespace std;

// GOAL: A Tutor manages a list of Students, and can look a student up.
// SKILLS: nested custom types, arrays of objects, returning a pointer, nullptr for "not found".
struct Student {
    string name;
    int student_id;
};

struct Tutor {
    string name;
    Student students[50];   // each Tutor has about 50 students
    int student_count;

    // Returns a pointer to the student with this name.
    // If nobody matches, returns nullptr (our agreed "not found" signal).
    Student* get_student_ptr(string target_name) {
        for (int i = 0; i < student_count; i++) {
            if (students[i].name == target_name) {
                return &students[i];
            }
        }
        return nullptr;
    }
};

int main() {
    Tutor t;
    t.name = "Ms. Rivera";
    t.student_count = 3;

    t.students[0].name = "Ava";
    t.students[0].student_id = 101;
    t.students[1].name = "Bob";
    t.students[1].student_id = 102;
    t.students[2].name = "Chen";
    t.students[2].student_id = 103;

    // Look someone up and modify them THROUGH the returned pointer:
    Student* found = t.get_student_ptr("Bob"); 
    if (found != nullptr) {
        // DIPERBAIKI: Menghapus kelebihan tutup kurung
        found->student_id = 999;   // change through the pointer
    }
    
    cout << t.students[1].student_id << endl;   // 999: same object!

    // Look up someone who doesn't exist:
    Student* missing = t.get_student_ptr("Zoe");
    if (missing == nullptr) {
        cout << "No student named Zoe." << endl;
    }
    return 0;
}