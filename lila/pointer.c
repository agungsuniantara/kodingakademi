#include <stdio.h>

void tukar(int x, int y){ // tanpa pointer
    int temp;
    temp = x;
    x = y;
    y = temp;
    printf("nilai x di dalam fungsi tukar: %d\n", x);
    printf("nilai y di dalam fungsi tukar: %d\n", y);
}

void tukar_pointer(int *x, int *y){ // dengan pointer
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
    printf("nilai x di dalam fungsi tukar_pointer: %d\n", *x);
    printf("nilai y di dalam fungsi tukar_pointer: %d\n", *y);
}

int main(){
    int a = 10;
    int b = 20;
    printf("nilai a: %d\n", a);
    printf("alamat a: %p\n", &a); // & = operator untuk mendapatkan alamat variabel
    printf("nilai b: %d\n", b);
    printf("alamat b: %p\n", &b);

    // pointer = variabel yang menyimpan alamat dari variabel lain

    int *p; // deklarasi pointer
    p = &a; // menyimpan alamat variabel a ke pointer p

    printf("alamat pointer p: %p\n", p);
    printf("nilai yang ditunjuk pointer p: %d\n", *p);  

    *p = 15; // mengubah nilai a melalui pointer p
    printf("nilai a setelah diubah melalui pointer p: %d\n", a);

    // studi kasus mengapa pointer itu penting

    int c = 30;
    int d = 40;

    printf("\nSebelum ditukar:\n");
    printf("nilai c: %d\n", c);
    printf("nilai d: %d\n", d);
    tukar(c, d);
    printf("Setelah ditukar:\n");
    printf("nilai c: %d\n", c);
    printf("nilai d: %d\n", d);

    // nilai c dan d tidak berubah karena yang dikirim ke fungsi tukar adalah salinan nilai c dan d

    printf("\nSebelum ditukar dengan pointer:\n");
    printf("nilai c: %d\n", c);
    printf("nilai d: %d\n", d);
    tukar_pointer(&c, &d); // mengirim alamat c dan d ke fungsi
    printf("Setelah ditukar:\n");
    printf("nilai c: %d\n", c);
    printf("nilai d: %d\n", d);

    // assignment

    // Kalkulator Update Nilai. Buatlah sebuah fungsi bernama updateNilai yang:
    // Menerima parameter alamat dari sebuah nilai (int *nilai).
    // Menerima parameter angka penambah (int tambah).
    // Di dalam fungsi, tambahkan nilai asli dengan penambah.

    // Di main():
    // Buat variabel skor = 100.
    // Panggil fungsi: updateNilai(&skor, 50);
    // Print skor. Output harus 150, bukan 100.

    // assignment 2

    // Buat variabel integer target = 10.
    // Buat pointer int *p yang menunjuk ke alamat target.
    // Tantangan: Ubah nilai target menjadi 500, TAPI syaratnya:    
    // Dilarang menulis target = 500;
    // Harus menggunakan pointer p.
    // Tampilkan nilai target di layar untuk membuktikan bahwa nilainya berubah.

    int angka[3] = {100, 200, 300};
    int *z = angka; // pointer menunjuk ke elemen pertama array

    printf("\nAlamat array angka: %p\n", angka);
    printf("elemen pointer z: %p\n", z);
    printf("elemen pertama: %d\n", *z); // 100
    printf("elemen kedua: %d\n", *(z + 1)); // 200
    printf("elemen ketiga: %d\n", *(z + 2)); // 300

    for (int i = 0; i < 3; i++){
        printf("elemen ke-%d: %d\n", i, *(z + i));
    }

    // assignment 3

    // buat variabel char kalimat[5] = "manish";
    // tukar karakter pertama dan terakhir menggunakan pointer.

    char kalimat[7] = "manish";
    char *ptr_start = &kalimat[0];
    char *ptr_end = &kalimat[5];

    printf("\nSebelum ditukar: %s\n", kalimat);
    // tukar karakter pertama dan terakhir
    char temp_char = *ptr_start;
    *ptr_start = *ptr_end;
    *ptr_end = temp_char;

    // assignment 4

    // buat array integer numbers[4] = {10, 20, 30, 40};
    // jumlahkan semua elemen dalam array menggunakan pointer dan tampilkan hasilnya.

    int numbers[4] = {10, 20, 30, 40};
    int *ptr_numbers = numbers;
    int total = 0;

    for (int i = 0; i < 4; i++){
        total += *(ptr_numbers + i); // total = total + numbers[i];
    }

    printf("Total: %d\n", total);

    return 0;
}