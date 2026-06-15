#include <stdio.h>
#include <string.h>

// struct ( structure ) = metode untuk deklarasi objek yang memiliki lebih dari 1 tipe data

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

typedef struct {
    char nama[50];
    int id_peserta;
    int umur;
    char kelas_pilihan[50];
} peserta;

int main(){
    struct Mahasiswa data_anik;
    strcpy(data_anik.nama, "anik");
    strcpy(data_anik.alamat, "denpasar");
    data_anik.umur = 20;
    
    printf("nama : %s \n", data_anik.nama);
    printf("alamat : %s \n", data_anik.alamat);
    printf("umur : %d \n", data_anik.umur);

    Mahasiswa_baru data_agung;
    strcpy(data_agung.nama, "agung");
    strcpy(data_agung.alamat, "denpasar");
    data_agung.umur = 27;
    
    printf("nama : %s \n", data_agung.nama);
    printf("alamat : %s \n", data_agung.alamat);
    printf("umur : %d \n", data_agung.umur);

    Mahasiswa_baru database[2]; // [[], []]
    strcpy(database[0].nama, "anik");
    strcpy(database[0].alamat, "denpasar");
    database[0].umur = 20;

    strcpy(database[1].nama, "agung");
    strcpy(database[1].alamat, "denpasar");
    database[1].umur = 27;

    printf("nama : %s \n", database[0].nama);
    printf("alamat : %s \n", database[0].alamat);
    printf("umur : %d \n", database[0].umur);

    printf("nama : %s \n", database[1].nama);
    printf("alamat : %s \n", database[1].alamat);
    printf("umur : %d \n", database[1].umur);

    printf("\nData Mahasiswa : \n");
    for (int i = 0; i < 2; i++){
        printf("%d. %s | %s | %d \n", i + 1, database[i].nama, database[i].alamat, database[i].umur);
    }

    // assignment

    // Gunakan typedef struct untuk membuat tipe data baru bernama Peserta. Struct ini harus memiliki anggota (member) berikut:
    // - nama (string/array of char, maksimal 50 karakter)
    // - id_peserta (integer)
    // - umur (integer)
    // - kelas_pilihan (string/array of char, maksimal 50 karakter - contoh pengisian: "Python", "Full-Stack Web", atau "Data Science")

    // Deklarasikan sebuah array dari Peserta yang dikonfigurasi untuk menampung data 3 orang peserta.
    // lakukan input data untuk 3 peserta.
    // tampilkan semua data peserta.
    // buat fitur, tampilkan data peserta yang sesuai jika user input kelas pilihan.

    peserta data[3];
    int jumlah;

    printf("masukan jumlah peserta : ");
    scanf("%d", &jumlah);

    for (int i = 0; i < jumlah; i++){
        printf("\nData peserta ke - %d \n", i + 1);
        printf("Masukan nama : ");
        fgets(data[i].nama, sizeof(data[i].nama), stdin);
        printf("Masukan id peserta : ");
        scanf("%d", &data[i].id_peserta);
        printf("Masukan umur : ");
        scanf("%d", &data[i].umur);
        printf("Masukan kelas pilihan : ");
        fgets(data[i].kelas_pilihan, sizeof(data[i].kelas_pilihan), stdin);
    }

    printf("\nData peserta : \n");
    for (int i = 0; i < jumlah; i++){
        printf("%d. %s | %d | %d | %s \n", i + 1, data[i].nama, data[i].id_peserta, data[i].umur, data[i].kelas_pilihan);
    }

    char cari[50];
    printf("masukan kelas yang ingin dilihat : ");
    fgets(cari, sizeof(cari), stdin);

    for (int i = 0; i < jumlah; i++){
        if (strcmp(data[i].kelas_pilihan, cari) == 0){
            printf("%d. %s | %d | %d \n", i + 1, data[i].nama, data[i].id_peserta, data[i].umur);
        }
    }

    return 0;
}