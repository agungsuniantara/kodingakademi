// main.cpp
#include <iostream>
#include "functions.h"

int main() {
    int a, b, pilihan;
    std::cout << "Masukkan angka pertama: ";
    std::cin >> a;
    std::cout << "Masukkan angka kedua: ";
    std::cin >> b;

    std::cout << "Pilih operasi:\n1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n";
    std::cout << "Pilihan: ";
    std::cin >> pilihan;

    switch (pilihan) {
        case 1:
            std::cout << "Hasil: " << tambah(a, b) << std::endl;
            break;
        case 2:
            std::cout << "Hasil: " << kurang(a, b) << std::endl;
            break;
        case 3:
            std::cout << "Hasil: " << kali(a, b) << std::endl;
            break;
        case 4:
            std::cout << "Hasil: " << bagi(a, b) << std::endl;
            break;
        default:
            std::cout << "Pilihan tidak valid." << std::endl;
    }

    return 0;
}
