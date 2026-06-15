#include <stdio.h>

int main(){
    // array = sekelompok variabel dengan tipe data yang sama yang disimpan dalam satu nama dan diakses dengan indeks

    // deklarasi array

    int angka[5] = {1, 2, 3, 4, 5}; // deklarasi array dengan tipe data integer dengan nama angka dan ukuran 5

    float angka2[5]; 

    angka2[0] = 10.0; // mengisi nilai array pada indeks ke 0
    angka2[1] = 20.0; // mengisi nilai array pada indeks ke 1
    angka2[2] = 30.0; // mengisi nilai array pada indeks ke 2
    angka2[3] = 40.0; // mengisi nilai array pada indeks ke 3
    angka2[4] = 50.0; // mengisi nilai array pada indeks ke 4

    printf("%d \n", angka[0]); // mengakses nilai array pada indeks ke 0
    printf("%.2f \n", angka2[0]); // mengakses nilai array pada indeks ke 0

    // looping array
    for (int i = 0; i < 5; i++){
        printf("index ke-%d : %d \n", i, angka[i]);
    }

    for (int i = 0; i < 5; i++){
        printf("index ke-%d : %.2f \n", i, angka2[i]);
    }

    int matrix[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    }; // deklarasi array 2 dimensi dengan tipe data integer dengan nama matrix dan ukuran 2x3

    printf("%d \n", matrix[0][0]); // mengakses nilai array pada indeks ke 0,0
    printf("%d \n", matrix[1][2]); // mengakses nilai array pada indeks ke 1,2

    // looping array 2 dimensi
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){
            printf("index ke-%d,%d : %d \n", i, j, matrix[i][j]);
        }
    }

    // studi kasus 1

    int data[5];

    for (int i = 0; i < 5; i++){
        printf("masukkan angka ke-%d : ", i);
        scanf("%d", &data[i]);
    }

    printf("angka yang anda masukkan adalah : \n");
    for (int i = 0; i < 5; i++){
        printf("angka ke-%d : %d \n", i, data[i]);
    }

    // studi kasus 2

    int data_angka[5] = {10, 20, 30, 40, 50};
    int max = data_angka[0];

    for (int i = 0; i < 5; i++){
        if (data_angka[i] > max){
            max = data_angka[i];
        }
    }

    printf("max value is %d \n", max);

    // assignment array ( easy )
    // 1. buatlah program untuk menghitung rata-rata dari 5 angka yang dimasukkan oleh user

    int data_1[5]; // [10, 20]
    int jumlah = 0; // 10 // 30 // 60 // 100 // 150

    for (int i = 0; i < 5; i++){
        printf("masukkan angka ke-%d : ", i); // 20
        scanf("%d", &data_1[i]);
        jumlah += data_1[i]; // jumlah = 30
    }

    float rata_rata = (float)jumlah / 5.0;
    printf("rata-rata dari 5 angka tersebut adalah %.2f \n", rata_rata);

    // 4. buatlah program untuk mencari nilai terkecil dari 5 angka yang dimasukkan oleh user

    int data[5]; // [10, 5, 8, 3, 6]

    for (int i = 0; i < 5; i++){
        printf("masukkan angka ke-%d : ", i);
        scanf("%d", &data[i]);
    }

    int min = data[0]; // min = 10

    for (int i = 0; i < 5; i++){
        if (data[i] < min){
            min = data[i];
        }
    }

    printf("min value is %d \n", min);

    // 5. buatlah program untuk menampilkan 5 angka yang dimasukkan oleh user dalam urutan terbalik


    return 0;
}