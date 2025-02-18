// functions.cpp
#include "functions.h"

int tambah(int a, int b) {
    return a + b;
}

int kurang(int a, int b) {
    return a - b;
}

int kali(int a, int b) {
    return a * b;
}

float bagi(int a, int b) {
    if (b == 0) {
        return 0; // Menangani pembagian dengan nol
    }
    return static_cast<float>(a) / b;
}
