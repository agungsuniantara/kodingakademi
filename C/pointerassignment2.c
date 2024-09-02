#include <stdio.h>

const int MAX = 3;
int main ()
{
    int var[] = {10, 100, 200};
    int i, *ptr[MAX];
    int tambah = 0;
    int average;

    for ( i = 0; i < MAX; i++)
    {
        ptr[i] = &var[i];
        // ptr menyimpan setiap alamat var index i
    }

    for ( i = 0; i < MAX; i++)
    {
        tambah = tambah + *ptr[i];
        // ptr mengakses alamat var index i yang sudah dihubungkan sebelumnya
    }

    average = tambah / MAX;
    printf("hasil average = %d", average);

    return 0;
}
