#include <stdio.h>
#include <string.h>

struct Mahasiswa {
    char nama[50];
    char alamat[100];
    int umur;
};

typedef struct {
    char nama[50];
    char alamat[100];
    int umur;
} Mahasiswa_baru;

int main(){
    // contoh yang tidak efisien jika menggunakan array biasa
    int nama[50]; // nama[0] = lila
    int alamat[50]; // alamat[0] = jakarta
    int umur[50]; // umur[0] = 20

    struct Mahasiswa data_lila;
    strcpy(data_lila.nama, "lila");
    strcpy(data_lila.alamat, "jakarta");
    data_lila.umur = 20;

    printf("nama: %s\n", data_lila.nama);
    printf("alamat: %s\n", data_lila.alamat);
    printf("umur: %d\n", data_lila.umur);

    struct Mahasiswa database[3];
    strcpy(database[0].nama, "lila");
    strcpy(database[0].alamat, "jakarta");
    database[0].umur = 20;

    strcpy(database[1].nama, "budi");
    strcpy(database[1].alamat, "bandung");
    database[1].umur = 22;

    strcpy(database[2].nama, "ani");
    strcpy(database[2].alamat, "surabaya");
    database[2].umur = 21;

    printf("\nData Mahasiswa:\n");
    printf("1. %s, %s, %d\n", database[0].nama, database[0].alamat, database[0].umur);
    printf("2. %s, %s, %d\n", database[1].nama, database[1].alamat, database[1].umur);
    printf("3. %s, %s, %d\n", database[2].nama, database[2].alamat, database[2].umur);

    printf("\n looping data mahasiswa:\n");
    for (int i = 0; i < 3; i++){
        printf("%d. %s, %s, %d\n", i+1, database[i].nama, database[i].alamat, database[i].umur);
    }

    Mahasiswa_baru data_budi;
    strcpy(data_budi.nama, "budi");
    strcpy(data_budi.alamat, "bandung");
    data_budi.umur = 22;

    printf("\nData Mahasiswa Baru:\n");
    printf("nama: %s\n", data_budi.nama);
    printf("alamat: %s\n", data_budi.alamat);
    printf("umur: %d\n", data_budi.umur);

    // assignment 1

    // Buatlah program menggunakan Struct dan Array untuk mengelola inventaris item di sebuah game RPG. 
    // Buat struct Item yang berisi : nama (string), harga (int), kekuatan (int).
    // Di main, buat array Item inventory[3].
    // Minta user menginput data untuk 3 item tersebut.
    // Tantangan Logika: Setelah input selesai, tampilkan item mana yang merupakan 
    // "Item Termahal" (Gunakan algoritma pencarian Max yang sudah dipelajari di materi Array).

    struct Item {
        char nama[50];
        int harga;
        int kekuatan;
    };

    struct Item inventory[3];

    for (int i = 0; i < 3; i++){
        printf("\nMasukkan data untuk item ke-%d:\n", i+1);
        printf("Nama item: ");
        scanf("%s", inventory[i].nama);
        printf("Harga item: ");
        scanf("%d", &inventory[i].harga);
        printf("Kekuatan item: ");
        scanf("%d", &inventory[i].kekuatan);
    }

    int max_harga_index = 0;
    for (int i = 1; i < 3; i++){
        if (inventory[i].harga > inventory[max_harga_index].harga){
            max_harga_index = i;
        }
    }

    printf("\nItem Termahal:\n");
    printf("Nama: %s\n", inventory[max_harga_index].nama);
    printf("Harga: %d\n", inventory[max_harga_index].harga);
    printf("Kekuatan: %d\n", inventory[max_harga_index].kekuatan);

    return 0;
}