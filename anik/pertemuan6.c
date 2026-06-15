#include <stdio.h>

// pointer adalah variabel yang menyimpan alamat memori dari variabel lain

void rubah_local(int *x){
    *x = 100;
}

void tukar(int *a, int *b){
    int temp = *a; // menyimpan nilai yang ditunjuk oleh a ke dalam variabel temp
    *a = *b; // mengubah nilai yang ditunjuk oleh a menjadi nilai yang ditunjuk oleh b
    *b = temp; // mengubah nilai yang ditunjuk oleh b menjadi nilai yang disimpan di temp (nilai awal a)
}

void updateNilai(int *nilai, int tambah){
    *nilai += tambah; // menambahkan nilai yang ditunjuk oleh nilai dengan tambah
}

int main(){
    int a = 10; // variabel a menyimpan nilai 10
    int b = 10; // variabel b menyimpan nilai 10

    printf("nilai a : %d\n", a); // menampilkan nilai a
    printf("alamat a : %p\n", &a); // menampilkan alamat a
    printf("nilai b : %d\n", b); // menampilkan nilai b
    printf("alamat b : %p\n", &b); // menampilkan alamat b

    int *p, *c;
    p = &a; // pointer p menyimpan alamat a

    printf("nilai p : %p\n", p); // menampilkan nilai p (alamat a)
    printf("nilai yang ditunjuk oleh p : %d\n", *p); // menampilkan nilai yang ditunjuk oleh p (nilai a)

    *p = 20; // mengubah nilai yang ditunjuk oleh p menjadi 20 (mengubah nilai a)
    printf("nilai a setelah diubah : %d\n", a); // menampilkan nilai a setelah diubah

    // studi kasus

    rubah_local(&a); // memanggil fungsi rubah_local dengan alamat a
    printf("nilai a setelah dipanggil fungsi rubah_local : %d\n", a); // menampilkan nilai a setelah dipanggil fungsi rubah_local

    // studi kasus 2

    int x = 5;
    int y = 10;
    tukar(&x, &y); // memanggil fungsi tukar dengan alamat x dan y
    printf("nilai x setelah ditukar : %d\n", x); // menampilkan nilai x setelah ditukar
    printf("nilai y setelah ditukar : %d\n", y); // menampilkan nilai y setelah ditukar

    // assignment 1

    // Kalkulator Update Nilai. Buatlah sebuah fungsi bernama updateNilai yang:
    // Menerima parameter alamat dari sebuah nilai (int *nilai).
    // Menerima parameter angka penambah (int tambah).
    // Di dalam fungsi, tambahkan nilai asli dengan penambah.

    // Di main():
    // Buat variabel skor = 100.
    // Panggil fungsi: updateNilai(&skor, 50);
    // Print skor. Output harus 150, bukan 100.

    int skor = 100;
    int angka;

    printf("masukkan angka penambah : ");
    scanf("%d", &angka);

    updateNilai(&skor, angka);
    printf("nilai skor setelah update : %d\n", skor);

    // assignment 2

    // Buat variabel integer target = 10.
    // Buat pointer int *p yang menunjuk ke alamat target.
    // Tantangan: Ubah nilai target menjadi 500, TAPI syaratnya:    
    // Dilarang menulis target = 500;
    // Harus menggunakan pointer p.
    // Tampilkan nilai target di layar untuk membuktikan bahwa nilainya berubah.

    int target = 10;
    int *l = &target; // pointer p menunjuk ke alamat target
    *l = 500; // mengubah nilai yang ditunjuk oleh p menjadi 500 (mengubah nilai target)
    printf("nilai target setelah diubah : %d\n", target); // menampilkan nilai target setelah diubah

    int angka100[3] = {1, 2, 3}; // array angka menyimpan 3 nilai: 1, 2, dan 3
    int *ptr = angka100; // pointer ptr menunjuk ke alamat pertama dari array angka

    printf("nilai pertama dalam array : %d\n", *ptr); // menampilkan nilai pertama dalam array (nilai yang ditunjuk oleh ptr)
    printf("alamat pertama dalam array : %p\n", ptr); // menampilkan alamat pertama dalam array (alamat yang ditunjuk oleh ptr)
    printf("nilai kedua dalam array : %d\n", *(ptr + 1)); // menampilkan nilai kedua dalam array (nilai yang ditunjuk oleh ptr + 1)
    printf("alamat kedua dalam array : %p\n", ptr + 1); // menampilkan alamat kedua dalam array (alamat yang ditunjuk oleh ptr + 1)
    printf("nilai ketiga dalam array : %d\n", *(ptr + 2)); // menampilkan nilai ketiga dalam array (nilai yang ditunjuk oleh ptr + 2)
    printf("alamat ketiga dalam array : %p\n", ptr + 2); // menampilkan alamat ketiga dalam array (alamat yang ditunjuk oleh ptr + 2)

    for (int i = 0; i < 3; i++){
        printf("nilai ke-%d dalam array : %d\n", i + 1, *(ptr + i)); // menampilkan nilai ke-i dalam array (nilai yang ditunjuk oleh ptr + i)
    }

    char nama[20] = "dimas"; // array nama menyimpan string "dimas"
    char *ptrNama = &nama[0]; // pointer ptrNama menunjuk ke alamat pertama dari array nama
    char *ptrNama2 = nama; // pointer ptrNama2 juga menunjuk ke alamat pertama dari array nama (nama adalah alamat pertama dari array nama)

    printf("huruf pertama dalam nama : %c\n", *ptrNama); // menampilkan huruf pertama dalam nama (nilai yang ditunjuk oleh ptrNama)
    printf("nama : %s\n", ptrNama2);

    // assignment 3

    // buat variabel char kalimat[5] = "manish";
    // tukar karakter pertama dan terakhir menggunakan pointer.

    // assignment 4

    // buat array integer numbers[4] = {10, 20, 30, 40};
    // jumlahkan semua elemen dalam array menggunakan pointer dan tampilkan hasilnya.

    return 0;
}