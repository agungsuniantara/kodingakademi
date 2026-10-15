// w1_demo.cpp
// W1: Basic Input/Output in C++
// Compile: make (or g++ -std=c++17 -Wall -Wextra -pedantic w1_demo.cpp -o w1_demo)

#include <iostream>
#include <string>

int main() {
    // ============================================================
    // PART 1: Printing with cout
    // ============================================================
    std::cout << "Hello, World!" << std::endl;

    // You can chain << many times in one line
    std::cout << "Welcome to " << "Algorithms " << "and " << "Data Structures!" << std::endl;

    // endl prints a newline AND flushes the output buffer.
    // "\n" only prints a newline (slightly faster, fine for now).
    std::cout << "Line 1" << std::endl;
    std::cout << "Line 2" << "\n";

    // ============================================================
    // PART 2: Reading input with cin
    // ============================================================
    int age;
    std::cout << "Enter your age: ";
    std::cin >> age;
    std::cout << "You are " << age << " years old." << std::endl;

    // Chained input: cin reads values separated by spaces or newlines.
    int a, b, c;
    std::cout << "Enter three numbers (space-separated): ";
    std::cin >> a >> b >> c;
    std::cout << "You entered: " << a << ", " << b << ", " << c << std::endl;

    // Reading a whole word (stops at whitespace)
    std::string name;
    std::cout << "Enter your first name: ";
    std::cin >> name;
    std::cout << "Hi," << std::endl << name << "!" << std::endl;

    // ============================================================
    // PART 3: Integer vs floating-point division (classic trap!)
    // ============================================================
    std::cout << "--- Division demo ---" << std::endl;

    // PREDICT before running: what will each line print?
    std::cout << "7 / 2   = " << 7 / 2 << std::endl;     // int / int -> integer division
    std::cout << "7 % 2   = " << 7 % 2 << std::endl;     // % is the remainder (modulo)
    std::cout << "7.0 / 2 = " << 7.0 / 2 << std::endl;   // one double -> floating-point division
    std::cout << "7 / 2.0 = " << 7 / 2.0 << std::endl;   // same result

    // The common bug: dividing two ints and EXPECTING a fraction
    int total_marks = 17;
    int num_tests = 2;
    double average_wrong = total_marks / num_tests;      // = 8.0  (int division happened FIRST)
    double average_right = static_cast<double>(total_marks) / num_tests;  // = 8.5
    std::cout << "Wrong average:   " << average_wrong << std::endl;
    std::cout << "Correct average: " << average_right << std::endl;

    // ============================================================
    // PART 4: The "Are You Ready" program
    // (the minimum bar from W1 Readings: sum of a list of numbers)
    // ============================================================
    int n;
    std::cout << "How many numbers will you enter? ";
    std::cin >> n;

    int sum = 0;
    for (int i = 0; i < n; i++) {
        int value;
        std::cin >> value;
        sum += value;
    }
    std::cout << "The sum is " << sum << std::endl;

    // Bonus: the average, using our division lesson
    if (n > 0) {
        double average = static_cast<double>(sum) / n;
        std::cout << "The average is " << average << std::endl;
    }

    return 0;
}
