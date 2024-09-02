#include <stdio.h>

struct orang{
    char nama[50];
    int umur;
};

void main(){
    struct orang panggil;

    strcpy(panggil.nama, "neilson");
    panggil.umur = 50;

    printf("nama = %s \n", panggil.nama);
    printf("umur = %d", panggil.umur);

}
