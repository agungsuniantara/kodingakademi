// Tipe Data

// Char = Karakter (a,b,c,d,dst)
// Integer (int) = angka (1,2,3,4,5,dst)
// float = angka (10.2,20.3,dst)
// double = angka (20.45643,dst)

// perbedaan antara double, int dan float :
// double bisa mencakup banyak angka dan angka koma sedangkan int / integer tidak
// integer hanya berupa angka bulat tidak ada angka koma
// contoh :

#include <stdio.h>

int main(){
    char sedikit = 'y';
    char tulisan[] = "ini char";
    int integer = 10;
    float flt = 10.21;
    double dbl = 10.2323232;

    printf("ini adalah char sedikit = %c \n", sedikit);
    printf("ini adalah char tulisan = %s \n", tulisan);
    printf("ini adalah integer = %d \n", integer);
    printf("ini adalah flt = %f \n", flt);
    printf("ini adalah dbl = %f \n", dbl);
}

// dapat dilihat ada %c, %s, %d, %f
// %c berfungsi untuk menampilkan single karakter
// %s berfungsi untuk menampilkan string
// %d berfungsi untuk menampilkan nilai angka
// %f berfungsi untuk menampilkan nilai angka isi koma
