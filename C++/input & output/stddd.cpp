#include <iostream>

int main() {
    int angka, angka2;

    std::cout << "Masukkan angka1: " << std::endl;
    std::cin >> angka;

    std::cout << "Masukkan angka2: " << std::endl;
    std::cin >> angka2;

    std::cout << "Angka adalah: " << angka << " " << angka2 << std::endl;

    printf("Angka adalah: %d %d\n", angka, angka2);

    return 0;
}
