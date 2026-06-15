#include <stdio.h>

int main(){
    // array (larik) = sekelompok variabel dengan tipe data yang sama yang diakses menggunakan indeks

    // deklarasi array
    int angka[5]; // array dengan tipe data integer dan ukuran 5 elemen

    // inisialisasi array
    angka[0] = 10;
    angka[1] = 20;
    angka[2] = 30;
    angka[3] = 40;
    angka[4] = 50;

    // akses array index
    printf("angka[0] = %d\n", angka[0]);
    printf("angka[1] = %d\n", angka[1]);

    // akses elemen array
    for (int i = 0; i < 5; i++){
        printf("angka[%d] = %d\n", i, angka[i]);
    }

    int angka2[5] = {1, 2, 3, 4, 5}; // deklarasi dan inisialisasi array

    angka2[2] = 10; // mengubah nilai elemen array pada index ke-2
    printf("angka2[2] = %d\n", angka2[2]);

    // array multidimensi
    int matrix[2][3] = {{1, 2, 3},
                      {4, 5, 6}};

    // akses elemen array multidimensi
    printf("matrix[0][0] = %d\n", matrix[0][0]);
    printf("matrix[0][0] = %d\n", matrix[0][1]);
    printf("matrix[0][0] = %d\n", matrix[0][2]);
    printf("matrix[1][2] = %d\n", matrix[1][0]);
    printf("matrix[1][2] = %d\n", matrix[1][1]);
    printf("matrix[1][2] = %d\n", matrix[1][2]);

    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){
            printf("matrix[%d][%d] = %d\n", i, j, matrix[i][j]);
        }
    }

    // studi kasus 1

    int data[5];

    for (int i = 0; i < 5; i++){
        printf("Masukkan angka ke-%d: ", i+1);
        scanf("%d", &data[i]);
    }

    printf("Data yang dimasukkan:\n");
    for (int i = 0; i < 5; i++){
        printf("data[%d] = %d\n", i, data[i]);
    }

    // studi kasus 2 (mencari nilai maksimum dalam array)

    int data_angka[5] = {12, 45, 9, 77, 30};
    int max = data_angka[0];

    for (int i = 1; i < 5; i++){
        if (data_angka[i] > max){
            max = data_angka[i];
        }
    }
    printf("Nilai maksimum dalam array adalah: %d\n", max);

    // assignment

    // Buat program kasir sederhana.

    // 1. Minta user input harga untuk 5 barang (simpan dalam Array).
    // 2. Tampilkan daftar harga yang sudah diinput.
    // 3. Hitung Total Harga (penjumlahan semua array).
    // 4. Jika total belanja di atas 100.000, berikan diskon 10%.
    // 5. Tampilkan total bayar akhir.

    int harga[5];

    // no 1
    for (int i = 0; i < 5; i++){
        printf("Masukkan harga barang ke-%d: ", i+1);
        scanf("%d", &harga[i]);
    }

    // no 2
    printf("\nDaftar harga barang:\n");
    for (int i = 0; i < 5; i++){
        printf("Harga barang ke-%d: %d\n", i+1, harga[i]);
    }

    // no 3
    int total_harga = 0;
    for (int i = 0; i < 5; i++){
        total_harga += harga[i]; // total_harga = total_harga + harga[i]
    }

    // asignment 2

    // 1. minta user menginputkan angka sebanyak 5 kali.
    // 2. simpan angka-angka tersebut dalam array.
    // 3. buat inputan untuk mencari angka dalam array.
    // 4. tampilkan apakah angka tersebut ada dalam array atau tidak.


    return 0;
}