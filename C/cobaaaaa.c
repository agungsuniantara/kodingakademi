#include <stdio.h>

struct data_diri{
    char nama[100];
    int umur;
    char alamat[100];
};

void main(){
    struct data_diri data1;
    struct data_diri data2;

    //data1
    strcpy(data1.nama, "anin");
    data1.umur = 17;
    strcpy(data1.alamat, "denpasar");

    printf("data 1 : \n");
    printf("nama = %s \n", data1.nama);
    printf("umur = %d \n", data1.umur);
    printf("alamat = %s \n", data1.alamat);

    //data 2
    strcpy(data2.nama, "agung");
    data2.umur = 24;
    strcpy(data2.alamat, "denpasar");

    printf("data 2 : \n");
    printf("nama = %s \n", data2.nama);
    printf("umur = %d \n", data2.umur);
    printf("alamat = %s \n", data2.alamat);

}
