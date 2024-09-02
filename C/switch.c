#include <stdio.h>

int main() {
    int pilihan;
    int angka;

    printf("Masukkan pilihan (1, 2, atau 3): ");
    scanf("%d", &pilihan);

    switch (pilihan) {
        case 1:
            angka = 1;
            printf("Anda memilih pilihan %d \n", angka);
            break; // Jangan lupa menggunakan 'break' setelah setiap kasus
        case 2:
            angka = 2;
            printf("Anda memilih pilihan %d \n", angka);
            break;
        case 3:
            angka = 3;
            printf("Anda memilih pilihan %d \n", angka);
            break;
        default:
            printf("Pilihan tidak valid\n");
    }

    return 0;
}
