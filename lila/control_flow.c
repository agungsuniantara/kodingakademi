#include <stdio.h>
#include <string.h>

int main(){

    // control flow (for loop, while loop)

    // for loop (perulangan dengan jumlah iterasi yang sudah ditentukan)

    for (int i = 1; i <= 5; i++){
        printf("For Loop Iteration: %d\n", i);
    }

    // while loop (perulangan dengan kondisi tertentu)

    int j = 1;
    while (j <= 5){
        printf("While Loop Iteration: %d\n", j);
        j++;
    }

    // do-while loop (perulangan yang dijalankan minimal satu kali)

    int k = 1;
    do {
        printf("Do-While Loop Iteration: %d\n", k);
        k++;
    } while (k <= 5);

    // studi kasus 

    int kondisi = 1;
    int angka = 0;
    while (kondisi){
        printf("angka = %d\n", angka);
        angka++;
        if (angka > 5){
            kondisi = 0;
            // break;
        }
    }

    // assignment

    // 1. Buat program yang menampilkan bilangan genap dari 2 hingga 20 menggunakan for loop.
    int i = 10;
    if (i % 2 == 0){
        printf("%d", i);
    }
    // 2. Buat program yang menampilkan bilangan ganjil dari 1 hingga 19 menggunakan while loop.
    int m = 1;
    while (m < 20){
        if (m % 2 != 0){
            printf("%d\n", m);
        }
        m++;
    }

    // input (scanf & fgets)

    char nama[50];
    int nim;
    float ipk;
    char grade;

    printf("--- input data mahasiswa ---\n");

    printf("nama: ");
    scanf("%s", nama);

    printf("nim: ");
    scanf("%d", &nim);

    printf("ipk: ");
    scanf("%f", &ipk);

    printf("grade: ");
    scanf(" %c", &grade);

    printf("\n--- data mahasiswa ---\n");
    printf("nama: %s\n", nama);
    printf("nim: %d\n", nim);
    printf("ipk: %.2f\n", ipk);
    printf("grade: %c\n", grade);

    // assignment

    // 1. Minta user menginput Alas (gunakan tipe data float).
    // 2. Minta user menginput Tinggi (gunakan tipe data float).
    // 3. Hitung luasnya dengan rumus: 0.5 * Alas * Tinggi.
    // 4. Tampilkan hasilnya dengan 2 angka di belakang koma.

    int a, b;

    printf("masukan angka : ");
    scanf("%d %d", &a, &b);
    printf("a : %d\n", a);
    printf("b : %d\n", b);

    getchar(); // membersihkan buffer

    char nama_lengkap[50];

    printf("Masukkan nama lengkap: ");
    fgets(nama_lengkap, sizeof(nama_lengkap), stdin);

    printf("Nama lengkap Anda adalah: %s", nama_lengkap);

    return 0;
}